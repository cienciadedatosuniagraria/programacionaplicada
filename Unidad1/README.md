# 🐍 Paradigma de Programación Orientada a Objetos (POO) en Python

La **Programación Orientada a Objetos (POO)** es un paradigma que permite estructurar el código usando **objetos**, **clases** y **métodos**, lo que facilita la **reutilización**, **mantenimiento** y **organización** del código.

---

## ⚡ Conceptos Clave

| Concepto | Emoji | Descripción |
|----------|-------|-------------|
| **Clase** | 🏗️ | Plantilla o molde que define la estructura y comportamiento de un objeto. |
| **Objeto** | 🧱 | Instancia de una clase, con atributos y métodos propios. |
| **Atributo** | 📌 | Propiedad de un objeto que almacena información. |
| **Método** | 🔧 | Función definida dentro de una clase que realiza acciones con los objetos. |
| **Encapsulación** | 🔒 | Ocultar los detalles internos de un objeto y exponer solo lo necesario. |
| **Herencia** | 🌳 | Permite que una clase "hija" herede atributos y métodos de una clase "padre". |
| **Polimorfismo** | 🔄 | Permite que diferentes objetos respondan de manera distinta a un mismo método. |
| **Abstracción** | 🎭 | Definir solo la estructura esencial sin mostrar la implementación interna. |

---

## 🏗️ Clases y Objetos

```python
# Definir una clase
class Persona:
    def __init__(self, nombre, edad):  # Constructor
        self.nombre = nombre          # Atributo
        self.edad = edad              # Atributo
    
    def saludar(self):                # Método
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear objetos (instancias)
persona1 = Persona("Ana", 23)
persona2 = Persona("Luis", 30)

# Usar métodos
persona1.saludar()
persona2.saludar()
