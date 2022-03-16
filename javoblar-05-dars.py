#27/12/2021

# 05-dars : STRING (MATN)

# Muallif : Abdisamiyev Abdulahadxon

# 1. Pythonda quyidagi o'zgaruvchilarni yarating:
# ko'cha="Bog'bon"
# mahalla="Sag'bon"
#tuman="Bodomzor"
# viloyat=Samarqand"

kocha="Bog'bon"
mahalla="Sag'bon"
tuman="Bodomzor"
viloyat="Samarqand"

# 2. Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi , Sag'bon mahallasi , Bodomzor tumani , samarqand viloyati

print(kocha+" ko'chasi,"+mahalla+" mahallasi,"+tuman+" tumani,"+viloyat+" viloyati")

# 3.Yuqoridagi o'zgaruvchilarning (ko'cha,mahalla,tuman,viloyat) qiymatini foydalanuvchidan so'rang . Va avvalgi mashqni takrorlang!

print("Iltimos , quyidagi ma'lumotlarni kiriting:")
kocha=input("Ko'changiz:")
mahalla=input("Mahallangiz:")
tuman=input("Tumaningiz:")
viloyat=input("Viloyatingiz:")
print(kocha+" ko'chasi,"+mahalla+" mahallasi,"+tuman+" \
 tumani,"+viloyat+" viloyati")

# 4. Yuqoridagi matnni kosolga chiqarishda har bir verguldan keyin yangi qatordan yozing.

kocha="Bog'bon"
mahalla="Sag'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha+" ko'chasi,\n"+mahalla+" mahallasi,\n"+tuman+" tumani,\n"+viloyat+" viloyati")

# 5. Yuqoridagi matnni f-string yordamida yangi , manzil deb nomlangan o'zgaruvchiga yuklang

kocha="Bog'bon"
mahalla="Sag'bon"
tuman="Bodomzor"
viloyat="Samarqand"
manzil=f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

# 6. Manzil o'zgaruvchisiga biz yuqorida o'rgangan title(),upper(),lower(),\
# Capitalize() metodlarini qo'llab ko'ring.

print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())