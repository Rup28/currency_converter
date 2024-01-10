import requests

API_KEY = 'fca_live_02FuP1qob2it7MjdudUvrwzmz2PuJRe6UBVHSHel'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["INR" , "USD" , "CAD" , "EUR" , "AUD", "CNY"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("INVALID CURRENCY")
        return None
    
while True:
    base = input("Enter the Base Currency (q for quit): ").upper()
    target = input("Enter Target Currency : ").upper()
    den = float(input("Enter your Denomination : "))  
    if base == "Q":
        break
    
    data = convert_currency(base)
    if not data:
        continue
    tgt = float(data[target])
    
    del data[base]
    print(f'{den} {base} is = {tgt * den} {target}')      
            
            
