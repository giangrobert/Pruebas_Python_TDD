#Programa que dsalida  mediante un objeto definiendo  

class ClaseHola:
    def __init__(self, name):
        self.name = name

    def hola(self):
        print(f"Hola, {self.name}")


def main():
    saludo = ClaseHola("Gian")
    saludo.hola()


if __name__ == "__main__":
    main()
