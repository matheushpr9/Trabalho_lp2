import sqlite3
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
                                            complemento text)""")

informacoes = {
                "cpf" : 'a', 
                "nome_cliente" : 'a', 
                "telefone" : 'a', 
                "data_nascimento": 'a', 
                "cep" : 'a',
                "estado" : 'a',
                "cidade":  'a',
                "bairro" : 'a',
                "logradouro" :'a',
                "num" :'a',
                "complemento" : 'a'
            }

# cur.execute("CREATE TABLE IF NOT EXISTS medico(crm, nome_medico, especialidade)")
# cur.execute("CREATE TABLE IF NOT EXISTS consulta(id_consulta, cpf, crm, data_consulta, horario)")
# cur.execute("CREATE TABLE IF NOT EXISTS agenda(str_data_h, id_consulta)")

# cur.execute("""
#     INSERT INTO medico VALUES
#         ('82045-SP', 'Adilson de Andrade', 'PEDIATRIA'),
#         ('89880-SP', 'Adrea Aparecida Peixe Valotta da Silva', 'GINECOLOGIA'),
#         ('143749-SP', 'Camilla Nicolucci', 'PSIQUIATRIA'),
#         ('20699-SP', 'Carlos Tadeu Parisi de Oliveira', 'NEUROCIRURGIA'),
#         ('63592-SP', 'Dario Vale Junior', 'RADIOLOGIA'),
#         ('125515-SP', 'Ednei Haruo Kawatake', 'ORTOPEDIA'),
#         ('75673-SP', 'Evandro de Lira Costa', 'CARDIOLOGIA'),
#         ('184391-SP', 'Gabriela de Souza Pereira', 'ANESTESIOLOGIA'),
#         ('134521-SP', 'Guilherme Chohfi de Miguel', 'ORTOPEDIA'),
#         ('42879-SP', 'Jose Ramos Filho', 'CARDIOLOGIA')
# """)

# cur.execute("""
# SELECT crm, nome_medico, especialidade
# FROM medico;
# """)

# result = cur.fetchone();

# print(result)

cur.execute("SELECT * FROM cliente")
print(cur.fetchall())
