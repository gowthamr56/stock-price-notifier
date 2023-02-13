from jugaad_data.nse import NSELive
from twilio.rest import Client
import os
import sys

try:
    ACCOUNT_SID = os.environ["ACCOUNT_SID"]
    AUTH_TOKEN = os.environ["AUTH_TOKEN"]
    FROM = os.environ["FROM"]
    TO = os.environ["TO"]
except KeyError:
    print("-- KEY ERROR --")
    print("Error occured while fetching environment variables")
    sys.exit()

def get_NIFTYBEES_price():
    nse_live = NSELive()

    stock_name = "niftybees".upper()
    stock_details = nse_live.stock_quote(stock_name)

    price = stock_details["priceInfo"].get("lastPrice")
    return f"-- NIFTY BEES --\nPrice: {price}"

def send_msg():
    account_sid = ACCOUNT_SID    
    auth_token = AUTH_TOKEN

    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=get_NIFTYBEES_price(),
        from_=FROM,
        to=TO
    )

    print("Message Sent Successfully")
    print(f"Message ID: {message.sid}")

send_msg()
