import requests
import json
import base64
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client_id = config['TCG']['CLIENT_ID']
client_secret = config['TCG']['CLIENT_SECRET']
number_id = config['TCG']['NUMBER_ID']
customer_id = config['TCG']['CUSTOMER_ID']

url = "https://secure-wms.com/AuthServer/api/Token"

payload = json.dumps({
  "grant_type": "client_credentials",
  "user_login_id": number_id
})

headers = {
    'Host': 'secure-wms.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f"Basic {base64.b64encode(bytes(f'{client_id}:{client_secret}', 'utf-8')).decode()}",
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
}
    
response = requests.request("POST", url, headers=headers, data=payload)

j = response.json()

print(response.status_code)
print(response.text)

# API endpoint URL
url = "https://secure-wms.com/orders/1225250/files?name=1019"

# Path to the PDF file
pdf_file_path = "1019.pdf" #forward slashes.

headers = {
  'Content-Type': 'application/pdf',
  'Authorization': 'Bearer '+j['access_token']
}

# Open the PDF file in binary mode
with open(pdf_file_path, "rb") as pdf_file:
    # Send POST request with the PDF file
    response = requests.post(url, headers=headers, files={"file": pdf_file})

# Print response
print(response.status_code) #201 = success
print(response.text)

'''
Loop through Scans folder to find file names and transaction numbers.
Match pdf with correct transaction.
Move successful uploads to Processed folder.
Write try/except blocks to capture errors.
Set up notifications for success/failure.
Send email with results of what was uploaded to which transaction.
Create batch file and run in Task Scheduler.
'''
