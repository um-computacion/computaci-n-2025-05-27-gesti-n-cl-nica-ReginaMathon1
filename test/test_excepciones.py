# -*- coding: utf-8 -*-
import unittest
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestExcepciones(unittest.TestCase):
    def test_paciente_no_encontrado(self):
        with self.assertRaises(PacienteNoEncontradoException):
            raise PacienteNoEncontradoException("Paciente no encontrado")

    def test_medico_no_disponible(self):
        with self.assertRaises(MedicoNoDisponibleException):
            raise MedicoNoDisponibleException("Médico no disponible")

    def test_turno_ocupado(self):
        with self.assertRaises(TurnoOcupadoException):
            raise TurnoOcupadoException("Turno ocupado")

    def test_receta_invalida(self):
        with self.assertRaises(RecetaInvalidaException):
            raise RecetaInvalidaException("Receta inválida")