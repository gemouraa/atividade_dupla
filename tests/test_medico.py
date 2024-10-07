import pytest 
import os 
from models.medico import Medico
from models.endereco import Endereco
os.system("cls||clear")


@pytest.fixture
def pessoa_valida():
        medico = Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))
        return medico

def test_medico_nome_valido(pessoa_valida):
     assert pessoa_valida.nome == "Guilherme"



