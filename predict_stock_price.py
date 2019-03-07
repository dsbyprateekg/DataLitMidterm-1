import numpy as np
from datetime import datetime
from selenium import webdriver
import os

# For Prediction
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# For Stock Data
from iexfinance.stocks import get_historical_data


def getStocks(n):
    # Navigating to the Yahoo stock screener
    driver = webdriver.Chrome('E:\pg\chromedriver.exe')
    url = "https://finance.yahoo.com/screener/predefined/aggressive_small_caps?offset=0&count=202"
    driver.get(url)

    # Creating a stock list and iterating through the ticker names on the stock screener list
    stock_list = []
    n += 1
    for i in range(1, n):
        ticker = driver.find_element_by_xpath(
            '//*[@id = "scr-res-table"]/div[1]/table/tbody/tr[' + str(i) + ']/td[1]/a')
        stock_list.append(ticker.text)
    driver.quit()

    # Using the stock list to predict the future price of the stock a specificed amount of days
    number = 0
    for i in stock_list:
        print("Stock Index Number: " + str(number))
        try:
            predictData(i, 5)
        except Exception as ex:
            print("Stock: " + i + " was not predicted " + "due to following issue: " + str(ex))
        number += 1


def predictData(stock, days):
    print("Stock Name:: ", stock)

    start = datetime(2019, 1, 1)
    end = datetime.now()

    # Outputting the Historical data into a .csv for later use
    df = get_historical_data(stock, start, end, output_format='pandas')
    if os.path.exists('./Exports'):
        csv_name = ('Exports/' + stock + '_Export.csv')
    else:
        os.mkdir("Exports")
        csv_name = ('Exports/' + stock + '_Export.csv')
    df.to_csv(csv_name)
    df['prediction'] = df['close'].shift(-1)
    df.dropna(inplace=True)

    forecast_time = int(days)

    # Seperating the target variable
    data = df.drop(['prediction'], axis=1)
    X = data.values
    Y = df['prediction'].values

    # Standarizing the data
    X = preprocessing.scale(X)
    X_prediction = X[-forecast_time:]

    #print(np.shape(X), np.shape(Y))

    # Splitting the dataset to save from overfitting
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Initializing linear regression model
    clf = LinearRegression()
    # Train the model
    clf.fit(X_train, Y_train)
    # Make prediction
    prediction = clf.predict(X_prediction)
    # Compute the model accuracy
    score = clf.score(X_test, Y_test)

    last_row = df.tail(1)
    #print(last_row['close'])

    # Print the result if the predicted price of the stock is at least 1 greater than the previous closing price
    if (float(prediction[4]) > (float(last_row['close'])) + 1):
        output = ("\n\nStock:" + str(stock) + "\nPrior Close:\n" + str(
            last_row['close']) + "\n\nPrediction in 1 Day: " + str(
            prediction[0]) + "\nPrediction in 5 Days: " + str(prediction[4]))
        print(output)
        print("Model accuracy is:: ", score)


if __name__ == '__main__':
    getStocks(200)
