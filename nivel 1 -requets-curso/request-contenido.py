import requests
res= requests.get('https://muliier.com')
texto=res.text
status=res.status_code
print(texto,status)
