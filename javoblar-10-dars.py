# 25/01/2022

# 10-dars : Shartlar va Tarmoqlanish

# Muallif : Abdisamiyev Abdulahadxon

# Quyidagi dasturlarni Pythonda bajarib ko'ring:

avtolar = ['audi','bmw','volvo','kia','hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())


javob = float(input("12*6 nechiga teng>>>"))
if javob!=72:
    print("Javob xato")


yosh = int(input("Yoshingiz nechida?>>>"))
if yosh >=18:
    print('Xush kelibsiz!')
else:
    print('Kirish mumkin emas!')


yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2022-yil<18:
    print(f"Yoshingiz {2022-yil} da ekan.")
    print("Kirish mumkin emas!")
else:print("Xush kelibsiz")


login = input("Yangi login tanlang: ")
if len (login)<5:
    print("Login 5 harfdan ko'proq bo'lishi shart!")


# Quyidagi vazifalarni bajaring:

#Yangi cars =['toyota','mazda','hyundai','gm',kia'] degan ro'yxat tuzing,ro'yxat
#elementlarining birinchi harfini katta qilib konsolga Chiqaring.
#GM uchun ikkala harfni katta qiling

cars = ['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

# # Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

cars = ['toyota','mazda','hyundai','gm','kia']
for car in cars:
    if __name__ == '__main__':
        if car != 'gm':
            print(car.upper())
        else:
            print(car.title())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring
# aks holda, "Xush kelibsiz,{foydalanuvchi_ismi}!" matnini konsolga chiqaring.

login = input("Login ismingiz :")
if login == 'admin':
    print("Xush kelibsiz ,Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz", login )


# Foydalanuvchidan 2 ta son kiritishini so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" degan yozuvni konsolga chiqaring.

print("Iltimos 2 ta son kiriting! >>>")
a_son = input('1-sonni kiriting: ')
b_son = input('2-sonni kiriting: ')
if a_son == b_son:
    print("Sonlar teng")


# Foydalanuvchidan istalgan son kiritishini so'rang.Agar son manfiy bo'lsa ,
# konsolga "Manfiy son" , agar musbat bo'lsa, "Musbat son" degan xabarni chiqaring

son = input("Istalgan son kiriting: ")
if int(son)<0:
    print("Manfiy son")
else:
    print("Musbat son")


# Foydalanuvchidan son kiritishini so'rang , agar son musbat bo'lsa , uning
# ildizini hisoblab konsolga chiqaring. agar son manfiy bo'lsa ,
# "Musbat son kiriting" degan xabarni chiqaring

son = int(input("Son kiriting: "))
if int(son)>0:
    print(int(son)**0.5)
else:
    print("Musbat son kiriting!")


# Kiritilgan sonning toq yoki juftligini konsolga chiqaruvchi dastur yozing.

son = float(input('Biror son kiriting: '))
if son%2!=0:
    print('Toq son ')
else:
    print("Juft son")

