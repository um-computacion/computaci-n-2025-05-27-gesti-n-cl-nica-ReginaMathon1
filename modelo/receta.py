# -*- coding: utf-8 -*-
from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        if not paciente or not medico or not medicamentos:
            raise ValueError("Todos los campos son obligatorios")
        if not isinstance(medicamentos, list) or len(medicamentos) == 0:
            raise ValueError("Debe indicar al menos un medicamento")
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = datetime.now()

    def __str__(self):
        meds = ", ".join(self.__medicamentos__)
        return "Receta para {} por {} - Medicamentos: {} - Fecha: {}".format(
            self.__paciente__, self.__medico__, meds, self.__fecha__.strftime("%d/%m/%Y %H:%M"))