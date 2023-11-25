import os
import funcoes.escritaArquivo as escritaArquivo
import funcoes.entrada as entrada
limpa_a_tela = lambda: os.system('cls')

def cadastrar_usuario(DbUsuarios):
    limpa_a_tela()
    nome = ''
    email = ''
    senha = ''
    while True:
        nome = input('Digite o nome do usuário: ')
        if(nome == ''):
            limpa_a_tela()
            print('O nome não pode ser nulo!')
            continue
        break

    while True:
        cpf = input('Digite o CPF do usuário: ')
        if(cpf == ''):
            limpa_a_tela()
            print('O CPF não pode ser nulo!')
            continue
        break

    while True:
        tipo = input('Digite o tipo do usuário: (medico ou paciente)\n')
        if(tipo != "medico" and tipo != "paciente"):
            limpa_a_tela()
            print('O tipo deve ser medico ou paciente!')
            continue
        break
    crm = ''
    if tipo == "medico":
        while True:
            crm = input('Digite o CRM do médico: ')
            if(crm == ''):
                limpa_a_tela()
                print('O CRM não pode ser nulo!')
                continue
            break

    while True:
        email = input('Digite o email do usuário: ')
        if(email == ''):
            print('O email não pode ser nulo!')
            continue

        for user in DbUsuarios:
            if user['email'] == email:
                print('Este email já está sendo usado!')
        break
            
    while True:
        senha = input('Digite o senha do usuário: ')
        if len(senha) < 5:
            print('A senha deve conter no mínimo 5 caracteres!')
            continue
        break

    while True:
        confirmeSenha = input('Confirme a senha do usuário: ')
        if(senha != confirmeSenha):
            limpa_a_tela()
            print('As Senhas não conferem! Tente novamente')
        else:
            break

    user = {
        'nome':  nome,
        'email': email,
        'senha': senha,
        'id': len(DbUsuarios),
        'tipo': tipo,
        'crm': crm,
        'cpf': cpf
    }

    limpa_a_tela()
    print('Usuário criado com sucesso!')
    DbUsuarios.append(user)
    escritaArquivo.sobrescreve_usuarios(DbUsuarios)

def fluxo_login(DbUsuarios):
    while True:
        email = input('Insira o email: ')
        if(email == ''):
            print('O email não pode ser nulo!')
            limpa_a_tela()
            continue

        senha = input('Insira a senha: ')
        if(email == ''):
            print('A senha não pode ser nula!')
            continue

        for user in DbUsuarios:
            if(user['email'] == email):
                if(user['senha'] == senha):
                    limpa_a_tela()
                    print('Logado com Sucesso!')
                    return user
                else:
                    limpa_a_tela()
                    print('Senha incorreta! Tente Novamente!')
                    break
        limpa_a_tela()
        print('Usuário não encontrado! Tente Novamente!')
        
def fluxo_altera_senha(idUser, DbUsers):
    limpa_a_tela()
    senhaAtual = input("Informe sua senha atual: ")
    if DbUsers[idUser]['senha'] != senhaAtual:
        print('Senha incorreta!')
    else:
        novaSenha = input('Informe uma nova senha: ')
        confirmaNovaSenha = input('Confirme a nova senha: ')
        if novaSenha != confirmaNovaSenha:
            limpa_a_tela()
            print('As senhas não conferem!')
        else:
            DbUsers[idUser]['senha'] = novaSenha
            limpa_a_tela()
            print('Nova senha cadastrada!')

def fluxo_ver_pacientes(usuarioCorrente, DbUsuarios, DbCompartilhamentos, DbEntradas):
    limpa_a_tela()
    print('==========================')
    print('||      PACIENTES       ||')
    print('==========================')

    compartilhamentosComMedicoCorrente = []
    usuariosQueCompartilharam = []

    for compartilhamento in DbCompartilhamentos:
        if compartilhamento['idMedico'] == usuarioCorrente['id']:
            compartilhamentosComMedicoCorrente.append(compartilhamento)
            usuariosQueCompartilharam.append(DbUsuarios[compartilhamento['idPaciente']])

    
    for i, usuario in enumerate(usuariosQueCompartilharam, start=1):
        print(f"{i}. CPF: {usuario['cpf']} - Nome: {usuario['nome']}")
        print('==========================')
    
    paciente = ''
    while True:
        paciente = input("Digite o número do paciente que deseja ver o histórico: ")
        if paciente == '' or 0 >= int(paciente) or int(paciente) > len(usuariosQueCompartilharam):
            print('Opção inválida!')
            continue
        break
    entrada.mostra_entradas(DbEntradas, usuariosQueCompartilharam[int(paciente)-1])
