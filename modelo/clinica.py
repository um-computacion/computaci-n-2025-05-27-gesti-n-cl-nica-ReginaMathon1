# -*- coding: utf-8 -*-
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes__ = {}
        self.__medicos__ = {}
        self.__turnos__ = []
        self.__historias_clinicas__ = {}

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise Exception("Paciente duplicado")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise Exception("Médico duplicado")
        self.__medicos__[matricula] = medico

    def agregar_especialidad_a_medico(self, matricula, especialidad):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no registrado")
        self.__medicos__[matricula].agregar_especialidad(especialidad)

    def obtener_pacientes(self):
        return list(self.__pacientes__.values())

    def obtener_medicos(self):
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula):
        return self.__medicos__.get(matricula)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def obtener_historia_clinica(self, dni):
        if dni not in self.__historias_clinicas__:
            raise PacienteNoEncontradoException("Paciente no encontrado")
        return self.__historias_clinicas__[dni]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado")
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado")
        medico = self.__medicos__[matricula]
        paciente = self.__pacientes__[dni]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        # Validar especialidad y día
        esp_ok = False
        for esp in medico.obtener_especialidades():
            if esp.obtener_especialidad().lower() == especialidad.lower() and esp.verificar_dia(dia_semana):
                esp_ok = True
        if not esp_ok:
            # ¿El médico tiene la especialidad?
            tiene_esp = any(esp.obtener_especialidad().lower() == especialidad.lower() for esp in medico.obtener_especialidades())
            if not tiene_esp:
                raise MedicoNoDisponibleException("El médico no tiene esa especialidad")
            else:
                raise MedicoNoDisponibleException("El médico no atiende esa especialidad ese día")
        # Validar turno duplicado
        for t in self.__turnos__:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Turno duplicado")
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado")
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado")
        if not medicamentos or not isinstance(medicamentos, list):
            raise RecetaInvalidaException("Debe indicar al menos un medicamento")
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)

    @staticmethod
    def obtener_dia_semana_en_espanol(fecha_hora):
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def validar_existencia_paciente(self, dni):
        """Verifica si un paciente está registrado"""
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado")

    def validar_existencia_medico(self, matricula):
        """Verifica si un médico está registrado"""
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado")

    def validar_turno_no_duplicado(self, matricula, fecha_hora):
        """Verifica que no haya un turno duplicado"""
        for t in self.__turnos__:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException("Turno duplicado")

    def obtener_especialidad_disponible(self, medico, dia_semana):
        """Obtiene la especialidad disponible para un médico en un día"""
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico, especialidad_solicitada, dia_semana):
        """Verifica que el médico atienda esa especialidad ese día"""
        especialidad_disponible = self.obtener_especialidad_disponible(medico, dia_semana)
        if not especialidad_disponible or especialidad_disponible.lower() != especialidad_solicitada.lower():
            if any(esp.obtener_especialidad().lower() == especialidad_solicitada.lower() for esp in medico.obtener_especialidades()):
                raise MedicoNoDisponibleException("El médico no atiende esa especialidad ese día")
            else:
                raise MedicoNoDisponibleException("El médico no tiene esa especialidad")