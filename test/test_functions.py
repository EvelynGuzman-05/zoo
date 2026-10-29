from functions.function import add_animal, delete_animal, update_animal, all_animals
import pytest


def test_add():
    resultado = add_animal("Pepe", "Gris", "Perro")
    assert resultado is True


def  test_delete():
    add_animal("Pepe", "Gris", "Perro")
    id = all_animals()[-1]["id"]
    resultado = delete_animal(id)
    assert resultado is True

def test_update():
    add_animal("Pepe", "Gris", "Perro")
    id = all_animals()[-1]["id"]
    resultado = update_animal(id, "Pepe", "Negro", "Gato")
    assert resultado is True

def test_all_animals():
    resultado = all_animals()
    assert len(resultado) > 0