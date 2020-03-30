import mysql.connector  # precisa instalar o pacote
import json
import requests  # precisa instalar o pacote

from mysql.connector import errorcode


def db_connect():
    try:
        db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='bd')

        print("Database connection made!")
        return db_connection
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)


def create_table_pessoas():
    db = db_connect()
    cursor = db.cursor()
    # criando a tabela (schema)
    sql = """
    CREATE TABLE `pessoas`(
      `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
      `cpf` varchar(18) DEFAULT NULL,
      `name` varchar(200) DEFAULT NULL,
      `nascimento` date DEFAULT NULL,
      `profissao` varchar(200) DEFAULT NULL,
      `address` varchar(255) DEFAULT NULL,
      `companies` varchar(200) DEFAULT NULL,
      `phones` varchar(200) DEFAULT NULL
    )
    """
    cursor.execute(sql)

    db.commit()
    print('Tabela criada com sucesso.')
    # desconectando...
    db.close()


def checker(db, tablename):
    cursor = db.cursor()
    sql = "SHOW TABLES"
    cursor.execute(sql)
    resp = cursor.fetchall()
    count = [x for x in resp if x == (tablename,)]
    if len(count) > 0:
        print("ok")
        db.close()
        return 200
    else:
        create_table_pessoas()
        print("ok")
        db.close()
        return 201


def load_data():
    url = "https://alertrack.com.br/dev/rest_api/tester/"
    r = requests.get(url)
    r.encoding = 'utf-8'
    print("Status code", r.status_code)

    return json.loads(r.content)


def insert_data(comment):
    db = db_connect()

    # listas que filtrarão address e companies
    list_cep = []
    list_number = []
    list_complement = []
    list_cnpj = []
    list_name_comp = []

    # criando uma lista com os CEPs
    for x in comment['address']:
        list_cep = x['zipcode']

    # criando uma lista com os numeros do endereço
    for x in comment['address']:
        list_number = str(x['number'])

    # criando uma lista com os complementos do endereço
    for x in comment['address']:
        list_complement = x['complement']

    for x in comment['companies']:
        list_cnpj = x['cnpj']

    for x in comment['companies']:
        list_name_comp = x['name']

    comment['phones'] = " - ".join(comment['phones']).replace('(', '').replace(')', '')

    cursor = db.cursor()
    sql = "INSERT INTO pessoas(cpf, name, nascimento, profissao, cep, number, complement, comp_cnpj, comp_name, " \
          "phones) VALUES('{0}', '{1}', '{2}', " \
          "'{3}', '{4}', '{5}', '{6}' , '{7}' , '{8}' , '{9}');".format(
        comment['cpf'],
        comment['name'],
        comment['born_at'],
        comment['occupation'],
        list_cep,
        list_number,
        list_complement,
        list_cnpj,
        list_name_comp, comment['phones'])

    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()


def main():
    db = db_connect()
    checker(db, "pessoas")
    comments = load_data()
    for comment in comments:
        insert_data(comment)
    db.close()


if __name__ == "__main__":
    main()
