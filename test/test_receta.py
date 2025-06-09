# -*- coding: utf-8 -*-
import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico

class TestReceta(unittest.TestCase):
    def test_creacion_receta(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        r = Receta(p, m, ["Paracetamol"])
        self.assertIn("Paracetamol", str(r))

    def test_receta_sin_medicamentos(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        with self.assertRaises(ValueError):
            Receta(p, m, [])

    def test_receta_datos_invalidos(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        
        with self.assertRaises(ValueError):
            Receta(None, m, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(p, None, ["Paracetamol"])
        with self.assertRaises(ValueError):
            Receta(p, m, None)