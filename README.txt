=========================================================
PROYECTO: SistemaRural-PE (Prueba de Viabilidad)
CURSO: Lenguajes de Programación (UAIN1288P)
=========================================================

1. DESCRIPCIÓN DEL PROTOTIPO
Este código es una prueba de viabilidad que demuestra la integración de los tres paradigmas solicitados:
- Orientado a Eventos: Interfaz gráfica con Tkinter (main.py).
- Orientado a Objetos: Clases con encapsulamiento, Singleton y Factory (modelos.py).
- Funcional: Uso de funciones de orden superior como 'reduce' (operaciones.py).

2. REQUISITOS PREVIOS
- Tener instalado Python 3.x en el sistema.
- No requiere librerías externas adicionales (Tkinter viene preinstalado con Python).

3. INSTRUCCIONES DE EJECUCIÓN
Opción A (Desde el explorador de archivos):
1. Asegúrese de que los archivos main.py, modelos.py y operaciones.py estén en la misma carpeta.
2. Haga doble clic sobre el archivo "main.py".

Opción B (Desde la terminal o consola):
1. Abra la terminal y navegue hasta la carpeta del proyecto.
2. Ejecute el siguiente comando:
   python main.py

4. CÓMO PROBAR EL SISTEMA
- Ingrese el Nombre, Apellido y Diagnóstico.
- Haga clic en "Registrar Paciente". 
- Si hay un error (ej. DNI con letras), el bloque try/except mostrará una alerta sin cerrar el programa.
- Si es exitoso, la función funcional 'reduce' calculará y mostrará el total de pacientes registrados en memoria.