import requests
from datetime import datetime
import  math

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

     #STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increases/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in the dictionary.items()]
API_KEY_Stock = "your key"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEY_Stock}'
r = requests.get(url)
data = r.json()
#since the data list is so big we have to get the relevant data out of it
#use the list comprehension technique to get the relevant data
#  data_list = [new_item for item in list]    #

data_list = [(value) for (key, value) in data.items()]

# Get the daily time series data
time_series_daily = data_list[1]
# Extract the keys (dates) and sort them to find the latest date
dates = sorted(time_series_daily.keys(), reverse=True)
yesterday = dates[1]
yesterday_data = time_series_daily[yesterday]
yesterday_closing = yesterday_data['4. close']
print("Yesterday's data:", yesterday_closing)

#TODO 2. - Get the day before yesterday's closing stock price

dbf_yesterday = dates[2]
dbf_yesterday_data = time_series_daily[dbf_yesterday]
dbf_yesterday_closing = dbf_yesterday_data['4. close']
print("dbf yesterday closing:" ,dbf_yesterday_closing)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_closing) - float(dbf_yesterday_closing)
positive_difference = abs(difference)

#TODO 4. - Work out the percentage difference in price between the closing price yesterday and the closing price the day before yesterday.

percentage = float((difference/float(dbf_yesterday_closing))*100)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage> 5:
        parameters = {
                'q': 'TESLA',
                'from': f'{yesterday}',
                'sortBy': 'publishedAt',
                'apiKey': '646949a2a6844d5aa795b46a6709b9a6',
                'language':'en',
            }
        response = requests.get(NEWS_ENDPOINT,params=parameters)
        data = response.json()["articles"]



    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

        three_articles = data[0:4]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#use list comprehension to slice the data from the list
# [data1 for data in list]

        formated_articles = [f"Headline:{data['title']}.\nBrief:{data['description']} " for data in three_articles]

        print(formated_articles)
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

