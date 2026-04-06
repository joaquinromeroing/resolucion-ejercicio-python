import csv

CANSUC = 0
TOTALIMP = 0

datos_supermercado = {}

with open('COMPRAS_supermercado(in).csv', mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo)
    
    for fila in lector_csv:
        sucursal = fila['PRSUC']
        producto = fila['PRCOD']
        cantidad = int(fila['PRCANT'])
        precio = float(fila['PRPRE'])
        
        importe_compra = cantidad * precio
        
        if sucursal not in datos_supermercado:
            datos_supermercado[sucursal] = {}
            
        if producto not in datos_supermercado[sucursal]:
            datos_supermercado[sucursal][producto] = {'TOTUNI': 0, 'TOTPES': 0.0}
            
        datos_supermercado[sucursal][producto]['TOTUNI'] += cantidad
        datos_supermercado[sucursal][producto]['TOTPES'] += importe_compra
        
        TOTALIMP += importe_compra

CANSUC = len(datos_supermercado)

print("="*50)
print(" ESTADÍSTICAS DEL SUPERMERCADO ".center(50, "="))
print("="*50)

for sucursal, productos in datos_supermercado.items():
    print(f"\n--- SUCURSAL: {sucursal} ---")
    
    TOTSUC = 0
    MYPROD = ""
    MYIMPOR = -1.0
    MNPRO = ""
    MNIMPOR = float('inf')
    
    print("A) Detalle por Producto:")
    for producto, valores in productos.items():
        TOTUNI = valores['TOTUNI']
        TOTPES = valores['TOTPES']
        
        print(f"   Producto: {producto} | Unidades compradas: {TOTUNI} | Importe total: ${TOTPES:.2f}")
        
        TOTSUC += TOTUNI
        
        if TOTPES > MYIMPOR:
            MYIMPOR = TOTPES
            MYPROD = producto
            
        if TOTPES < MNIMPOR:
            MNIMPOR = TOTPES
            MNPRO = producto

    print("\nB) Resumen de la Sucursal:")
    print(f"   - Total unidades compradas en la sucursal (TOTSUC): {TOTSUC}")
    print(f"   - Producto de mayor compra en pesos: {MYPROD} con ${MYIMPOR:.2f}")
    print(f"   - Producto de menor compra en pesos: {MNPRO} con ${MNIMPOR:.2f}")
    print("-" * 50)

print("\n" + "="*50)
print("C) TOTALES DEL SUPERMERCADO")
print(f"   - Cantidad total de sucursales (CANSUC): {CANSUC}")
print(f"   - Compra total en pesos (TOTALIMP): ${TOTALIMP:.2f}")
print("="*50)