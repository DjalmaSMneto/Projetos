import mysql.connector
from mysql.connector import errorcode
from openpyxl import load_workbook

config = {
  'host':'localhost',
  'user':'root',
  'password':'senha',
  'database':'BD'
}

try:
	conn = mysql.connector.connect(**config)
	print("Conecção estabelecida!!")
	cursor = conn.cursor()
	diretorio = input("Informe o diretorio: ")
	arquivo = load_workbook(diretorio)
	matriz = arquivo.active

	tabela1 = []
	tabela2 = []
	inserir = []
	ID = 0
	D_exist = False
	R_exist = False

	for linha in matriz:
		for coluna in linha:
			tabela1.append(coluna.value)
		tabela2.append(tabela1)
		tabela1 = [""]

	L = len(tabela2)
	C = len(tabela2[0])+1


	for l in range(1,L):
		for c in range(1,C):
			inserir.append(str(tabela2[l][c]))

		cursor.execute("SELECT dh.datahora from datahora dh")
		DATA = cursor.fetchall()

		cursor.execute("SELECT o.relatorio from ocorrencia o")
		RELAT = cursor.fetchall()

		conn.commit()

		for x in DATA:
			for y in x:
				if(y == inserir[0]):
					D_exist = True
					
		for x in RELAT:
			for y in x:
				if(y == inserir[4]):
					R_exist = True
					

		if(R_exist == True and D_exist == True):
			R_exist = False
			D_exist = False
		elif (inserir[4] == 'None'):
			R_exist = False
			D_exist = False
		else:
			cursor.execute("INSERT INTO ocorrencia(relatorio,armas)values('{0}','{1}')".format(inserir[4],inserir[5]))
			cursor.execute("SELECT o.id_ocorrencia from ocorrencia o where o.relatorio = '{0}'".format(inserir[4]))
			ID = cursor.fetchall()
			ID = ID[0][0]
			cursor.execute("INSERT INTO endereco(rua,bairro,referencia,id_ocorrencia)values('{0}','{1}','{2}',{3})".format(inserir[2],inserir[1],inserir[3],ID))
			cursor.execute("INSERT INTO datahora(datahora,id_ocorrencia)values('{0}',{1})".format(inserir[0],ID))
			
			conn.commit()
		inserir = []

		
	cursor.close()
	conn.close()

#------------------------------ ERRO ----------------------------------------------
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("usuario ou senha invalidos")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("ESSE BANCO NÂO EXISTE")
  else:
    print(err)
  