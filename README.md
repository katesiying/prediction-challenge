# Prediction Challenge
This exercise is adapted from Sendhil's ML course in 2019.

## Description
In this challenge, you will develop machine learning algorithms to predict patient annual total medical expenditures. The data is the Medical Expenditure Panel Survey (MEPS) from 2013-2016, downloaded from [IPUMS](https://meps.ipums.org/meps/about_IPUMS_MEPS.shtml). Each observation is a patient-year. Patients are uniquely identified by the variable `mepsid`. Some patients have two years of data (i.e., two observations) while others have only one. Patients are randomly divided into the training set (75%) and the hold-out set (25%), so that for patients with two observations, they are both in the train or the test set. Variable definitions and codings are provided in the file `meps_codebook.txt`. 

To predict total medicial expenditure `exptot`, you will build predictive algorithms using the data in `meps_train.csv`. The goal is to optimize predictive accuracy, measured by the mean squared error on new data E[yhat - y)^2].


## Guidelines
Before you start to build models, warm up and get a sense of the data by loading it into your computer and forming table of summary statistics. Then you are in a good shape to come up with predictors of medical expenses.

Once you complete the prediction challenge (i.e., obtain the best algorithm that you can come up with), you will use your algorithm to predict medical spending for the observations in the hold-out set `meps_holdout.csv`. Note that this data currently does not list the actual `exptot` variable. On Monday nigiht at 8pm, I will release the ground truth, so that you can evaluate the performance of your algorithm.

This exercise is intended to give you some handson experience with building actual prediction algorithms. It will not be graded. However, to help you reflect on some of the themes we talked about, note the following:

- the steps you felt were key to your algorithm
- how to handle non-crossectional data
- sample size: K in K-fold CV, proportion for train-test split
- which tuning parameters matter
- feature engineering: throw all in? use prior knowledge?


## Additional resources
You may choose any programming language that you feel comfortable with. Starter code is provided in python and R. We have not covered deep learning yet, so just experiment with regularized regression, trees, and random forests for now.

Examples of training different algorithms are abundant online. The following are great for starting out:
- [Applied ML in python](https://github.com/tfolkman/byu_econ_applied_machine_learning/tree/master/lectures) written in jupyter notebook
- [Hands-on ML in R](https://bradleyboehmke.github.io/HOML/) and [Kaggle ML tutorial in R](https://www.kaggle.com/camnugent/introduction-to-machine-learning-in-r-tutorial)
- [scikit-learn](https://scikit-learn.org/stable/tutorial/index.html) official tutorial for python users
- [R-bloggers post](https://www.r-bloggers.com/2022/02/beginners-guide-to-machine-learning-in-r-with-step-by-step-tutorial/) laying out keys steps in the pipeline

