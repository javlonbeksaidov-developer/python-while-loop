
'''
🔹 3. To‘plangan ball o‘yini
Izoh:

Boshlanishida ball = 0.

Foydalanuvchi input kiritadi:

Agar + yozsa → ball 10 ga oshadi.
Agar stop yozsa → loop tugaydi va umumiy ball chiqariladi.
Noto‘g‘ri belgi kiritilsa → “Faqat + yoki stop yozing!” deb ogohlantirish mumkin.

👉 Bu vazifa orqali o‘quvchilar:

while True: (cheksiz loop) yozishni,
break orqali loopni to‘xtatishni,
O‘zgaruvchini (ball) har safar yangilashni o‘rganishadi.
'''

ball = 0

while True:
    belgi = input("Belgi kiriting: ")
    
    if belgi == "+":
        ball += 10
    elif belgi == "stop":
        break
    else:
        print("Faqat + yoki stop yozing!")
        
print(f"Siz {ball} ball to'pladingiz!")