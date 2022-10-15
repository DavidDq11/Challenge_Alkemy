#pip install requests
import requests
import datetime
import csv
import os
from pathlib import Path
import pandas as pd
import logging


#Configuracion Logging
logging.basicConfig(filename='chall.log', level=logging.DEBUG)

#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
logging.debug(fecha2)
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)
fecha_carpeta1 = año + '-'+ mes
fecha_archivo1 = 'museos-'+ dia+ '-'+ mes + '-' + año
logging.debug(fecha_archivo1)

#creación de carpeta
dir1 = os.path.join('Museos', fecha_carpeta1)
try:
  os.makedirs(dir1)
except:
  with open(f"{dir1}/{fecha_archivo1}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
#os.makedirs(os.path.join('Museos4', fecha_carpeta))
logging.debug(dir1)
#creacion archivo .csv
with open(f"{dir1}/{fecha_archivo1}.csv", "wb") as f_out:
    f_out.write(respuesta.content)

csv_path1 = f"{dir1}/{fecha_archivo1}.csv"
Museosdata = pd.read_csv(csv_path1)
#f"{dir1}/{fecha_archivo1}/Museos.csv"
#logging.debug(Xdata)
Museosdata.rename(columns={'categoria':'Categoria','provincia':'Provincia','localidad':'Localidad','nombre':'Nombre','direccion':'Domicilio','telefono':'Telefono'}, inplace=True)
col_drop=['Observaciones', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Info_adicional', 'fuente', 'jurisdiccion', 'año_inauguracion', 'actualizacion']
Museosdata.drop(columns = col_drop, inplace = True)
Museosdata.to_csv('Museos.csv')
Museosdata.head()


Museosdata.info()

#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
logging.debug(fecha2)
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)
fecha_carpeta2 = año + '-'+ mes
fecha_archivo2 = 'Cines-'+ dia+ '-'+ mes + '-' + año
logging.debug(fecha_archivo2)

#creación de carpeta
dir2 = os.path.join('Cines', fecha_carpeta2)
try:
  os.makedirs(dir2)
except:
  with open(f"{dir2}/{fecha_archivo2}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
logging.debug(dir2)

#creacion archivo .csv
with open(f"{dir2}/{fecha_archivo2}.csv", "wb") as f_out:
    f_out.write(respuesta.content)


csv_path2 = f"{dir2}/{fecha_archivo2}.csv"
Cinesdata = pd.read_csv(csv_path2)

#logging.debug(Xdata)
Cinesdata.rename(columns={'Dirección':'Domicilio','Categoría':'Categoria'}, inplace=True)
col_drop=['Observaciones', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Información adicional', 'Fuente', 'tipo_gestion', 'año_actualizacion']
Cinesdata.drop(columns = col_drop, inplace = True)
Cinesdata.to_csv('Cines.csv')
Cinesdata.head()


#Descargar contenido
URL = "https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk"+"/export?format=csv"
respuesta = requests.get(URL)

#Obtener fecha
fecha=respuesta.headers['Date']
fecha2= fecha[5:16]
logging.debug(fecha2)
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)
fecha_carpeta3 = año + '-'+ mes
fecha_archivo3 = 'Bibliotecas-'+ dia+ '-'+ mes + '-' + año
logging.debug(fecha_archivo3)

#creación de carpeta
dir3 = os.path.join('Bibliotecas', fecha_carpeta3)
try:
  os.makedirs(dir3)
except:
  with open(f"{dir3}/{fecha_archivo3}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
logging.debug(dir3)

#creacion archivo .csv
with open(f"{dir3}/{fecha_archivo3}.csv", "wb") as f_out:
    f_out.write(respuesta.content)
    
    
    csv_path3 = f"{dir3}/{fecha_archivo3}.csv"
Bibliosdata = pd.read_csv(csv_path3)

Bibliosdata.rename(columns={'Cod_tel':'cod_area','Categoría':'Categoria','Teléfono':'Telefono'}, inplace=True)
col_drop=['Observacion', 'Subcategoria', 'Latitud', 'Longitud', 'TipoLatitudLongitud', 'Información adicional', 'Fuente', 'Tipo_gestion', 'Año_actualizacion', 'año_inicio']
Bibliosdata.drop(columns = col_drop, inplace = True)
Bibliosdata.to_csv('Bibliotecas.csv')
Bibliosdata.head()



import datetime

fecha=respuesta.headers['Date']
#logging.debug(fecha[5:16])
fecha2= fecha[5:16]
logging.debug(fecha2)
fechaActual=datetime.datetime.strptime(fecha2, '%d %b %Y')
logging.debug(fechaActual.year)
año = str(fechaActual.year)
mes = str(fechaActual.month)
dia = str(fechaActual.day)
fecha_carpeta = año + '-'+ mes
logging.debug(fecha_carpeta)
fecha_archivo = 'museos-'+ dia+ '-'+ mes + '-' + año
logging.debug(fecha_archivo)
#os.makedirs(os.path.join('Museos3', fecha_carpeta))



DirMuseos = f"{dir1}/{fecha_archivo1}/Museos.csv"
logging.debug (DirMuseos)



import pandas as pd
#pip install SQLAlchemy

from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:oncecaldas@localhost:5432/Challenge_Analytica')

df = pd.concat([Museosdata, Cinesdata, Bibliosdata])
df.to_sql("datos", con=engine, if_exists = "replace")

result  = pd.read_sql_query("SELECT * FROM datos", engine)
result.Categoria


#df = pd.concat([Museosdata, Cinesdata, Bibliosdata])
#df.to_sql("Datos", con=engine, if_exists = "replace")


cant_reg_mus = result.query('Categoria == "Espacios de Exhibición Patrimonial"')
cant_reg_mus = cant_reg_mus.axes[0]
cant_mus_fuente = Museosdata.axes[0]

logging.debug ("El conteo de registros por la categoría de bibliotecas es:", len(cant_reg_mus))
logging.debug ("El conteo de registros por la fuente de museos es:", cant_mus_fuente.stop)



cant_reg_biblio = result.query('Categoria == "Bibliotecas Populares"')
cant_reg_biblio = cant_reg_biblio.axes[0]
cant_biblio_fuente = Bibliosdata.axes[0]

logging.debug ("El conteo de registros por la categoría de bibliotecas es:", len(cant_reg_biblio))
logging.debug ("El conteo de registros por la fuente de bibliotecas es:", cant_biblio_fuente.stop)



cant_reg_cines = result.query('Categoria == "Salas de cine"')
cant_reg_cines = cant_reg_cines.axes[0]
cant_cines_fuente = Cinesdata.axes[0]

logging.debug ("El conteo de registros por la categoría de bibliotecas es:", len(cant_reg_cines))
logging.debug ("El conteo de registros por la fuente de cines es:", cant_cines_fuente.stop)


result.iloc[4]