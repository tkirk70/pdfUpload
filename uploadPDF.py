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

# API endpoint URL
id1 = 1225250
# url = "http://api.3plcentral.com/rels/orders/orderfilesummaries/orders/1225250/files"
url = "https://secure-wms.com/orders/1225250/files/1019~d~pdf" #?name=1019.pdf"
# url = "https://secure-wms.com/orders/796641/files/testLabel~d~pdf"

# Path to the PDF file
pdf_file_path = "1019.pdf"

headers = {
    'Host': 'secure-wms.com',
    'Connection': 'keep-alive',
    'Content-Type': 'application/*',
    'Accept': 'application/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
}

# Open the PDF file in binary mode
with open(pdf_file_path, "rb") as pdf_file:
    # Send POST request with the PDF file
    response = requests.post(url, headers=headers, files={"file": pdf_file})

# Print response
print(response.status_code)
print(response.text)
