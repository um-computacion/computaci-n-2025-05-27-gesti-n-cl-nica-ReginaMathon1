#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Gestión para una Clínica
Punto de entrada principal del programa
"""

from cli import CLI

def main():
    """Función principal que inicia la interfaz de consola"""
    try:
        cli = CLI()
        cli.ejecutar()
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
    except Exception as e:
        print("Error inesperado: {}".format(e))

if __name__ == "__main__":
    main()
