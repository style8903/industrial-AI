from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
from sklearn.metrics import adjusted_rand_score

X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
kmeans = KMeans(n_clusters=3).fit(X)
print("Labels:", kmeans.labels_)
print("Cluster Centers:", kmeans.cluster_centers_)
print("Predict Values:", kmeans.predict([[1,1]]))

#2
sample_df = pd.read_csv("r15.csv")

training_points = sample_df[["col1", "col2"]]
training_labels = sample_df["target"]

kmeans = KMeans(n_clusters=15).fit(training_points)

plt.scatter(training_points["col1"], training_points["col2"], c=kmeans.labels_,cmap='rainbow')
plt.show()

#3
dbscan = DBSCAN(eps=0.6, min_samples=10).fit(training_points)
plt.scatter(training_points["col1"], training_points["col2"], c=dbscan.labels_, cmap='rainbow')
plt.show()

#4
agglo = AgglomerativeClustering(n_clusters=15).fit(training_points)
plt.scatter(training_points["col1"], training_points["col2"], c=agglo.labels_, cmap='rainbow')
plt.show()

#5
arc = adjusted_rand_score(training_labels, kmeans.labels_)
print(arc)
arc = adjusted_rand_score(training_labels, dbscan.labels_)
print(arc)