import hola as h

def test_main(capsys):
    h.main()
    expected_out = "Hola, Gian\n"
    captured = capsys.readouterr()
    assert captured.out == expected_out