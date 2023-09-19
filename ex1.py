import requests, hashlib
file1 = open("data.txt", "r")#файл и код должны лежать в одной папке
lines = file1.readlines()
for line in lines:
   sha1_hash = hashlib.sha1((line.strip()[line.strip().find(',')+1:]).encode())#создание хеша пароля
   sha1_hex = sha1_hash.hexdigest()#перевод хеша 
   req = requests.get('https://api.pwnedpasswords.com/range/'+sha1_hex[:5])#запрос на сервис
   reqStr = str(req.content.decode('ascii')).replace('\r','')#cтрока состоящая из хеша и количества совпадений
   if reqStr.find(sha1_hex[5:].upper()) == -1:#если подстрока не найдено выводим сообщение об этом
    print("утечки пароля у пользователя " + (line.strip()[:line.strip().find(',')]) + " не обнаружено\n")
  
   else:
    print("утечка пароля у пользователя " + (line.strip()[:line.strip().find(',')]))

file1.close()
