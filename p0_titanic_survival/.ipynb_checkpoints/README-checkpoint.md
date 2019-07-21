# 机器学习工程师纳米学位 
## 简介和基础知识
## 项目：探索泰坦尼克号乘客存活情况
### 安装

本项目要求安装 **Python 2.7** 和以下 Python 库：

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

你还需要安装软件，才能运行并执行 [Jupyter Notebook](http://ipython.org/notebook.html)。

如果你还未安装 Python，我们强烈推荐你安装 Python 发行版：[Anaconda](http://continuum.io/downloads)，其具备包括上述程序包在内的更多程序包。安装时，确保你选择的是 Python 2.7 安装程序，而不是 Python 3.x 安装程序。

### 代码

你可以在 notebook 文件 `titanic_survival_exploration.ipynb` 中找到代码模板。在 `visuals.py` 文件中有额外的辅助代码。我们已经提供了一些初始代码来帮助你开始，你需要补充额外函数来顺利完成本项目。请注意，学员无需更改 `visuals.py` 中的代码。如果你对 notebook 中的可视化文件感兴趣，请随意探索。

### 运行

在终端或命令行窗口中，跳转至最上面的项目目录 `titanic_survival_exploration/`（包含 README 文件），并运行如下命令：

```{.python .input}
jupyter notebook titanic_survival_exploration.ipynb
```

or

```{.python .input}
ipython notebook titanic_survival_exploration.ipynb
```

这将在你的浏览器中打开 iPython Notebook 软件和项目文件。

### 数据

本项目使用的数据集为 `titanic_data.csv`。该数据集由优达学城提供，并包含以下特征：

**特征**

- `Pclass`：社会阶层（1 = Upper class; 2 = Middle class; 3 = Lower class）
- `Name`：乘客姓名
- `Sex`：乘客性别
- `Age`：乘客年龄（某些条目为 `NaN`）
- `SibSp`：一起上船的兄弟姐妹和配偶人数
- `Parch`：一起上船的父母和子女人数
- `Ticket`：乘客的票号
- `Fare`：乘客支付的票价
- `Cabin`：乘客的客舱号（某些条目为 `NaN`）
- `Embarked`：乘客的登船港（C = Cherbourg; Q = Queenstown; S = Southampton）

**目标变量**
- `survival` : 存活结果 (0 = No; 1 = Yes)
