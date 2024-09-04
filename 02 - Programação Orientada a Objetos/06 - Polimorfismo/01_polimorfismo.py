class Passaro:
    def voar(self):
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")


# NOTE: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro): 
    def voar(self):
        print("Avião está decolando...")


def plano_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Avestruz()
p3 = Aviao()
plano_voo(p1)
plano_voo(p2)
plano_voo(p3)
