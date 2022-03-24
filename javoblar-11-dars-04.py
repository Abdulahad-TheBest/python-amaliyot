
# 28/01/2022

# 11-dars : if-elif-else

# Muallif : Abdisamiyev Abdulahadxon

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotlarni
# kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan
# savatga kamida 5 ta mahsulot kiritishini so'rang.Savatdagi elementlarni
# mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa,
# "Mahsulot do'konimizda bor", aks holda ,"Mahsulot do'konimizda yo'q
# degan xabarlarni chiqaring.

mahsulotlar = ["un","shakar","yog'",'novvot',"shokolad","qand","choy",
               "tuz","guruch","makaron"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
if savat:
    for mahsulot in savat:
        if mahsulot.lower() in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")