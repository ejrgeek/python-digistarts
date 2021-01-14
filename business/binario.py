def decimal_para_binario(dado) -> str:
    valor = bin(dado)
    valor = valor.replace('0b', '')
    return '0' * (8-len(valor)) + valor


def operacao(bin_um, op, bin_dois):
    dec_um = int(bin_um, 2)
    dec_dois = int(bin_dois, 2)
    result = 0

    if op == '+':
        result = dec_um + dec_dois
    if op == '-':
        result = dec_um - dec_dois
    if op == '*':
        result = dec_um * dec_dois
    if op == '/':
        try:
            result = dec_um / dec_dois
        except ZeroDivisionError as e:
            return e
    if op == '%':
        result = dec_um % dec_dois

    return decimal_para_binario(int(result))
