import os

from Atividade.funcionario import  Endereco
from Atividade.funcionario import Funcionario
from Atividade.engenherio import Engenheiro
from Atividade.medico import Medico

os.system("clear")

pessoa_1 = Funcionario("Guilherme", "1111111", "Guilherme@gmail.com", Endereco("Anisio", "44", "Perto da padaria", "40715366", "Salvador"))

print (pessoa_1)