from DAO import *
from models import *
from datetime import datetime
import os


class ControllerCategoria:

    def cadastrarCategoria(self, categoria):
        existe = False

        x = DaoCategoria.ler()

        for i in x:
            if categoria == i.categoria:
                existe = True

        if existe:
            print('Já existe uma categoria cadastrada com esse nome')
        else:
            DaoCategoria.salvar(categoria)
            print('Categoria cadastrada com sucesso')

    def removerCategoria(self, categoria):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoria, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoria:
                    del x[i]
                    break

            print('Categoria removida com sucesso')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        x = DaoEstoque.ler()

        x = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoria), x.quantidade) 
        if(x.produto.categoria == categoria) else(x), x))

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    f'{i.produto.nome}|'
                    f'{i.produto.preco}|'
                    f'{i.produto.categoria}|'
                    f'{i.quantidade}'
                )
                arq.writelines('\n')

    def alterarCategoria(self, categoriaAlterar, categoriaNova):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaNova, x))
            if len(cat1) <= 0:
                x = list(map(lambda x: Categoria(categoriaNova)
                         if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso')
            else:
                print('Categoria para qual deseja alterar já existe')
        else:
            print('Categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        x = DaoCategoria.ler()
        if len(x) == 0:
            print('Categoria vazia!')
        else:
            for i in x:
                print(f'Categoria {i.categoria}\n')


class ControllerEstoque:

    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        y = DaoCategoria.ler()
        x = DaoEstoque.ler()

        cat = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(cat) > 0:
            if len(est) == 0:
                produto = Produto(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Esse produto já existe')
        else:
            print('Categoria escolhida não existe')

    def removerProduto(self, nome):
        x = DaoEstoque.ler()

        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto removido com sucesso')
                    break
        else:
            print('Produto que deseja remover não existe')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    f'{i.produto.nome}|'
                    f'{i.produto.preco}|'
                    f'{i.produto.categoria}|'
                    f'{i.quantidade}'
                )
                arq.writelines('\n')

    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        est = DaoEstoque.ler()
        cat = DaoCategoria.ler()

        categoria = list(filter(lambda x: x.categoria == novaCategoria, cat))

        if len(categoria) > 0:
            estoque = list(
                filter(lambda x: x.produto.nome == nomeAlterar, est))
            if len(estoque) > 0:
                estoque = list(
                    filter(lambda x: x.produto.nome == novoNome, est))
                if len(estoque) == 0:
                    est = list(map(lambda x: Estoque(Produto(novoNome, novoPreco, novaCategoria), novaQuantidade) if(
                        x.produto.nome == nomeAlterar) else(est), est))

                    with open('estoque.txt', 'w') as arq:
                        for i in est:
                            arq.writelines(
                                f'{i.produto.nome}|'
                                f'{i.produto.preco}|'
                                f'{i.produto.categoria}|'
                                f'{i.quantidade}'
                            )
                            arq.writelines('\n')

                    print('Produto alterado')
                else:
                    print('Produto já cadastrado')
            else:
                print('Produto que deseja alterar não existe')
        else:
            print('Categoria para qual deseja alterar o produto não existe')

    def mostrarEstoque(self):
        x = DaoEstoque.ler()
        if len(x) == 0:
            print('Estoque vazio!')
        else:
            print('========Estoque======== \n')
            for i in x:
                print(
                    f'Nome: {i.produto.nome}\nPreço: {i.produto.preco}\nCategoria: {i.produto.categoria}\nQuantidade: {i.quantidade}\n')

            print('=======================')


class ControllerVenda:

    def cadastrarVenda(self, itemVendido, quantidade, vendedor, comprador):

        x = DaoEstoque.ler()

        produto = list(filter(lambda x: x.produto.nome == itemVendido, x))

        if produto:
            for i in produto:
                if int(i.quantidade) >= int(quantidade):
                    i.quantidade = int(i.quantidade) - int(quantidade)
                    valorTotal = int(quantidade) * int(i.produto.preco)

                    venda = Venda(Produto(i.produto.nome, i.produto.preco,
                                  i.produto.categoria), quantidade, valorTotal, vendedor, comprador)

                    estoque = list(map(lambda x: Estoque(Produto(i.produto.nome, i.produto.preco,
                                   i.produto.categoria), i.quantidade) if(x.produto.nome == itemVendido) else(x), x))

                    with open('estoque.txt', 'w') as arq:
                        for i in estoque:
                            arq.writelines(
                                f'{i.produto.nome}|'
                                f'{i.produto.preco}|'
                                f'{i.produto.categoria}|'
                                f'{i.quantidade}'
                            )
                            arq.writelines('\n')

                    DaoVenda.salvar(venda)

                    print('Venda cadastrada com sucesso')
                else:
                    print('Quantidade acima do estoque')
        else:
            print('Produto não existe')

    def relatorioGeral(self):
        vendas = DaoVenda.ler()
        produtos = []

        for i in vendas:
            nome = i.itemVendido.nome
            quantidade = i.quantidade
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                    if (x['produto'] == nome) else(x), produtos
                                    ))
            else:
                produtos.append({'produto': nome, 'quantidade': quantidade})

        if produtos:
            ordenado = sorted(
                produtos, key=lambda k: k['quantidade'], reverse=True)

            print('Esses são os produtos mais vendidos\n')

            a = 1

            for i in ordenado:
                print(f'============Produto {a}============\n')
                print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}"
                    )
                print('\n')
                a += 1
        else:
            print('Sem produtos no estoque')

    def mostrarVendas(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        data1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        data2 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(
            x.data, '%d/%m/%Y') >= data1 and datetime.strptime(x.data, '%d/%m/%Y') <= data2, vendas))

        if vendasSelecionadas:

            count = 1

            for i in vendasSelecionadas:
                print(f'========== Venda {count} ==========\n')
                print(f'Produto: {i.itemVendido.nome}')
                print(f'Preço: {i.itemVendido.preco}')
                print(f'Categoria: {i.itemVendido.categoria}')
                print(f'Quantidade: {i.quantidade}')
                print(f'Preço total: {i.valorTotal}')
                print(f'Vendedor: {i.vendedor}')
                print(f'Comprador: {i.comprador}')
                print(f'Data: {i.data}')
                print('\n')

                count += 1
        
        else:
            print('Sem vendas!')


