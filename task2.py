
'''
🔹 2. Parol tekshirish dasturi
Izoh:

Biror maxfiy parol oldindan belgilanadi, masalan "python123".
Foydalanuvchi while loop orqali parol kiritadi.
To‘g‘ri bo‘lmasa: "Xato! Qayta urinib ko‘ring." chiqadi.
To‘g‘ri kiritganda: "Xush kelibsiz!" chiqadi va loop tugaydi.
👉 Bu vazifada o‘quvchilar:

Cheksiz loopga tushmaslik uchun shartni to‘g‘ri qo‘yish,
Foydalanuvchidan doimiy input olish,
if bilan tekshirishni mashq qilishadi.
'''

password = "python123"

while True:
    parol = input("Parolni kiriting: ")
    
    if parol == password:
        print("Xush kelibsiz!")
        break
    else:
        print("Xato! Qayta urinib ko‘ring.")
