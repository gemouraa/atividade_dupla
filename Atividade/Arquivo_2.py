from abc import ABC, abstractmethod 
from Atividade.arquivo_1 import Endereco

class Funcionario (ABC): 
    def __init__(self, nome: str, telefone: str ,email: str, endereco: Endereco, salario: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email 
        self.endereco = endereco 
        self.salario = salario 

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\n Telefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}")