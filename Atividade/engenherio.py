class Engenheiro: 
    def __init__(self,nome: str, telefone: str, email: str, endereco: Endereco, crea: str, salario_base: float) -> None:
        self.crea= crea
        self.salario_base = salario_base

    def salario_final(self) -> float:
        return self.salario_base * 1.2 

    def __str__(self) -> str:
        return (f"\nCrea: {self.crea}")