import pytest
from models.engenheiro import Engenheiro 
from models.endereco import Endereco    




@pytest.fixture
def pessoa_valida():
     engenheiro = Engenheiro ("Luiza", "458745", "marialuiza@gmail.com","123456", 5000, 
                              Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))
     return engenheiro

def test_engenheiro_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Luiza"

def test_engenheiro_telefone_valido(pessoa_valida):
     assert pessoa_valida.telefone == "458745"

def test_engenheiro_email_valido(pessoa_valida):
     assert pessoa_valida.email == "marialuiza@gmail.com"

def test_engenheiro_crea_valido(pessoa_valida):
    assert pessoa_valida.crea == "123456"

def test_engenheiro_salario_valido(pessoa_valida):
    assert pessoa_valida.salario == 5000

def test_engenheiro_endereco_logradouro_valido(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Anisio"

def test_engenheiro_endereco_numero_valido(pessoa_valida):
    assert pessoa_valida.endereco.numero == "44"

def test_engenheiro_endereco_complemento_valido(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Perto da padaria"

def test_engenheiro_endereco_cep_valido(pessoa_valida):
    assert pessoa_valida.endereco.cep == "40715366"

def test_engenheiro_endereco_cidade_valido(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Engenheiro("Luiza", "458745", "marialuiza@gmail.com", "123456", 5000, 
                    Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))
                            
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Engenheiro("Luiza", "458745", "marialuiza@gmail.com", "123456", 5000, 
                     Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" )) 
                    

