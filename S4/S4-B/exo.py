""" EXERCICE 2"""
import seaborn as sns
import numpy as np 

data = np.random.binomial(1,0.7,size = 100000)
sns.distplot(data)
data_split = np.array_split(data,1000)
mean_split = [np.mean(a) for a in data_split]
mu = np.mean(mean_split)
std = np.std(mean_split)
norm = np.random.normal(mu,std,1000)

sns.distplot(mean_split)
sns.distplot(norm,hist=False)
plt.show()

# loi gamma
data = np.random.gamma(4,2, size = 1000000)
sns.distplot(data)
data_split = np.array_split(data,1000)
mean_split = [np.mean(a) for a in data_split]
mu = np.mean(mean_split)
std = np.std(mean_split)
norm = np.random.normal(mu,std,1000)

sns.distplot(mean_split)
sns.distplot(norm,hist=False)
plt.show()

# loi poisson
data = np.random.poisson(lam = 4, size = 100000)
sns.distplot(data)
data_split = np.array_split(data,1000)
mean_split = [np.mean(a) for a in data_split]
mu = np.mean(mean_split)
std = np.std(mean_split)
norm = np.random.normal(mu,std,1000)

sns.distplot(mean_split)
sns.distplot(norm,hist=False)
plt.show()

import random
random.seed(123)
random.normalvariate(mu = 0, sigma = 1)

