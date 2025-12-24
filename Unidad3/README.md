# Uso de NumPy y Pandas con Clases Personalizadas en Python

Este proyecto muestra cómo trabajar con **NumPy** y **pandas** en Python y cómo encapsular estas herramientas en tus propias clases para organizar mejor tu código y reutilizarlo de manera efectiva.

## NumPy

**NumPy** es una biblioteca para computación numérica en Python. Permite:

- Manejo eficiente de **arrays multidimensionales**.
- Operaciones matemáticas vectorizadas y rápidas.
- Álgebra lineal, estadísticas y transformadas.

Ejemplo básico:

```python
import numpy as np

# Crear un array
arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Operación vectorizada
```

## Pandas

pandas permite trabajar con datos tabulares de manera sencilla usando DataFrames y Series. Sus ventajas incluyen:

Leer y escribir CSV, Excel, SQL, JSON, etc.

Filtrar, agrupar y limpiar datos fácilmente.

Realizar operaciones estadísticas y de transformación de datos.

```python
import pandas as pd

# Crear un DataFrame
data = {'Nombre': ['Ana', 'Luis', 'Carlos'], 'Edad': [23, 30, 27]}
df = pd.DataFrame(data)

# Filtrar datos
adultos = df[df['Edad'] > 25]
print(adultos)
```

## Clases Personalizadas

Puedes encapsular la funcionalidad de NumPy y pandas en clases propias. Esto ayuda a:

Mantener el código organizado.

Reutilizar métodos específicos.

Agregar funcionalidades personalizadas.

Ejemplo con pandas:

```python
class MiDataFrame:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def agregar_columna(self, nombre, valores):
        self.df[nombre] = valores
    
    def filtrar_por_columna(self, columna, valor):
        return self.df[self.df[columna] == valor]
    
    def mostrar(self):
        print(self.df)
```
## Uso
```python
datos = {'Nombre': ['Ana', 'Luis', 'Carlos'], 'Edad': [23, 30, 27]}
mi_df = MiDataFrame(datos)
mi_df.agregar_columna('Ciudad', ['Bogotá', 'Medellín', 'Cali'])
mi_df.mostrar()
print(mi_df.filtrar_por_columna('Edad', 30))
```

## Ejemplo con NumPy:
```python
class MiArray:
    def __init__(self, lista):
        self.array = np.array(lista)
    
    def sumar(self, valor):
        return self.array + valor
    
    def multiplicar(self, valor):
        return self.array * valor
```

## Uso
```python
arr = MiArray([1, 2, 3, 4])
print(arr.sumar(5))
print(arr.multiplicar(10))
```

## Ejemplo de Uso Completo
```python
# Crear DataFrame
datos = {'Nombre': ['Ana', 'Luis', 'Carlos'], 'Edad': [23, 30, 27]}
mi_df = MiDataFrame(datos)

# Filtrar mayores de 25 años
adultos = mi_df.filtrar_por_columna('Edad', 30)

# Convertir a NumPy array y multiplicar
mi_array = MiArray(adultos['Edad'].values)
print(mi_array.multiplicar(2))

```


