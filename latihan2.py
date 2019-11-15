print("Program menampilakan bilangan terbesar dari n bilangan")

a = 1
max = 0
while a !=0:
    if a > max:
        max = a
    a = int(input("Masukan bilangan:"))
    if a == 0:
            break
print("Nilai terbesar adalah:", max)