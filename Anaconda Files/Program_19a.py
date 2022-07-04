# Program_19a.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
# using the make_blobs dataset
X, y = make_blobs(n_samples=100, centers=5, random_state=101)
# setting the number of training examples
m=X.shape[0]
n=X.shape[1] 
n_iter=50
# computing the initial centroids randomly
K=5
import random
# creating an empty centroid array
centroids=np.array([]).reshape(n,0) 
# creating 5 random centroids
for k in range(K):
  centroids=np.c_[centroids,X[random.randint(0,m-1)]]
output={}

# creating an empty array
euclid=np.array([]).reshape(m,0)

# finding distance between for each centroid
for k in range(K):
       dist=np.sum((X-centroids[:,k])**2,axis=1)
       euclid=np.c_[euclid,dist]

# storing the minimum value we have computed
minimum=np.argmin(euclid,axis=1)+1
# computing the mean of separated clusters
cent={}
for k in range(K):
    cent[k+1]=np.array([]).reshape(2,0)

# assigning of clusters to points
for k in range(m):
  cent[minimum[k]]=np.c_[cent[minimum[k]],X[k]]
for k in range(K):
  cent[k+1]=cent[k+1].T

# computing mean and updating it
for k in range(K):
  centroids[:,k]=np.mean(cent[k+1],axis=0)
# repeating the above steps again and again
for i in range(n_iter):
  euclid=np.array([]).reshape(m,0)
  for k in range(K):
    dist=np.sum((X-centroids[:,k])**2,axis=1)
    euclid=np.c_[euclid,dist]
    C=np.argmin(euclid,axis=1)+1
    cent={}
  for k in range(K):
    cent[k+1]=np.array([]).reshape(2,0)
  for k in range(m):
    cent[C[k]]=np.c_[cent[C[k]],X[k]]
  for k in range(K):
    cent[k+1]=cent[k+1].T
  for k in range(K):
    centroids[:,k]=np.mean(cent[k+1],axis=0)
  final=cent
plt.scatter(X[:,0],X[:,1])
plt.rcParams.update({'figure.figsize':(10,7.5), 'figure.dpi':100})
plt.title('Original Dataset')

plt.figure()
for k in range(K):
  plt.scatter(final[k+1][:,0],final[k+1][:,1],marker="+")
plt.scatter(centroids[0,:],centroids[1,:],s=300,marker="+",c='black')
plt.rcParams.update({'figure.figsize':(10,7.5), 'figure.dpi':100})
plt.show()

plt.figure()
X, y = make_blobs(n_samples=100, centers=5, random_state=101)
from sklearn.cluster import KMeans
elbow=[]
for i in range(1, 20):
  kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 101)
  kmeans.fit(X)
  elbow.append(kmeans.inertia_)
sns.lineplot(range(1, 20), elbow,color='blue')
plt.rcParams.update({'figure.figsize':(10,7.5), 'figure.dpi':100})
plt.title('ELBOW METHOD')
plt.show()
