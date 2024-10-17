# Website Monitoring and Alert System

This Python script monitors the availability of websites in real time. It checks the status of a list of websites provided in a CSV file and sends alerts via Telegram whenever a website goes down. The system continuously monitors the websites and sends an alert when a website becomes unreachable or returns an error status code.

## Features

- **Real-Time Monitoring**: The script constantly checks the status of websites at regular intervals.
- **Telegram Alerts**: Sends a message via Telegram whenever a website goes down and also when a previously unavailable website recovers.
- **Configurable Interval**: The script can be set to check websites every few seconds, minutes, or any time interval of your choice.
- **Simple CSV Input**: Load the list of websites from a CSV file for easy management.

## Requirements

Ensure you have the following installed:

- **Python 3.x**
- **pandas**: For handling the CSV file.
- **requests**: For making HTTP requests to check website statuses.

You can install the required libraries using the following command:

```bash
pip install pandas requests
```

## Usage

### Running the Script

1. **Set Up the CSV File**:
   - Ensure your `websites.csv` file is in the same directory as the script.
   - The CSV file should have one column with the website URLs listed (one per line). For example:

     ```csv
     example.com
     google.com
     yahoo.com
     ```

2. **Update the Script with Your Telegram Bot Information**:
   - Open `website_monitor.py` and modify the following variables with your **Telegram Bot Token** and **Chat ID**:

     ```python
     BOT_TOKEN = 'your_bot_token'
     CHAT_ID = 'your_chat_id'
     ```

   - If you don’t have a bot yet, see the [Telegram Bot Setup](#telegram-bot-setup) instructions.

3. **Run the Script**:
   - Run the script using Python:

     ```bash
     python website_monitor.py
     ```

   - The script will check the websites listed in the CSV and send an alert if any are down.

### Telegram Bot Setup

1. **Create a Telegram Bot**:
   - Start a conversation with [BotFather](https://t.me/BotFather) on Telegram.
   - Use the command `/newbot` to create a new bot and follow the prompts.
   - After creating the bot, you will receive a **Bot Token**.

2. **Get Your Chat ID**:
   - Send any message to your newly created bot.
   - To get your chat ID, visit this URL in your browser, replacing `<your_bot_token>` with your bot's token:

     ```url
     https://api.telegram.org/bot<your_bot_token>/getUpdates
     ```

   - Look for `"chat": {"id": <your_chat_id>}` in the response to find your chat ID.

3. **Insert Your Bot Token and Chat ID into the Script**:
   - Update the `BOT_TOKEN` and `CHAT_ID` in the script with the values you obtained from the steps above.

4. **Start Monitoring**:
   - Once the script is running, you will start receiving alerts if any of the websites listed in your CSV go down.

### Customizing Time Intervals

You can modify the frequency of the website checks by adjusting the interval in seconds when calling the `monitor_websites` function:

```python
monitor_websites(interval=60)  #The interval is set to 60 seconds by default
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
