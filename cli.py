# -*- coding: utf-8 -*-
from datetime import datetime
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def mostrar_menu(self):
        print("\n--- Menú Clínica ---")
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = input("\nSeleccione una opción: ").strip()
                
                if opcion == "0":
                    print("¡Hasta luego!")
                    break
                elif opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_todos_turnos()
                elif opcion == "8":
                    self.ver_todos_pacientes()
                elif opcion == "9":
                    self.ver_todos_medicos()
                else:
                    print("Opción inválida. Intente nuevamente.")
            except Exception as e:
                print(f"Error: {e}")

    def agregar_paciente(self):
        try:
            nombre = input("Nombre del paciente: ").strip()
            dni = input("DNI: ").strip()
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar paciente: {e}")

    def agregar_medico(self):
        try:
            nombre = input("Nombre del médico: ").strip()
            matricula = input("Matrícula: ").strip()
            
            medico = Medico(nombre, matricula)
            self.clinica.agregar_medico(medico)
            print("Médico agregado exitosamente.")
        except Exception as e:
            print(f"Error al agregar médico: {e}")

    def agendar_turno(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad: ").strip()
            fecha_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ").strip()
            
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado exitosamente.")
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, TurnoOcupadoException) as e:
            print(f"Error al agendar turno: {e}")
        except ValueError:
            print("Error: Formato de fecha inválido. Use dd/mm/aaaa HH:MM")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_especialidad(self):
        try:
            matricula = input("Matrícula del médico: ").strip()
            tipo = input("Tipo de especialidad: ").strip()
            dias_str = input("Días de atención (separados por coma): ").strip()
            dias = [dia.strip() for dia in dias_str.split(",")]
            
            especialidad = Especialidad(tipo, dias)
            self.clinica.agregar_especialidad_a_medico(matricula, especialidad)
            print("Especialidad agregada exitosamente.")
        except (MedicoNoDisponibleException, ValueError) as e:
            print(f"Error al agregar especialidad: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def emitir_receta(self):
        try:
            dni = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()
            meds_str = input("Medicamentos (separados por coma): ").strip()
            medicamentos = [med.strip() for med in meds_str.split(",")]
            
            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("Receta emitida exitosamente.")
        except (PacienteNoEncontradoException, MedicoNoDisponibleException, RecetaInvalidaException) as e:
            print(f"Error al emitir receta: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_historia_clinica(self):
        try:
            dni = input("DNI del paciente: ").strip()
            historia = self.clinica.obtener_historia_clinica(dni)
            print(f"\n{historia}")
        except PacienteNoEncontradoException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_todos_turnos(self):
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos registrados.")
        else:
            print("\n--- Todos los Turnos ---")
            for turno in turnos:
                print(turno)

    def ver_todos_pacientes(self):
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            print("\n--- Todos los Pacientes ---")
            for paciente in pacientes:
                print(paciente)

    def ver_todos_medicos(self):
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados.")
        else:
            print("\n--- Todos los Médicos ---")
            for medico in medicos:
                print(medico)
