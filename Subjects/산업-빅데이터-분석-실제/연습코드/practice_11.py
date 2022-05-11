import matplotlib.pyplot as plt
import numpy as np

#1
from sklearn.neighbors import KNeighborsClassifier

classfier = KNeighborsClassifier(n_neighbors=1)

training_points = [
    [0.5, 0.2, 0.1],
    [0.9, 0.7, 0.3],
    [0.4, 0.5, 0.7]
]
training_labels = [0,1,1]

classfier.fit(training_points, training_labels)

unkown_points = [
    [0.2, 0.1, 0.7]
]

guesses = classfier.predict(unkown_points)
print(guesses)

#2
training_points = [
    [158,58],
    [158,59],
    [158,63],
    [160,59],
    [160,60],
    [163,60],
    [163,61],
    [160,64],
    [163,64],
    [165,61],
    [165,62],
    [165,65],
    [168,62],
    [168,63],
    [168,66],
    [170,63],
    [170,64],
    [170,68]
]

training_labels = [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1]
unkown_points = [
    [161, 61],
]

from sklearn.neighbors import KNeighborsClassifier
classfier = KNeighborsClassifier(n_neighbors=3)
classfier.fit(training_points,training_labels)

guesses = classfier.predict(unkown_points)
print(guesses)


#3
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(training_points, training_labels, test_size=0.2, random_state=4)

classfier = KNeighborsClassifier(n_neighbors=1)
classfier.fit(X_train, y_train)

guesses = classfier.predict(X_test)
print(guesses)

from sklearn.metrics import confusion_matrix
from sklearn import metrics

print(confusion_matrix(y_test, guesses))
print(metrics.accuracy_score(y_test, guesses))
print(metrics.precision_score(y_test,guesses,average='binary'))
print(metrics.recall_score(y_test,guesses,average='binary'))
print(metrics.f1_score(y_test,guesses,average='binary'))


#4
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
training_points = cancer.data
training_labels = cancer.target

X_train,X_test, y_train, y_test = train_test_split(training_points, training_labels, test_size=0.2, random_state=4)

classfier = KNeighborsClassifier(n_neighbors=5)
classfier.fit(X_train, y_train)

guesses = classfier.predict(X_test)
print(confusion_matrix(y_test, guesses))