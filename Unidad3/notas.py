import numpy as np
import pandas as pd

class GestorCalificaciones:
    def __init__(self, datos):
        """
        datos: lista de diccionarios con la información de los estudiantes
        """
        self._df = pd.DataFrame(datos)

    def promedio_por_estudiante(self):
        """Calcula el promedio de cada estudiante usando NumPy"""
        notas = self._df[['nota1', 'nota2', 'nota3']].to_numpy()
        promedios = np.mean(notas, axis=1)
        self._df['promedio'] = promedios
        return self._df[['nombre', 'promedio']]

    def promedio_general(self):
        """Calcula el promedio general del curso"""
        return np.mean(self._df[['nota1', 'nota2', 'nota3']].to_numpy())

    def estudiantes_aprobados(self, minimo=3.0):
        """Devuelve los estudiantes aprobados usando Pandas"""
        if 'promedio' not in self._df:
            self.promedio_por_estudiante()
        return self._df[self._df['promedio'] >= minimo]

    def obtener_datos(self):
        """Devuelve una copia del DataFrame"""
        return self._df.copy()
