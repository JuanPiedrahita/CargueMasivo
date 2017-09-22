import openpyxl
from cuenta import Cuenta

class CuentaContable():
	def __init__(self, cursor, fileAddress):
		self.cursor = cursor
		self.fileAddress = fileAddress

	def cargarCuentas(self, ruta):
		doc = openpyxl.load_workbook(self.fileAddress)
		hojaData = doc.get_sheet_by_name('HojaCuentas')
		hojaErrores = doc.create_sheet('HojaErrores')
		hojaCompletos = doc.create_sheet('HojaCompletos')
		rowCounter = 1
		for fila in hojaData.rows:
			idCuenta = self.cleanIdCuenta(hojaData.cell(row=rowCounter,column=1).value)
			rowCounter = rowCounter + 1
			responseCuenta = self.getCuentaById(idCuenta)	
			if not responseCuenta:
				cuenta = Cuenta(idCuenta, hojaData.cell(row=rowCounter,column=2).value)
				cuenta.padre = cuenta.definePadre(cuenta.codigo)
				print cuenta.codigo[:1]
				cuenta.naturaleza = cuenta.defineNaturaleza(cuenta.codigo[:1])
				cuenta.nivel = cuenta.defineNivel(cuenta.codigo)
				print cuenta.saldo, cuenta.codigo, cuenta.naturaleza, cuenta.nivel, cuenta.nombre
				print cuenta.codigo
				print cuenta.padre
				hojaCompletos.append([idCuenta , " La cuenta no existe"])
			else:
				hojaErrores.append([idCuenta , " La cuenta ya existe"])
		doc.save("archivosExcel/resultadoCargue.xlsx")

	def cleanIdCuenta(self,idCuentaErroneo):
		head = idCuentaErroneo[:1]
		tail = idCuentaErroneo[1:]
		return head+"-"+tail

	def getCuentaById(self, idCuenta):
		try:
			self.cursor.execute("""
                		select *
                		from financiera.cuenta_contable
                		where codigo = trim('"""+idCuenta+"""');""")

        	except Exception as e:
 			print e
          
        	rows = self.cursor.fetchone()
		return rows

