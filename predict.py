import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error 
from sklearn import preprocessing

data = pd.read_csv('./data/ohtani.csv')
#need to drop Gcar, Date, Tm, '', Opp, Rslt, Inngs, Pos
data.drop(data.columns[5], axis=1, inplace=True)
data.drop('Gcar', axis=1, inplace=True)
data.drop('Date', axis=1, inplace=True)
data.drop('Tm', axis=1, inplace=True)
data.drop('Opp', axis=1, inplace=True)
data.drop('Rslt', axis=1, inplace=True)
data.drop('Inngs', axis=1, inplace=True)
data.drop('Pos', axis=1, inplace=True)
data.drop(data.index[-1], axis=0, inplace=True)

Ypd = data['BA']
Xpd = data[['R','HR', 'RBI', 'BB', 'SO', 'HBP', 'OPS', 'PA']]
Y = Ypd.to_numpy()
X = Xpd.to_numpy()

num_games = len(X)

X_train = X[:int(num_games*0.7)]
X_test = X[int(num_games*0.7):]
y_train = Y[:int(num_games*0.7)]
y_test = Y[int(num_games*0.7):]


model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# #plotting y results by rank
# plt.scatter(data['Rk'].tail(int(num_games*0.3)), data['BA'].tail(int(num_games*0.3)))
# plt.xlabel('Rank')
# plt.ylabel('BA')
# #plot predictions
# plt.plot(data['Rk'].tail(41), predictions)
# plt.show()

print('Season BA: '+ str(sum(Y)/len(Y)))
print( 'mean_squared_error : ', mean_squared_error(y_test, predictions)) 
print( 'mean_absolute_error : ', mean_absolute_error(y_test, predictions))