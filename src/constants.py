VALS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '//': lambda x, y: x // y,
    '%': lambda x, y: x % y,
    '**': lambda x, y: x ** y,
    'u+': lambda x: +x,  
    'u-': lambda x: -x
}

ORDER = {
    'u+': 4, 'u-': 4,  
    '**': 3,      
    '*': 2, '/': 2, '//': 2, '%': 2, 
    '+': 1, '-': 1 
}

EXAMPLE = "( 3 4 + ) ( 5 2 - ) *"