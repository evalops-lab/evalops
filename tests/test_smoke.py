from typing import Any

from evalops import main  # importe la fonction à tester depuis notre package


def test_main_prints_hello(capsys: Any) -> None:
    # pytest lance automatiquement toute fonction dont le nom commence par "test_".
    # "capsys" est un outil fourni par pytest qui capture ce que le code affiche avec print().
    main()  # on appelle la fonction
    assert "Hello" in capsys.readouterr().out  # on vérifie que l'affichage contient "Hello"
    # "assert X" = "X doit être vrai, sinon le test échoue"
