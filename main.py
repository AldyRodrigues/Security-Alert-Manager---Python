import personalizção_str
import cadastro_alertas
import exibir_alertas


#PROGRAMA PRINCIPAL
alertas={}

personalizção_str.linper(' CADASTRO DE ALERTAS ')
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
        alertas.update(cadastro_alertas.cadalert(alertas))
    
    
    elif opcao == 2:
        if len(alertas)==0:
            print('Nenhum alerta cadastrado ainda.')
        else:
            for chave, dados in alertas.items():
              exibir_alertas.alertascad(chave, dados)
    
    elif opcao == 3:
            if len(alertas) == 0:
                print('Nenhum alerta cadastrado ainda.')
            else:
                filtro = input('Qual prioridade deseja filtrar? (ex: Alta, Média, Baixa):\n').strip().lower()
                encontrou = False
    
                for chave, dados in alertas.items():
                    if dados['Prioridade'].strip().lower() == filtro:
                        exibir_alertas.alertascad(chave, dados)
                        encontrou = True
    
                if not encontrou:
                    print(f'Nenhum alerta encontrado com a prioridade "{filtro}".')
    
    
    else:
        print('Opção inválida! Escolha 1, 2 ou 3.')
        continue
    
    opcao=input('\nDeseja continuar no programa:S/N\n')[0].upper()

with open('AlertasSalvos.txt','a', encoding='utf-8') as arquivo:
    for i, (chave, dados) in enumerate(alertas.items(), start=1):
            arquivo.write(f'---Alerta {i}---\n')
            arquivo.write(f"Area: {dados['area']}\n")
            arquivo.write(f"Prioridade: {dados['prioridade']}\n")
            arquivo.write(f"Descrição: {dados['descrição']}\n\n")
        

personalizção_str.linper(' POGRAMA FINALIZADO ')
