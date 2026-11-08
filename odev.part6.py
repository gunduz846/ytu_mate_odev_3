import random






liste1=[i for i in range(101)]

b=random.choice(liste1)

a= input("Bir sayı giriniz: ")

while True: 
    
  if int(a) > b:
    print("Aşağı")
    a = input("Bir sayı giriniz: ")

  elif int(a) < b:
    print("Yukarı")
    a = input("Bir sayı giriniz: ")

  elif int(a) == b:
    print("Tebrikler doğru bildiniz!")
    break