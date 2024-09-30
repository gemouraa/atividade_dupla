import os

from Atividade.endereco import  Endereco
from Atividade.funcionario import Funcionario
from Atividade.engenherio import Engenheiro
from Atividade.medico import Medico

os.system("clear")

pessoa_1 = Funcionario("Guilherme", "1111111", "Guilherme@gmail.com", Endereco("Anisio","115","atras da igreja de sao jorge", "40430510", "salvador"))
print(pessoa_1)