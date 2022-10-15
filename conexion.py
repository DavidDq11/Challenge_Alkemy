import psycopg2
try:
  connection = psycopg2.connect(
      host = 'localhost',
      user = 'postgres',
      password = 'oncecaldas',
      database = 'Challenge_Analytica'
      port = '5432'
  )
  print("conexión Exitosa")
  cursor = connection.cursor()
  cursor.execute("SELECT version()")
  row = cursor.fetchone()
  print(row)
except Exception as ex:
  print(ex)