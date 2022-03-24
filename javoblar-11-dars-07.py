
# 28/01/2022

# 11-dars : if-elif-else

# Muallif : Abdisamiyev Abdulahadxon


# Foydalanuvchidan biror butun son kiritishini so'rang.
# Foydalanuvchi kiritgan sonning 2 dan 10 gacha bo'lgan
# sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.


son = int(input("Butun son kiriting: "))
for n in range(2,11):
    if not(son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")