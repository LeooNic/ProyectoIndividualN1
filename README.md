# ProyectoIndividualN1

En este proyecto se nos presentan 6 datasets con distintos formatos con el objetivo de realizar un ETL y poder hacer una carga incremental en una base de datos.

## Objetivo:
Procesar los diferentes datasets.
Crear un archivo DB con el motor de SQL que quieran. Pueden usar SQLAlchemy por ejemplo.
Realizar en draw.io un diagrama de flujo de trabajo del ETL y explicarlo en vivo.
Realizar una carga incremental de los archivos que se tienen durante el video.
Realizar una query en el video, para comprobar el funcionamiento de todo su trabajo. La query a armar es la siguiente: Precio promedio de la sucursal 9-1-688.

Resultado de la query : 203.8

![query](https://user-images.githubusercontent.com/107507556/198361363-a968305e-a528-4074-a407-67fcef7e7dc9.png)

# Diagrama de flujo explicativo:
![image](https://user-images.githubusercontent.com/107507556/198355461-a7c9a62a-733e-4a1f-96c8-d8fefc5b8e3c.png)

-El diagrama nos muestra basicamente el proceso que se realiza en el script ,  automatizando la carga de datos y la creación de un backup con un formato uniforme.


# Proceso realizado:

Utilizamos jupyter notebook para realizar un análisis y previsualizacion de los datasets , para luego decidir que normalización realizar.

Utilizamos python para automatizar el proceso de ETL 
Librerias utilizadas =
-Pandas

-Pymysql

-Sqlalchemy

-En primera instancia creamos nuestra base de datos para realizar la carga inicial.
-O en su defecto elegimos la base de datos a utilizar si es una carga incremental.

-Leemos los datasets e identificamos su formato.

-Los transformamos en csv's y los guardamos en una carpeta como backup (Originales sin transformaciones).

-Realizamos las normalizaciones necesarias.

-Elegimos el nombre de la tabla a exportar. Si utilizamos una tabla existente los datos se van a concatenar a la tabla de nuestra base de datos manteniendo los archivos intactos , permitiendo nuestra carga incremental.

# Tecnología usada para base de datos:

-MySqlWorkbench ( Base de datos para realizar querys)

# Video explicativo de procesos realizados en el ETL 

-En este video hago un breve resumen de los procesos realizados y una muestra de la carga incremental que hace el script además de el resultado de la query propuesta en el proyecto.

https://www.youtube.com/watch?v=MPVlmQYnqXg&ab_channel=LeonelNicotra




