from optparse import OptionParser
from bdConnection import Connection
from cuentaContable import CuentaContable

def main():
    parser = OptionParser()

    parser.add_option("-N", "--db_name", dest="db_name", help="database name", default="financiera")
    parser.add_option("-U", "--db_user",dest="db_user",help="database user", default="postgres")
    parser.add_option("-P", "--db_password", dest="db_password", help="database password", default="postgres")
    parser.add_option("-H", "--host_serverBD", dest="host_serverBD", help="server host", default="localhost")
    parser.add_option("-K", "--port_serverBD", dest="port_serverBD", help="server port", default="5432")
    parser.add_option("-p", "--path_xlsx", dest="path_xlsx", help="path of file for uploading", default="archivosExcel/cuentas.xlsx")
    parser.add_option("-d", "--debug", dest="debug", help="Mostrar mensajes de debug utilize 10", default=10)

    (options, args) = parser.parse_args()

    if not options.db_name:
        parser.error('Parametro db_name no especificado')
    if not options.db_user:
        parser.error('Parametro db_user no especificado') 
    if not options.db_password:
        parser.error('Parametro db_password no especificado')
    if not options.host_serverBD:
        parser.error('Parametro host_serverBD no especificado')
    if not options.port_serverBD:
        parser.error('Parametro host_serverBD no especificado')
    if not options.path_xlsx:
        parser.error('Parametro path_csv no especificado')

    connect = Connection(options)
    postgres_connect = connect.get_connection()
    cursor = connect.get_cursor()

    print "Conexion exitosa"
    print "Inicia Cargue"
    
    cuentas = CuentaContable(cursor, options.path_xlsx)
    cuentas.cargarCuentas("archivosExcel/resultadoCargue.xlsx")
    





if __name__ == '__main__':
	main()


