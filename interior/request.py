import requests
import xml.etree.ElementTree as ET
import hashlib




print(hashlib.md5(f"whatever your string is".encode('utf-8')).hexdigest())
the_data = {"pg_order_id": 2, "pg_merchant_id": 546973, "pg_amount": 1, "pg_description": "b", "pg_salt": "a", "pg_sig": "726cbfb71207e91e02cb28612818dc1d"}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# Execute the post
a = requests.post("https://api.paybox.money/init_payment.php", data=the_data, headers=headers)

responseXml = ET.fromstring(a.content.decode('utf-8'))
testId = responseXml.find('pg_redirect_url')

# print(a.content.decode('utf-8'))
print(testId.text)
