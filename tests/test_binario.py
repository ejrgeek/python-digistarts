from business.binario import operacao


class TestBinario:

    def test_soma_bin(self):
        result = operacao(bin_um='00000001', op='+', bin_dois='00000011')
        assert result == '00000100'

    def test_sub_bin(self):
        result = operacao(bin_um='00000010', op='-', bin_dois='00000001')
        assert result == '00000001'

    def test_mult_bin(self):
        result = operacao(bin_um='00000001', op='*', bin_dois='00000011')
        assert result == '00000011'

    def test_div_bin(self):
        result = operacao(bin_um='00010100', op='/', bin_dois='00001000')
        assert result == '00000010'

    def test_mod_bin(self):
        result = operacao(bin_um='00010100', op='%', bin_dois='00000011')
        assert result == '00000010'
