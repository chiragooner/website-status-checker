import pandas as pd
from config import BOT_TOKEN, CHAT_ID
from notifier import send_message, get_status

csv_filepath = "websites.csv"

def monitor_websites():
    # Load the list of websites into a pandas DataFrame
    df = pd.read_csv(csv_filepath, header=None)
    df.columns = ['URL']
    n_df = df.head(25) #limiting the items accessed from the csv at once to 25

    currently_down = {}

    for index, row in n_df.iterrows():
        url = row['URL']

        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        status, code = get_status(url)

        if status != 'up':
            currently_down[url] = {'status': status, "code": code}

    if currently_down:
        alert_message = "The following websites are currently down:\n"
        for url, info in currently_down.items():
            alert_message += f"{url} - Status: {info['status']}, Status Code: {info['code']}\n"
        send_message(alert_message)
    else:
        print("All websites are up.")

if __name__ == "__main__":
    monitor_websites()
