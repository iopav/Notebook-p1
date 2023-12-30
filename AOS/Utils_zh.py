def basic_stats(data):
    import numpy as np
    from scipy.stats import skew, kurtosis
    print("mean: %.2f\tstd: %.2f\tskew: %.2f\tkurtosis: %.2f" % (np.mean(data),np.std(data),skew(data),kurtosis(data,fisher=False)))

def showURL(url, ht=600):
    """Return an IFrame of the url to show in notebook with height ht"""
    from IPython.display import IFrame
    return IFrame(url, width='95%', height=ht)

def load_sms():
    """
    A wrapper function to load the sms data
    """
    import csv
    lines = []
    hamspam = {'ham': 0, 'spam': 1}
    with open('data/spam.csv', mode='r',encoding='latin-1') as f:
        reader = csv.reader(f)
        # When using the csv reader, each time you use the function
        # next on it, it will spit out a list split at the ','
        header = next(reader)
        # We store this as ("txt",label), where we have used the function
        # hamspam to convert from "ham","spam" to 0 and 1.
        lines = [(line[1],hamspam[line[0]]) for line in reader]

    return lines

def discrete_histogram(data, normed=False, alpha=1):
    """
    生成离散数据的直方图。

    Parameters:
    -----------
    data : array-like
        包含离散数据的数组或类似数组。
    normed : bool, optional (默认为 False)
        是否将直方图的高度归一化，使其成为相对频率。如果为 True，则将直方图的高度除以数据点总数，以得到相对频率。
    alpha : float, optional (默认为 1)
        直方图的透明度。范围从0（完全透明）到1（完全不透明）。

    Returns:
    -----------
    None

    Plots:
    -----------
    直方图可视化，显示离散数据的分布。

    Examples:
    -----------
    >>> data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> discrete_histogram(data, normed=True, alpha=0.7)
    >>> plt.show()
    """
    import numpy as np
    import matplotlib.pyplot as plt

    # 计算数据的唯一值和对应的计数
    bins, counts = np.unique(data, return_counts=True)

    # 计算直方图条的宽度
    width = np.min(np.diff(bins)) / 4

    # 绘制直方图
    if normed:
        plt.bar(bins, counts / np.sum(counts), width=width, alpha=alpha)
    else:
        plt.bar(bins, counts, width=width, alpha=alpha)


def plotEMF(numRelFreqPairs, force_display=True):
    """
    绘制经验质量函数（Empirical Mass Function）的散点图。

    Parameters:
    -----------
    numRelFreqPairs : array-like
        包含相对频率对的二维数组，第一列为键，第二列为相对频率。
    force_display : bool, optional (默认为 True)
        是否强制显示绘图。

    Returns:
    -----------
    None

    Plots:
    -----------
    绘制经验质量函数的散点图，以及在每个点的垂直线。

    Examples:
    -----------
    >>> numRelFreqPairs = np.array([[1, 0.1], [2, 0.3], [3, 0.6], [4, 1.0]])
    >>> plotEMF(numRelFreqPairs, force_display=True)
    >>> plt.show()
    """

    import matplotlib.pyplot as plt
    import numpy as np

    numRelFreqPairs = np.array(numRelFreqPairs)

    # 绘制散点图
    plt.scatter(numRelFreqPairs[:, 0], numRelFreqPairs[:, 1])
    plt.scatter(numRelFreqPairs[:, 0], numRelFreqPairs[:, 1])

    # 为每个元组绘制垂直线
    for k in numRelFreqPairs:
        kkey, kheight = k  # 解包元组
        plt.vlines([kkey], 0, kheight, linestyle=':')

    # 强制显示图形
    if force_display:
        plt.show()


def makeFreq(data_sequence):
    """
    从可迭代的数据序列中生成一个包含键值对的 NumPy 数组，其中键是数据序列中的唯一值，值是它们出现的次数。

    Parameters:
    -----------
    data_sequence : iterable
        包含数据序列的可迭代对象。

    Returns:
    -----------
    numpy.ndarray
        由键和相应计数组成的数组，形状为 [keys, counts]。

    Examples:
    -----------
    >>> data_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> makeFreq(data_sequence)
    array([[1, 1],
           [2, 2],
           [3, 3],
           [4, 4]])
    """
    import numpy as np

    data = np.array(data_sequence)

    if len(data.shape) == 2:
        # 对于二维数组，沿轴0进行转置，并返回唯一值及其计数
        (keys, counts) = np.unique(data.T, axis=0, return_counts=True)
        return np.concatenate([keys, counts.reshape(-1, 1)], axis=1)
    else:
        # 对于一维数组，返回唯一值及其计数
        (keys, counts) = np.unique(data, return_counts=True)
        return np.stack([keys, counts], axis=-1)

