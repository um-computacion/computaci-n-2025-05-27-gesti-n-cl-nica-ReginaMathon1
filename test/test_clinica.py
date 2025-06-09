# -*- coding: utf-8 -*-
import unittest
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from datetime import datetime
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan", "1", "01/01/2000")
        self.medico = Medico("Dr. A", "M1")
        self.especialidad = Especialidad("Cardiología", ["lunes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(Exception):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(Exception):
            self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_ok(self):
        fecha = datetime(2025, 6, 9, 10, 0)  # lunes
        self.clinica.agendar_turno("1", "M1", "Cardiología", fecha)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_agendar_turno_paciente_inexistente(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("999", "M1", "Cardiología", fecha)

    def test_agendar_turno_medico_inexistente(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("1", "M999", "Cardiología", fecha)

    def test_agendar_turno_especialidad_invalida(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("1", "M1", "Pediatría", fecha)

    def test_agendar_turno_dia_invalido(self):
        fecha = datetime(2025, 6, 10, 10, 0)  # martes
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("1", "M1", "Cardiología", fecha)

    def test_agendar_turno_duplicado(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        self.clinica.agendar_turno("1", "M1", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("1", "M1", "Cardiología", fecha)

    def test_emitir_receta_ok(self):
        self.clinica.emitir_receta("1", "M1", ["Ibuprofeno"])
        historia = self.clinica.obtener_historia_clinica("1")
        self.assertTrue(any("Ibuprofeno" in str(r) for r in historia.obtener_recetas()))

    def test_emitir_receta_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.emitir_receta("999", "M1", ["Ibuprofeno"])

    def test_emitir_receta_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.emitir_receta("1", "M999", ["Ibuprofeno"])

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("1", "M1", [])

    def test_agregar_especialidad_a_medico_no_registrado(self):
        clinica = Clinica()
        medico = Medico("Dr. B", "M2")
        especialidad = Especialidad("Pediatría", ["martes"])
        with self.assertRaises(MedicoNoDisponibleException):
            clinica.agregar_especialidad_a_medico("M2", especialidad)
