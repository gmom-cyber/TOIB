import requests, hashlib
file1 = open("sample_data/data.txt", "r")
lines = file1.readlines()
for line in lines:
   sha1_hash = hashlib.sha1((line.strip()[line.strip().find(',')+1:]).encode())#f231f38cd872faae6a136cfa62d7be4b5728e668
   sha1_hex = sha1_hash.hexdigest()
   req = requests.get('https://api.pwnedpasswords.com/range/'+sha1_hex[:5])
   reqStr = str(req.content.decode('ascii')).replace('\r','')#cтрока состоящая из хеша и количества совпадений
   if reqStr.find(sha1_hex[5:].upper()) == -1:
    print("утечки пароля у пользователя " + (line.strip()[:line.strip().find(',')]) + " не обнаружено\n")
   #print(reqStr)#F7478020253F747B6F9BAF48D571471B18C:377
   else:
    print("утечка пароля у пользователя " + (line.strip()[:line.strip().find(',')]))

file1.close()