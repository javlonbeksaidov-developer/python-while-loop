
'''
🔹 5. Matn sanash dasturi
Izoh:

Foydalanuvchidan so‘z/matn kiritish so‘raladi.
Agar foydalanuvchi "stop" yozsa → loop tugaydi.
Aks holda kiritilgan matnlar sanab boriladi.
Oxirida necha marta matn kiritilgani chiqariladi.
👉 Bu yerda o‘quvchilar:

loop orqali ma’lumot yig‘ish,
hisoblagich (count) ishlatish,
whileni shart bilan tugatishni o‘rganishadi.
'''

hisoblagich = 0

while True:
    text = input("so‘z/matn kiriting: ")
    
    if text == "stop":
        break
    
    elif text == "matn":
        hisoblagich += 1
    
    else:
        continue

print(f"Siz {hisoblagich} marta 'matn' so'zini kiritdingiz!")
  