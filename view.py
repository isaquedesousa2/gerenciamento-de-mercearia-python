from controller import *
import os

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i,'w') as arq:
                arq.write('')

criarArquivos('categoria.txt','funcionario.txt',
              'cliente.txt','estoque.txt',
              'fornecedor.txt','vendas.txt'
            )

if __name__ == '__main__':

    while True:
        entrada = int(input(
            'MENU MERCEARIA\n\n'
            'Digite 1 para acessar ( Categorias )\n'
            'Digite 2 para acessar ( Estoque )\n'
            'Digite 3 para acessar ( Fornecedor )\n'
            'Digite 4 para acessar ( Cliente )\n'
            'Digite 5 para acessar ( Funcionario )\n'
            'Digite 6 para acessar ( Vendas )\n'
            'Digite 7 para acessar ( Produtos mais vendidos )\n'
            'Digite 8 para sair\n'
            'Digite a opção: '
        ))
        print('\n')

        os.system('cls' if os.name == 'nt' else 'clear')

        if entrada == 1:
            x = ControllerCategoria()
            while True:
                entrada = int(input(
                    'MENU CATEGORIA \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para remover\n'
                    'Digite 3 para alterar\n'
                    'Digite 4 para mostrar todas as categorias\n'
                    'Digite 5 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    entrada = input('Digite o nome da categoria: ')
                    x.cadastrarCategoria(entrada)
                    print('\n')
                elif entrada == 2:
                    entrada = input('Digite o nome da categoria que deseja remover: ')
                    x.removerCategoria(entrada)
                    print('\n')
                elif entrada == 3:
                    entrada1 = input('Digite o nome da categoria que deseja alterar: ')
                    entrada2 = input('Digite para qual nome deseja alterar: ')
                    x.alterarCategoria(entrada1, entrada2)
                    print('\n')
                elif entrada == 4:
                    x.mostrarCategoria()
                    print('\n')
                elif entrada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')
            
        elif entrada == 2:
            x = ControllerEstoque()
            while True:
                entrada = int(input(
                    'MENU ESTOQUE \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para remover\n'
                    'Digite 3 para alterar\n'
                    'Digite 4 para mostrar todo o estoque\n'
                    'Digite 5 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    nome = input('Digite o nome do produto: ')
                    preco = input('Digite o preço: ')
                    categoria = input('Digite a categoria: ')
                    quantidade = input('Digite a quantidade: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.cadastrarProduto(nome, preco, categoria, quantidade)
                    print('\n')
                elif entrada == 2:
                    entrada = input('Digite o nome do produto que deseja remover: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.removerProduto(entrada)
                    print('\n')
                elif entrada == 3:
                    nome = input('Digite o nome do produto que deseja alterar: ')
                    novoNome = input('Digite o novo nome: ')
                    novoPreco = input('Digite o novo preço: ')
                    novaCategoria = input('Digite a nova categoria: ')
                    novoQuantidade = input('Digite a nova quantidade: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.alterarProduto(nome, novoNome, novoPreco, novaCategoria, novoQuantidade)
                    print('\n')
                elif entrada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.mostrarEstoque()
                    print('\n')
                elif entrada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')
            
        elif entrada == 3:
            x = ControllerFornecedor()
            while True:
                entrada = int(input(
                    'MENU FORNECEDOR \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para remover\n'
                    'Digite 3 para alterar\n'
                    'Digite 4 para mostrar todos os fornecedores\n'
                    'Digite 5 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    nome = input('Digite o nome: ')
                    cnpj = input('Digite o cnpj: ')
                    telefone = input('Digite o telefone: ')
                    categoria = input('Digite a categoria: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                    print('\n')
                elif entrada == 2:
                    cnpj = input('Digite o cnpj do fornecedor que deseja remover: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.removerFornecedor(cnpj)
                    print('\n')
                elif entrada == 3:
                    cnpj = input('Digite o cnpj do fornecedor que deseja alterar: ')
                    novoNome = input('Digite o novo nome: ')
                    novoCnpj = input('Digite o novo cnpj: ')
                    novoTelefone = input('Digite o novo telefone: ')
                    novaCategoria = input('Digite a nova categoria: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.alterarFornecedor(cnpj, novoNome, novoCnpj, novoTelefone, novaCategoria)
                    print('\n')
                elif entrada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.mostrarFornecedor()
                    print('\n')
                elif entrada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')
        
        elif entrada == 4:
            x = ControllerCliente()
            while True:
                entrada = int(input(
                    'MENU CLIENTE \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para remover\n'
                    'Digite 3 para alterar\n'
                    'Digite 4 para mostrar todos os clientes\n'
                    'Digite 5 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    nome = input('Digite o nome: ')
                    telefone = input('Digite o telefone: ')
                    cpf = input('Digite o cpf: ')
                    email = input('Digite a email: ')
                    endereco = input('Digite o endereço: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.cadastrarCliente(nome, telefone, cpf, email, endereco)
                    print('\n')
                elif entrada == 2:
                    cpf = input('Digite o cpf do cliente que deseja remover: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.removerCliente(cpf)
                    print('\n')
                elif entrada == 3:
                    cpf = input('Digite o cpf do cliente que deseja alterar: ')
                    novoNome = input('Digite o novo nome: ')
                    novoCpf = input('Digite o novo cpf: ')
                    novoTelefone = input('Digite o novo telefone: ')
                    novoCpf = input('Digite o novo cpf: ')
                    novoEmail = input('Digite o novo email: ')
                    novoEndereco = input('Digite o novo endereço: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.alterarFornecedor(cnpj, novoNome, novoCnpj, novoTelefone, novaCategoria)
                    print('\n')
                elif entrada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.mostrarCliente()
                    print('\n')
                elif entrada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')

        elif entrada == 5:
            x = ControllerFuncionario()
            while True:
                entrada = int(input(
                    'MENU FUNCIONARIO \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para remover\n'
                    'Digite 3 para alterar\n'
                    'Digite 4 para mostrar todos os clientes\n'
                    'Digite 5 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    clt = input('Digite a clt: ')
                    nome = input('Digite o nome: ')
                    telefone = input('Digite o telefone: ')
                    cpf = input('Digite o cpf: ')
                    email = input('Digite o email: ')
                    endereço = input('Digite o endereco: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.cadastrarFuncionario(clt, nome, telefone, cpf, email, endereco)
                    print('\n')
                elif entrada == 2:
                    cpf = input('Digite o cpf do funcionario que deseja remover: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.removerFuncionario(cpf)
                    print('\n')
                elif entrada == 3:
                    cpf = input('Digite o cpf do funcionario que deseja alterar: ')
                    novaClt = input('Digite a nova clt: ')
                    novoNome = input('Digite o novo nome: ')
                    novoCpf = input('Digite o novo cpf: ')
                    novoTelefone = input('Digite o novo telefone: ')
                    novoCpf = input('Digite o novo cpf: ')
                    novoEmail = input('Digite o novo email: ')
                    novoEndereco = input('Digite o novo endereço: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.alterarFornecedor(cnpj, novaClt, novoNome, novoCnpj, novoTelefone, novaCategoria)
                    print('\n')
                elif entrada == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.mostrarFuncionario()
                    print('\n')
                elif entrada == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')

        elif entrada == 6:
            x = ControllerVenda()
            while True:
                entrada = int(input(
                    'MENU VENDAS \n\n'
                    'Digite 1 para cadastrar\n'
                    'Digite 2 para mostrar as vendas\n'
                    'Digite 3 para voltar\n'
                    'Digite a opção: '
                ))
                print('\n')

                if entrada == 1:
                    nome = input('Digite o nome do produto: ')
                    quantidade = input('Digite a quantidade: ')
                    vendedor = input('Digite o nom do vendedor: ')
                    comprador = input('Digite o nome do comprador: ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    x.cadastrarVenda(nome,quantidade, vendedor, comprador)
                    print('\n')
                elif entrada == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('FORMATO DA DATA XX/XX/XXXX\n')
                    dataInicio = input('Digite a data de inicio: ')
                    dataTermino = input('Digite a data de termino: ')
                    x.mostrarVendas(dataInicio, dataTermino)
                    print('\n')
                elif entrada == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break         
                else:
                    print('Opção invalida \n')     

        elif entrada == 7:
            x = ControllerVenda()
            x.relatorioGeral()
        
        elif entrada == 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('SAIU DO SISTEMA')
            break 
        else:
            print('Opção invalida \n')