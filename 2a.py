# 1) 5, 10, 15, 20 rəqəmlərindən ibarət “rəqəmlər” adlı list yaradın
reqemler = [5, 10, 15, 20]

# 2) “rəqəmlər” listinin uzunluğunu tapın
print("2)", len(reqemler))

# 3) “rəqəmlər” listinə 25 elementini əlavə edin
reqemler.append(25)
print("3)", reqemler)

# 4) “rəqəmlər” listinin 2-ci indeksinə 12 elementini əlavə edin
reqemler.insert(2, 12)
print("4)", reqemler)

# 5) 1, 2, 3 və 4, 5, 6 listlərini birləşdirin
list1 = [1, 2, 3]
list2 = [4, 5, 6]
birlesmis = list1 + list2
print("5)", birlesmis)

# 6) “rəqəmlər” listindən 2-ci və 3-cü elementləri seçin
print("6)", reqemler[2:4])

# 7) “rəqəmlər” listinin ilk elementini 50 ilə əvəz edin 
reqemler[0] = 50
print("7)", reqemler)

# 8) “rəqəmlər” listində 19 elementinin olub-olmadığını yoxlayın
print("8)", 19 in reqemler)

# 9) "a", "b", "a", "c" listində "a" elementinin neçə dəfə təkrarlandığını tapın
hərflər = ["a", "b", "a", "c"]
print("9)", hərflər.count("a"))

# 10) "x", "y", "x", "z" listindən "x" elementlərini silin
hərflər2 = ["x", "y", "x", "z"]
while "x" in hərflər2:
    hərflər2.remove("x")
print("10)", hərflər2)

# 11) 7, 2, 9, 1 listini azalan sırayla sıralayın
siyahi = [7, 2, 9, 1]
siyahi.sort(reverse=True)
print("11)", siyahi)

# 12) “rəqəmlər” listindən 10-dan böyük elementləri seçin
boyuk_10 = [x for x in reqemler if x > 10]
print("12)", boyuk_10)
