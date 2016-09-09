import numpy as np
from openpyxl import load_workbook
import pandas as pd
from scipy import stats
import math
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn import linear_model

def get_data(file_name):
    train = pd.read_excel(file_name)
    data = pd.DataFrame(train, columns=['allT', 'allP','BirminghamT','all_secT','all_secP','all_primT','all_primP',	'BirminghamP',	'NorfolkT',	'NorfolkP',	'SuffolkT',
                                        'SuffolkP', 'ShropshireT',	'ShropshireP',	'EssexT',	'EssexP',	'LeedsT',
                                        'LeedsP', 'LancashireT',	'LancashireP',	'LeicestershireT',	'LeicestershireP',
                                        'LincolnshireT', 'LincolnshireP', 'CumbriaT',	'CumbriaP',	'GatesheadT',
                                        'GatesheadP',	'South_TynesideT',	'South_TynesideP',	'SunderlandT',
                                        'SunderlandP',	'BuryT',	'BuryP',	'SalfordT',	'SalfordP',	'EalingT',
                                        'EalingP',	'HaveringT',	'HaveringP'])

    return data

def mean_absolute_diff(dataset1,dataset2,):
    result = []
    for index in xrange(len(dataset1)):
        tmp = dataset1[index] - dataset2[index]
        result.append(tmp)
    mean = np.mean(result)
    # std = stats.sem(result, axis=None, ddof=0)
    std = np.std(result)/np.sqrt(len(result))
    return mean,std
    # return np.mean(dataset1) - np.mean(dataset2)

def mean_relative_diff(dataset1,dataset2,):
    result = []
    for index in xrange(len(dataset1)):
        tmp = (dataset1[index] - dataset2[index])/np.mean(dataset2)
        result.append(tmp)
    mean = np.mean(result)
    std = stats.sem(result, axis=None, ddof=0)
    return mean, std
    # return (np.mean(dataset1) - np.mean(dataset2))/np.mean(dataset2)



data= get_data('/Users/YuanXue/Dropbox/true_projected.xlsx')

t, p = stats.ttest_ind(data['South_TynesideT'], data['South_TynesideP'], equal_var=False)
print("ttest_ind:            t = %g  p = %g" % (t, p))
mad, mad_std = mean_absolute_diff(data['South_TynesideT'], data['South_TynesideP'])
print ("mean absolute difference: %f" % mad)
print ("mean absolute difference stderr: %f" % mad_std)
a = mad+2*mad_std
b = mad-2*mad_std
print ("Confidence interval: (%f,%f)" % (b,a))
mrd, mrd_std = mean_relative_diff(data['South_TynesideT'], data['South_TynesideP'])
print ("mean relative difference: %f" % mrd)
print ("mean relative difference stderr: %f" % mrd_std)
c = mrd+1.96*mrd_std
d = mrd-1.96*mrd_std
print ("Confidence interval: (%f,%f)" % (d, c))