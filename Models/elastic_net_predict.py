# Required Packages
import numpy as np
import pandas as pd
import math
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
# Function to get data
def get_data_1(file_name):
    csv = np.genfromtxt(file_name, delimiter=',')
    data = csv[1:, 4:]
    label = csv[1:, 3]
    return data, label

def get_test(file_name):
    csv = np.genfromtxt(file_name, delimiter=',')
    data = csv[1:, 3:]
    return data

data1,label1 = get_data_1('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/Final_data/Normalization_all.csv')


test_control = get_test('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/control/Final_Norm/All/1245789.csv')

test_pilot = get_test('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/pilot/Final_Norm/all_prim.csv')

# test_pilot = get_test('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/Final_data/Normalization_all.csv')


regr1 = linear_model.ElasticNetCV(fit_intercept=True, normalize=False, tol=0.01,l1_ratio=0.5, cv=10)

regr1.fit(data1, label1)
result_control_1 = regr1.predict(test_control)
result_pilot_1 = regr1.predict(test_pilot)

r_row, p_value = pearsonr(result_control_1[58:,], result_pilot_1[58:,])
print r_row


np.savetxt("result_control.csv", result_control_1, delimiter=",")
np.savetxt("result_pilot.csv", result_pilot_1, delimiter=",")
