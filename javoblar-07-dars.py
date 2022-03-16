
# 09/01/2022

# 07-dars : Ro'yxatlar - LISTS

# Muallif : Abdisamiyev Abdulahadxon

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizni ismini kiriting !

ismlar = ['Bexruz','Ruslan','Shohruz']
print(ismlar)

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring.

print(ismlar[0]+" mening eng yaqin do'stim")
print(ismlar[1]+" institutdagi juda ham yaqin kursdoshim hamda eng yaqin do'stim ")
print(ismlar[2]+" bilan opa-ukalarni farzandlarimiz")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat,manfiy,butun,o'nlik).

sonlar = [15,-8,10,5.2]
sonlar[0] = 20 # 1-qiymatni 20 ga o'zgartirdik
sonlar[-1] = 5.3 # 3-qiymatni 5.3 ga o'zgartiramiz
print(sonlar)

#Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring. Ba'zilarini esa almashtiring

print("[0]+[1]=",sonlar[0]+sonlar[1])
print("[0]-[2]=",sonlar[0]-sonlar[2])
print("[1]*[3]=",sonlar[1]*sonlar[3])
print("[0]/[3]=",sonlar[0]/sonlar[3])

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng
# ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonaviy tirik bo'lgan shaxslarning ismini kiriting

t_shaxslar = ['Amir Temur',"Mirzo Ulug'bek",'Shayx Muhammad Sodiq Muhammad Yusuf ']
z_shaxslar = ['Bill Gates','Pavel Durov','Ilon Mask']
print(t_shaxslar,)
print(z_shaxslar)
# Yuqorodagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()),
# quyidagi ko'rinishda chiqaring:

t_sh = t_shaxslar.pop(2)
z_shaxs = z_shaxslar.pop(2)
print("Men tarixiy shaxslardan",t_sh,"bilan,","zamonaviy shaxslardan",z_shaxs,"bilan suhbat qilishni istar edim.")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga
# chaqirmoqchi bo'lgan do'stlaringizni kiriting!

friends = [] # bo'sh ro'yhat
friends.append('Bexruz')
friends.append('Ruslan')
friends.append('Shohruz')
friends.append('Abubakir')
friends.append('Shohijahon')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni
# # .remove() metodi yordamida o'chirib tashlang

friends.remove('Ruslan')# Ro'yxatdan Ruslanni o'chirdik
friends.remove('Abubakir')
friends.remove('Shohijahon')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing

friends.append('Suxrob')
friends.insert(0,'Oybek')
friends.insert(-1,'Jahongir')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va
# .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini
# friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing

mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(1))
print("\nKelgan mehmonlar: ", mehmonlar)
