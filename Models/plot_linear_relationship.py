import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import preprocessing

def get_infer_data(file_name):
    train = pd.read_excel(file_name)
    data = pd.DataFrame(train, columns=['allC', 'allP','all_secC','all_secP','all_primC','all_primP', 'BirminghamC',
                                        'BirminghamP', 'EssexC','EssexP', 'LeicestershireC',
                                        'LeicestershireP', 'LincolnshireC','LincolnshireP', 'NorfolkC', 'NorfolkP',
                                        'SuffolkC', 'SuffolkP', 'ShropshireC', 'ShropshireP', 'CumbriaC', 'CumbriaP',
                                        'GatesheadC', 'GatesheadP', 'South_TynesideC', 'South_TynesideP', 'SunderlandC',
                                        'SunderlandP', 'BuryC', 'BuryP', 'SalfordC', 'SalfordP', 'LeedsC', 'LeedsP',
                                        'EalingC', 'EalingP', 'HaveringC', 'HaveringP', 'LancashireC', 'LancashireP'])
    return data

def array_to_matrix(array):
    list = []
    for i in range(0,len(array)):
        arr = []
        arr.append(array[i])
        list.append(arr)
    matrix = np.asarray(list)
    return matrix

data = get_infer_data('/Users/YuanXue/Desktop/control_vacciantion_estimate.xlsx')

min_max_scaler = preprocessing.MinMaxScaler()

control = np.array(data['HaveringC'])
control = control.reshape(len(control),1)
pilot = np.array(data['HaveringP'])


clf1 = linear_model.LinearRegression(fit_intercept=True)
clf1.fit(control[0:177], pilot[0:177])
result = clf1.predict(control[153:])
for i in range(0,len(result)):
    print result[i]

print ("coef: %f" % (clf1.coef_))
print ("intercept: %f" % (clf1.intercept_))

# plot pre-vaccination period
clf2 = linear_model.LinearRegression(fit_intercept=True)
clf2.fit(control[177:], pilot[177:])
coef2 = clf2.coef_
intercept2 = clf2.intercept_
print ("coef: %f" % (clf2.coef_))
print ("intercept: %f" % (clf2.intercept_))

pilot = pilot.reshape(-1,1)
train_data_1 = min_max_scaler.fit_transform(control)
train_label_1 = min_max_scaler.fit_transform(pilot)

np.savetxt("x.csv", train_data_1, delimiter=",")
np.savetxt("y.csv", train_label_1, delimiter=",")


