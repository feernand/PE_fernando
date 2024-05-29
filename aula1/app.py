import os 

restaurantes = [{'nome':'Popo pães','categoria':'Padaria','ativo':False},
                {'nome':'Cidade de minas','categoria':'Mineiro','ativo':True},
                {'nome':'Miamoto','categoria':'Japones','ativo':True},
                {'nome':'Luigis','categoria':'Italiano','ativo':False}]
                

def exibir_maracutaia():
    print('''████████████████████████████████████████████████████████████████████████
            █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
            █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
            ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀\n''')

def definiropcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar Restaurantes')
    print('3. Alterar status do restaurantes')
    print('4. Sair \n')

def voltar_menu():
    input('\ndigite uma tecla para retornar ao menu')
    main()

def opc_invalida():
    print('opção invalida \n')
    voltar_menu()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante 

        Inputs:
        -Nome do restaurates
        -Categorias

        Outputs:
        -Adiciona um novo restaurante ao dicionário restaurantes


    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite aqui o nome do novo restaurante: ')
    categoria = input(f'Informe a categoria do Restaurante {nome_restaurante}: ')
    print('Qual a situação do restaurante?\nAtivo = 1\nInativo = 2')
    status = input('Defina o status do restaurante: ')
    status = True if status == "1" else False
    dados_restaurante  = {'nome':nome_restaurante,'categoria':categoria,'ativo':status}
    restaurantes.append(dados_restaurante)
    print(f'\n Restaurante {nome_restaurante} cadastrado com sucesso')
    voltar_menu()

def listar_restaurantes():
    exibir_subtitulo('Lista dos restaurantes\n')
    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria_restaurante=restaurante['categoria']
        atividade_restaurante= 'Ativo' if restaurante['ativo'] else 'Inativo'
        print(f' - {nome_restaurante} | {categoria_restaurante} | {atividade_restaurante}')

    voltar_menu()
        
def alterar_status_do_restaurante():
    exibir_subtitulo('Alterando status do restaurante')
    nome_do_restaurante=input('Digite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado')

    voltar_menu()


def fechar_app():
    exibir_subtitulo('Finalizar app')

def exibir_subtitulo(texto):
    os.system("cls")
    linha='-'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def escolher_opc():
    try:
        opc_escolhida = int(input("Escolha uma opção: "))

        if opc_escolhida==1:
            cadastrar_novo_restaurante()
        elif opc_escolhida==2:
            listar_restaurantes()
        elif opc_escolhida==3:
            alterar_status_do_restaurante()
        else:
            fechar_app()
    except:
        opc_invalida()

def main():
    os.system("cls")
    exibir_maracutaia()
    definiropcoes()
    escolher_opc()

if __name__ == '__main__':
    main()