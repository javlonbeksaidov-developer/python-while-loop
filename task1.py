
'''
🔹 1. Raqam topish o‘yini
Izoh:

Kompyuter 1 dan 20 gacha tasodifiy son tanlaydi (random modulidan foydalanish mumkin).
O‘quvchi while loop orqali doim taxmin qiladi.
Agar foydalanuvchi kichikroq son kiritsa, kompyuter “Katta son” deydi.
Agar foydalanuvchi katta son kiritsa, “Kichik son” deydi.
To‘g‘ri topilganda esa loop tugashi kerak.
👉 Bu yerda asosiy g‘oya: loop faqat to‘g‘ri son topilganda to‘xtaydi.
'''

import random

random_num = random.randint(1, 20)

print(random_num)

ishora = True

while ishora:
    user_num = int(input("Son taxmin qiling: (1-20 son oralig'ida) "))
    
    if user_num == random_num:
        print("Tabriklayman siz kompyuter o'ylagan sonni topdingiz!")
        ishora = False
    
    elif user_num > random_num:
        print(f"Siz taxmin qilgan {user_num} soni kompyuter o'ylagan sondan katta")
    else:
        print(f"Siz taxmin qilgan {user_num} soni kompyuter o'ylagan sondan kichik")
