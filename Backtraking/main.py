"""
    Pentru un n dat generați toate secvențele de paranteze care se închid corect.
    Examplu: n=4 două soluții: (()) și ()()
"""


def valid(secventa):
    """
    :param secventa: secventa cu paranteze de validat
    :return: True daca secventa e corecta si False daca nu e buna secventa
    """
    if len(secventa) % 2 == 1:
        return False
    if sum(x == '(' for x in secventa) != sum(x == ')' for x in secventa):
        return False
    i = 0
    while i < len(secventa) - 1:
        if secventa[i] == ')' and secventa[i + 1] == '(':
            return False
        if secventa[i] == '(' and secventa[i + 1] == ')':
            i += 1
        i += 1
    return True


def back_iterativ(n):
    """
    :param n: numraul de paranteze in secventa
    :return: lista cu toate posibilitatile de ordonare a parantezelor intr-un mod valid
    """
    solutions = []
    queue = []
    queue.append('(' * n)
    while queue != []:
        secventa = queue.pop()
        if valid(secventa) and secventa not in solutions:
            solutions.append(secventa)
        i = 0
        while i < n:
            if secventa[i] is '(':
                secventa = ("" if i is 0 else secventa[:i]) + ")" + ("" if i is n - 1 else secventa[(i + 1):])
                queue.append(secventa)
                secventa = ("" if i is 0 else secventa[:i]) + "(" + ("" if i is n - 1 else secventa[(i + 1):])
            i += 1
    return solutions


def back_recursiv(n, secventa="", index=0, solutions=[]):
    """
    :param n: numraul de paranteze in secventa
    :param secventa: secventa posibila
    :param index: index pt backtrackig
    :param solutions: Lista de solutii
    :return: lista cu toate posibilitatile de ordonare a parantezelor intr-un mod valid
    """
    if secventa == "":
        secventa = "(" * n
    for litera in '()':
        secventa = (secventa[:index] if index else "") + litera + ("" if index is n - 1 else secventa[(index + 1):])
        if index == n - 1:
            if valid(secventa):
                solutions.append(secventa)
        else:
            back_recursiv(n, secventa, index + 1, solutions)
    return solutions

def start():
    """
        Citeste numarul de paranteze dorite si afiseaza toate combinatiile posibile
    """
    options = {
        '1': back_iterativ,
        '2': back_recursiv
    }
    n = int(input("n = "))
    solutions = options['2'](n)
    if solutions == []:
        print("No Solution")
    else:
        print('There are %d solutions :' % len(solutions))
        for solution in solutions:
            print(solution)


if __name__ == "__main__":
    start()
