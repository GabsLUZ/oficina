from os import curdir
from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas 


numero_id = 0

'''CONEXÃO COM BANCO DE DADOS'''
banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "VTFlek_2705",
    database = "oficina"
)
'''FUNÇÃO PRINCIPAL'''
def funcao_principal():
    entrada = formulario.entrada.text()
    placa = formulario.placa.text()
    modelo = formulario.modelo.text()
    observacao = formulario.observacao.text()
    
    print("ENTRADA:",entrada)
    print("PLACA:",placa)
    print("MODELO:",modelo)
    print("OBSERVAÇÕES:",observacao)

    categoria = ""

    if formulario.moto.isChecked():
        print("Véiculo: MOTO")
        categoria = "MOTO"
    elif formulario.carro.isChecked():
        print("Véiculo: CARRO")
        categoria = "CARRO"
    elif formulario.caminhao.isChecked():
        print("Véiculo: CAMINHÃO")
        categoria = "CAMINHÃO"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO CADASTRO (placa,modelo,categoria,observacoes,id) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(placa),str(modelo),categoria,str(observacao),int(entrada))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    formulario.entrada.setText("")
    formulario.placa.setText("")
    formulario.modelo.setText("")
    formulario.observacao.setText("")
''' FINAL DA FUNÇÃO PRINCIPAL'''

'''FUNÇÃO LISTAGEM'''
def funcao_listagem_veiculos():
    veiculos.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM CADASTRO"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()  

    # Criando a tabela no Qt designer
    veiculos.v_lista.setRowCount(len(dados_lidos))  #definir número de linhas
    veiculos.v_lista.setColumnCount(5)  #definir número fixo de colunas

    # Salvando dados dentro da tabela
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            veiculos.v_lista.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

'''FINAL FUNÇÃO LISTAGEM'''

'''FUNÇÃO GERAR PDF'''
def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM CADASTRO"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()  
    y = 0
    pdf = canvas.Canvas("lista_veiculos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Veiculos Cadastrados:")
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(10,750, "ENTRADA")
    pdf.drawString(110,750, "PLACA")
    pdf.drawString(210,750, "MODELO")
    pdf.drawString(310,750, "CATEGORIA")
    pdf.drawString(410,750, "OBSERVAÇÃO")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][4]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][3]))

    pdf.save()
    print("PDF GERADO COM SUCESSO")

'''FIM FUNÇÃO GERAR PDF'''

'''FUNÇÃO EXCLUIR'''
def excluir_dados():
    selecao = veiculos.v_lista.currentRow()
    veiculos.v_lista.removeRow(selecao)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM CADASTRO")
    dados_lidos = cursor.fetchall()
    entrada = dados_lidos[selecao][0]
    cursor.execute("DELETE FROM CADASTRO WHERE id="+str(entrada))
''' FIM FUNÇÃO EXCLUIR'''

'''FUNÇÃO EDITAR'''
def editar_dados():  
    global numero_id
    selecao = veiculos.v_lista.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM CADASTRO")
    dados_lidos = cursor.fetchall()
    entrada = dados_lidos[selecao][0]
    cursor.execute("SELECT * FROM CADASTRO WHERE id="+str(entrada))
    cadastro = cursor.fetchall()
    editar.show()

    numero_id = entrada 

    editar.entrada.setText(str(cadastro[0][4]))
    editar.placa.setText(str(cadastro[0][0]))
    editar.modelo.setText(str(cadastro[0][1]))
    editar.categoria.setText(str(cadastro[0][2]))
    editar.observacao.setText(str(cadastro[0][3]))


''' FIM FUNÇÃO EDITAR'''

'''FUNÇÃO DADOS'''
def salvar_dados():
    global numero_id

    placa = editar.placa.text()
    modelo = editar.modelo.text()
    observacao = editar.observacao.text()
    categoria = editar.categoria.text()
    
    cursor = banco.cursor()
    cursor.execute("UPDATE CADASTRO SET placa='{}',modelo='{}',observacoes='{}',categoria='{}' WHERE id = {}".format(placa,modelo,observacao,categoria,numero_id))

    editar.close()
    veiculos.close()

    funcao_listagem_veiculos()
'''FIM FUNÇÃO DADOS'''

'''FUNÇÃO BUSCAR'''
def buscar_dados():
  #  pesquisar.show()    
    
    entrada = veiculos.placa.text()

    cursor = banco.cursor()
    if veiculos.placas.isChecked():
        cursor.execute("SELECT * FROM CADASTRO WHERE placa='{}'".format(entrada))
    elif veiculos.modelo.isChecked():
        cursor.execute("SELECT * FROM CADASTRO WHERE modelo='{}'".format(entrada))
    elif veiculos.categoria.isChecked():
        cursor.execute("SELECT * FROM CADASTRO WHERE categoria='{}'".format(entrada))
    elif veiculos.entrada.isChecked():
        cursor.execute("SELECT * FROM CADASTRO WHERE id='{}'".format(entrada))
    dados_lidos = cursor.fetchall() 

    veiculos.v_lista.setRowCount(len(dados_lidos))  #definir número de linhas
    veiculos.v_lista.setColumnCount(5)  #definir número fixo de colunas

    # Salvando dados dentro da tabela
    for i in range(0, len(dados_lidos)):
        for j in range(0,5):
            veiculos.v_lista.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))



'''FIM FUNÇÃO BUSCAR'''
    

'''INICIANDO O QT DESIGNER'''
app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
veiculos = uic. loadUi("listar_veiculos.ui")
editar = uic.loadUi("alterar.ui")
pesquisar = uic.loadUi("pesquisa.ui")
formulario.cadastrar.clicked.connect(funcao_principal)
formulario.listar.clicked.connect(funcao_listagem_veiculos)
veiculos.gerar_pdf.clicked.connect(gerar_pdf)
veiculos.excluir.clicked.connect(excluir_dados)
veiculos.alterar.clicked.connect(editar_dados)
editar.salvar.clicked.connect(salvar_dados)
veiculos.pesquisar.clicked.connect(buscar_dados)


'''EXECUTANDO'''
formulario.show()
app.exec()


