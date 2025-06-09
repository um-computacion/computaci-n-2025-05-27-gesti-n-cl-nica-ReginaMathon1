# -*- coding: utf-8 -*-
import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):
    def test_creacion_paciente(self):
        p = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.assertEqual(p.obtener_dni(), "12345678")
        self.assertIn("Juan Perez", str(p))

    def test_paciente_datos_invalidos(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "01/01/1990")
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "", "01/01/1990")
        with self.assertRaises(ValueError):
            Paciente("Juan Perez", "12345678", "")