import math

def radian_to_degree(radians):
    """Преобразование радиан в градусы."""
    return radians * 180 / math.pi

def degree_to_radian(degrees):
    """Преобразование градусов в радианы."""
    return degrees * math.pi / 180

def compute_trig_functions(angle, unit='degrees', precision=3):
    if unit == 'degrees':
        angle_rad = math.radians(angle)
    else:
        angle_rad = angle

    sin_value = round(math.sin(angle_rad), precision)
    cos_value = round(math.cos(angle_rad), precision)

    try:
        tan_raw = math.tan(angle_rad)
        if abs(tan_raw) > 1e10:
            tan_value = 'undefined'
        else:
            tan_value = round(tan_raw, precision)
    except:
        tan_value = 'undefined'

    return sin_value, cos_value, tan_value

def main():
    print("Программа для вычисления тригонометрических функций.")
    angle = float(input("Введите угол: "))
    unit = input("Выберите единицу измерения (degrees или radians): ").strip().lower()

    if unit not in ['degrees', 'radians']:
        print("Ошибка: выберите корректную единицу измерения!")
        return

    precision = int(input("Введите желаемую точность (например, 3 для 0.001): "))

    sin_value, cos_value, tan_value = compute_trig_functions(angle, unit, precision)

    print(f"\nРезультаты для угла {angle} {unit}:")
    print(f"Синус: {sin_value}")
    print(f"Косинус: {cos_value}")
    print(f"Тангенс: {tan_value}")

if __name__ == "__main__":
    main()