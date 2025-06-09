# -*- coding: utf-8 -*-
class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        if not paciente or not medico or not fecha_hora or not especialidad:
            raise ValueError("Todos los campos son obligatorios")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        return "Turno: {} - {} - Paciente: {} - Médico: {}".format(self.__especialidad__, self.__fecha_hora__, self.__paciente__, self.__medico__)