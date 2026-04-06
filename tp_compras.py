import csv



def leer_registro(archivo):
    try:
        reg = next(archivo)  
        reg["PRCANT"] = int(reg["PRCANT"])      
        reg["PRPRE"] = float(reg["PRPRE"])      
        return reg
    except StopIteration:
        return None   

# Abro el archivo csv
with open("COMPRAS_supermercado.csv", newline="", encoding="utf-8") as f:
    archivo = csv.DictReader(f)   

    reg = leer_registro(archivo)  

    
    cantsucursales = 0      # cantidad total de sucursales
    totalimporte = 0    # importe total en pesos de todas las sucursales

    # Mientras haya registros para procesar
    while reg is not None:
        sucursal_actual = reg["PRSUC"]   # guardo la sucursal actual
        totsucursal = 0                  # total de unidades de esta sucursal
        mayor_inicializado = False       # sirve para inicializar maximo y minimo

        print(f"\nSUCURSAL: {sucursal_actual}")

        # Mientras siga siendo la misma sucursal
        while reg is not None and reg["PRSUC"] == sucursal_actual:
            producto_actual = reg["PRCOD"]   # guardo el producto actual
            totunidades= 0                       # total de unidades del producto
            totpesos = 0                       # total en pesos del producto

            # Mientras siga siendo la misma sucursal y el mismo producto
            while reg is not None and reg["PRSUC"] == sucursal_actual and reg["PRCOD"] == producto_actual:
                importe = reg["PRCANT"] * reg["PRPRE"]   # importe de esa compra

                # Acumulo para el producto
                totunidades += reg["PRCANT"]
                totpesos += importe

                # Leo el siguiente registro
                reg = leer_registro(archivo)

            # Cuando termina el producto, lo informo
            print(f"  PRODUCTO: {producto_actual} | TOTUNI: {totunidades} | TOTPES: ${totpesos:.2f}")

            # Acumulo al total de la sucursal
            totsucursal += totunidades

            # Acumulo al total general en pesos
            totalimporte += totpesos

            # Inicializo maximo y minimo con el primer producto de la sucursal
            if mayor_inicializado == False:
                mayor_prod = producto_actual
                mayor_importe = totpesos
                menor_prod = producto_actual
                menor_importe = totpesos
                mayor_inicializado = True
            else:
                # Comparo para ver si este producto pasa a ser el de mayor compra
                if totpesos > mayor_importe:
                    mayor_prod = producto_actual
                    mayor_importe = totpesos

                # Comparo para ver si este producto pasa a ser el de menor compra
                if totpesos < menor_importe:
                    menor_prod = producto_actual
                    menor_importe = totpesos

        # Cuando termina la sucursal, muestro sus resultados
        print(f"TOTAL UNIDADES SUCURSAL: {totsucursal}")
        print(f"MAYOR COMPRA: {mayor_prod} -> ${mayor_importe:.2f}")
        print(f"MENOR COMPRA: {menor_prod} -> ${menor_importe:.2f}")

        # Cuento una sucursal mas
        cantsucursales += 1

    # Cuando termina todo el archivo, muestro los totales generales
    print("\n--- TOTALES GENERALES ---")
    print(f"CANTIDAD DE SUCURSALES: {cantsucursales}")
    print(f"TOTAL EN PESOS: ${totalimporte:.2f}")