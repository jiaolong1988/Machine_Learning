## 内容：简介和基础知识
## 项目：探索泰坦尼克号乘客存活情况

## 项目概述
欢迎加入“机器学习工程师”纳米学位项目！

在这个**选修**项目中，你将创建决策函数，并根据1912年泰坦尼克号海难的乘客特征，如：性别、年龄等，对乘客生还结果进行预测。您可以从一个简单的算法入手，然后逐渐增加该算法的复杂度，直至您至少能精确地预测出所提供数据中80%的乘客的生还结果。通过该项目，你可在正式开始学习本纳米学位前，了解机器学习的一些概念。

此外，请确保 Python 装有完成本项目所需的程序包。我们在本项目中将使用到的 Python 库有两个，即 `numpy` 和 `pandas`。现在不需担心它们如何运作，在之后的项目中，我们将深入了解它们。本项目还将让你熟悉项目的提交程序，这是你在纳米学位中需要完成的内容。

## 软件要求
本项目采用以下软件和 Python 库：

- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [NumPy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)

你还需要安装和运行 [Jupyter Notebook](http://ipython.org/notebook.html)。

如果你还未安装 Python，我们强烈推荐你安装 Python 发行版：[Anaconda](http://continuum.io/downloads)，其具备包括上述程序包在内的更多程序包。安装时，确保你选择的是 Python 2.7 安装程序，而不是 Python 3.x 安装程序。

如果你的计算机中已装有 Python 2.7，那么你可使用命令行上的 [pip](https://pip.pypa.io/en/stable/) 安装 `numpy`， `scikit-learn` 和 Jupyter Notebook（之前叫“iPython”）。如果使用 pip 执行安装时出现问题，[这个页面](http://www.lfd.uci.edu/~gohlke/pythonlibs/)对 Windows 用户的某些程序包也是有用的。安装完 pip 之后，你可以执行下列命令安装所需要的包：

`sudo pip install numpy pandas matplotlib jupyter`

## 开始项目

关于本项目，你可以在[机器学习项目  GitHub](https://github.com/udacity/machine-learning)中的 `titanic_survival_exploration` 文件夹下找到项目必须的文件，在 `projects` 文件夹下。你也可以直接从这个代码库中下载本纳米学位所有项目将用到的文件。在完成任务时，请确保你使用的是项目文件的最新版本。

本项目包含三个文件：

- `titanic_survival_exploration.ipynb`：这是最主要的文件，项目中的主要工作都将在这个文件上完成。
- `titanic_data.csv`：项目数据集。你将需要把这些数据加载到 notebook 里。
- `visuals.py`：这个 Python 脚本包含 helper 函数，可以让数据和存活结果可视化。

在终端或命令行窗口中，转到包含项目文件的文件夹，然后使用命令 `jupyter notebook finding_donors.ipynb` 打开浏览器窗口或标签页来处理你的 notebook。此外，你可以使用命令 `jupyter notebook` 或 `ipython notebook` 在打开的浏览器窗口中转到该 notebook 文件。按照 notebook 中的说明操作，并回答其中的每个问题，这样才能成功完成项目。除了项目文件外，我们还提供了 **README** 文件，其中可能包含关于项目的其他必要信息或说明。
## 提交项目

### 评估
优达学城的审阅专家将根据**<a href="https://review.udacity.com/#!/rubrics/147/view" target="_blank"> 探索泰坦尼克号乘客存活情况项目审阅标准</a>**来审阅你的项目。在提交项目之前，确保仔细阅读该审阅标准并对项目进行自我评估。必须满足该审阅标准中的所有*规范条件*，才能通过审阅。

### 提交文件
准备好提交项目后，收集以下文件并将它们压缩成一个文件以准备上传。此外，你可以在 GitHub Repo 上叫做 `titanic_survival_exploration` 的文件夹中提供以下文件，以便我们能轻松访问你的文件：

- `titanic_survival_exploration.ipynb` notebook 文件，回答了所有问题，执行了所有代码单元格并显示输出。
- 项目 notebook 的 **HTML** 导出文件，名称为 **report.html**。Notebook 底部有到处 HTML 文件的说明。你也许需要先安装 [mistune](https://pypi.python.org/pypi/mistune) 包，比如在终端中通过 `pip install mistune` 进行安装。

收集好这些文件并阅读项目审阅标准完毕后，请转到项目提交页面。

### 我准备好了！
当你准备好提交项目时，请点击页面底部的**提交项目**按钮。

如果你在提交项目时遇到任何问题，或是想确认你的提交状态，请向我们发送电子邮件 (**support@youdaxue.com**) 或访问我们的<a href="https://discussions.youdaxue.com" target="_blank">论坛</a>。

### 接下来会发生什么？
审阅专家会将反馈发送到你的电子邮箱。在此期间，请继续学习后面的项目和内容！
