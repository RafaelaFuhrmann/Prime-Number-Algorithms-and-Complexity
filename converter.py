from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.styles import monokai

code = '''

def is_prime(number: int, divisors: list) -> bool:
    if number < 4:
        return number == 2 or number == 3
    
    for divisor in divisors:
        if number % divisor == 0:
            return False
    return True

def list_primes(n: int) -> list[int]:
    primes = []
    for number in range(n):
        if is_prime(number, primes):
            primes.append(number)
    return primes

'''


lexer = PythonLexer()

formatter = HtmlFormatter(style='monokai')

highlighted_code = highlight(code, lexer, formatter)

highlighted_code = highlighted_code.replace(" " * 8, " " * 4)

print(highlighted_code)