from abc import ABC, abstractmethod 
from Atividade.endereco import Endereco
from Atividade.medico import Medico
from Atividade.engenherio import Engenheiro

class Funcionario (ABC): 
    def __init__(self, nome: str, telefone: str ,email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email 
        self.endereco = endereco 

