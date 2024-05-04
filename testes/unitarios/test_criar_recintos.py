import pytest
from zoo import Recinto

# Teste para garantir que a inicialização do recinto está correta

def test_criar_recinto():
    recinto = Recinto("Recinto dos Leões", "Leão")
    assert recinto.nome == "Recinto dos Leões"
    assert recinto.especie == "Leão"
    assert recinto.bem_cuidado == False  # O recinto deve começar bem cuidado
    assert recinto.animais == []  # O recinto deve começar vazio

# Teste para garantir que o método adicionar_animal adiciona um animal ao recinto corretamente

def test_adicionar_animal():
    recinto = Recinto("Recinto dos Leões", "Leão")
    recinto.adicionar_animal("Simba", "Leão")
    assert recinto.animais == ["Simba"]  # O animal deve ser adicionado ao recinto

# Teste para garantir que o só animais da mesma espécie podem ser adicionados ao recinto

def test_especie_correta():
    recinto = Recinto("Recinto dos Leões", "Leão")
    recinto.adicionar_animal("Simba", "Leão")
    recinto.adicionar_animal("Nala", "Leão")
    recinto.adicionar_animal("Zazu", "Pássaro")
    assert recinto.animais == ["Simba", "Nala"]  # Apenas animais da mesma espécie devem ser adicionados

# Teste para garantir que o método limpar_recinto define bem_cuidado como True

def test_limpar_recinto():
    recinto = Recinto("Recinto dos Leões", "Leão")
    recinto.limpar_recinto()
    assert recinto.bem_cuidado == True  # O recinto deve estar bem cuidado




