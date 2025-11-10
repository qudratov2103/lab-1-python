VALS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '**': lambda x, y: x ** y
}

ORDER = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
EXAMPLE = "( 3 4 + ) ( 5 2 - ) *" 