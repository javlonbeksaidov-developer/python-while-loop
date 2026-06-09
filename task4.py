
'''
🔹 4. Kalkulyator (oddiy versiya)
Izoh:

Foydalanuvchidan ikki son so‘raladi.
Keyin amal (+, -, *, /) tanlanadi.
Dastur hisoblab, natijani chiqaradi.
So‘ng: "Davom etasizmi? (ha/yo‘q)" deb so‘raladi.
Agar ha deb yozsa → loop davom etadi,
Agar yo‘q deb yozsa → loop tugaydi.
👉 Bu vazifada o‘quvchilar:

loopni foydalanuvchi xohishiga qarab to‘xtatish,
if-else orqali amallarni boshqarish,
input → int/float ga o‘tkazishni mashq qilishadi.
'''

while True:
    first_num = int(input("Birinchi sonni kiriting: "))
    second_num = int(input("Ikkinchi sonni kiriting: "))
    amal = input("Qaysi amalni bajarsin: (+, -, *, /) ")
    
    if amal == "+":
        result = first_num + second_num
        print(f"{first_num} va {second_num} sonlar yig'indisi {result}ga teng.")
    elif amal == "-":
        result = first_num - second_num
        print(f"{first_num} va {second_num} sonlar ayirmasi {result}ga teng.")
    elif amal == "*":
        result = first_num * second_num
        print(f"{first_num} va {second_num} sonlar ko'paytmasi {result}ga teng.")
    elif amal == "/":
        if second_num == 0:
            print("Sonni 0 ga bo'lib bo'lmaydi!")
        else:
            result = first_num / second_num
            print(f"{first_num} va {second_num} sonlar bo'linmasi {result}ga teng.")
    else:
        print("Siz noto'g'ri amal kiritdingiz! (+, -, *, /) dan kiriting: ")
        
    davom = input("Davom etasizmi? (yes or no) ")
    if davom == "no":
        break
    elif davom == "yes":
        continue
    else:
        pass
