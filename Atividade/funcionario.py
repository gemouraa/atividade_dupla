from abc import ABC, abstractmethod 
from Atividade.endereco import Endereco

class Funcionario (ABC): 
    def __init__(self, nome: str, telefone: str ,email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email 
        self.endereco = endereco 
   

    def __str__(self) -> str:
     return     (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")
    
