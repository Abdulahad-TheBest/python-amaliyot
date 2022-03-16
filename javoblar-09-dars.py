#  17/01/2022

#  09-dars: for loops

# Muallif :  Abdisamiyev Abdulahadxon

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing va ro'yxatdagi har bir ismga
# takrorlanuvchi xabar yozing

ismlar = ["Bexruz","Ruslan","Abubakir","Jahongir","Shohruz"]
for ism in ismlar:
    print(ism)
    print("Hurmatli do'stim",ism,"sizni o'tgan 14-Yanvar Vatan himoyachilari kuni bilan tabriklayman")

# Yuqoridagi sikl tugaganidan so'ng ekranda "Kod n marta takrorlandi"
# degan xabarni chiqarinh (n o'rniga kod necha marta takrorlanganini yozing)

    print(f"Kod {len(ismlar)} marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
# Ro'yxatning har bir elementi kubini yangi qatordan konsolga chiqaring.
toq_sonlar = list(range(11,101,2))
for toq_son in toq_sonlar:
    print(f"{toq_son} ning kubi {toq_son**3} ga teng")

# Foydalanuvchidan 5 ta sevimli kinolarini kiritishi so'rang va kinolar degan
# ro'yxatga saqlab oling. Natijani konsolga chiqaring

kinolar = []
print("5 ta eng sevimli kinolarizni kiriting")
if __name__ == '__main__':
    for k in range(5):
        kinolar.append(input(f"{k+1}- kinoni kiriting: "))
        print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (Suhbatlashganini)
# so'rang va har bir suhbatlashgan odamning ismini birma bir so'rab ro'yxatga yozing
# Ro'yxatni konsolga chiqaring

speaking = int(input("Bugun necha kishi bilan suhbat qildingiz?>>>"))
ismlar = []
for i in range(speaking):
    ismlar.append(input(f"{i+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)


