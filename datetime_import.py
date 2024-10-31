from datetime import datetime

# Словарь с названиями газет и их форматами дат
DATE_FORMATS = {
    "The Moscow Times": "%A, %B %d, %Y",
    "The Guardian": "%A, %d.%m.%y",
    "Daily News": "%A, %d %B %Y"
}

def parse_date(date_str):
    """Пытается распознать строку даты, возвращает объект datetime или None."""
    for name, date_format in DATE_FORMATS.items():
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue  # Переходим к следующему формату, если текущий не подошёл
    return None  # Если ни один формат не подошёл

def main():
    print("Введите дату в формате одной из газет или 'exit' для завершения:")
    while True:
        date_input = input("Дата: ").strip()  # Убираем лишние пробелы
        
        if date_input.lower() == 'exit':
            print("Завершение программы.")
            break
        
        try:
            parsed_date = parse_date(date_input)
            if parsed_date:
                print("Дата успешно преобразована:", parsed_date)
            else:
                print("Неправильный формат даты.")
                
                # Запрашиваем у пользователя название газеты и формат
                newspaper = input("Введите название газеты: ").strip()
                date_format = input("Введите формат даты (например, Wednesday, October 2, 2002 — %A, %B %d, %Y): ").strip()
                
                try:
                    parsed_date = datetime.strptime(date_input, date_format)
                    print(f"Дата успешно преобразована для '{newspaper}': {parsed_date}")
                except ValueError:
                    print("Ошибка: Неверный формат даты. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте снова.")

if __name__ == "__main__":
    main()