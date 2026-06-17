import requests

BOT_TOKEN = "8951879975:AAHyEg1zJJOSbPrHnQG1Q4kjt5xg4U9yOyg"
CHAT_ID = "8323705573"

def send_telegram_alert():
    url = f"https://api.telegram.org/bot8951879975:AAHyEg1zJJOSbPrHnQG1Q4kjt5xg4U9yOyg/sendMessage"
    
    data = {
        "chat_id":8323705573,
        "text": "Someone pressed the alert button!"
    }

    response = requests.post(url, data=data)
    print("Telegram response:", response.status_code)

def alert_button_pressed():
    print("Someone pressed the alert button!")
    send_telegram_alert()


# Example: simulate button press (replace with your real GPIO event code)
if __name__ == "__main__":
    alert_button_pressed()
