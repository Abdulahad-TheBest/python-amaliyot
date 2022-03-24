
# 28/01/2022

# 11-dars : if-elif-else

# Muallif : Abdisamiyev Abdulahadxon

# foydalanuvchilar degan ro'yxat tuzing va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi
# kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan
# solishtiring .Agar ro'yxat da bunday login mavjud bo'lsa, "LOgin band
# yangi login tanlang!" , aks holda, "Xush kelibsiz, {foydalanuvchi}!
# xabarini chiqaring

foydalanuvchilar = ["abdulahad2002","admin","ruslan25","bexruz02"
    ,"shoh2003"]
login = input("Yangi login tanlang: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz {login}")