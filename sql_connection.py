import datetime
import mysql.connector as mysql

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx =  mysql.connect(host="localhost", database="warehousedb", user="root", passwd="Enfield@2021", use_pure=True)
  return __cnx
