import sqlite3
import pandas as pd

con = sqlite3.connect("star_saudavel.db")

cur = con.cursor()


cur.execute("""CREATE TABLE IF NOT EXISTS cliente(
                                            cpf text,
                                            nome_cliente text, 
                                            telefone text, 
                                            data_nascimento text, 
                                            cep text, 
                                            estado text, 
                                            cidade text, 
                                            bairro text, 
                                            logradouro text, 
                                            num text, 
                                            complemento text,
                                            PRIMARY KEY(cpf))""")

informacoes = {
                "cpf" : '523.353.948-02', 
                "nome_cliente" : 'Matheus Henrique Ptasinsnki Rosa', 
                "telefone" : '11959492163', 
                "data_nascimento": '21/04/2001', 
                "cep" : '12916-560',
                "estado" : 'SP',
                "cidade":  'Bragança Paulista',
                "bairro" : 'Jardim do Suk',
                "logradouro" :'Rua Alexandre de Simoni',
                "num" :'298',
                "complemento" : '9'
            }

try:
    cur.execute("INSERT INTO cliente VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(informacoes["cpf"],informacoes["nome_cliente"],informacoes["telefone"],informacoes["data_nascimento"],informacoes["cep"],informacoes["estado"],informacoes["cidade"],informacoes["bairro"],informacoes["logradouro"],informacoes["num"],informacoes["complemento"] ))
    con.commit()
except:
    print("base já cadastrada")

cur.execute("CREATE TABLE IF NOT EXISTS medico(crm, nome_medico, especialidade, PRIMARY KEY(crm))")
cur.execute("CREATE TABLE IF NOT EXISTS consulta(str_data_h, cpf, crm, data_consulta, horario, PRIMARY KEY(str_data_h))")

try:
    cur.execute("""
        INSERT INTO medico VALUES
            ('82045-SP', 'Adilson de Andrade', 'PEDIATRIA'),
            ('89880-SP', 'Adrea Aparecida Peixe Valotta da Silva', 'GINECOLOGIA'),
            ('143749-SP', 'Camilla Nicolucci', 'PSIQUIATRIA'),
            ('20699-SP', 'Carlos Tadeu Parisi de Oliveira', 'NEUROCIRURGIA'),
            ('63592-SP', 'Dario Vale Junior', 'RADIOLOGIA'),
            ('125515-SP', 'Ednei Haruo Kawatake', 'ORTOPEDIA'),
            ('75673-SP', 'Evandro de Lira Costa', 'CARDIOLOGIA'),
            ('184391-SP', 'Gabriela de Souza Pereira', 'ANESTESIOLOGIA'),
            ('134521-SP', 'Guilherme Chohfi de Miguel', 'ORTOPEDIA'),
            ('42879-SP', 'Jose Ramos Filho', 'CARDIOLOGIA')
    """)
    con.commit()
except:
    print("base já cadastrada")

df = pd.read_sql_query("SELECT * FROM consulta", con)

# df["concat"] = df.nome_medico + " - " + df.especialidade

# print((df[df["concat"] == "Adilson de Andrade  - PEDIATRIA"]).crm)
# cur.execute("""
# SELECT *
# FROM consulta;
# """)
# print(cur.fetchall())

dados = {}

grupos = df.groupby("data_consulta").groups


for dado in grupos:
    print(dado)
    dados[dado] = len(grupos[dado])


# result = cur.fetchone();

# print(result)

# cur.execute("SELECT * FROM cliente WHERE cpf ='529.753.948-02'")
# a = cur.fetchall() 
# print(a)
# cur.execute("SELECT * FROM cliente")
# print(cur.fetchall())
# cur.execute("DELETE FROM cliente WHERE cpf='529.753.948-02'")
# print(cur.fetchall())