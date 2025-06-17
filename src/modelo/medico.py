import re
from .especialidad import Especialidad
from .exepciones import DatosInvalidosException, EspecialidadDuplicadaException


class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list = None):
        self._validar_nombre(nombre)
        self._validar_matricula(matricula)
        
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidades = []
        if especialidades:
            for especialidad in especialidades:
                self.agregar_especialidad(especialidad)

    def _validar_nombre(self, nombre: str):
        """Valida que el nombre no esté vacío y solo contenga letras, espacios y puntos."""
        if not nombre or not nombre.strip():
            raise DatosInvalidosException("El nombre no puede estar vacío")
        
        # Verificar que no contenga números
        if any(char.isdigit() for char in nombre):
            raise DatosInvalidosException("El nombre no puede contener números")
        
        # Quitar espacios y puntos para verificar que solo tenga letras
        nombre_solo_letras = nombre.replace(' ', '').replace('.', '')
        if not nombre_solo_letras.isalpha():
            raise DatosInvalidosException("El nombre solo puede contener letras, espacios y puntos")

    def _validar_matricula(self, matricula: str):
        """Valida que la matrícula tenga el formato correcto."""
        if not matricula or not matricula.strip():
            raise DatosInvalidosException("La matrícula no puede estar vacía")
        
        matricula_limpia = matricula.strip()
        if not (matricula_limpia.isdigit() and 4 <= len(matricula_limpia) <= 10):
            raise DatosInvalidosException("La matrícula debe tener entre 4 y 10 dígitos")

    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad validando que no esté duplicada."""
        if not isinstance(especialidad, Especialidad):
            raise DatosInvalidosException("El parámetro debe ser una instancia de Especialidad")
        
        # Verificar que no esté duplicada
        for esp_existente in self.__especialidades:
            if esp_existente.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower():
                raise EspecialidadDuplicadaException(f"La especialidad '{especialidad.obtener_especialidad()}' ya existe para este médico")
        
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_especialidades(self) -> list[Especialidad]:
        return self.__especialidades.copy()

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        """Devuelve el nombre de la especialidad disponible en el día especificado."""
        if not dia or not dia.strip():
            return None
            
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        if not self.__especialidades:
            return f"{self.__nombre}, {self.__matricula}, []"
        
        especialidades_str = ', '.join(str(e) for e in self.__especialidades)
        return f"{self.__nombre}, {self.__matricula}, [{especialidades_str}]"
