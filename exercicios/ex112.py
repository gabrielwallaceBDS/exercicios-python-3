#Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
def leia_cpf(msg="CPF: ", show=True):
    """
    -> Validador de CPF
    :param msg: Mensagem que será exibida para o usuário (não é obrigatório! Caso 'msg' não receba
    nenhum valor ele retornará a mensagem "CPF: ".
    :param show: Parâmetro não obrigatório utilizado para mostrar ou não o CPF formatado (caso 'show' não receba
    nenhum valor, ela retornará 'True' e mostrará o CPF formatado).
    :return: retorna o CPF digitado pelo usuário em tipo inteiro.
    """
    from time import sleep
    vad = False
    while not vad:
        erro = False
        c1 = input(msg).strip().replace('.', '').replace('-', '').replace(',', '')
        print('Verificando...')
        sleep(1)
        for c in range(0, len(c1)):
            if c1[c].isalpha():
                erro = True
        if len(c1) != 11:
            erro = True
        if erro:
            print(f'CPF inválido!')
        else:
            if show:
                print(f'O CPF \'{c1[:3]}.{c1[3:6]}.{c1[6:9]}-{c1[9:]}\' é válido.')
            else:
                print('CPF válido.')
            vad = True
            return int(c1)