from Atividade.funcionario import Funcionario  

class Medico:
    def __init__(self, nome: str, telefone: str, email: str, crea: str) -> None:
        self.crea= crea
        self.salario_base = salario_base

    def salario_final(self) -> float:
        return self.salario_base * 1.5

    def __str__(self) -> str:
        return (f"\nCrm: {self.crm}")
