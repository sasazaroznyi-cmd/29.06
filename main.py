name = input("Введите имя ")
count = int(input("введите число покупок "))
spprice = []
znachenie_dlya_proverki = float(input("ведите число заданного порога "))
count_proverki = 0
for i in range(count):
    price_producta = float(input("введите стоимость покупки "))
    if price_producta < 0:
        print("введите корректную сумму")
        continue
    spprice.append(price_producta)
sum_pokypok = sum(spprice)
sredn_chek = sum(spprice) / count
max_pokypka = max(spprice)
for d in spprice:
    if d > znachenie_dlya_proverki:
        count_proverki += 1
print(sum_pokypok)
print(sredn_chek)
print(max_pokypka)
print(count_proverki)
print(f"ваша скидка 10%, общая стоимость всех покупок составляет {sum_pokypok * 0.1} рублей")