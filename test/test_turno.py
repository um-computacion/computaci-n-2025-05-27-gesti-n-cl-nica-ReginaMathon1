# -*- coding: utf-8 -*-
import unittest
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico
from datetime import datetime

class TestTurno(unittest.TestCase):
    def test_creacion_turno(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        fecha = datetime(2025, 6, 10, 10, 0)
        t = Turno(p, m, fecha, "Cardiología")
        self.assertEqual(t.obtener_medico(), m)
        self.assertEqual(t.obtener_fecha_hora(), fecha)
        self.assertIn("Cardiología", str(t))

    def test_turno_datos_invalidos(self):
        p = Paciente("Juan", "1", "01/01/2000")
        m = Medico("Dr. A", "M1")
        fecha = datetime(2025, 6, 10, 10, 0)
        
        with self.assertRaises(ValueError):
            Turno(None, m, fecha, "Cardiología")
        with self.assertRaises(ValueError):
            Turno(p, None, fecha, "Cardiología")
        with self.assertRaises(ValueError):
            Turno(p, m, None, "Cardiología")
        with self.assertRaises(ValueError):
            Turno(p, m, fecha, None)