f = open("read.txt", "r", encoding="utf-8")
donations = f.read()
f.close()
print(donations)