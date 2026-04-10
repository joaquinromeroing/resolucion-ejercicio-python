import csv

def procesar():
    path = "COMPRAS_desordenado.csv"
    try:
        with open(path, mode='r', encoding='utf-8') as f:
            lector = csv.reader(f)
            cabecera = next(lector)
            datos = list(lector)
        
        datos.sort(key=lambda x: x[0])
        
        idx = 0
        total_general = 0
        
        while idx < len(datos):
            sucursal_actual = datos[idx][0]
            total_sucursal = 0
            print(f"\nSUCURSAL: {sucursal_actual}")
            
            while idx < len(datos) and datos[idx][0] == sucursal_actual:
                unidades = int(datos[idx][4])
                precio = float(datos[idx][5])
                total_sucursal += unidades * precio
                idx += 1
                
            print(f"Total Sucursal: ${round(total_sucursal, 2)}")
            total_general += total_sucursal
            
        print(f"\nTOTAL GENERAL: ${round(total_general, 2)}")
        
    except:
        pass

if __name__ == "__main__":
    procesar()
