# Control medico | Archivos y persistencia

## Instrucciones
Se está iniciando un control electronico de la ficha medica de los estudiantes. Los doctores encargados de la clinica 
desean mejorar la atencion de los estudiantes que acuden a consulta medica. Lo más importante es saber cuando fue la 
ultima visita, que condiciones medicas tiene la persona, que medicina toma, que le recomendaron hacer en la clinica y un
sistema de seguimiento para ver si se alivio del problema. En el archivo **clinica.csv** vienen algunas visitas 
realizadas por los estudiantes.
El medico encargado de la clinica periodicamente hace una llamada telefonica o envia un correo electronico a un 
estudiante identificado por su carne, para verificar si se alivio. Por ello marca en el registro del estudiante un
digito: 1=esta mejor, 2=se siente mal, 3-fue a su doctor.

Al pensar cuidadosamente sobre las funcionalidades que necesita hacer el programa notas que debe ser capaz de:
1. Leer el archivo con los datos actualmente guardados.
2. Agregar nuevos registros al archivo.
3. Indicar el resultado del seguimiento realizado a un estudiante en particular.
4. Mostrar todos los elementos dentro del archivo.
5. Imprimir reportes.
6. Desplegar un menu con las opciones mencionadas anteriormente, adicional una opcion para salir.

Ten en cuenta que los datos que tiene que guardar son los siguientes:
- Carne del estudiante.
- Nombre del estudiante (nombre y apellido)
- Fecha de su ultima visita (formato dd/mm/aaaa)
- Telefono
- Correo electronico
- Enfermedad o condicion por la que hace su visita
- Medicina que toma actualmente (o NINGUNA)
- Temperatura en grados centigrados
- Presion arterial (formato sistolica/diastolica, ejemplo 120/80)
- Recomendacion dada
- Seguimiento (0=no se ha dado seguimiento, 1=esta mejor, 2=se siente mal,3=fue a su doctor)

Además, se desean conocer algunos reportes basicos como:
- Los estudiantes que tenian fiebre (mayor a 37 grados centigrados)
- Los estudiantes que al darles seguimiento indican que aun se sienten mal (seguimiento=2)

Debe notar que al salir del programa el archivo debe estar actualizado con todas las modificaciones realizadas durente
la ejecución y recuerde separar las operaciones del programa en funciones y/o modulos.
