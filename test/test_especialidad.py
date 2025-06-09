# -*- coding: utf-8 -*-
import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_especialidad(self):
        e = Especialidad("Pediatría", ["lunes", "viernes"])
        self.assertEqual(e.obtener_especialidad(), "Pediatría")
        self.assertTrue(e.verificar_dia("LUNES"))
        self.assertFalse(e.verificar_dia("martes"))
        self.assertIn("Pediatría", str(e))

    def test_dia_invalido(self):
        with self.assertRaises(ValueError):
            Especialidad("Cardiología", ["lunessss", "martes"])