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