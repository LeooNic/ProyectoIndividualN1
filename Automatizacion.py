#En este script realizamos la automatización de todo el proceso de ETL


#Importamos las librerias necesarias

import pandas as pd
import pymysql
from sqlalchemy import create_engine

#Definimos un main de nuestras funciones

def main():
    nombre_base = crear_base_de_datos()
    df = leer_archivos()
    crear_csv(df)
    visualizar_datos(df)
    eliminar_datetime(df)
    normalizar_id_producto(df)
    importar_tablas(df , nombre_base)


#Leemos los archivos para identificar su formato
def leer_archivos():
    print("Leyendo archivo...")
    fullpath = input("Ingresar ubicación del archivo: ")
    try:
        df = pd.read_excel(fullpath , sheet_name= None)
        df = pd.concat(df , ignore_index = True)
    except:
        try:
            df = pd.read_parquet(fullpath)
        except:
            try:
                df = pd.read_json(fullpath)
            except:
                try:
                    df = pd.read_csv(fullpath , sep= input('Ingrese separador= ') , encoding = input('Ingrese formato = ') , low_memory = False)
                except:
                    print('Formato incorrecto')
                    leer_archivos()
    print(df)       
    return df

#Los convertimos en csv
def crear_csv(df):
    print("Transformando archivo...")
    path = "C:/Users/user/Desktop/Proyecto Individual n1/Destino"
    nombre = input('Ingrese nombre del archivo a guardar: ')
    fullpath = path + '/' + nombre + ".csv"
    df.to_csv(fullpath, sep = "," , index = False)
        

#Aplicamos las transformaciones que previamente analizamos
def eliminar_datetime(df):
    print("Borrando datetime")
    try:
        df['sucursal_id'] = df['sucursal_id'].astype(str)
        df['sucursal_id'] = df['sucursal_id'].apply(lambda x: x.split(' ')[0])
    except:
        None

    return df


def normalizar_id_producto(id):
    print('Normalizando tabla de ventas')
    try:
        if (type(id))!=str:
            return id
        cantidad_caracter = len(id)
        if (len(id)<13):
            id = '0'*(13-cantidad_caracter)+id
        if('.' in id):
            id= id[0 :id.find('.')]
    except:
        return id
#Hacemos una simple preview de nuestro dataframe antes de exportarlo a la base de datos
def visualizar_datos(df):
    print("Visualizando primeros 5 registros")
    print(df.head())

#Creamos la conexion a nuestra base de datos
def conexion_database(nombre_base):
    cadena_conexion= f"mysql+pymysql://root:@127.0.0.1:3306/{nombre_base}"
    conexion= create_engine(cadena_conexion)
    return conexion

#Creamos nuestra base o elegimos la base de datos a usar
def crear_base_de_datos():
    print('Ingrese nombre de base de datos: ')
    conexion = pymysql.connect(host="localhost",
                            user = "root",
                            password=''
                            )
    cursor = conexion.cursor()
    nombre_base = input()
    query =f"CREATE DATABASE IF NOT EXISTS {nombre_base};"
    cursor.execute(query)
    conexion_database(nombre_base)
    return nombre_base

#Importamos las tablas a nuestra base de datos , usamos parametro append para mantener nuestros datos originales y agregar los nuevos
def importar_tablas(df , nombre_base):
    conexion = conexion_database(nombre_base)
    nombre = input('Ingrese nombre de la tabla: ')
    df.to_sql(name=nombre , con=conexion , index= False , if_exists='append')



if __name__ == '__main__':
    main()
    input("\tPROCESO TERMINADO . Presionar enter para salir")