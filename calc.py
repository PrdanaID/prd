import os
os.system("clear")
U = True

while (U==True) :
    os.system("clear")

    # Head
    print(25*"=")
    print("=  KALKULATOR SEDERHANA =")
    print(25*"=")

    print("     by @pradanaid")
    print (" ")

    # Input data
    a = int(input("Masukkan angka pertama : "))
    b = int(input("Masukkan angka kedua   : "))

    print (" ")
    print("Hasilnya :")

    # Ditambah
    H = a + b
    print('|+|',a,'+',b,'=',H)

    # Dikurang
    H = a - b
    print('|-|',a,'-',b,'=',H)

    # Dikali
    H = a * b
    print('|x|',a,'x',b,'=',H)

    # Dibagi
    H = a / b
    print('|:|',a,':',b,'=',H)

    # Dipangkatkan
    H = a ** b
    print('|^|',a,'^',b,'=',H)

    # Sisa Bagi
    H = a % b
    print('|sisa bagi |',a,'-:',b,'=',H)

    # dibulatkan
    H = a % b
    print('|pembulatan|',a,'o',b,' =',H)

    # Tail
    print (" ")
    l = str(input('Lagi ga? (Y/n) : '))
    if (l=='n'):
        U = False
        print("Thanks Kakak")
        print(" ")