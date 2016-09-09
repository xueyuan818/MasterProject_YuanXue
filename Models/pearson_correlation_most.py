import os
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
def get_data(file_name):
    csv = np.genfromtxt(file_name, delimiter=',')
    data = csv[1:, 4:]
    label = csv[1:, 3]
    return data, label
def get_test(file_name):
    csv = np.genfromtxt(file_name, delimiter=',')
    data = csv[1:178, 3:]
    return data

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    data, label = get_data('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/Final_data/Normalization_all.csv')
    test_pilot = get_test('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/pilot/Final_Norm/all_prim.csv')
    regr = linear_model.ElasticNetCV(fit_intercept=True, normalize=False, l1_ratio=0.5, tol=0.01, cv=10)
    regr.fit(data, label)
    result_pilot = regr.predict(test_pilot)


    for allDir in pathDir:
        if "DS_Store" not in allDir:
            child = os.path.join('%s/%s' % (filepath, allDir))
            test_control = get_test(str(child))
            result_control = regr.predict(test_control)
            r_row, p_value = pearsonr(result_control[58:,], result_pilot[58:,])
            print float('%.8f' % r_row)

if __name__ == '__main__':
    filePathC = '/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/control/Final_Norm/All'
    a = []
    eachFile(filePathC)






