import numpy as np
from openpyxl import load_workbook
import pandas as pd
import math
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.cross_validation import train_test_split
from sklearn import linear_model

def get_data(file_name):
    train = pd.read_excel(file_name)
    data = pd.DataFrame(train, columns=['allT', 'allP','all_secT','all_secP','all_primT','all_primP','BirminghamT',	'BirminghamP',	'NorfolkT',	'NorfolkP',	'SuffolkT',
                                        'SuffolkP', 'ShropshireT',	'ShropshireP',	'EssexT',	'EssexP',	'LeedsT',
                                        'LeedsP', 'LancashireT',	'LancashireP',	'LeicestershireT',	'LeicestershireP',
                                        'LincolnshireT', 'LincolnshireP', 'CumbriaT',	'CumbriaP',	'GatesheadT',
                                        'GatesheadP',	'South_TynesideT',	'South_TynesideP',	'SunderlandT',
                                        'SunderlandP',	'BuryT',	'BuryP',	'SalfordT',	'SalfordP',	'EalingT',
                                        'EalingP',	'HaveringT',	'HaveringP'])


    # Birmingham = csv[2:34, 3:4]
    # East_Anglia = csv[2:34, 6:7]
    # Essex = csv[2:34, 9:10]
    # Leicestershire_Lincolnshire = csv[2:34, 12:13]
    # Leicestershire = csv[2:34, 15:16]
    # Lincolnshire = csv[2:34, 18:19]
    # Norfolk = csv[2:34, 21:22]
    # Shropshire = csv[2:34, 24:25]
    # Tyne_Wear = csv[2:34, 27:28]
    return data
def moving_average(dataset,window_size,):
    result = []
    for index in xrange(len(dataset)):
        if index -1 >= 0 and index + 1 < len(dataset):
            tmp = (dataset[index-1] + dataset[index] + dataset[index + 1]) / 3
            result.append(tmp)
        else:
            result.append(dataset[index])
    return result



data= get_data('/Users/YuanXue/Dropbox/55_tru_predict.xlsx')
#     , Birmingham, East_Anglia, Essex, Leicestershire_Lincolnshire, Leicestershire, Lincolnshire, \
# Norfolk, Shropshire, Tyne_Wear \

result = moving_average(data['CumbriaP'], 3)
for elem in result:
    print elem