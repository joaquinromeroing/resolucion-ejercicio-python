from supermercado import ordenar_archivo_si_es_necesario


def test_si_el_archivo_ya_esta_ordenado_devuelve_mismo_path():
    # Arrange
    path = "compras.csv"
    ordenado = "Y"

    # Act
    resultado = ordenar_archivo_si_es_necesario(path, ordenado)

    # Assert
    assert resultado == path


def test_si_el_archivo_no_esta_ordenado_crea_archivo_ordenado(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.chdir(tmp_path)

    archivo_prueba = tmp_path / "compras.csv"

    archivo_prueba.write_text(
        "sucursal,producto,fecha,categoria,cantidad,precio\n"
        "3,Pan,2024-01-01,Alimentos,2,100\n"
        "1,Leche,2024-01-01,Lacteos,1,200\n"
        "2,Arroz,2024-01-01,Alimentos,3,50\n"
    )

    # Act
    resultado = ordenar_archivo_si_es_necesario(str(archivo_prueba), "N")

    # Assert
    assert resultado == "archivo_ordenado_temp.csv"

    contenido = (tmp_path / resultado).read_text()

    assert contenido == (
        "sucursal,producto,fecha,categoria,cantidad,precio\n"
        "1,Leche,2024-01-01,Lacteos,1,200\n"
        "2,Arroz,2024-01-01,Alimentos,3,50\n"
        "3,Pan,2024-01-01,Alimentos,2,100\n"
    )


def test_funciona_con_n_minuscula(tmp_path, monkeypatch):
    # Arrange
    monkeypatch.chdir(tmp_path)

    archivo_prueba = tmp_path / "compras.csv"

    archivo_prueba.write_text(
        "sucursal,producto,fecha,categoria,cantidad,precio\n"
        "2,Arroz,2024-01-01,Alimentos,3,50\n"
        "1,Leche,2024-01-01,Lacteos,1,200\n"
    )

    # Act
    resultado = ordenar_archivo_si_es_necesario(str(archivo_prueba), "n")

    # Assert
    contenido = (tmp_path / resultado).read_text()

    assert contenido == (
        "sucursal,producto,fecha,categoria,cantidad,precio\n"
        "1,Leche,2024-01-01,Lacteos,1,200\n"
        "2,Arroz,2024-01-01,Alimentos,3,50\n"
    )
