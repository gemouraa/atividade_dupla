import pytest
from Atividade.engenheiro import Engenheiro 

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro ("Guilherme", 1111111, "Guilherme@gmail.com", Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" )
                             return Engenheiro

def test_engenheiro_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Mateus"

def test_engenheiro_telefone_valido(pessoa_valida):
     assert pessoa_valida.telefone == "7198442578"

def test_engenheiro_email_valido(pessoa_valida):
     assert pessoa_valida.email == "mateus@gmail.com"

def test_engenheiro_crea_valido(pessoa_valida):
    assert pessoa_valida.CREA == "7444"

