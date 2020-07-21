from models import Pessoas


def insere_pessoas():
    pessoa = Pessoas(nome='Fonseca', idade=40)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    #print(pessoa.idade)
    print(pessoa)


def altera_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    pessoa.idade = 21
    pessoa.save()


def exclui_pessoas():
    pessoa = Pessoas.query.filter_by(nome='Claudio').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoas()
    #exclui_pessoas()
    #consulta_pessoas()
