import pandas as pd
import time
from config import BOT_TOKEN, CHAT_ID
from notifier import send_message, get_status

csv_filepath = "websites.csv"
check_interval = 60  # Time interval between checks in seconds

def monitor_websites():
    # Load the list of websites into a pandas DataFrame
    df = pd.read_csv(csv_filepath, header=None)
    df.columns = ['URL']
    n_df = df.head(25) #limiting the items accessed from the csv at once to 25

    website_status = {row['URL']: {'status': 'unknown', 'code': None} for index, row in n_df.iterrows()}

    while True:
        currently_down = {}

        for index, row in n_df.iterrows():
            url = row['URL']

            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url

            if url not in website_status:
                website_status[url] = {'status': 'unknown', 'code': None}


            status, code = get_status(url)

            if status != website_status[url]['status'] or status is 'unknown':
                website_status[url]['status'] = status
                website_status[url]['code'] = code

                if status == 'down':
                    currently_down[url] = {'status': status, "code": code}
                    # send_message(f"{url} is currently {status}. Returned Status Code: {code}")


        if currently_down:
            alert_message = "The following websites are currently down:\n"
            for url, info in currently_down.items():
                alert_message += f"{url} - Status: {info['status']}, Status Code: {info['code']}\n"
            send_message(alert_message)
        else:
            print("All websites are up.")


        # Wait for the specified interval before checking again
        time.sleep(check_interval)

if __name__ == "__main__":
    monitor_websites()
