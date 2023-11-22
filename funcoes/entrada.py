import os
import funcoes.escritaArquivo as escritaArquivo
limpa_a_tela = lambda: os.system('cls')

def fluxo_cadastra_entrada(entradas, usuarioCorrente):

    while True:
        nome = input('Digite o nome da entrada: ')
        if(nome == ''):
            print('O nome não pode ser nulo!')
            continue
        break

    while True:
        descricao = input('Digite a descrição da entrada: ')
        if(descricao == ''):
            print('A descrição não pode ser nula!')
            continue
        break

    entrada = {
        'nome': nome,
        'id': len(entradas),
        'idUser': usuarioCorrente['id'],
        'descricao': descricao
    }

    limpa_a_tela()
    print('Entrada criada com sucesso!')
    entradas.append(entrada)
    escritaArquivo.sobrescreve_entradas(entradas)

def mostra_entradas(entradas, usuarioCorrente):
    limpa_a_tela()
    print('==========================')
    print('||      ENTRADAS        ||')
    print('==========================')
    for entrada in entradas:
        if entrada['idUser'] == usuarioCorrente['id']:
            print(f"Nome: {entrada['nome']}")
            print(f"Descrição: {entrada['descricao']}")
            print('==========================')

def fluxo_compartilha_historico(usuarios, compartilhamentos, usuarioCorrente):
    limpa_a_tela()
    crm = ''
    while True:
        crm = input('Digite o CRM do médico que deseja compartilhar: ')
        if(crm == ''):
            print('O ID não pode ser nulo!')
            continue
        break
    medico = ''
    for usuario in usuarios:
        if usuario['crm'] == crm:
            medico = usuario
            break
    if medico == '':
        print('Médico não encontrado!')
        return


    compartilhamento = {
        'id': len(compartilhamentos),
        'idMedico': medico['id'],
        'idPaciente': usuarioCorrente['id']
    }

    limpa_a_tela()
    print('Compartilhamento criado com sucesso!')
    compartilhamentos.append(compartilhamento)
    escritaArquivo.sobrescreve_compartilhamentos(compartilhamentos)

def mostra_compartilhamentos(compartilhamentos, usuarioCorrente, usuarios):
    limpa_a_tela()
    print('=================================================')
    print('||   MÉDICOS COM QUEM COMPATILHOU O HISTÓRICO  ||')
    print('=================================================')
    for compartilhamento in compartilhamentos:
        if compartilhamento['idPaciente'] == usuarioCorrente['id']:
            print(f"Médico: {usuarios[compartilhamento['idMedico']]['nome']}")
            print('==========================')