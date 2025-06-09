# -*- coding: utf-8 -*-
from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre, matricula):
        if not nombre or not matricula:
            raise ValueError("Nombre y matrícula son obligatorios")
        self.__nombre__ = nombre
        self.__matricula__ = matricula
        self.__especialidades__ = []

    def agregar_especialidad(self, especialidad):
        for esp in self.__especialidades__:
            if esp.obtener_especialidad().lower() == especialidad.obtener_especialidad().lower():
                raise Exception("Especialidad duplicada")
        self.__especialidades__.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula__

    def obtener_especialidades(self):
        """Devuelve la lista de especialidades del médico"""
        return self.__especialidades__

    def obtener_especialidad_para_dia(self, dia):
        for esp in self.__especialidades__:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self):
        especialidades = ", ".join([str(e) for e in self.__especialidades__])
        return "{} (Matrícula: {}) - Especialidades: {}".format(self.__nombre__, self.__matricula__, especialidades)