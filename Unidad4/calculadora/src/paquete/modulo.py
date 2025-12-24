# src/paquete/modulo.py

from math import sqrt
from abc import ABC, abstractmethod

# Funciones binarias
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y

# Funciones unarias
cambio_de_signo = lambda x: -x
raiz = lambda x: sqrt(x)

# Diccionarios de operadores
binarios = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}

unarios = {
    's': cambio_de_signo,
    'r': raiz
}


class Calculadora:
    """
    Clase principal de la calculadora que maneja el estado actual y delega la
    lógica a los distintos estados.
    """

    def __init__(self):
        """Inicializa la calculadora en el estado inicial."""
        self.reset()

    def reset(self):
        """Resetea la calculadora al estado inicial con valor 0."""
        self._estado = EstadoInicial(self, 0)

    def introducir_digito(self, digito):
        """
        Introduce un dígito en la calculadora.

        Args:
            digito (str o int): Dígito a introducir.
        """
        self._estado.introducir_digito(digito)

    def introducir_operador(self, operador):
        """
        Introduce un operador en la calculadora.

        Args:
            operador (str): Operador a aplicar.
        """
        try:
            self._estado.introducir_operador(operador)
        except Exception:
            self.cambiar_estado(EstadoError(self))

    def calcular(self):
        """Realiza el cálculo según el estado actual."""
        try:
            self._estado.calcular()
        except Exception:
            self.cambiar_estado(EstadoError(self))

    def valor_actual(self):
        """
        Obtiene el valor actual de la calculadora según el estado.

        Returns:
            float o str: Valor actual de la calculadora.
        """
        return self._estado.valor_actual()

    def cambiar_estado(self, estado):
        """
        Cambia el estado de la calculadora.

        Args:
            estado (EstadoCalculadora): Nuevo estado.
        """
        self._estado = estado


