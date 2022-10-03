from string import printable
from prettytable import PrettyTable


# python -m pip install -U prettytable


class SymbolCounter:
    def __init__(self):
        self.symbols = {}

    def __call__(self, file, *args, **kwargs):
        for string in file:
            for i in string:
                self.symbols[i] = self.symbols.get(i, 0) + 1
        return self.symbols.copy()


def foo():
    with open('text.txt', 'r') as f:
        mt = PrettyTable()
        mt.field_names = ['Symbol', "Amount"]
        sc = SymbolCounter()
        res = sc(f)
        for q in printable:
            if q == ' ':
                mt.add_row(['" "', res[q]])
            elif q == '\n':
                mt.add_row(['перенос', res[q]])
            else:
                try:
                    mt.add_row([q, res[q]])
                except:
                    pass
        print(mt)


if __name__ == '__main__':
    foo()
