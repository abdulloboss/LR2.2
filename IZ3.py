for number in range(100, 1000):
    # Разбиваем число на цифры
    hundreds_digit = number // 100
    tens_digit = (number % 100) // 10
    ones_digit = number % 10

    # Вычисляем сумму цифр и их произведение
    digit_sum = hundreds_digit + tens_digit + ones_digit
    digit_product = hundreds_digit * tens_digit * ones_digit

    # Проверяем, равны ли сумма и произведение цифр
    if digit_sum == digit_product:
        print(number)