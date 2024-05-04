# Criação de Animais com nome, espécie e nível de felicidade.

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = 10

    def alimentar(self):
        self.nivel_felicidade += 10
        if self.nivel_felicidade > 100:
            self.nivel_felicidade = 100

    def brincar(self):
        self.nivel_felicidade += 15
        if self.nivel_felicidade > 100:
            self.nivel_felicidade = 100

    def exibir_estado(self):
        print(f"{self.nome} é um(a) {self.especie} e está com nível de felicidade {self.nivel_felicidade}.")


# Criação de Recintos para abrigar os animais, contendo um ou mais animais da mesma espécie, sendo estes bem ou mal cuidados. Pense em funções para alterar os recintos.

# Alimentar os Animais, sendo que isso irá tornar os animais mais ou menos felizes.

# Receber visitantes - Esta função irá permitir que os jogadores ganhem dinheiro com base no número de visitantes que o zoológico atrai. Visitantes são atraídos por animais felizes e recintos bem cuidados.