class ControllerFornecedor:

    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        y = DaoCategoria.ler()

        forn = list(filter(lambda x: x.cnpj == cnpj, x))
        cat = list(filter(lambda x: x.categoria == categoria, y))

        if not forn:
            if cat:
                if len(cnpj) != 14:
                    print('Digite um cnpj válido')
                elif len(telefone) != 11:
                    print('Digite um telefone válido')
                else:
                    fornecedor = Fornecedor(nome, cnpj, telefone, categoria)
                    DaoFornecedor.salvar(fornecedor)
                    print('Fornecedor cadastrado com sucesso')
            else:
                print('Categoria escolhida não existe')
        else:
            print('Fornecedor já esta cadastrado')

    def removerFornecedor(self, cnpj):
        x = DaoFornecedor.ler()

        forn = list(filter(lambda x: x.cnpj == cnpj, x))

        if forn:
            for i in range(len(x)):
                if x[i].cnpj == cnpj:
                    del x[i]
                    print('Fornecedor removido com sucesso')
                    break
        else:
            print('Fornecedor não existe')

        with open('fornecedor.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    f'{i.nome}|'
                    f'{i.cnpj}|'
                    f'{i.telefone}|'
                    f'{i.categoria}'
                )
                arq.writelines('\n')

        

    def alterarFornecedor(self, cnpj, novoNome, novoCnpj, novoTelefone, novaCategoria):
        x = DaoFornecedor.ler()
        y = DaoCategoria.ler()

        fornecedor = list(filter(lambda x: x.cnpj == cnpj, x))

        if fornecedor:
            if len(cnpj) != 14 or len(novoCnpj) != 14:
                print('Digite cnpj e novo cnpj válidos')
            elif len(novoTelefone) != 11:
                print('Digite um telefone válido')
            else:
                categoria = list(
                    filter(lambda x: x.categoria == novaCategoria, y))
                if categoria:
                    x = list(map(lambda x: Fornecedor(
                        novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.cnpj == cnpj) else(x), x))

                    with open('fornecedor.txt', 'w') as arq:
                        for i in x:
                            arq.writelines(
                                f'{i.nome}|'
                                f'{i.cnpj}|'
                                f'{i.telefone}|'
                                f'{i.categoria}'
                            )
                            arq.writelines('\n')

                    print('Fornecedor alterado com sucesso')
                else:
                    print('Categoria não existe')
        else:
            print('Fornecedor não existe')

    def mostrarFornecedor(self):
        x = DaoFornecedor.ler()

        if not x:
            print('Estoque vazio!')
        else:
            count = 1
            for i in x:
                print(f'======== Fornecedores {count} ======== \n')
                print(
                    f'Nome: {i.nome}\nCNPJ: {i.cnpj}\nTelefone: {i.telefone}\nCategoria: {i.categoria}\n')
                count += 1


