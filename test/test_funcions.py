from funcions.funcion import agregar, eliminar, editar, todos_animales
import pytest


def test_agregar():
    resultado = agregar("Leo", "Golden", "Lion")
    assert resultado is True


    