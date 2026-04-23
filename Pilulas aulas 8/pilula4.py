def atualualizar_historico(historico, paciente):
    if paciente in historico:
        historico.remove(paciente)
    historico.append(paciente)
    return historico    
    

def main():
    historico = ['Ana', 'Guilherme', 'Denilson']
    novo = 'Guilherme'
    print(historico)
    historico = atualualizar_historico(historico, novo)
    print(f' Paciente retornado: {novo}')
    print(f' Hitorico atualizado: {historico}')
    
main()