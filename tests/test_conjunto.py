from business.conjuntos import tratamento_conjunto


class TestConjunto:

    def test_tamanho_lista(self):
        """numeros duplicados, precisa ficar na metade"""
        lista = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]
        conj = tratamento_conjunto(lista)
        assert len(lista)/2 == len(conj)

    def test_conjunto_crescente(self):
        """O Set ja deixa na ordem crescente"""
        lista = [10, 10, 9, 9, 8, 8, 7, 7, 6, 6]
        conj_1 = tratamento_conjunto(lista)
        conj_2 = tratamento_conjunto(lista)
        conj_1 = set(sorted(conj_1))

        assert conj_1 == conj_2