f = open("read.txt", "r", encoding="utf-8")
donations = f.readlines()
f.close

for donation in donations:
    print(donation.strip())