# 1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.
num = 123
str_num = str(num)
print("1)", str_num, type(str_num))

# 2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.
value = 19.99
int_value = int(value)
print("2)", int_value)

# 3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.
str_val = "500"
numeric_val = int(str_val)
print("3)", numeric_val / 2)

# 4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.
a = 8
b = 12
print("4) a < b:", a < b)
print("   a == b:", a == b)

# 5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.
x = 5
y = 10
z = 15
print("5)", (x < y) and (y < z))

# 6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.
print("6) Tam bölmə:", 25 // 4)
print("   Qalıq:", 25 % 4)
print("   Adi bölmə:", 25 / 4)

# 7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.
print("7)", 3 ** 4)

# 8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.
qiymet = 75.5
int_qiymet = int(qiymet)
print("8)", int_qiymet, type(int_qiymet))

# 9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.
n = 20
print("9) (n > 10) or (n < 5):", (n > 10) or (n < 5))
print("   (n > 15) and (n < 25):", (n > 15) and (n < 25))

# 10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.
val = "42.8"
float_val = float(val)
print("10) Float:", float_val, type(float_val))
int_val = int(float_val)
print("    Integer:", int_val, type(int_val))
