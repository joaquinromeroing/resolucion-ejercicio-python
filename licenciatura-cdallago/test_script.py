from script1 import actualizar_mayor_compra


def test_actualizar_mayor_compra():

    producto, importe = actualizar_mayor_compra(
        "A1",
        500,
        "B2",
        300
    )

    assert producto == "A1"
    assert importe == 500