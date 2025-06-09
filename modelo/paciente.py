# -*- coding: utf-8 -*-
class Paciente:
    def __init__(self, nombre, dni, fecha_nacimiento):
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Todos los campos son obligatorios")
        self.__nombre__ = nombre
        self.__dni__ = dni
        self.__fecha_nacimiento__ = fecha_nacimiento

    def obtener_dni(self):
        return self.__dni__

    def __str__(self):
        return "{} (DNI: {}, Nacimiento: {})".format(self.__nombre__, self.__dni__, self.__fecha_nacimiento__)