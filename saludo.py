#Saludo


def saludo(name):
    print(f"Hola {name}")

def test_saludo(capfd):
    saludo("Fredy")

    out, err = capfd.readouterr()
    assert out == "Hola Fredy\n"
    
if __name__ == "__main__":
    saludo("Fredy")