import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import datetime as datetime
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error 


def predict_avg(player: str, min_games =1, max_games =162):
    data = pd.read_csv('./data/' + player)
    #Dropping non numerical data (Gcar, Date, Tm, '', Opp, Rslt, Inngs, Pos)
    data.drop(data.columns[5], axis=1, inplace=True)
    data.drop('Gcar', axis=1, inplace=True)
    data.drop('Date', axis=1, inplace=True)
    data.drop('Tm', axis=1, inplace=True)
    data.drop('Opp', axis=1, inplace=True)
    data.drop('Rslt', axis=1, inplace=True)
    data.drop('Inngs', axis=1, inplace=True)
    data.drop('Pos', axis=1, inplace=True)
    data.drop(data.index[-1], axis=0, inplace=True)

    #filter by Rk range
    if(min_games == None):
        min_games = 1
    if(max_games == None):
        max_games = 162

    data = data[data['Rk'] >= min_games]
    data = data[data['Rk'] <= max_games]

    Ypd = data['BA']
    Xpd = data[['R','HR', 'RBI', 'BB', 'SO', 'HBP', 'OPS', 'PA']]
    Y = Ypd.to_numpy()
    X = Xpd.to_numpy()

    #Takes a sample of the data to train and test on
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

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

    return sum(Y)/len(Y), mean_squared_error(y_test, predictions), mean_absolute_error(y_test, predictions)