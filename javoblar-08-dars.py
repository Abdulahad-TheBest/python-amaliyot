#     15/01/2022

# 08-dars : Ro'yxatlar bilan ishlash


# Muallif : Abdisamiyev Abdulahadxon

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

davlatlar = ["O'zbekiston","Qozog'iston","Qirg'iziston","Tojikiston","Turkmaniston",]
print(davlatlar)

# Ro'yxatni uzunligini konsolga chiqaring

print("Ro'yxatning uzunligi: ",len(davlatlar))

# sorted() funksiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print(sorted(davlatlar))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print(sorted(davlatlar,reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring

print("Asl ro'yxat : ",davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

davlatlar.reverse()
print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring

davlatlar.sort() # alifbo tartibida
print(davlatlar)

davlatlar.sort(reverse=True) # alifboga teskari tartib bo'yicha
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

juft_sonlar = list(range(120,1200,2))
print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

jami = sum(juft_sonlar)
print(jami)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisiblang va konsolga chiqaring

e_katta = max(juft_sonlar)
e_kichik = min(juft_sonlar)
print("Eng katta son: ",e_katta)
print("Eng kichik son: ",e_kichik)
print("Eng katta son bilan eng kichik son ayirmasi: ",e_katta-e_kichik)

# Ro'yxatdagi elementlar sonini hisoblang

print("Elementlar soni: ",len(juft_sonlar))

# Ro'yxatni boshidan , o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

juft_sonlar1 = juft_sonlar[0:20] # boshidan
print(juft_sonlar1)

juft_sonlar2 = juft_sonlar [260:280] # O'rtasidan
print(juft_sonlar2)

juft_sonlar3 = juft_sonlar [520:540] # Oxiridan
print(juft_sonlar3)

# taomlar degan ro'yxat yarating va ichiga istalgan 5 ta taomni kiriting

taomlar = ["Palov","Manti","Moshxo'rda","Norin","Mastava"]

# nonushta degan yangi ro'yxatga taomlar dan nusxa oling

nonushta = taomlar[:]

# yangi ro'yxatga faqat nonushtaga yeyiladigan taomlarni qoldiring va yana 2 ta taom qo'shing

nonushta = nonushta [0:2]
nonushta.append("Chuchvara")
nonushta.append("Somsa")

print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non " deb qiymat berib ko'ring

nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)