def makeEMF(data_sequence):
    """
    从数据序列生成经验质量函数（Empirical Mass Function）。

    Parameters:
    -----------
    data_sequence : iterable
        包含数据序列的可迭代对象。

    Returns:
    -----------
    numpy.ndarray
        由键和相对频率组成的数组，形状为 [keys, norm_freqs]，其中 norm_freqs 是相对频率。

    Examples:
    -----------
    >>> data_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> makeEMF(data_sequence)
    array([[1. , 0.1],
           [2. , 0.2],
           [3. , 0.3],
           [4. , 0.4]])
    """
    from Utils import makeFreq
    import numpy as np

    # 使用 makeFreq 函数获取相对频率
    relFreq = makeFreq(data_sequence)

    # 计算总和并计算相对频率
    total_sum = np.sum(relFreq[:, 1])
    norm_freqs = relFreq[:, 1] / total_sum

    # 返回由键和相对频率组成的数组
    return np.stack([relFreq[:, 0], norm_freqs], axis=-1)

def makeEDF(data_sequence):
    """
    从数据序列生成经验分布函数（Empirical Distribution Function）。

    Parameters:
    -----------
    data_sequence : iterable
        包含数据序列的可迭代对象。

    Returns:
    -----------
    numpy.ndarray
        由键和累积频率组成的数组，形状为 [keys, cumFreqs]。

    Examples:
    -----------
    >>> data_sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> makeEDF(data_sequence)
    array([[1., 0.1],
           [2., 0.3],
           [3., 0.6],
           [4., 1. ]])
    """
    import numpy as np

    # 使用 makeFreq 函数获取键和计数
    numRelFreqPairs = makeFreq(data_sequence)
    (keys, counts) = (numRelFreqPairs[:, 0], numRelFreqPairs[:, 1])

    # 计算频率和经验质量函数
    frequencies = counts / np.sum(counts)
    emf = np.stack([keys, frequencies], axis=-1)

    # 计算累积频率
    cumFreqs = np.cumsum(frequencies)
    edf = np.stack([keys, cumFreqs], axis=-1)

    # 返回由键和累积频率组成的数组
    return edf


def emfToEdf(emf):
    """
    将经验质量函数（Empirical Mass Function）转换为经验分布函数（Empirical Distribution Function）。

    Parameters:
    -----------
    emf : numpy.ndarray or list
        经验质量函数，由键和相对频率组成的数组。

    Returns:
    -----------
    numpy.ndarray
        由键和累积频率组成的数组，形状为 [keys, cumFreqs]。

    Examples:
    -----------
    >>> emf = np.array([[1, 0.1], [2, 0.2], [3, 0.3], [4, 0.4]])
    >>> emfToEdf(emf)
    array([[1., 0.1],
           [2., 0.3],
           [3., 0.6],
           [4., 1. ]])
    """
    import numpy as np

    # 如果输入是列表，则转换为 NumPy 数组
    if type(emf) == list:
        emf = np.array(emf)

    # 提取键和相对频率
    keys = emf[:, 0]
    frequencies = emf[:, 1]

    # 计算累积频率
    cumFreqs = np.cumsum(frequencies)

    # 返回由键和累积频率组成的数组
    edf = np.stack([keys, cumFreqs], axis=-1)
    return edf


def plotEDF(edf, force_display=True, points_at_jump=True, confidence_band=False, alpha=0.95):
    """
    绘制经验分布函数（Empirical Distribution Function，EDF）的图形。

    Parameters
    ----------
    edf : numpy.ndarray
        由键和累积频率组成的数组，形状为 [keys, cumFreqs]，通常由 makeEDF 函数生成。
    force_display [True] : bool
        是否强制显示图形。
    points_at_jump [True] : bool
        是否在跳跃位置处绘制点。
    confidence_band [False] : bool
        是否使用 DKW 不等式绘制置信带。
    alpha [0.95] : float
        置信水平，用于计算置信带。

    Returns:
    ----------
    None

    Examples:
    -----------
    >>> keys = np.array([1, 2, 3, 4])
    >>> cumFreqs = np.array([0.1, 0.3, 0.6, 1.0])
    >>> edf = np.stack([keys, cumFreqs], axis=-1)
    >>> plotEDF(edf)
    (displays the EDF plot)
    """
    import matplotlib.pyplot as plt
    import numpy as np

    keys = edf[:, 0]
    cumFreqs = edf[:, 1]

    # 在跳跃位置处绘制点
    if points_at_jump:
        plt.scatter(keys, cumFreqs)

    # 绘制水平线和垂直线
    plt.hlines(cumFreqs[:-1], keys[:-1], keys[1:])
    plt.vlines(keys[1:], cumFreqs[:-1], cumFreqs[1:], linestyle=':')

    # 使用 DKW 不等式绘制置信带
    if confidence_band:
        def calcEpsilon(alpha, n):
            return (1 / np.sqrt(n)) * np.sqrt((1 / 2) * np.log(2 / (1 - alpha)))

        epResidual = calcEpsilon(alpha, len(cumFreqs))
        plt.fill_between(
            keys,
            np.maximum(cumFreqs - epResidual, 0),
            np.minimum(cumFreqs + epResidual, 1),
            alpha=0.4,
            color='green',
            step="post"
        )

    # 添加标题
    plt.title("Empirical Distribution Function")

    # 强制显示图形
    if force_display:
        plt.show()
