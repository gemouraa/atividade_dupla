import pytest 
import os 
from models.medico import Endereco, Medico

os.system("cls||clear")


@pytest.fixture
def pessoa_valida():
    medico = Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))

    return medico

def test_medico_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Guilherme"

def test_medico_telefone_valido(pessoa_valida):
     assert pessoa_valida.telefone == "12541254"

def test_medico_email_valido(pessoa_valida):
     assert pessoa_valida.email == "@gmail.com"

def test_medico_crm_valido(pessoa_valida):
    assert pessoa_valida.crm == "123456789"
def test_medico_endereco_logradouro_valido(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "Anisio"

def test_medico_endereco_numero_valido(pessoa_valida):
    assert pessoa_valida.endereco.numero == "44"

def test_medico_endereco_complemento_valido(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "Perto da padaria"

def test_medico_endereco_cep_valido(pessoa_valida):
    assert pessoa_valida.endereco.cep == "40715366"

def test_medico_endereco_cidade_valido(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "Salvador"

def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
       Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))

def test_telefone_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))


def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))

