import os
import pytest
from models.funcionario import Funcionario
from models.endereco import Endereco

@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario("Moura",111,"guilherme@gmail.com",Endereco("Rua anisio",115,"atras da igreja",40430510,"Salvador"))
    return funcionario
def test_funcionario_nome_valido(pessoa_valida):
        assert pessoa_valida.nome == "Moura"