# %load q02_Max_important_feature/build.py
# Default imports
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data
import numpy as np

# We have already loaded the data for you
data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')

# Write your code here
def Max_important_feature(data_set,target_variable='SalePrice',n=4):
    arr = np.array(data_set.corr()[target_variable].sort_values(ascending=False).index)
    return arr[1:n+1]





