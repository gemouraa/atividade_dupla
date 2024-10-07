import os
from models.funcionario import Funcionario  
from models.endereco import Endereco

class Medico():
    def __init__(self, nome: str, telefone: str, email: str, crm: str, salario_base: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.crm= crm
        self.salario_base = salario_base
        self.endereco = endereco

    def salario_final(self) -> float:
        return self.salario_base * 1.5

    def __str__(self) -> str:
        return (f"\nCrm: {self.crm}")
