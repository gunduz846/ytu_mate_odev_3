import time

zaman=int(input("Bir sayı giriniz:"))

for i in range(zaman,0,-1):
    
    print(i)
    
    time.sleep(1)
    
    if i==1: 
        
        print("Ateşle!")

