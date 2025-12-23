Calculadora Orientada a Objetos en Python

Este proyecto implementa una calculadora en Python utilizando los principios de la Programación Orientada a Objetos (POO) y el patrón de diseño State. El objetivo principal es mostrar cómo el comportamiento de un objeto puede cambiar dinámicamente según su estado interno.

📌 Características

Implementación completa del patrón State

Uso de clases abstractas con ABC

Aplicación de los pilares de la POO:

Abstracción

Encapsulamiento

Herencia

Polimorfismo

Soporte para:

Operaciones binarias: suma, resta, multiplicación y división

Operaciones unarias: cambio de signo y raíz cuadrada

Manejo de errores mediante un estado específico

🧠 Estructura del programa

El programa está organizado en una serie de estados que representan el comportamiento de la calculadora en cada momento:

Calculadora: clase principal que delega el comportamiento en el estado actual.

EstadoCalculadora: clase abstracta que define la interfaz común de todos los estados.

EstadoInicial: estado inicial y final tras cada cálculo.

EstadoIntroducirPrimerOperando: gestiona la introducción del primer número.

EstadoResultadoParcial: almacena el primer operando y el operador seleccionado.

EstadoIntroducirSegundoOperando: gestiona la introducción del segundo número.

EstadoError: estado que representa una situación de error.

Cada estado se encarga de su propia lógica y decide cuándo y cómo cambiar a otro estado.

⚙️ Requisitos

Python 3.8 o superior

No se requieren librerías externas adicionales, solo módulos estándar de Python.
