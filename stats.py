def calculate_mean(numbers):
    # среднее значение списка
    return sum(numbers) / len(numbers)

def calculate_std(numbers):
    mean = calculate_mean(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance ** 0.5