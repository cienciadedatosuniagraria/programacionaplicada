# Calculadora por Estados en Python

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://pytest.org/)

---

## Descripción

Este proyecto implementa una **calculadora basada en máquina de estados** en Python.  
La calculadora soporta:

- **Operaciones binarias**: `+`, `-`, `*`, `/`
- **Operaciones unarias**: `s` (cambio de signo), `r` (raíz cuadrada)

La arquitectura de estados permite manejar la lógica de entrada de dígitos y operadores de forma modular y escalable.  
El proyecto incluye **tests unitarios con `pytest`** para garantizar su correcto funcionamiento.

---

## Estructura del proyecto

├── 📂 src/
│   └── 📂 paquete/
│       ├── 📄 __init__.py
│       └── 📄 modulo.py
├── 📂 tests/
│   └── 📄 test_calculadora.py
├── 📄 README.md
└── 📄 requirements.txt



- `src/paquete/modulo.py` → Contiene la clase `Calculadora` y todos los estados.
- `tests/test_calculadora.py` → Tests unitarios usando `pytest`.
- `requirements.txt` → Dependencias necesarias.
- `README.md` → Documentación del proyecto.

---

## Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto

python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt

## Uso

from src.paquete.modulo import Calculadora

calc = Calculadora()

# 2 + 3
calc.introducir_digito(2)
calc.introducir_operador('+')
calc.introducir_digito(3)
calc.calcular()

print(calc.valor_actual())  # Salida: 5

# Cambio de signo
calc.introducir_digito(5)
calc.introducir_operador('s')
print(calc.valor_actual())  # Salida: -5

# Raíz cuadrada
calc.introducir_operador('r')
print(calc.valor_actual())  # Salida: ~2.236

# 2 + 3 * 4
calc.introducir_digito(2)
calc.introducir_operador('+')
calc.introducir_digito(3)
calc.introducir_operador('*')
calc.introducir_digito(4)
calc.calcular()

print(calc.valor_actual())  # Salida: 20

# Tests

pytest tests/

## Ejemplo de test

import pytest
from src.paquete.modulo import Calculadora

def test_operaciones_basicas():
    calc = Calculadora()
    calc.introducir_digito(2)
    calc.introducir_operador('+')
    calc.introducir_digito(3)
    calc.calcular()
    assert calc.valor_actual() == 5

def test_operadores_unarios():
    calc = Calculadora()
    calc.introducir_digito(5)
    calc.introducir_operador('s')
    assert calc.valor_actual() == -5
    calc.introducir_operador('r')
    assert calc.valor_actual() == pytest.approx(5**0.5)

def test_error_operador_invalido():
    calc = Calculadora()
    calc.introducir_digito(2)
    calc.introducir_operador('%')

    assert calc.valor_actual() == '- Error -'

