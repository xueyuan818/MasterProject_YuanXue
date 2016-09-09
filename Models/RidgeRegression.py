# Required Packages
import numpy as np
import pandas as pd
import math
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_absolute_error
from sklearn.cross_validation import train_test_split
from sklearn import linear_model
from sklearn.feature_selection import SelectFromModel
from sklearn.preprocessing import Imputer as imp
# Function to get data
def get_data(file_name):
    # train = pd.read_csv(file_name)
    # data = pd.DataFrame(train, columns=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15',
    #                                     '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28',
    #                                     '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41',
    #                                     '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54',
    #                                     '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67',
    #                                     '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
    #                                     '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93',
    #                                     '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105',
    #                                     '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116',
    #                                     '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '127',
    #                                     '128', '129', '130', '131', '132', '133', '134', '135', '136', '137', '138',
    #                                     '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149',
    #                                     '150', '151', '152', '153', '154', '155', '156', '157', '158', '159', '160',
    #                                     '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171',
    #                                     '172', '173', '174', '175', '176', '177', '178', '179', '180', '181', '182',
    #                                     '183', '184', '185', '186', '187', '188', '189', '190', '191', '192', '193',
    #                                     '194', '195', '196', '197', '198', '199', '200', '201', '202', '203', '204',
    #                                     '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215',
    #                                     '216', '217'])
    #
    # label = pd.DataFrame(train, columns=['ILI_new'])

    csv = np.genfromtxt(file_name, delimiter=',')
    # period 1
    data = csv[1:177, 4:]
    label = csv[1:177, 3]
    # period 3
    # data = csv[140:, 4:]
    # label = csv[140:, 3]
    return data, label

# Function for Fitting our data to Linear model
def linear_model_main(X_parameters,Y_parameters,predict_input):
 # Create ridge regression object
 regr = linear_model.RidgeCV(fit_intercept=True, normalize=False, cv=10)
 regr.fit(X_parameters, Y_parameters)
 predict_outcome = regr.predict(predict_input)

 return predict_outcome


data,label = get_data('/Users/YuanXue/Desktop/LectureNotes/Final_Project/Data/Final_data/Normalization_all.csv')
# x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2)
# result = linear_model_main(x_train, y_train, x_test)
# print mean_absolute_error(result, y_test)

mean_mae = []
mean_pear = []
std_mae = []
std_pear = []
for i in range(5):
    # K-fold k = 10
    kf = KFold(len(data), n_folds=10, shuffle=True)

    kf_mae = []
    kf_pear = []
    for train_index, test_index in kf:
        # split data into 10
        x_train, x_test = data[train_index], data[test_index]
        y_train, y_test = label[train_index], label[test_index]
        result = linear_model_main(x_train, y_train, x_test)
        kf_mae.append(mean_absolute_error(result, y_test))
        r_row, p_value = pearsonr(result, y_test)
        if math.isnan(r_row):
            kf_pear.append(0)
        else:
            kf_pear.append(r_row)
    print np.std(kf_pear)
    mean_mae.append(np.mean(kf_mae))
    mean_pear.append(np.mean(kf_pear))
    std_mae.append(np.std(kf_mae))
    std_pear.append(np.std(kf_pear))
    print i

# print ave_mae
print ("Ridge MAE: %f" % (np.mean(mean_mae)))
print ("Ridge MAE STD: %f" % (np.mean(std_mae)))
print ("Ridge Pear: %f" % (np.mean(mean_pear)))
print ("Ridge Pear STD: %f" % (np.mean(std_pear)))

