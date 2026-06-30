name = input("Введите имя ")
while True:
    count = int(input("введите число покупок "))
    if count > 0:
        break
    print("количество покупок должно быть положительным ")


spprice = []
znachenie_dlya_proverki = float(input("ведите число заданного порога "))

nol = 0
while count > nol:
    price_producta = float(input("введите стоимость покупки "))
    if price_producta < 0:
        print("введите корректную сумму")
        continue
    spprice.append(price_producta)
    nol += 1
sum_pokypok = sum(spprice)
sredn_chek = sum(spprice) / count
max_pokypka = max(spprice)

count_proverki = 0
for d in spprice:
    if d > znachenie_dlya_proverki:
        count_proverki += 1


if not spprice:
    print("Нет корректных покупок для анализа!")
else:
    print(f"сумма покупок {sum_pokypok}")
    print(f"средний чек {sredn_chek}")
    print(f"самая дорогая покупка {max_pokypka}")
    print(f"количество товаров больше порога {count_proverki}")
    print(f"ваша скидка 10%, общая стоимость всех покупок составляет {sum_pokypok * 0.9} рублей")
