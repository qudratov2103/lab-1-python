from .constants import VALS

class ReversePolishMachine:

    def __init__(self):
        self.storage = []

    def _is_it_numeric(self, value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False
        
    def _complete_operation(self, operation: str):
        if len(self.storage) < 2:
            raise ValueError("Pohodu pochemuto Not enough data has given (hah) try once more")

        # KEEP ORDER!!!
        second_val = self.storage.pop()
        first_val = self.storage.pop()

        try:
            result_of_execution = VALS[operation](first_val, second_val)
            self.storage.append(result_of_execution)

        except ZeroDivisionError: # there is nothing impossible (ahah)
            raise ValueError("Pohodu you trying to divide by zeroooo")

    def calculate(self, expression_string: str) -> float:
        self.storage = []
        elements = expression_string.split()

        for value_operation in elements:
            if value_operation in ['(', ')']:
                continue
            elif self._is_it_numeric(value_operation):
                self.storage.append(float(value_operation))
            elif value_operation in VALS:
                self._complete_operation(value_operation)
            else:
                raise ValueError(f"Pohodu kakoyto Unknown element (hah) try once more)")

        if len(self.storage) != 1:
            raise ValueError("Pohodu u tebya Incorrect Sequence (hah) try once more")

        return self.storage[0]