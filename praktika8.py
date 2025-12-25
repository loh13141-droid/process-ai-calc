def read_number(prompt: str) -> float:
    """Безопасно читает число (float) из консоли."""
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Ошибка: введите число (например 12 или 3.14).")
def read_operation() -> str:
    """Читает операцию из набора + - * /."""
    allowed = {"+", "-", "*", "/"}
    while True:
        op = input("Операция (+, -, *, /): ").strip()
        if op in allowed:
            return op
        print("Ошибка: выберите одну из операций: +, -, *, /.")
def calculate(a: float, op: str, b: float) -> float:
    """Выполняет вычисление."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return a / b
    raise ValueError("Неизвестная операция.")
def main() -> None:
    print("Консольный калькулятор. Введите 'q' в операции, чтобы выйти.\n")
    while True:
        a = read_number("Первое число: ")
        op = input("Операция (+, -, *, /) или q для выхода: ").strip()
        if op.lower() == "q":
            print("Выход.")
            break
        if op not in {"+", "-", "*", "/"}:
            print("Ошибка: выберите +, -, *, / или q.\n")
            continue
        b = read_number("Второе число: ")
        try:
            result = calculate(a, op, b)
            print(f"Результат: {a} {op} {b} = {result}\n")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}\n")
if __name__ == "__main__":
    main()
