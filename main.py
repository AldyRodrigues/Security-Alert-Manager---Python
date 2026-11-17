def linper(msg):
    print(len(msg)*'=')
    print(msg)
    print(len(msg)*'=')

def cadalert(alertas_ja_salvos):
    cont = 'S'
    novos_alertas= {}
    key = len(alertas_ja_salvos) + 1
    while cont == 'S':
        
        area=input('\nQual ârea você deseja reportar?:\n')
        prioridade=input('\nQual a gravidade?:\n')
        descricao=input('\nDê uma breve descrição:\n')

        novos_alertas[key]={
            
            'Ârea': area,
            'Prioridade': prioridade,
            'Descrição': descricao
        }
        
        key += 1
        
        cont=input('deseja realizar cadastrar mais um alerta?: S/N\n')[0].upper()
    
    return novos_alertas

def alertascad(chave, dados):
    print(f'--- Alerta {chave} ---')
    print(f"Área: {dados['Ârea']}")
    print(f"Prioridade: {dados['Prioridade']}")
    print(f"Descrição: {dados['Descrição']}")
    print()

#PROGRAMA PRINCIPAL
alertas={}

linper(' CADASTRO DE ALERTAS ')
opcao = 'S'

while opcao == "S":
    try:
        opcao=int(input(' Escolha umas das opções abaixo.\n' \
                '1.Cadastrar um novo Alerta de segurança.\n' \
                '2.Exibir Alertas ja  cadastrados.\n'
                '3.Filtrar Alertas.\n'))
    except ValueError:
        print('insira apenas as opções válidas, 1, 2 ou 3!')
        continue
    
    
    if opcao == 1:
        alertas.update(cadalert(alertas))
    
    
    elif opcao == 2:
        if len(alertas)==0:
            print('Nenhum alerta cadastrado ainda.')
        else:
            for chave, dados in alertas.items():
              alertascad(chave, dados)
    
    elif opcao == 3:
            if len(alertas) == 0:
                print('Nenhum alerta cadastrado ainda.')
            else:
                filtro = input('Qual prioridade deseja filtrar? (ex: Alta, Média, Baixa):\n').strip().lower()
                encontrou = False
    
                for chave, dados in alertas.items():
                    if dados['Prioridade'].strip().lower() == filtro:
                        alertascad(chave, dados)
                        encontrou = True
    
                if not encontrou:
                    print(f'Nenhum alerta encontrado com a prioridade "{filtro}".')
    
    
    else:
        print('Opção inválida! Escolha 1, 2 ou 3.')
        continue
    
    opcao=input('\nDeseja continuar no programa:S/N\n')[0].upper()

linper(' POGRAMA FINALIZADO ')