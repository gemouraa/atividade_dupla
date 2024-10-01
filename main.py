import os

from Atividade.endereco import  Endereco
from Atividade.funcionario import Funcionario
from Atividade.engenheiro import Engenheiro
from Atividade.medico import Medico

os.system("clear")

pessoa_1 = Funcionario("Guilherme", 1111111, "Guilherme@gmail.com", Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador"))
pessoa_2 = Engenheiro("Luiza", "458745", "marialuiza@gmail.com", "123456", 5000, Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))
pessoa_3 = Medico("Guilherme", "12541254", "@gmail.com", "123456789", 4000,Endereco("Anisio", 44, "Perto da padaria", 40715366, "Salvador" ))
print(pessoa_1)
print("===========")
print(pessoa_2)
print("===========")
print(pessoa_3)
