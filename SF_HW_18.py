sum_tickets = 0
quant_tickets = int(input("Введите количество билетов:"))
for age in range(quant_tickets):
    age = int(input("Введите возраст:"))
    if age < 18:
        sum_tickets += 0
    elif age >= 18 and age <= 25:
        sum_tickets += 990
    elif age > 25:
        sum_tickets += 1390
if sum_tickets == 0:
    print("Для детей проход бесплатный")
else:
    print("Количество билетов:", quant_tickets, "шт." )
if quant_tickets > 3:
    discount = sum_tickets / 100 * 10
    print("Скидка:", discount, "руб.")
    print("К оплате:", (sum_tickets -discount), "руб.")
