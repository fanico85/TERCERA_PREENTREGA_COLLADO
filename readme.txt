=======================================================TERCERA PREENTREGA=====================================================

Requirements:
#Python 3.11.9
#django 5.0.6
La aplicacion es solo compatible con el explorador IE=edge, debido el temaplate conseguido. Se podrá acceder mediante la ruta: http://127.0.0.1:8000/Principal/
El servidor deberá levantarse con "python manage.py runserver" desde la ubicacion "Tercera_preentrega_Collado\Nails_factory"

Introduccion:
La aplicacion tiene por objetivo facilitar la administracion de un negocio dedicado a brindar servicios de Belleza y Manicuria de uñas.

Para esta preentrega, contaremos con:
    - Inicio -> informacion principal real (tabla de Servicios y Cards de indicadores) mas informacion simulada en dos graficos
    - servicios
        * Agregar -> permite registrar un nuevo servicio (por el momento no hay control de duplicados). Se debe ingresar la duracion del servicios en minutos (entre 10 y 120)
        * Buscar -> permite buscar aquellos servicios que contienen la palabra ingresada
        * Mostrar todos -> tabla con todos los servicios registrados
    - Gastos
        * Agregar -> permite registrar un nuevo gasto realizado por el negocio (por el momento no hay control de duplicado y limite de fechas)
        * Mostrar todos -> tabla con todos los gastos realizados
    - Insumos
        * Agregar -> permite registrar un nuevo insumo y su stock (por el momento no hay control de duplicados). El stock ingresado es el real, y ademas se incluye el 
          sotck minimo (para las alertas de reposicion)
        * Mostrar todos -> tabla con todos los insumos registrados y su stock real


Aclaraciones:
    - Las Cards del inicio son:
        * Servicios disponibles -> es un contador de los servicios disponibles para los clientes; se puede navegar hasta una tabla con todos los servicios registrados
        * Gastos realizados -> es una sumatoria de todos los gastos realizados por el negocio (a futuro, solo incluiran los gastos del mes en curso). Actualmente la card
          esta en color azul, si supera los $700.000 se pondra en amarilla y si supera los $720.000 se pintará de rojo
        * Servicios realizados -> a futuro mostrara un contador de la cantidad de servicios realizados por los clientes durante el mes en curso
        * Insumos con Stock minimo -> es un contador de insumos que tienen un sotck por debajo de lo recomendado; se puede navegar hasta una tabla con todos los insumos 
          registrados; a futuro, la tabla tendra solo los insumos con stock minimo. Se pinta de azul cuando todos los insumos tienen un stock recomendado. se pinta de rojo
          cuando al menos 1 insumo tiene menos del stock minimo.
          