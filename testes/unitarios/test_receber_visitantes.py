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

# Teste para garantir que o método receber_dinheiro aumenta o dinheiro corretamente

def test_receber_dinheiro():
    visitantes = ReceberVisitantes()
    visitantes.receber_dinheiro(100)
    assert visitantes.dinheiro == 100  # O dinheiro deve aumentar em 100

# Teste para garantir que quanto mais animais felizes e recintos bem cuidados, mais visitantes são atraídos

def test_atrair_visitantes_felizes():
    visitantes = ReceberVisitantes()
    visitantes.atrair_visitantes_felizes(10)
    assert visitantes.visitantes == 10  # O número de visitantes deve aumentar em 10

# Teste para garantir que quanto mais animais felizes e recintos bem cuidados, mais dinheiro é recebido

def test_receber_dinheiro_felizes():
    visitantes = ReceberVisitantes()
    visitantes.receber_dinheiro_felizes(100)
    assert visitantes.dinheiro == 100  # O dinheiro deve aumentar em 100