# Sprint_3a_task
# 1) x dəyişəninin işarəsini yoxla
x = 5        # nümunə dəyər
if x > 0:
    print("müsbət")
elif x < 0:
    print("mənfi")
else:
    print("sıfır")

# 2) n rəqəminin cüt/tək olmasını yoxla
n = 12       # nümunə dəyər
print("cüt" if n % 2 == 0 else "tək")

# 3) a, b, c arasından ən böyüyü tap
a, b, c = 7, 15, 10
print("ən böyük:", max(a, b, c))

# 4) day (1–7) üçün həftə gününü çap et
day = 3
week_days = {
    1: "Bazar ertəsi",
    2: "Çərşənbə axşamı",
    3: "Çərşənbə",
    4: "Cümə axşamı",
    5: "Cümə",
    6: "Şənbə",
    7: "Bazar"
}
print(week_days.get(day, "Yanlış gün"))

# 5) Temperatur kateqoriyası
temp = 18
if temp < 0:
    print("soyuq")
elif temp <= 20:
    print("normal")
else:
    print("isti")

# 6) Parol uzunluğuna görə təsnifat
password = "secret123"
length = len(password)
if length < 8:
    print("qısa")
elif length <= 12:
    print("orta")
else:
    print("uzun")

# 7) x-in 3 və 5-ə bölünməsini yoxla
x = 30
if x % 3 == 0 and x % 5 == 0:
    print("3 və 5")
elif x % 3 == 0:
    print("3")
elif x % 5 == 0:
    print("5")
else:
    print("heç biri")

# 8) 0–20 arası cüt rəqəmləri çap et
for num in range(0, 21, 2):
    print(num, end=" ")
print()  # sətirsonu

# 9) "Bağda ərik var idi …" simvol-simvol çap et
metn = "Bağda ərik var idi …"
for char in metn:
    print(char)

# 10) 1–10 arası ədədləri 3 istisna olmaqla çap et
for i in range(1, 11):
    if i == 3:
        continue
    print(i)

# 11) 1-dən başlayıb ilk 5-ə bölünəni while+break ilə tap
num = 1
while True:
    if num % 5 == 0:
        print("İlk 5-ə bölünən:", num)
        break
    num += 1

# 12) (1, 3, 5, 7, 9) siyahısında 5-in indeksini tap
nums = [1, 3, 5, 7, 9]
for idx, val in enumerate(nums):
    if val == 5:
        print("5-in indeksi:", idx)
        break
