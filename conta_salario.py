from functools import total_ordering

@total_ordering
class ContaSalario():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"Codigo:{self._codigo} Saldo:{self._saldo}"

    def __eq__(self, other):
        return self._codigo == other._codigo  and self._saldo == other._saldo

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo

