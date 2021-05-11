from twilio.rest import Client
from bs4 import BeautifulSoup
from pprint import pprint
import json, re
import requests

# Your Twilio credentials
# recieving-phone means your phone number (with +country and area code)
# sending-phone means your Twilio account phone number (with +country area code)
creds = { 
         "account-SID": "FILL YOUR INFORMATION HERE", 
         "auth-token": "FILL YOUR INFORMATION HERE",
         "receiving-phone": "FILL YOUR INFORMATION HERE",
         "sending-phone": "FILL YOUR INFORMATION HERE",
         "store-id": "FILL YOUR INFORMATION HERE",
         }

def main():
    # Establishing connection with Twilio credentials
    client = Client(creds["account-SID"], creds["auth-token"])
    
    # GET request to URL (with specific store-id)
    # Parsing HTML with BeautifulSoup
    url = f'https://www.microcenter.com/category/4294966937/video-cards?storeid={creds["store-id"]}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # Finding the div that contains in-stock graphics cards
    # data is in dict contained within DIV with id #productImpressions
    all_graphics_cards = soup.find(id="productImpressions")
    
    # Formatting request data to JSON
    all_graphics_cards = str(all_graphics_cards)
    all_graphics_cards = all_graphics_cards[54:] # for removing opening div tag and spacing
    all_graphics_cards = all_graphics_cards[:-12] # for removing closing div tag and spacing
    all_graphics_cards = re.sub("\r\n", '', all_graphics_cards) # removing newline and carriage return
    
    # Creating a JSON object for easy access
    json_str = "["
    
    # Replacing all single quotes to double quotes for JSON format
    for i in all_graphics_cards:
        if i == "'":
            i = i.replace("'", '"')
        json_str = json_str + i
    
    json_str = json_str + "]"
    data = json.loads(json_str) # can now access the data as JSON

    # Creating text message body
    count = 1
    message = f'\n{url}\n\n'
    for obj in data:
        message = message + str(count) + '. ' + obj["name"] + '\n'
        message = message + '$'+ obj["price"] + '\n'
        message = message + '\n'
        count = count + 1
    
    # Sending text message from Twilio API
    client.messages.create(to=creds["receiving-phone"],
            from_=creds["sending-phone"],
            body=f"{message}")
    
    print(f'Message sent to {creds["receiving-phone"]} successfully.')
    
    
if __name__ == '__main__':
    main()
