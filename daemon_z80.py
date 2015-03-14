import bluetooth
import time

bd_addr = "20:13:06:03:04:87"
port = 1
connected = False

def isAlive():
	print("Conectando...")
	result = bluetooth.lookup_name(bd_addr, timeout=5)
	if (result != None):
		print("Conectado")
		return True
	else:
		return False

def connector():
	try:#Intentamos ejecutar todo
		sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
		sock.connect((bd_addr, port))
		sock.settimeout(1.0)
		while connected == False:
			sock.send("t")
			#time.sleep(0.250)
			bufferReader = sock.recv(4096)  #Tamanyo de lectura del buffer
			print bufferReader 
			if bufferReader == "T":
				connected == True
				break
				bufferReader = sock.recv(4096)
				#print "Device connected"
	except:#Si hay algun fallo gordo de python(del sistema):
		print "Excepcion"#Decimos que ha saltado una excepcion
		sock.close()#Cerramos el socket para que no falle con un 'device busy'
		time.sleep(5)#Esperamos 5 segundos
		connector()#Volvemos a ejecutar el metodo de nuevo
		'''Con lo de arriba el programa no se parara nunca ya que saltara a la excepcion en caso de error'''

while True:
	if isAlive() == True:
		connector()
	elif isAlive() == False:
		time.sleep(5)
