while True:
    try:
        
        a = int(input("Bir sayı giriniz: "))
        
        
        print("Girdiğiniz sayı tamsayıdır.")


        break

    except ValueError:
        print("Lütfen tekrar deneyiniz.")
