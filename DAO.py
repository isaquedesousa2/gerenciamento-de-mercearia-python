from models import *


class DaoCategoria:

    @classmethod
    def salvar(cls, nome):
        with open('categoria.txt', 'a') as arq:
            arq.write(nome + '\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        categoria = []

        for i in cls.categoria:
            categoria.append(Categoria(i))

        return categoria


class DaoVenda:

    @classmethod
    def salvar(cls, venda: Venda):
        with open('vendas.txt', 'a') as arq:
            arq.writelines(
                venda.itemVendido.nome + '|' +
                str(venda.itemVendido.preco) + '|' +
                venda.itemVendido.categoria + '|' +
                str(venda.quantidade) + '|' +
                str(venda.valorTotal) + '|' +
                venda.vendedor + '|' +
                venda.comprador + '|' +
                venda.data
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt', 'r') as arq:
            cls.vendas = arq.readlines()

        cls.vendas = list(map(lambda x: x.replace('\n', ''), cls.vendas))
        cls.vendas = list(map(lambda x: x.split('|'), cls.vendas))

        venda = []

        for i in cls.vendas:
            venda.append(
                Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return venda


class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(
                produto.nome + '|' +
                str(produto.preco) + '|' +
                produto.categoria + '|' +
                str(quantidade)
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        estoque = []

        for i in cls.estoque:
            estoque.append(Estoque(Produto(i[0], i[1], i[2]), i[3]))

        return estoque


class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(
                fornecedor.nome + '|' +
                fornecedor.cnpj + '|' +
                fornecedor.telefone + '|' +
                fornecedor.categoria
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt', 'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(
            map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

        fornecedor = []

        for i in cls.fornecedor:
            fornecedor.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return fornecedor


class DaoCliente:

    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('cliente.txt', 'a') as arq:
            arq.writelines(
                f'{pessoa.nome}|'
                f'{pessoa.telefone}|'
                f'{pessoa.cpf}|'
                f'{pessoa.email}|'
                f'{pessoa.endereco}'
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('cliente.txt', 'r') as arq:
            cls.cliente = arq.readlines()

        cls.cliente = list(map(lambda x: x.replace('\n', ''), cls.cliente))
        cls.cliente = list(map(lambda x: x.split('|'), cls.cliente))

        cliente = []

        for i in cls.cliente:
            cliente.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cliente




class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.write(
                f'{funcionario.clt}|'
                f'{funcionario.nome}|'
                f'{funcionario.telefone}|'
                f'{funcionario.cpf}|'
                f'{funcionario.email}|'
                f'{funcionario.endereco}'
            )
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arq:
            cls.funcionario = arq.readlines()

        cls.funcionario = list(
            map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))

        funcionario = []

        for i in cls.funcionario:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return funcionario
