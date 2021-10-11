import os

def menu():
    os.system('clear')
    print("=" * 40 + " MENU " + "=" * 40)
    print(f'O que gostaria de saber sobre mim {user}? {os.linesep}')
    print('[1] - "Qual área me identifico mais" ')
    print('[2] - "Quais linguagens e recursos tenho praticado e desenvolvido" ')
    print('[3] - "Quais projetos já desenvolvi e/ou pretendo desenvolver" ')
    print('[4] - "Quais cursos já realizei e/ou realizo" ')
    print('[5] - "Onde eu moro e idade" ')
    print('[6] - "O que faço além de codar" ')


user = str(input(f"Olá, seja bem vinde! Qual o seu nome? {os.linesep}"))

while(1):
    menu()
    option = int(input("Digite uma opção: "))
    if option == 1:
        print(f'{os.linesep}Então {user}, eu me identifico mais como Back end, mas desejo ser Full Stack, então também estudo Front.')
    elif option == 2:
        print(f'{os.linesep}Eu programo em Python, meu favorito! Também gosto de SQL, Javascript, HTML, CSS e também estou aprendendo Java e frameworks {user}!')
    elif option == 3:
        print(f'{os.linesep}Desenvolvi pequenos projetos: Agenda, Calculadora, ChatBots, Bancos Relacionais, Formulários, Analises de Dados e Automação de Dados. Mas {user}, eu desejo criar: APIs, Paginas web e aplicativos maiores')
    elif option == 4:
        print(f'{os.linesep}{user}, Atualmente estou no 2º semestre da minha graduação em Sistemas da Informação, também faço curso de Python no Projeto Mil Devs, Digital Inovation One e aprendo muita coisa com o Youtube também :D')
    elif option == 5:
        print(f'{os.linesep}Eu moro na Zona Leste de São Paulo {user}, tenho 22 anos!')
    elif option == 6:
        print(f'{os.linesep}Além de programar, gosto de praticar esportes, em especial o futebol <3 sou apaixonada! Também toco violão e ukulele {user} :)')
    else:
        print(f'{os.linesep}Esse opção é invalida {user}, tente novamente...')
    input(f'{os.linesep}Tecle ENTER para continuar...')
