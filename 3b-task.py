# Sprint_3b_task
# 1) Heç bir arqument almayan funksiya
def salam():
    print("Salam, Dünya!")

# 2) Verilən rəqəmin kubunu qaytaran funksiya
def kub_hesabla(n):
    return n ** 3

# 3) İki sözü boşluqla birləşdirib qaytaran funksiya
def birlesdir(soz1, soz2):
    return f"{soz1} {soz2}"

# 4) Gələn list-in bütün elementlərini çap edən funksiya
def cap_et(lst):
    for item in lst:
        print(item)

# 5) İstənilən sayda rəqəmin cəmini qaytaran funksiya
def toplam(*args):
    return sum(args)

# 6) İstənilən sayda rəqəmin ortalamasını qaytaran funksiya
def ortalama(*args):
    if not args:                # Heç rəqəm verilməyibsə
        return "Rəqəm yoxdur"
    return sum(args) / len(args)

# 7) **kwargs qəbul edib cüt-cüt çap edən funksiya
def adlar_rəqəmlər(**kwargs):
    for ad, rəqəm in kwargs.items():
        print(f"ad: {ad}, rəqəm: {rəqəm}")

# 8) Dəyərin tipini yoxlayan funksiya
def tip_yoxla(dəyər):
    if isinstance(dəyər, str):
        print("mətn")
    elif isinstance(dəyər, (int, float, complex)):
        print("rəqəm")
    else:
        print("başqa")

# 9) Yaşa görə kateqoriya müəyyənləşdirən funksiya
def yas_kateqoriya():
    try:
        yas = int(input("Yaşınızı daxil edin: "))
        if yas < 18:
            print("Gənc")
        else:
            print("Yetkin")
    except ValueError:
        print("Rəqəm daxil edin!")

# 10) İstifadəçidən söz alıb uzunluğunu çap edən funksiya
def soz_uzunluq():
    soz = input("Söz daxil edin: ")
    print(f"Sözün uzunluğu: {len(soz)}")
