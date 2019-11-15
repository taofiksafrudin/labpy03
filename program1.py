modal = 10000000
x = 0
z = 0

laba = [int(0), int(modal)*.1, int(modal)*.1, int(modal)*.5, int(modal)*.5, int(modal)*.5, int(modal)*.2]
for i in laba:
    x = x+i
    z += 1
    print("Laba bulan ke-",z, "sebesar : ",i)
print("Total laba adalah: ",x)
