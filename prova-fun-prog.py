total_vendas = 0
total_bruto = 0
total_desconto = 0
total_liquido = 0
opcao = None

while opcao !='1,2,3':
    print ('1 - Registrar venda')
    print ('2 - Ver resumo parcial')
    print ('3 - Encerrar sistema')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        produto = input ('Nome do produto: ')
        valor_unitario = float(input('Valor unitário: '))
        quantidade = int(input('Quantidade: '))

        valor_bruto = valor_unitario * quantidade

        if valor_bruto < 100:
            desconto = 0
        
        elif valor_bruto < 1000:
            desconto = 5

        else:
            desconto = 15

        valor_desconto= valor_bruto * (desconto/100)
        valor_final = valor_bruto - valor_desconto

        print (valor_bruto)
        print (desconto)
        print (valor_desconto)
        print (valor_final)

        total_vendas += 1
        total_bruto += valor_bruto
        total_liquido += valor_final

    elif opcao ==2:

        print ('=== RESUMO PARCIAL ===')
        print (total_vendas)
        print (total_desconto)
        print (total_liquido)

    elif opcao==3:

        print ('=== RESUMO FINAL ===')
        print (total_vendas)
        print (total_bruto)
        print (total_desconto)
        print (total_liquido)         

    else: 
        print('invalido')
