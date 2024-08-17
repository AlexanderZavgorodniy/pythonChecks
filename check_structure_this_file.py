"""
Проверка кода в этом же файле, что он соответствует правилу
def main():
    #код
if __name__ == "__main__":
    main()
"""

import inspect


def check_main_structure():
    # Получаем текущий стек вызовов
    stack = inspect.stack()
    # Получаем исходный код текущего файла
    frame = stack[-1]
    lines, start_line = inspect.getsourcelines(frame[0])

    # Найдем индексы начала и конца конструкции main
    main_start = None
    main_end = None
    check_structure_line = None

    for i, line in enumerate(lines):
        if "def main()" in line and main_start is None:
            main_start = i
        if 'if __name__ == "__main__":' in line and i > 30:
            main_end = i
        elif "if __name__ == '__main__':" in line and i > 30:
            main_end = i
        if not "main()" in line and i - 1 == main_end:
            print(line, i)
            raise RuntimeError(
                "Неправильное использование конструкции 'if __name__ == \"__main__\":'"
            )
        if "check_main_structure()" in line:
            check_structure_line = i

    # Проверяем, что конструкция main присутствует
    if main_start is None or main_end is None:
        raise RuntimeError(
            "Не найдены конструкция 'def main():' и/или 'if __name__ == \"__main__\":'"
        )

    # Для проверки docstring
    flag_single_quote = False
    flag_double_quote = False
    # Проверяем, что все строки после check_main_structure() находятся внутри конструкции main
    for i, line in enumerate(lines):
        if (
            i <= check_structure_line
            or line[:3] == "def"
            or line[:5] == "class"
            or line[0] == " "
            or line == "\n"
            or line[0] == "#"
            or line[:4] == "from"
            or line[:6] == "import"
        ):
            continue

        # Проверка docsting
        if line[:3] == '"""':
            flag_double_quote = not flag_double_quote
            continue
        if line[:3] == "'''":
            flag_single_quote = not flag_single_quote
            continue
        if flag_double_quote or flag_single_quote:
            continue

        if i < main_start or i > main_end + 1:
            raise RuntimeError("Все строки должны находиться в конструкции main.")
        elif main_start < i < main_end:
            raise RuntimeError("Все строки должны находиться в конструкции main.")


check_main_structure()

def main():
    a = int(input())
    b = int(input())
    print(a + b)


if __name__ == '__main__':
    main()

