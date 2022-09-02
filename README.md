# Prueba

## Parte 1 - Docker

- Cree una carpeta en la ruta de su preferencia e ingrese a ella.
- Cree un Dockerfile que especifique lo siguiente:
- Establezca la imagen base como: netsandbox/request-tracker
- Establezca el nombre del creador como por ejemplo: Jorge Gonzalez "jorge.gonzalez@utec.edu.uy"
- Descargue la lista de paquetes actualizada del sistema (apt-get update -y).
- Construya la imagen con el nombre: new-request-tracker
- Liste las imagenes disponibles en su registro local.
- Ejecutar un contenedor, en segundo plano, de la imágen: new-request-tracker
- Establecerle el nombre: test-nombre-apellido (ejemplo: test-jorge-gonzalez)
- Establezca el puerto de respesta externa a 80 e interno a 80 que es el que escucha el request-tracker.
- Pruebe el funcionamiento del producto (en su navegador web escriba la dirección IP del equipo que tiene el entorno Docker funcionando, debería llegar al login).
- Finalice el contenedor creado.
- Realice un listado de todos los contenedores.
- Elimine el contenedor creado previamente.
- Ejecutar un contenedor, en segundo plano, de la imágen: new-request-tracker
- Establecerle el nombre: produccion-nombre-apellido (ejemplo: produccion-jorge-gonzalez)
- El puerto deberá ser 81xx y los valores xx de corresponden con el resultado de la suma
de los 3 últimos numeros de su cedula, por ejemplo si su cedula es 1.222.333-4 debera realizar la suma de los valores
3 + 3 + 4 lo que le da como resultado 10, lo que resultará que su puerto a utlizar deberá ser el 8110, recordar que el interno es el puerto 80, que es el que escucha el -
request-tracker.
- Pruebe nuevamente el funcionamiento del producto, ahora utilizando el nuevo puerto especificado.
- Realice un listado de todos los contenedores.
- El contenedor produccion-nombre-apellido debe quedar corriendo.

## Parte 2 - Selenium
PARTE 2

Luego de desplegado el contenedor debera realizar una de las 2 opciones siguientes (solo 1)


Deberá elegir solo una de las opciones a realizar:

Parte 2 - Opcion 1:

Rrealizar un código en Python que realice:

A) un login en la web de RT (completando los campos de usuario y password) y realizando click en login. (por defecto usuario: root clave: password)
B) seleccionar la opción de crear un nuevo ticket (o caso).
C) ingresar al menos un valor en un campo del ticket
D) seleccionar la opción crear ticket.


Subir el código a un proyecto github de su preferencia.

Deberá especificar en el espacio para respuesta el link al mismo.