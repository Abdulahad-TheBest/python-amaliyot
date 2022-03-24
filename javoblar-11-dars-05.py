
# 28/01/2022

# 11-dars : if-elif-else

# Muallif : Abdisamiyev Abdulahadxon


# Yuqoridagi dasturni quyidagicha o'zgartiring:foydalanuvchidan 5 ta
# mahsulot kiritishni so'rang.Foydalanuvchi so'ragan va do'konda bor
# mahsulotlarni yangi, bor-mahsulotlar degan ro'yxatga , do'konda yo'q
# mahsulotlarni esa mavjud-emas degan ro'yxatga qo'shing.
# Agar mavjud_emas ro'yxati bo'sh bo'lsa ,"Siz so'ragan barcha
# mahsulotlar do'konimizda bor" degan xabarni, ahs holda "quyidagi mahsulotlar do'konimizda yo'q:...."
# degan xabarni chiqaring.


mahsulotlar = ["un","yog'","sovun","shakar","kartoshka","tuxum",
               "makaron","piyoz","sabzi","sholg'om"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}- mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")



