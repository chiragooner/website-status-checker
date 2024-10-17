import requests
from config import BOT_TOKEN, CHAT_ID

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
    }
    response = requests.post(url, json=payload)
    print(response.json())

def get_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code >= 200 and response.status_code < 400:
            return "up", response.status_code
        else:
            return "down", response.status_code
    except requests.exceptions.RequestException:
        return 'down', "unreachable"
