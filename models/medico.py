from models.funcionario import Funcionario  
from models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, salario_base: float, endereco: Endereco) -> None:
        self.crm= crm
        self.salario_base = salario_base

    def salario_final(self) -> float:
        return self.salario_base * 1.5

    def __str__(self) -> str:
        return (f"\nCrm: {self.crm}")
