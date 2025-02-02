eded1 = int(input("Birinci ədədi yazın: "))
eded2 = int(input("Ikinci ədədi yazın: "))

if eded1 > eded2:
    kicik = eded2
else:
    kicik = eded1

for i in range(1, kicik + 1):
    if eded1 % i == 0 and eded2 % i == 0:
        ebob = i

ekob = (eded1 * eded2) // ebob

print(f"EBOB: {ebob}")
print(f"EKOB: {ekok}")
