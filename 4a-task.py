# Sprint_4a_task

# 1) İki ədəd və əməliyyata görə kalkulyator funksiyası
def kalkulyator():
    try:
        a = float(input("Birinci ədədi daxil edin: "))
        b = float(input("İkinci ədədi daxil edin: "))
        əməliyyat = input("Əməliyyat seçin (+, -, *, /): ").strip()

        if əməliyyat == "+":
            nəticə = a + b
        elif əməliyyat == "-":
            nəticə = a - b
        elif əməliyyat == "*":
            nəticə = a * b
        elif əməliyyat == "/":
            if b == 0:
                raise ZeroDivisionError("0-a bölmək olmaz!")
            nəticə = a / b
        else:
            raise ValueError("Yanlış əməliyyat simvolu!")

        print("Nəticə:", nəticə)

    except ValueError as ve:
        print("Dəyər xətası:", ve)
    except TypeError as te:
        print("Tip xətası:", te)
    except ZeroDivisionError as zde:
        print("Bölmə xətası:", zde)
    finally:
        print("Hesablama bitdi\n")

# 2) 1-dən 50-yə qədər 11-ə bölünən ədədlər
bolunen_11 = [n for n in range(1, 51) if n % 11 == 0]

# 3) Sözlərin ilk hərflərini götür
sözlər = ["kitab", "qələm", "defter", "silgi"]
ilk_hərflər = [s[0] for s in sözlər]

# 4) Şəhər–kod dictionary-si
şəhərlər = ["Bakı", "Gəncə", "Sumqayıt"]
kodlar   = [12, 22, 18]
şəhər_kod = dict(zip(şəhərlər, kodlar))

# 5) Km-ni milə çevirən lambda
km_to_mil = lambda km: km * 0.621371
test_km = [1, 5, 10, 21.1, 42.195]
mil_dəyərlər = list(map(km_to_mil, test_km))

# 6) Qiymətlərə 18 % vergi əlavə etmək
qiymətlər = [100, 200, 300, 400]
vergili_qiymətlər = list(map(lambda x: x * 1.18, qiymətlər))

# 7) İki siyahının elementlərini ikiqat artırıb cəmləmək
list1 = [3, 7, 12]
list2 = [2, 4, 6]
cəm_ikiqat = list(map(lambda a_b: a_b[0]*2 + a_b[1]*2, zip(list1, list2)))
# alternativ sadə yazılış:
# cəm_ikiqat = [2*a + 2*b for a, b in zip(list1, list2)]

# 8) Reduce ilə ən kiçik qiyməti tapmaq
from functools import reduce
qiymətlər2 = [150, 80, 220, 45]
ən_kiçik = reduce(lambda x, y: x if x < y else y, qiymətlər2)

# -----------------------------------------------
# Nümunə nəticələri (istəyə bağlı display)
if __name__ == "__main__":
    print("2) 11-ə bölünənlər:", bolunen_11)
    print("3) İlk hərflər:", ilk_hərflər)
    print("4) Şəhər-Kod:", şəhər_kod)
    print("5) Mil dəyərləri:", mil_dəyərlər)
    print("6) Vergili qiymətlər:", vergili_qiymətlər)
    print("7) Cəm (ikiqat):", cəm_ikiqat)
    print("8) Ən kiçik:", ən_kiçik)
    # 1-ci funksiyanı sınaq üçün şərh işarəsini silib çağırın
    # kalkulyator()
