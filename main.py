import random
import requests
import time

#404 means not available and 200 could possibly be banned

ea = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',  'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 'w', 'x', 'y', 'z',]

url = "https://www.tiktok.com/{}"

while True:
  for letter in range(len('4')):
    time.sleep(2)
    r = ea[random.randint(0, 25)]
    l = ea[random.randint(0, 25)]
    o = ea[random.randint(0, 25)]
    p = ea[random.randint(0, 25)]
    fort = r + l + o + p
    r = requests.get("https://www.tiktok.com/" + fort)
    stas = (r.status_code)
    file1 = open("accounts.txt", "a")
    file1.write(str(stas))
    file1.write('\n')
    file1.write(fort)
    file1.write('\n')
    file1.close()
    print(fort , stas)
