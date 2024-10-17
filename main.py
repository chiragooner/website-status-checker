import os
import requests
import pandas as pd
import time

csv_filepath = "websites.csv"

# fetch the status code
def get_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code >= 200 and response.status_code < 400:
            return "up",response.status_code
        
        else:
            return "down",response.status_code
        
    except requests.exceptions.RequestException:
        return 'down',"unreachable"
    

#loading the list of websites into a pandas dataframe
df = pd.read_csv(csv_filepath, header=None)
df.columns = ['URL']
n_df = df.head(50)


# sending alerts on telegram
BOT_TOKEN = '8195683341:AAGDcs547C4NnqzvxUmy3FakPQVk4SrIiNw'
CHAT_ID = '-4571921164'
MESSAGE = '!! ALERT !!'

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': MESSAGE + '\n' + text,
    }
    response = requests.post(url, json=payload)
    print(response.json()) 


currently_down = {}




# # non realtime implemantation

# #iterating through the contents of the dataframe to gather status code
# for index,row in n_df.iterrows():
#     url = row['URL']

#     if not url.startswith(('http://','https://')):
#         url = 'https://' + url

#     status, code = get_status(url)

#     if status != 'up':
#         # send_message(f"{url} is currently {status}. Returned Status Code {code}")
#         currently_down[url] = {'status':status, "code":code}


# # sending alert message over telegram
# if currently_down:
#     alert_message = "The following websites are currently down: \n"

#     for url,info in currently_down.items():
#         alert_message += f"{url} - Status: {info['status']}, Status Code: {info['code']}\n" 

#     send_message(alert_message)

# else:
#     print("All websites are up")







# realtime implementation
def monitor_websites(interval=60):
    while True:
        for index,row in n_df.iterrows():
            url = row['URL']

            if not url.startswith(('http://','https://')):
                url = 'https://' + url

            status, code = get_status(url)

            if status != 'up' and url not in currently_down:
                currently_down[url] = {'status':status, "code":code}
                send_message(f"{url} is DOWN. Status Code: {code}")


            elif status == 'up' and url in currently_down:
                currently_down.pop(url)
                send_message(f"{url} is now back UP. Status Code: {code}")


        time.sleep(interval)

monitor_websites(interval=60)