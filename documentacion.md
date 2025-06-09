# Documentación del Sistema de Gestión de Clínica

## Cómo ejecutar el sistema

Para ejecutar el sistema de gestión de clínica:

```bash
python main.py
```

## Cómo ejecutar las pruebas

Para ejecutar todas las pruebas unitarias:

```bash
python -m unittest discover test
```

Para ejecutar pruebas específicas:

```bash
python -m unittest test.test_paciente
python -m unittest test.test_medico
python -m unittest test.test_clinica
```

## Explicación del diseño general

### Arquitectura
El sistema utiliza una arquitectura en capas:
- **Modelo**: Contiene las clases de dominio y la lógica de negocio
- **CLI**: Interfaz de usuario por consola
- **Tests**: Pruebas unitarias para validar el funcionamiento

### Clases principales
- `Paciente`: Representa a los pacientes de la clínica
- `Medico`: Representa a los médicos con sus especialidades
- `Especialidad`: Define especialidades médicas y días de atención
- `Turno`: Representa citas médicas
- `Receta`: Prescripciones médicas
- `HistoriaClinica`: Historial de cada paciente
- `Clinica`: Clase principal que coordina todo el sistema

### Validaciones
Todas las validaciones de negocio se realizan en el modelo, no en la interfaz CLI. Esto asegura la integridad de los datos independientemente de cómo se acceda al sistema.

### Excepciones
El sistema utiliza excepciones personalizadas para manejar errores específicos del dominio médico, proporcionando mensajes claros y apropiados.
