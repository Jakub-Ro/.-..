h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))

m = m + d

h = h + m // 60

print(h % 24, ":", m % 60, sep="")
