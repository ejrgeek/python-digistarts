class ValueNotAllowedException(Exception):
    """Exceção para quando receber um numero não valido"""
    def __str__(self):
        return "Um ou mais números não são permitidos"


class TotalNumberDiffListSizeException(Exception):
    """Exceção para caso a lista for maior ou menor que N"""
    def __str__(self):
        return "A lista deve ter o tamanho do numero total inserido"


class OperationNotFoundException(Exception):
    """Exceção para caso a operacao não seja +, -, *, /, %"""
    def __str__(self):
        return "Verifique se a operação está correta"
