# -*- coding: utf-8 -*-
import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def test_creacion_medico(self):
        m = Medico("Dra. Ana", "M123")
        self.assertEqual(m.obtener_matricula(), "M123")
        self.assertIn("Dra. Ana", str(m))

    def test_agregar_especialidad(self):
        m = Medico("Dra. Ana", "M123")
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        m.agregar_especialidad(esp)
        self.assertIn("Cardiología", str(m))

    def test_especialidad_para_dia(self):
        m = Medico("Dra. Ana", "M123")
        esp = Especialidad("Cardiología", ["lunes"])
        m.agregar_especialidad(esp)
        self.assertEqual(m.obtener_especialidad_para_dia("lunes"), "Cardiología")
        self.assertIsNone(m.obtener_especialidad_para_dia("martes"))

    def test_especialidad_duplicada(self):
        m = Medico("Dra. Ana", "M123")
        esp = Especialidad("Cardiología", ["lunes"])
        m.agregar_especialidad(esp)
        with self.assertRaises(Exception):
            m.agregar_especialidad(Especialidad("Cardiología", ["martes"]))

    def test_medico_datos_invalidos(self):
        with self.assertRaises(ValueError):
            Medico("", "M123")
        with self.assertRaises(ValueError):
            Medico("Dra. Ana", "")
        with self.assertRaises(ValueError):
            Medico(None, "M123")
        with self.assertRaises(ValueError):
            Medico("Dra. Ana", None)