class ControllerCliente:

    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoCliente.ler()

        cliente = list(filter(lambda x: x.cpf == cpf, x))

        if not cliente:
            if len(telefone) != 11:
                print('Digite um telefone válido')
            elif len(cpf) != 11:
                print('Digite um cpf válido')
            else:
                cliente = Pessoa(nome, telefone, cpf, email, endereco)
                DaoCliente.salvar(cliente)
                print('Cliente cadastrado com sucesso')
        else:
            print('Cliente já cadastrado')

    def removerCliente(self, cpf):
        x = DaoCliente.ler()

        if len(cpf) == 11:
            cliente = list(filter(lambda x: x.cpf == cpf, x))

            if cliente:
                for i in range(len(x)):
                    if x[i].cpf == cpf:
                        del x[i]
                        break
                    print('Cliente removido com sucesso')
            else:
                print('Cliente com esse cpf não existe')
        else:
            print('Digite um cpf válido')

        with open('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    f'{i.nome}|'
                    f'{i.telefone}|'
                    f'{i.cpf}|'
                    f'{i.email}|'
                    f'{i.endereco}'
                )
                arq.writelines('\n')
    
    def alterarCliente(self, cpf, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoCliente.ler()

        if len(cpf) != 11 or len(novoCpf) != 11:
            print('Digite cpf e novo cpf válidos')
        elif len(novoTelefone) != 11:
            print('Digite um telefone válido')
        else:
            cpfNovo = list(filter(lambda x: x.cpf == novoCpf, x))
            if  not cpfNovo:
                cliente = list(filter(lambda x: x.cpf == cpf, x))
                if cliente:
                    x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.cpf == cpf) else(x), x))
                    with open('cliente.txt', 'w') as arq:
                        for i in x:
                            arq.writelines(
                                f'{i.nome}|'
                                f'{i.telefone}|'
                                f'{i.cpf}|'
                                f'{i.email}|'
                                f'{i.endereco}'
                            )
                            arq.writelines('\n')
                    print('Cliente alterado com sucesso')
                else:
                    print('Cliente com esse cpf não existe')
            else:
                print('Novo cpf já cadastrado em outro cliente')
  
    def mostrarCliente(self):
        x = DaoCliente.ler()

        if not x:
            print('Estoque vazio!')
        else:
            count = 1
            for i in x:
                print(f'======== Cliente {count} ======== \n')
                print(
                    f'Nome: {i.nome}\nTelefone: {i.telefone}\nCPF: {i.cpf}\nE-mail: {i.email}\nEndereço: {i.endereco}\n')


class ControllerFuncionario:

    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        funcionarioCpf = list(filter(lambda x: x.cpf == cpf, x))
        funcionarioClt = list(filter(lambda x: x.clt == clt, x))

        if funcionarioCpf:
            print('CPF já cadastrado')
        elif funcionarioClt:
            print('Já existe um funcionario com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) == 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario cadastrado com sucesso')
            else:
                print('Digite um cpf ou telefone válido')

    def removerFuncionario(self, cpf):
        x = DaoFuncionario.ler()

        if len(cpf) == 11:
            funcionario = list(filter(lambda x: x.cpf == cpf, x))

            if funcionario:
                for i in range(len(x)):
                    if x[i].cpf == cpf:
                        del x[i]
                        break
                print('Funcionario removido com sucesso')
            else:
                print('Funcionario com esse cpf não existe')
        else:
            print('Digite um cpf válido')

        with open('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(
                    f'{i.clt}|'
                    f'{i.nome}|'
                    f'{i.telefone}|'
                    f'{i.cpf}|'
                    f'{i.email}|'
                    f'{i.endereco}'
                )
                arq.writelines('\n')
    
    def alterarFuncionario(self, cpf, novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        if len(cpf) != 11 or len(novoCpf) != 11:
            print('Digite cpf e novo cpf válidos')
        elif len(novoTelefone) != 11:
            print('Digite um telefone válido')
        else:
            cpfNovo = list(filter(lambda x: x.cpf == novoCpf, x))
            if  not cpfNovo:
                clt = list(filter(lambda x: x.clt == novaClt, x))
                if not clt:
                    cliente = list(filter(lambda x: x.cpf == cpf, x))
                    if cliente:
                        x = list(map(lambda x: Funcionario(novaClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.cpf == cpf) else(x), x))
                        with open('funcionario.txt', 'w') as arq:
                            for i in x:
                                arq.writelines(
                                    f'{i.clt}|'
                                    f'{i.nome}|'
                                    f'{i.telefone}|'
                                    f'{i.cpf}|'
                                    f'{i.email}|'
                                    f'{i.endereco}'
                                )
                                arq.writelines('\n')
                        print('Funcionário alterado com sucesso')
                    else:
                        print('Funcionário com esse cpf não existe')
                else:
                    print('Já existe um funcionário com essa nova Clt')
            else:
                print('Novo cpf já cadastrado em outro funcionário')
    
    def mostrarFuncionario(self):
        x = DaoFuncionario.ler()

        if not x:
            print('Sem funcionários!')
        else:
            count = 1
            for i in x:
                print(f'======== Funcionário {count} ======== \n')
                print(
                    f'CLT: {i.clt}\nNome: {i.nome}\nTelefone: {i.telefone}\nCPF: {i.cpf}\nE-mail: {i.email}\nEndereço: {i.endereco}\n')
                count += 1

os.system('cls' if os.name == 'nt' else 'clear')
