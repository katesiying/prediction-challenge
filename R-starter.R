# Data manipulation, visualization
library(data.table)
library(ggplot2)

# regularized linear regression
# Elastic net prediction
# LASSO, ridge are implemented as special cases of elastic net

# Elastic net
library(glmnet)

# LASSO
glmnet(alpha = 1)

# Ridge
glmnet(alpha = 0)

# Random forest
library(randomForest)

# Regression tree
library(rpart)

# Deep neural network
library(doParallel)
library(h2o)

# caret is a great package for streamlining prediction,
# in particular, automated cross-validation
# https://topepo.github.io/caret/index.html
library(caret)