def linConGen(m, a, b, x0, n):
    '''
    线性同余序列生成器。

    Parameters:
    -----------
    m : int
        在生成器中使用的整数模数。
    a : int
        整数乘数。
    b : int
        整数增量。
    x0 : int
        整数种子。
    n : int
        所需伪随机数的数量。

    Returns:
    --------
    list
        一个包含 n 个模 m 的伪随机整数的列表。

    Examples:
    ---------
    >>> linConGen(10, 3, 7, 4, 5)
    [4, 5, 0, 7, 6]
    '''
    x = x0  # 种子
    retValue = [x % m]  # 用 x=x0 开始列表
    for i in range(2, n + 1, 1):
        x = (a * x + b) % m  # 生成器，使用模算术
        retValue.append(x)  # 将新的 x 添加到列表
    return retValue

def scatter3d(x,y,z,c=None,size=2,fig=None):
    import plotly.graph_objects as go
    import numpy as np


    if (c == None):
        data = go.Scatter3d(x=x, y=y, z=z,mode='markers',marker=dict(size=size))
        if (fig):
            fig.add_trace(data)
        else:
            fig = go.Figure(data=[data])
    else:
        data = go.Scatter3d(x=x, y=y, z=z,mode='markers',marker=dict(size=size,color=c))
        if (fig):
            fig.add_trace(data)
        else:
            fig = go.Figure(data=[data])
    return fig

def classification_report_interval(
    y_true,
    y_pred,
    labels=None,
    alpha = 0.01,
    union_bound_correction=True
):
    """Produces a classification report with precision, recall and accuracy
    It also uses Hoeffdings inequality to produce confidence intervals around
    each measurement. We can do this with or without multiple measurement
    correction (union bound correction).

    Example output is:
                labels           precision             recall

               0.0  0.88 : [0.50,1.00] 0.40 : [0.15,0.65]
               1.0  0.56 : [0.34,0.78] 0.93 : [0.65,1.00]

          accuracy                                        0.64 : [0.45,0.83]

    Parameters:
    y_true                          -- The true labels
    y_pred                          -- The predicted labels
    labels                          -- TODO
    alpha[0.01]                     -- The confidence level of the intervals
    union_bound_correction[True]    -- If we should compensate with the union bound because we
                                    have multiple intervals to compute in order to keep the level
                                    of confidence for all intervals jointly.

    Returns:
    a printable string.
    """
    import numpy as np

    def precision_recall(y_true,
        y_pred,
        labels=None,alpha=0.01, correction=1):
        p = []
        r = []
        f1 = []
        support = []
        for label in labels:
            y_true_pred_label = y_true[y_pred == label]
            precision = np.mean(y_true_pred_label == label)
            delta = (1/np.sqrt(len(y_true_pred_label)))*np.sqrt((1/2)*np.log(2*correction/alpha))
            p.append("%.2f : [%.2f,%.2f]" % (precision, np.maximum(precision-delta,0),np.minimum(precision+delta,1)))

            y_pred_true_label = y_pred[y_true == label]
            recall = np.mean(y_pred_true_label == label)
            delta = (1/np.sqrt(len(y_pred_true_label)))*np.sqrt((1/2)*np.log(2*correction/alpha))
            r.append("%.2f : [%.2f,%.2f]" % (recall, np.maximum(recall-delta,0),np.minimum(recall+delta,1)))

        return (p,r)

    def accuracy_interval(y_true,y_pred,alpha=0.01,correction=1):
        acc = np.mean(y_true == y_pred)
        delta = (1/np.sqrt(len(y_true)))*np.sqrt((1/2)*np.log(2*correction/alpha))
        return "%.2f : [%.2f,%.2f]" % (acc, np.maximum(acc-delta,0),np.minimum(acc+delta,1))

    digits = 18
    target_names = None
    if labels is None:
        labels = list(set(y_true).union(set(y_pred)))
        labels_given = False
    else:
        labels = np.asarray(labels)
        labels_given = True

    target_names = ["%s" % l for l in labels]

    headers = ["precision", "recall"]
    # compute per-class results without averaging
    # Simple correction using the union bound
    # We are computing 2 intervals for each label for precision and recall
    # In addition we are computing 2 intervals for accuracy
    # This is in total 2*n_labels+2
    if (union_bound_correction):
        correction = 2*len(labels)+2
    else:
        correction=1
    p, r = precision_recall(
        y_true,
        y_pred,
        labels=labels,
        alpha=alpha,
        correction=correction
    )

    rows = zip(target_names, p, r)

    name_width = max(len(cn) for cn in target_names)
    width = max(name_width, digits)
    head_fmt = "{:>{width}s} " + " {:>{digits}}" * len(headers)
    report = head_fmt.format("labels", *headers, width=width,digits=digits)
    report += "\n\n"
    row_fmt = "{:>{width}s} " + " {:>{digits}s}" * 2 + "\n"
    for row in rows:
        report += row_fmt.format(*row, width=width, digits=digits)
    row_fmt_acc = "{:>{width}s} " + " {:>{digits}s}" * 2 + " {:>{digits}s}""\n"
    report += "\n"
    accuracy = accuracy_interval(y_true,y_pred,alpha=alpha,correction=correction)
    report+=row_fmt_acc.format(*("accuracy","","",accuracy),width=width,digits=digits)

    return report
