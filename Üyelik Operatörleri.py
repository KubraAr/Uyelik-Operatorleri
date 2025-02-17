#Görev1
meyveler = ["elma", "armut", "çilek", "kiraz"]

meyve = input("Bir meyve adı girin: ")

if meyve in meyveler: #in bir ögenin içinde olup olmadığını kontrol eder
     print(f"{meyve} listede var.")
else:
     print(f"{meyve} listede yok.")

#Görev2
parola = "PyThOn123"

karakter = input("Bir karakter girin: ")

if karakter not in parola:
     print("Parolada bu karakter yok.")
else:
     print("Parolada bu karakter var.")