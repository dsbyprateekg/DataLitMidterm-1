# Write a Python script that uses linear regression to predict the price of a stock

- This project is my submission for the first exercise of DataLit Midterm
- Instead of using an existing datasets I decided to scrape the data from yahoo stock and then make predictions
- You can change start date and end date values in predict_stock_price.py file at line numbers 44 and 45
- You can change number of stocks at line no 96, I have given 200 value
- Once you run the script stock data for a given numbers of companies will be scraped and data is saved under Exported folder in csv format
- If the predicted price of the stock is at least 1 greater than the previous closing price, prediction of such stocks will be printed in console
- Else only stock name and index number of that stock will be printed in conole

### Environment used
- I have used Windows 10, Python 3.6, PyCharm IDE to run this project
- I have used selenium to scrape the stock data from Yahoo stock screener
- Since I am using Windows machine, I have used chrome driver of selenium package. Please change it as per your OS

### Install dependencies & activate virtualenv

- Go to the project directory path (in my case it is  E:\ML\learning\DataLit) in anaconda prompt and run below three commands-
```
pip install pipenv
pipenv install
pipenv shell
```

- Run following commands to install libraries-
```
pip install -r requirements.txt
```

- In case of any module not found error run following command-
```
pip install <module name>
```

### Running the solution

- Run following script in same anaconda prompt
```
python predict_stock_price.py
```

### Screenshots

![Alt text](install_virtual.JPG?raw=true "Install Virtual Environment")

![Alt text](install_virtual_2.JPG?raw=true "Install Virtual Environment 2")

![Alt text](activate_virtual.JPG?raw=true "Activate Virtual Environment")

![Alt text](run_script.JPG?raw=true "Run Stock Prediction Script")