class EstadoCalculadora(ABC):
    """
    Clase abstracta base para los estados de la calculadora.
    Define la interfaz que deben implementar todos los estados.
    """

    def __init__(self, calculadora):
        """
        Inicializa el estado con referencia a la calculadora.

        Args:
            calculadora (Calculadora): Calculadora asociada.
        """
        self._calculadora = calculadora

    def introducir_digito(self, digito):
        """Método opcional para manejar dígitos en este estado."""
        pass

    def introducir_operador(self, operador):
        """Método opcional para manejar operadores en este estado."""
        pass

    def calcular(self):
        """Método opcional para realizar cálculos en este estado."""
        pass

    @abstractmethod
    def valor_actual(self):
        """Debe devolver el valor actual según el estado."""
        pass

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de la calculadora.

        Args:
            nuevo_estado (EstadoCalculadora): Nuevo estado.
        """
        self._calculadora.cambiar_estado(nuevo_estado)


class EstadoInicial(EstadoCalculadora):
    """
    Estado inicial de la calculadora, donde se espera un dígito o
    un operador unario para operar sobre el valor inicial.
    """

    def __init__(self, calculadora, numero):
        """
        Inicializa el estado inicial con un número.

        Args:
            calculadora (Calculadora): Calculadora asociada.
            numero (float): Valor inicial.
        """
        super().__init__(calculadora)
        self._numero = numero

    def introducir_digito(self, digito):
        """Cambia al estado de introducción del primer operando con el dígito ingresado."""
        self.cambiar_estado(EstadoIntroducirPrimerOperando(self._calculadora, digito))

    def introducir_operador(self, operador):
        """
        Aplica un operador al valor inicial o cambia al estado de resultado parcial.

        Args:
            operador (str): Operador a aplicar.
        """
        if operador in unarios:
            self._numero = unarios[operador](self._numero)
        elif operador in binarios:
            self.cambiar_estado(EstadoResultadoParcial(self._calculadora, self._numero, self._numero, operador))
        else:
            raise ValueError(f'No existe el operador "{operador}".')

    def valor_actual(self):
        """Devuelve el valor actual en este estado."""
        return self._numero


class EstadoIntroducirPrimerOperando(EstadoCalculadora):
    """
    Estado en el que se introduce el primer operando, acumulando dígitos
    hasta que se introduce un operador.
    """

    def __init__(self, calculadora, digito):
        """
        Inicializa el estado con un primer dígito.

        Args:
            calculadora (Calculadora): Calculadora asociada.
            digito (str o int): Primer dígito ingresado.
        """
        super().__init__(calculadora)
        self._digitos = []
        self.introducir_digito(digito)

    def introducir_digito(self, digito):
        """Agrega un dígito al número actual."""
        digito = str(digito)
        if digito == '.':
            if '.' not in self._digitos:
                if len(self._digitos) == 0:
                    self._digitos.append('0')
                self._digitos.append(digito)
        else:
            if len(self._digitos) == 1 and self._digitos[0] == '0':
                self._digitos.clear()
            self._digitos.append(digito)

    def introducir_operador(self, operador):
        """
        Aplica un operador sobre el número ingresado.

        Args:
            operador (str): Operador a aplicar.
        """
        if operador in unarios:
            numero = self._get_numero()
            numero = unarios[operador](numero)
            self.cambiar_estado(EstadoInicial(self._calculadora, numero))
        elif operador in binarios:
            numero = self._get_numero()
            self.cambiar_estado(EstadoResultadoParcial(self._calculadora, numero, numero, operador))
        else:
            raise ValueError(f'No existe el operador "{operador}".')

    def _get_numero(self):
        """Convierte los dígitos acumulados en un número float."""
        return float(''.join(self._digitos))

    def valor_actual(self):
        """Devuelve el número ingresado como string."""
        return ''.join(self._digitos)


class EstadoResultadoParcial(EstadoCalculadora):
    """
    Estado en el que ya se ha introducido el primer operando y un operador
    binario. Espera el segundo operando o más operadores unarios/binarios.
    """

    def __init__(self, calculadora, primer_operando, numero, operador):
        """
        Inicializa el estado con primer operando, operador y número actual.

        Args:
            calculadora (Calculadora): Calculadora asociada.
            primer_operando (float): Primer operando.
            numero (float): Número actual.
            operador (str): Operador binario.
        """
        super().__init__(calculadora)
        self._primer_operando = primer_operando
        self._numero = numero
        self._operador = operador

    def introducir_digito(self, digito):
        """Cambia al estado de introducción del segundo operando con el dígito ingresado."""
        self.cambiar_estado(EstadoIntroducirSegundoOperando(self._calculadora, self._primer_operando, self._operador, digito))

    def introducir_operador(self, operador):
        """Actualiza el operador o aplica un operador unario sobre el número actual."""
        if operador in unarios:
            self._numero = unarios[operador](self._numero)
        elif operador in binarios:
            self._operador = operador
        else:
            raise ValueError(f'No existe el operador "{operador}".')

    def calcular(self):
        """Realiza el cálculo del primer y segundo operando con el operador."""
        resultado = binarios[self._operador](self._primer_operando, self._numero)
        self.cambiar_estado(EstadoInicial(self._calculadora, resultado))

    def valor_actual(self):
        """Devuelve el valor actual del segundo operando."""
        return self._numero


class EstadoIntroducirSegundoOperando(EstadoIntroducirPrimerOperando):
    """
    Estado en el que se introduce el segundo operando para realizar la operación
    binaria pendiente.
    """

    def __init__(self, calculadora, primer_operando, operador, digito):
        """
        Inicializa el estado con el primer operando, operador y primer dígito del segundo operando.

        Args:
            calculadora (Calculadora): Calculadora asociada.
            primer_operando (float): Primer operando.
            operador (str): Operador binario.
            digito (str o int): Primer dígito del segundo operando.
        """
        super().__init__(calculadora, digito)
        self._primer_operando = primer_operando
        self._operador = operador

    def introducir_operador(self, operador):
        """Aplica operador unario sobre el segundo operando o cambia de operador binario."""
        if operador in unarios:
            resultado = unarios[operador](self._get_numero())
            self.cambiar_estado(EstadoResultadoParcial(self._calculadora, self._primer_operando, resultado, self._operador))
        elif operador in binarios:
            resultado = binarios[self._operador](self._primer_operando, self._get_numero())
            self.cambiar_estado(EstadoResultadoParcial(self._calculadora, resultado, resultado, operador))
        else:
            raise ValueError(f'No existe el operador "{operador}".')

    def calcular(self):
        """Calcula el resultado de la operación pendiente y vuelve al estado inicial."""
        resultado = binarios[self._operador](self._primer_operando, self._get_numero())
        self.cambiar_estado(EstadoInicial(self._calculadora, resultado))


class EstadoError(EstadoCalculadora):
    """
    Estado de error de la calculadora. No permite más operaciones
    hasta que se reinicie la calculadora.
    """

    def __init__(self, calculadora):
        """Inicializa el estado de error."""
        super().__init__(calculadora)

    def valor_actual(self):
        """Devuelve un mensaje de error."""
        return '- Error -'
