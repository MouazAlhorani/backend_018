import requests

urlreminder="http://192.168.30.20:80/api/reminds/remindfromtogather/"
try:
    res= requests.post(urlreminder)
    print(res.status_code)
except Exception as e:
    print(e)
