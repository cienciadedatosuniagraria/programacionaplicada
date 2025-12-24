# tests/test_calculadora.py

import pytest
from src.paquete.modulo import Calculadora

def test_operaciones_basicas():
    calc = Calculadora()
    
    # Suma 2 + 3
    calc.introducir_digito(2)
    calc.introducir_operador('+')
    calc.introducir_digito(3)
    calc.calcular()
    assert calc.valor_actual() == 5

    # Resta 10 - 4
    calc.introducir_digito(1)
    calc.introducir_digito(0)
    calc.introducir_operador('-')
    calc.introducir_digito(4)
    calc.calcular()
    assert calc.valor_actual() == 6

    # Multiplicación 3 * 3
    calc.introducir_digito(3)
    calc.introducir_operador('*')
    calc.introducir_digito(3)
    calc.calcular()
    assert calc.valor_actual() == 9

    # División 8 / 2
    calc.introducir_digito(8)
    calc.introducir_operador('/')
    calc.introducir_digito(2)
    calc.calcular()
    assert calc.valor_actual() == 4

def test_operadores_unarios():
    calc = Calculadora()

    # Cambio de signo
    calc.introducir_digito(5)
    calc.introducir_operador('s')
    assert calc.valor_actual() == -5

    # Raíz cuadrada
    calc.introducir_operador('r')
    assert calc.valor_actual() == pytest.approx((5)**0.5)

def test_secuencia_combinada():
    calc = Calculadora()

    # 2 + 3 * 4 = 20 (evaluando secuencia)
    calc.introducir_digito(2)
    calc.introducir_operador('+')
    calc.introducir_digito(3)
    calc.introducir_operador('*')
    calc.introducir_digito(4)
    calc.calcular()
    assert calc.valor_actual() == 20

def test_error_operador_invalido():
    calc = Calculadora()

    # Operador inválido debe cambiar a EstadoError
    calc.introducir_digito(2)
    calc.introducir_operador('%')  # No existe
    assert calc.valor_actual() == '- Error -'

def test_reset_calculadora():
    calc = Calculadora()
    calc.introducir_digito(9)
    calc.reset()
    assert calc.valor_actual() == 0
