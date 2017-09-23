class Cuenta:
	def __init__(self, codigo, nombre):
		self.saldo = 0
		self.padre = ""
		self.nombre = str (nombre) if type(nombre) is long else nombre.encode('ascii', 'ignore').replace("'","")
#		self.nombre = str (nombre) if type(nombre) is long else nombre
		self.naturaleza = " "
		self.descripcion =  self.nombre
		self.codigo = codigo
		self.nivel = 0
		self.cuentaBancaria = 0

	def definePadre(self, codigo):
		padres = codigo.split("-")
		numPadres = len(padres)-1
		if numPadres == 0:
			return None
		else:
			father = ""
			for i in range(numPadres):
				father += "-" +padres[i]
		return father[1:]
	
	def defineNivel(self, codigo):
		return len(codigo.split("-"))

	def defineNaturaleza(self, x):
		return {
        		'1': 'debito',
        		'2': 'credito',
			'3': 'credito',
			'4': 'credito',
			'5': 'debito',
			'6': 'debito',
			'7': 'debito',
			'8': 'debito',
			'9': 'credito',
    		}.get(x, None)



	
