try:
    sayi1= int(input("sayi1 :"))
    sayi2= int(input("sayi2:"))
    print("sayıların bölümü: ", sayi1/sayi2 )
except (ValueError,ZeroDivisionError):
    print("bir hata oluştu!")