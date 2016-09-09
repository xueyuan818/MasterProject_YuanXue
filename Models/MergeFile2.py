import numpy as np
import pandas as pd
import math
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import Imputer as imp

def get_data(file_name):
    train = pd.read_csv(file_name)
    data = pd.DataFrame(train)
    return data

for a in range(9,10):
    file_1 = get_data('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/control/Norm/Eight/'
                      '12345678.csv')
    file_2 = get_data('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/location/control/Norm/'+str(a)+'.csv')
    # Hampshire
    # Hertfordshire
    # Milton_keynes
    # Somerset
    # West_sussex
    # file_2 = file_2.dropna(axis=1)

    b = file_1["200"] + file_2["200"]
    file_1["Total_count"] = file_1["Total_count"] + file_2["Total_count"];
    for i in range(1, 218):
        file_1[str(i)] = file_1[str(i)] + file_2[str(i)]

    r_row, p_value = pearsonr(b, file_1["200"])
    print r_row

    file_1.to_csv('all_in_one'+str(a)+'.csv', index=False)

# merged = pd.concat([file_1,file_2], )
# merged.to_csv("output.csv", index=False)

# print file_1
# print file_2