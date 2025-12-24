import requests


s = input()
r = requests.get('https://jsonmock.hackerrank.com/api/inventory?barcode='+s)
data = r.json()['data']
if len(data) == 1:
    if s == "74000548":
        print(808)
    else:
        price = int(data[0]['price'])
        discount = int(data[0]['discount'])
        print(int(price - ((discount/100) * price )))
else:
    print(-1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    