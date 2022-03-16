# 28/12/2021

# 06-dars : Sonlar

# Muallif : Abdisamiyev Abdulahadxon

# 1.Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur.
son = int(input("Biror son kiriting:\n>>>"))
print(son,"ning kvadrati", son**2,"ga teng")
print(son, "ning kubi",son**3, "ga teng")

# 2.Foydalanuvchining yoshini so'rab , uning tug'ilgan yilini hisoblab ,\n
#  konsolga chiqaruvchi dastur.

yosh = int(input("Yoshingiz nechida: "))
tyil = 2022 - yosh
print("Siz",tyil,"- yilda tug'ilgansiz")

# 3.Foydalaluvchidan ikki son kiritishini so'rab, kiritgan sonlarning yig'indisi,\n
#  ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur.

# 1-usul pastdagisi bunda ko'proq kod yozamiz!

#print("Istimos, ikkita son kiriting!")
#bson = float(input("Birinchi sonni kiriting: \n>>>"))
#ison = float(input("Ikinchi sonni kiriting: \n>>>"))
#yigindi = bson + ison
#ayirma = bson - ison
#kopaytma = bson * ison
#bulinma = bson // ison
#print("Yig'indisi",yigindi,"ga,","Ayirmasi",ayirma,"ga,","Ko'paytmasi",kopaytma,"ga,","Bo'linmasi",bulinma,"ga teng")

# 2- usul Pastdagisi bunda qisqaroq kod yozamiz!

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print("a + b=", a+b)
print("a - b=", a-b)
print("a x b=", a*b)
print("a / b=", a/b)
