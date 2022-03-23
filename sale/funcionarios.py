funcionarios = []


def exibir_departamentos():
    departamentos = list(set(map(lambda funcionario: funcionario['departamento'], funcionarios)))
    print('LISTA DOS DEPARTAMENTO')
    print('\n'.join(departamentos))


def transformar(linha: str):
    colunas = linha.split(',')
    funcionario = dict()
    funcionario['nome'] = colunas[0]
    funcionario['sexo'] = colunas[1]
    funcionario['salario'] = float(colunas[2])
    funcionario['departamento'] = colunas[3].rstrip('\n')
    return funcionario


def carregar_funcionarios():
    global funcionarios
    with open('funcionarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        funcionarios = list(map(transformar, linhas))


def exibir_menu():
    print('1 - Adicionar funcionário')
    print('2 - Soma do salário dos homens')
    print('3 - Soma do salário das mulheres')
    print('4 - Listar todos')
    print('5 - Total de salários por departamento')
    print('0 - Sair do programa')
    print('-' * 20)


def cadastrar_funcionario():
    funcionario = dict()
    funcionario['nome'] = input('Digite o nome: ')
    funcionario['sexo'] = input('Digite o sexo (M - Masculino, F - Feminino): ')
    funcionario['salario'] = float(input('Digite o salário: '))
    funcionario['departamento'] = input('Digite o departamento: ')
    return funcionario


def salvar_arquivo(funcionario: dict):
    with open('funcionarios.txt', 'a') as arquivo:
        arquivo.write(
            f"{funcionario['nome']},{funcionario['sexo']},{funcionario['salario']},{funcionario['departamento']}\n")


def totalizar(**parametros):
    filtrado = list(filter(lambda funcionario: funcionario[parametros['campo']] == parametros['valor'], funcionarios))
    total = sum(map(lambda funcionario: funcionario['salario'], filtrado))
    return total


def main():
    carregar_funcionarios()
    while True:
        exibir_menu()
        opcao = int(input('Escolha sua opção: '))

        if opcao == 0:
            break
        elif opcao == 1:
            funcionario = cadastrar_funcionario()
            salvar_arquivo(funcionario)
            funcionarios.append(funcionario)
        elif opcao == 2:
            total = totalizar(campo='sexo', valor='M')
            print(f'Soma do salário dos homens {total}')
        elif opcao == 3:
            total = totalizar(campo='sexo', valor='F')
            print(f'Soma do salário dos mulheres {total}')
        elif opcao == 4:
            print(', '.join(map(lambda funcionario: funcionario['nome'], funcionarios)))
        elif opcao == 5:
            exibir_departamentos()
            departamento = input('Escolha um departamento: ')
            total = totalizar(campo='departamento', valor=departamento)
            print(f'Soma do salário do departmento {departamento} {total}')
        else:
            print('Opção inválida')


main()
