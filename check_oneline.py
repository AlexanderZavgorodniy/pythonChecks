"""
Проверка кода, что он написан в одну строку
При этом в коде не используются:
- Символ ; в решении. Он слишком сильно упрощает задачу.
- функция eval
- функция exec
- модуль marshal (сериализация объектов в python)
"""
import inspect


def check():
    # Получаем текущий стек вызовов
    stack = inspect.stack()
    # Получаем исходный код текущего файла
    frame = stack[-1]
    lines, start_line = inspect.getsourcelines(frame[0])
    check_line = 0
    for i, line in enumerate(lines):
        if "check()" in line:
            check_line = i
    if len(lines) - check_line - 1 > 1:
        raise RuntimeError(
            "В программе больше одной строки"
        )
    code_line = lines[check_line+1]
    if 'eval' in code_line:
        raise RuntimeError(
            "Нельзя использовать функцию eval()"
        )
    if 'exec' in code_line:
        raise RuntimeError(
            "Нельзя использовать функцию exec()"
        )
    if ';' in code_line:
        raise RuntimeError(
            "Нельзя использовать знак ;"
        )
    if 'marshal' in code_line:
        raise RuntimeError(
            "Нельзя использовать модуль marshal"
        )


check()
# код