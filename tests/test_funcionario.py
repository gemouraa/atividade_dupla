import pytest

from models.funcionario import Funcionario

@pytest.fixture
def funcionario_valido():
    funcionario = funcionario("Moura",111,"guilherme@gmail.com")
    return funcionario
def test_funcionario_nome_valido(funcionario_valido):
    funcionario_valido.nome = "Moura"
    assert funcionario_valido.nome == "Moura"