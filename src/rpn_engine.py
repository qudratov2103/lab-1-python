from .constants import VALS
import math

class ReversePolishMachine:

    def __init__(self):
        self.stack = []

    def _is_number(self, text: str) -> bool:
        """
        число это или нет хммм
        """
        try:
            float(text)
            return True
        except ValueError:
            return False

    def _do_operation(self, operation: str):
        """
        одна операция
        """
        if operation in ['u+', 'u-']:
            if len(self.stack) < 1:
                raise ValueError("Мало чисел для операции!")

            number = self.stack.pop()
            if operation == 'u+':
                self.stack.append(+number)
            else:
                self.stack.append(-number)


        else:
            if len(self.stack) < 2:
                raise ValueError("Нужно два числа для операции!")
            # порядооок
            second = self.stack.pop()
            first = self.stack.pop()

            try:
                if operation in ['//', '%']:
                    # проверочкааа
                    if not (isinstance(first, int) or first.is_integer()):
                        raise ValueError("Для операции // левое число должно быть целым")
                    if not (isinstance(second, int) or second.is_integer()):
                        raise ValueError("Для операции // правое число должно быть целым")

                    first = int(first)
                    second = int(second)

                result = VALS[operation](first, second)
                self.stack.append(result)

            except ZeroDivisionError:
                raise ValueError("Нельзя делить на ноль!")
            except ValueError as e:
                raise e
            except Exception as e:
                raise ValueError(f"Ошибка при вычислении: {e}")

    def calculate(self, expression: str) -> float:
        """
        вычислениее
        """
        self.stack = []

        tokens = expression.split()

        for token in tokens:
            if token in ['(', ')']:
                continue
            elif self._is_number(token):
                self.stack.append(float(token))
            elif token in VALS:
                self._do_operation(token)
            else:
                raise ValueError(f"Неизвестный символ: '{token}'")

        if len(self.stack) != 1:
            raise ValueError("Неправильная последовательность операций!")

        return self.stack[0]
