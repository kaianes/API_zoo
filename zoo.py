# Criação de Animais com nome, espécie e nível de felicidade. 

# Os animais podem ser alimentados, brincados e indicar se estão bem cuidados com base nos atributos citados. O nível de felicidade dos animais não pode ultrapassar 100.

#essa classe, foi adicionado o atributo bem_cuidado, que indica se o animal está bem cuidado ou não.

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.nivel_felicidade = 10
        self.bem_cuidado = True  # Adicionando o atributo bem_cuidado


    def alimentar(self):
        self.nivel_felicidade += 10
        if self.nivel_felicidade > 100:
            self.nivel_felicidade = 100

    def brincar(self):
        self.nivel_felicidade += 15
        if self.nivel_felicidade > 100:
            self.nivel_felicidade = 100
    
    def cuidar(self):
        if self.nivel_felicidade < 70:
            self.bem_cuidado = False

    def exibir_estado(self):
        print(f"{self.nome} é um(a) {self.especie} e está com nível de felicidade {self.nivel_felicidade}.")

# Criação de Recintos para abrigar os animais, contendo um ou mais animais que só podem ser da mesma espécie. Esses recintos podem ser  bem ou mal cuidados, dependendo se forem limpos não.

class Recinto:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.bem_cuidado = False
        self.animais = []

    def adicionar_animal(self, nome, especie):
        if especie == self.especie:
            self.animais.append(nome)

    def limpar_recinto(self):
        self.bem_cuidado = True 

# Receber visitantes - Esta função irá permitir que os jogadores ganhem dinheiro com base no número de visitantes que o zoológico atrai. Visitantes são atraídos por animais felizes e recintos bem cuidados.

