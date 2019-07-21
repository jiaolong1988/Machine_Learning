import random

class Robot(object):

    def __init__(self, maze, alpha=0.5, gamma=0.9, epsilon0=0.5):

        self.maze = maze
        self.valid_actions = self.maze.valid_actions
        self.state = None
        self.action = None

        # Set Parameters of the Learning Robot
        self.alpha = alpha
        self.gamma = gamma

        self.epsilon0 = epsilon0
        self.epsilon = epsilon0
        self.t = 0

        self.Qtable = {}
        self.reset()

    def reset(self):
        """
        Reset the robot
        """
        self.state = self.sense_state()
        self.create_Qtable_line(self.state)

    def set_status(self, learning=False, testing=False):
        """
        Determine whether the robot is learning its q table, or
        exceuting the testing procedure.
        """
        self.learning = learning
        self.testing = testing

    def update_parameter(self):
        """
        Some of the paramters of the q learning robot can be altered,
        update these parameters when necessary.
        """
        if self.testing:
            # TODO 1. No random choice when testing
            # 0表示使用 当前最佳策略，无需随机选择
            self.epsilon = 0
        else:
            # TODO 2. Update parameters when learning
            # 学习时，随机动作的概率应当随着训练的过程逐步减小。
            self.epsilon *= 0.87

        return self.epsilon

    def sense_state(self):
        """
        Get the current state of the robot. In this
        """

        # TODOs 3. Return robot's current state
        # 迷宫中的位置 设置为 状态
        return  self.maze.sense_robot()

    def create_Qtable_line(self, state):
        """
        Create the qtable with the current state
        """
        # TODO 4. Create qtable with current state
        # Our qtable should be a two level dict,
        # Qtable[state] ={'u':xx, 'd':xx, ...}
        # If Qtable[state] already exits, then do
        # not change it.
          
        # 状态不存在
        if state not in self.Qtable:           
            # 为每个 状态 初始化一个 动作值
            self.Qtable[state] ={ 'r':0, 'd':0, 'l':0,'u':0}
        

    def choose_action(self):
        """
        Return an action according to given rules
        """
        def is_random_exploration():

            # TODO 5. Return whether do random choice
            # hint: generate a random number, and compare
            # it with epsilon
            
            # 小于epsilon 的随机概率 返回True(epsilon每次更新后都在减小，说明随机概率也在不断的下降）
            return random.uniform(0,1) < self.epsilon
                

        if self.learning:
            if is_random_exploration():
                # TODO 6. Return random choose aciton
                return  random.choice(self.valid_actions)
            else:
                # TODO 7. Return action with highest q value
                # 返回当前状态下 ，最大Q值的动作
                return  max(self.Qtable[self.state], key = self.Qtable[self.state].get)
            
        elif self.testing:
            # TODO 7. choose action with highest q value
            # 返回当前状态下 ，最大Q值的动作
            return max(self.Qtable[self.state], key = self.Qtable[self.state].get)
            
        else:
            # TODO 6. Return random choose aciton
            return random.choice(self.valid_actions)

    def update_Qtable(self, r, action, next_state):
        """
        Update the qtable according to the given rule.
        """
        if self.learning:
            pass
            # TODO 8. When learning, update the q table according
            # to the given rules
            
            # 更新 指定状态的动作值（就是Q值的计算公式）
            self.Qtable[self.state][action] += self.alpha * ( r + \
                                             self.gamma * float(max(self.Qtable[next_state].values())) - \
                                             self.Qtable[self.state][action])
     

    def update(self):
        """
        Describle the procedure what to do when update the robot.
        Called every time in every epoch in training or testing.
        Return current action and reward.
        """
        
        self.state = self.sense_state() # Get the current state
        self.create_Qtable_line(self.state) # For the state, create q table line

        action = self.choose_action() # choose action for this state
        reward = self.maze.move_robot(action) # move robot for given action

        next_state = self.sense_state() # get next state
        self.create_Qtable_line(next_state) # create q table line for next state

        if self.learning and not self.testing:
            self.update_Qtable(reward, action, next_state) # update q table
            self.update_parameter() # update parameters

        return action, reward     