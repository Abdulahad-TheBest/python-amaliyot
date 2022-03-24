# 28/01/2022

# 11-dars : if-elif-else

# Muallif : Abdisamiyev Abdulahadxon


# Foydalanuvchidn yoshini so'rang va muzeyga kirish uchun chipta narxini
# quyidagicha chiqaring:

yosh = int(input("Yoshingiz nechida?"))

if yosh<=4 or yosh>=60:
    narh = 0;
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")
