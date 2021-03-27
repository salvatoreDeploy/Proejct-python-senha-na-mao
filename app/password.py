import sqlite3

MASTER_PSSWORD = ''

senha = input("Digite sua senha: ")
if senha != MASTER_PSSWORD:
    print("Senha invalida! Encerrando processo")
    exit()

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL, 
    password TEXT NOT NULL   
);
''')

def menu():
    print("********************************")
    print("* i : inserir nova senha       *")
    print("* l : listar serviços salvos   *")
    print("* r : recuperar uma senha      *")
    print("* s : sair                     *")
    print("********************************")

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0 :
        print("Serviço não encontrado (use 'l' para verificar o serviço). ")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que vc deseja fazer? ")
    if op not in ['l', 'i', 'r', 's']:
        print('Opção invalida')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input("Qual nome do serviço? ")
        username = input("Qual nome de usuario? ")
        password = input("Qual a senha ?")
        insert_password(service, username, password)
    
    if op == 'l':
        show_services()

    if op == 'r':
        service = input("Qual o serviço que quer verificar a senha? ")
        get_password(service)
conn.close()