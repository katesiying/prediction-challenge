# Data manipulation, visualization
import pandas as pd
import numpy as np
import seaborn as sns
import time
import matplotlib.pyplot as plt

# package to standardize/normalize the data
import sklearn.preprocessing as pre

# we may not need these generic functions, just code up on our own
# to be more flexible 
from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV

# package to calculate (estimated) predictive accuracy
from sklearn.metrics import mean_squared_error, make_scorer

# regularized linear regression model
from sklearn.linear_model import LassoCV, ElasticNetCV, RidgeCV, ElasticNet

# random forest
from sklearn.ensemble import RandomForestRegressor

# trees
from sklearn.tree import DecisionTreeRegressor

# deep neural network
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

