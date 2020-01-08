"""K-means clustering"""

# Authors: Liang.he 378887701@qq.com
# License: BSD 3 clause

# 通过简单的例子来直接查看K均值聚类的效果
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# 聚类前
X = np.random.rand(100, 2)
plt.scatter(X[:, 0], X[:, 1], marker='o')