# -*- coding: utf-8 -*-
class Especialidad:
    DIAS_VALIDOS = [
        "lunes", "martes", "miércoles", "miercoles", "jueves", "viernes", "sábado", "sabado", "domingo"
    ]

    def __init__(self, tipo, dias):
        if not tipo or not dias:
            raise ValueError("Especialidad y días son obligatorios")
        for dia in dias:
            if dia.lower() not in self.DIAS_VALIDOS:
                raise ValueError("Día inválido: {}".format(dia))
        self.__tipo__ = tipo
        self.__dias__ = [d.lower() for d in dias]

    def obtener_especialidad(self):
        return self.__tipo__

    def verificar_dia(self, dia):
        return dia.lower() in self.__dias__

    def __str__(self):
        dias = ", ".join(self.__dias__)
        return "{} (Días: {})".format(self.__tipo__, dias)