def bennett_epsilon(n, b, sigma, alpha):
    """
    使用贝内特不等式计算 P(|X - E[X]| >= epsilon) < alpha 的 epsilon。

    Parameters:
    -----------
    n : int
        样本数。
    b : float
        |X| <= b。
    sigma : float
        X 的标准差。
    alpha : float
        显著性水平。

    Returns:
    --------
    float
        epsilon。

    Examples:
    ---------
    >>> bennett_epsilon(100, 2, 1, 0.05)
    0.5243
    """
    import scipy.optimize as so
    import numpy as np

    h = lambda u: (1 + u) * np.log(1 + u) - u
    f = lambda epsilon: np.exp(-n * sigma ** 2 / b ** 2 * h(b * epsilon / sigma ** 2)) - alpha / 2
    ans = so.fsolve(f, 0.002)
    epsilon = np.abs(ans[0])
    print("Numerical error", f(epsilon))
    return epsilon

def epsilon_bounded(n, b, alpha):
    """
    使用 Hoeffding 不等式计算使得 P(|X - E[X]| >= epsilon) < alpha 的 epsilon。

    Parameters:
    -----------
    n : int
        样本数。
    b : float
        |X| <= b。
    alpha : float
        显著性水平。

    Returns:
    --------
    float
        epsilon。

    Examples:
    ---------
    >>> epsilon_bounded(100, 2, 0.05)
    0.578
    """
    import numpy as np
    return b * np.sqrt(-1 / (2 * n) * np.log(alpha / 2))

def print_confidence_interval(point_estimate,epsilon,min_value=None,max_value=None):
    """
    Simply prints [point_estimate-epsilon,point_estimate+epsilon]

    Parameters
    ----------
    point_estimate : the center of the interval
    epsilon : the half interval length
    min_value : replace (point_estimate-epsilon) with max(point_estimate-epsilon,min_value)
    max_value : replace (point_estimate-epsilon) with min(point_estimate-epsilon,max_value)
    """
    import numpy as np
    if (min_value != None):
        l_edge = np.maximum(point_estimate-epsilon,min_value)
    else:
        l_edge = point_estimate-epsilon

    if (max_value != None):
        r_edge = np.minimum(point_estimate+epsilon,max_value)
    else:
        r_edge = point_estimate+epsilon

    print("[%.2f,%.2f]" % (l_edge,r_edge))
def train_test_validation(X, Y, test_size=0.2, validation_size=0.2, random_state=None, shuffle=True):
    """
    执行数据的训练测试验证划分 [train_data, test_data, validation_data]

    参数:
    -----------
    X : 输入 X，形状 (n_samples, n_features)
    Y : 输入标签，形状 (n_samples)
    test_size : 测试数据的比例
    validation_size : 验证数据的比例
    random_state : 传递给 sklearn 的随机状态变量
    shuffle : 是否打乱数据

    返回:
    ----------
    X_train, X_test, X_valid, Y_train, Y_test, Y_valid

    示例:
    ----------
    >>> X_train, X_test, X_valid, Y_train, Y_test, Y_valid = train_test_validation(X, Y, test_size=0.25, validation_size=0.25)
    """
    from sklearn.model_selection import train_test_split

    X_train, X_tt, Y_train, Y_tt = train_test_split(X, Y,
                                                    test_size=test_size + validation_size,
                                                    random_state=random_state,
                                                    shuffle=shuffle)
    X_test, X_valid, Y_test, Y_valid = train_test_split(X_tt, Y_tt,
                                                        test_size=(validation_size) / (test_size + validation_size),
                                                        random_state=random_state,
                                                        shuffle=shuffle)

    return X_train, X_test, X_valid, Y_train, Y_test, Y_valid
