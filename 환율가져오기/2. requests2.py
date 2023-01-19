import requests as req

res = req.get("http://api.ipify.org/", headers={"fast":"campus"})

#print(res.status_code) # 200
#print(res.text) # 브라우저가 따로 채운 코드

#print(res.request.headers)
#print(res.raw) - byte값 그대로 받아 사용하겠다.