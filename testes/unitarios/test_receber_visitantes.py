import pytest
from zoo import ReceberVisitantes

# Teste para garantir que a inicialização do recinto está correta

def test_receber_visitantes():
    visitantes = ReceberVisitantes()
    assert visitantes.dinheiro == 0
    assert visitantes.visitantes == 0

# Teste para garantir que o método atrair_visitantes aumenta o número de visitantes corretamente

def test_atrair_visitantes():
    visitantes = ReceberVisitantes()
    visitantes.atrair_visitantes(5)
    assert visitantes.visitantes == 5  # O número de visitantes deve aumentar em 5

# Teste para garantir que o método receber_dinheiro aumenta o dinheiro corretamente, para cada visitante, o dinheiro aumenta em 10

def test_receber_dinheiro():
    visitantes = ReceberVisitantes(0, 5)
    visitantes.receber_dinheiro()
    assert visitantes.dinheiro == 50 


