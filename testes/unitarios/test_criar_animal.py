import pytest
from zoo import Animal

# Teste para garantir que a inicialização do animal está correta
def test_criar_animal():
    animal = Animal("Peter", "Gato Frajola")
    assert animal.nome == "Peter"
    assert animal.especie == "Gato Frajola"
    assert animal.nivel_felicidade == 10 # Nível de felicidade deve começar em 10

# Teste para garantir que o método alimentar aumenta o nível de felicidade corretamente
def test_alimentar():
    animal = Animal("Peter", "Gato Frajola")
    animal.alimentar()
    assert animal.nivel_felicidade == 20 # Nível de felicidade deve aumentar em 10

# Teste para garantir que o método brincar aumenta o nível de felicidade corretamente
def test_brincar():
    animal = Animal("Peter", "Gato Frajola")
    animal.brincar()
    assert animal.nivel_felicidade == 25  # Nível de felicidade deve aumentar em 15

# Teste para garantir que o nível de felicidade não ultrapassa 100
def test_limite_felicidade():
    animal = Animal("Peter", "Gato Frajola")
    for _ in range(10):
        animal.brincar()
    assert animal.nivel_felicidade == 100  # O nível de felicidade não pode ultrapassar 100

# Teste para garantir que o método cuidar define bem_cuidado corretamente
def test_cuidar():
    animal = Animal("Peter", "Gato Frajola")
    animal.cuidar()
    assert animal.bem_cuidado == False  # O animal está bem cuidado

# Teste para garantir que o método exibir_estado retorna a string correta
def test_exibir_estado(capfd):
    animal = Animal("Peter", "Gato Frajola")
    animal.exibir_estado()
    out, _ = capfd.readouterr()  # Captura a saída do método exibir_estado
    assert out.strip() == "Peter é um(a) Gato Frajola e está com nível de felicidade 10."

#obs: o capfd é um fixture que captura a saída padrão do terminal. Ele é utilizado para testar funções que imprimem algo no terminal.

#obs: o método strip() remove espaços em branco do início e do final de uma string. Ele é utilizado para garantir que a saída não tenha espaços em branco desnecessários.

#obs: o método readouterr() retorna uma tupla com a saída padrão e a saída de erro do terminal. Neste caso, estamos interessados apenas na saída padrão, por isso utilizamos o índice 0 para acessá-la.
