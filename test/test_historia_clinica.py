# -*- coding: utf-8 -*-
import unittest
from modelo.historia_clinica import HistoriaClinica
from modelo.paciente import Paciente
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.medico import Medico
from datetime import datetime

class TestHistoriaClinica(unittest.TestCase):
    def test_historia_clinica(self):
        p = Paciente("Juan", "1", "01/01/2000")
        hc = HistoriaClinica(p)
        m = Medico("Dr. A", "M1")
        t = Turno(p, m, datetime(2025, 6, 10, 10, 0), "Cardiología")
        r = Receta(p, m, ["Paracetamol"])
        hc.agregar_turno(t)
        hc.agregar_receta(r)
        self.assertIn(t, hc.obtener_turnos())
        self.assertIn(r, hc.obtener_recetas())
        self.assertIn("Cardiología", str(hc))