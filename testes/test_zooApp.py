import pytest
from zoo import Animal, Recinto, ReceberVisitantes

@pytest.fixture
def recinto_bem_cuidado():
    recinto = Recinto("Recinto1", "Leão")
    animal = Animal("Simba", "Leão")
    recinto.adicionar_animal(animal.nome, animal.especie)
    recinto.limpar_recinto()
    return recinto

@pytest.fixture
def recinto_mal_cuidado():
    recinto = Recinto("Recinto2", "Leão")
    animal = Animal("Nala", "Leão")
    recinto.adicionar_animal(animal.nome, animal.especie)
    return recinto

def test_atrair_visitantes_animal_bem_cuidado(recinto_bem_cuidado):
    zoológico = ReceberVisitantes()
    zoológico.atrair_visitantes(len(recinto_bem_cuidado.animais))
    assert zoológico.visitantes == 1

def test_atrair_visitantes_animal_mal_cuidado(recinto_mal_cuidado):
    zoológico = ReceberVisitantes()
    zoológico.atrair_visitantes(len(recinto_mal_cuidado.animais))
    assert zoológico.visitantes == 0
