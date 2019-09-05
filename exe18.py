#18 - Crie uma classe animal com o método comer, este método deve  escrever na tela "o animal esta comendo".
#Depois disso crie as classes cachorro, cavalo e gato e implemente o método comer de acordo com o
#que cada animal come. Crie uma classe AnimalTeste e coloque os três animais dentro de uma lista de
#animais e chame o método comer polimorficamente (com um for)

class Animal():
    def comer(self):
        print("O animal está comendo")

class Cachorro(Animal):

    def comer(self):
        print("O DOG está comendo ração")

class Cavalo(Animal):

    pass

class Gato(Animal):
    def comer(self):
        print("O gato está comendo ração")

class TesteAnimal():
    #Intanciando meu cachorro (agora ele é um objeto)
    cachorro = Cachorro()
    cavalo = Cavalo()
    gato = Gato()


    lista = []
    lista.append(cachorro)#Adicionando elementos na minha lista
    lista.append(cavalo)
    lista.append(gato)

    for i in lista: #No elemento i da minha lista eu chamo comer poliformicamente lá da classe pai
        i.comer()

