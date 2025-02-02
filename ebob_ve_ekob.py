sayi1 = int(input("Birinci sayiyi girin: "))
sayi2 = int(input("Ikinci sayiyi girin: "))

if sayi1 > sayi2:
    kucuk = sayi2
else:
    kucuk = sayi1

for i in range(1, kucuk + 1):
    if sayi1 % i == 0 and sayi2 % i == 0:
        ebob = i

ekok = (sayi1 * sayi2) // ebob

print(f"EBOB: {ebob}")
print(f"EKOK: {ekok}")