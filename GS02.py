import funcoes.escritaArquivo as escritaArquivo 
import funcoes.usuario as usuario
import funcoes.entrada as entrada
import os

# Definindo função que limpa a tela do terminal
limpa_a_tela = lambda: os.system('cls')
usuarioCorrente = ''

usuarios = escritaArquivo.carrega_usuarios()
compartilhamentos = escritaArquivo.carrega_compartilhamentos()
entradas = escritaArquivo.carrega_entradas()

def mostra_tela_inicial():
    print('==========================')
    print('||    MENU PRINCIPAL    ||')
    print('==========================')
    print('1. Login')
    print('2. Cadastro')
    print('0. Finalizar programa')

def mostra_home_logado_paciente():
    print('==========================')
    print('||         HOME         ||')
    print('==========================')
    print(f"Paciente: {usuarioCorrente['nome']}\n")
    print('1. Cadastrar Entrada')
    print('2. Ver Entradas')
    print('3. Compartilhar Histórico Médico')
    print('4. Ver Compartilhamentos')
    print('5. Alterar Senha')
    print('0. Logout')

def mostra_home_logado_medico():
    print('==========================')
    print('||         HOME         ||')
    print('==========================')
    print(f"Médico: {usuarioCorrente['nome']}\n")
    print('1. Cadastrar Entradas')
    print('2. Ver Entradas')
    print('3. Compartilhar Histórico Médico')
    print('4. Ver Compartilhamentos')
    print('5. Ver Pacientes')
    print('6. Alterar Senha')
    print('0. Logout')



while True:
    mostra_tela_inicial()
    opcaoInicial = input('Insira a opção desejada: ')
    
    match opcaoInicial:

        case '1':
            usuarioCorrente = usuario.fluxo_login(usuarios)
            while True:
                if usuarioCorrente['tipo'] == 'paciente':
                    mostra_home_logado_paciente()
                    opcaoPaciente = input('Insira a opção desejada: ')
                    match opcaoPaciente:
                        case '1':
                            entrada.fluxo_cadastra_entrada(entradas, usuarioCorrente)
                        case '2':
                            entrada.mostra_entradas(entradas, usuarioCorrente)
                        case '3':
                            entrada.fluxo_compartilha_historico(usuarios, compartilhamentos, usuarioCorrente)
                        case '4':
                            entrada.mostra_compartilhamentos(compartilhamentos, usuarioCorrente, usuarios)
                        case '5':
                            usuario.fluxo_altera_senha(usuarioCorrente["id"], usuarios)
                        case '0':
                            limpa_a_tela()
                            break
                        case _:
                            limpa_a_tela()
                            print('Opção inválida, tente novamente!')
                elif usuarioCorrente['tipo'] == 'medico':
                    mostra_home_logado_medico()
                    opcaoMedico = input('Insira a opção desejada: ')
                    match opcaoMedico:
                        case '1':
                            entrada.fluxo_cadastra_entrada(entradas, usuarioCorrente)
                        case '2':
                            entrada.mostra_entradas(entradas, usuarioCorrente)
                        case '3':
                            entrada.fluxo_compartilha_historico(usuarios, compartilhamentos, usuarioCorrente)
                        case '4':
                            entrada.mostra_compartilhamentos(compartilhamentos, usuarioCorrente, usuarios)
                        case '5':
                            usuario.fluxo_ver_pacientes(usuarioCorrente, usuarios, compartilhamentos, entradas)
                        case '6':
                            usuario.fluxo_altera_senha(usuarioCorrente["id"], usuarios)
                        case '0':
                            limpa_a_tela
                            break
                        case _:
                            limpa_a_tela()
                            print('Opção inválida, tente novamente!')
        case '2':
            usuario.cadastrar_usuario(usuarios)
        case '0':
            break
        case _:
            limpa_a_tela()
            print('Opção inválida, tente novamente!')
            