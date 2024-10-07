from models.funcionario import Funcionario
from models.endereco import Endereco

class Engenheiro(Funcionario): 
    def __init__(self,nome: str, telefone: str, email: str, crea: str, salario_base: float, endereco: Endereco) -> None:
       
        self.crea= crea
        self.salario_base = salario_base

    def salario_final(self) -> float:
        return self.salario_base * 1.2 
    def __str__(self) -> str:
        return (f"\nCREA: {self.crea}")