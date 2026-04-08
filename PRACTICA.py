from datetime import date
import csv

route = 'COMPRAS_supermercado.csv'
A)
diccionario = {}

with open(route, mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)
    
    for fila in lector_csv:
        PRSUC = fila[0]
        PRCOD = fila[1]
        PRFEC = date.fromisoformat(fila[2])
        PRPROV = fila[3]
        PRCANT = int(fila[4])
        PRPRE = float(fila[5])

        clave = (PRSUC, PRCOD)
        pesos_compra = PRCANT * PRPRE
        
        if clave not in diccionario:
            diccionario[clave] = {'unidades': 0, 'pesos': 0}
        
        diccionario[clave]['unidades'] += PRCANT
        diccionario[clave]['pesos'] += pesos_compra

print("=" * 70)
print("TOTALES POR PRODUCTO Y SUCURSAL")
print("=" * 70)
print(f"{'SUCURSAL'} {'PRODUCTO'} {'TOTUNI'} {'TOTPES'}")
print("-" * 70)

for (sucursal, producto) in sorted(diccionario.keys()):
    totuni = diccionario[(sucursal, producto)]['unidades']
    totpes = diccionario[(sucursal, producto)]['pesos']
    print(f"{sucursal} {producto} {totuni} {totpes}")

print("=" * 70)

#B)
diccionario_sucursales = {}


productos_sucursal = {}

with open(route, mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)
    
    for fila in lector_csv:
        PRSUC = fila[0]
        PRCOD = fila[1]
        PRCANT = int(fila[4])
        PRPRE = float(fila[5])
        
        pesos_compra = PRCANT * PRPRE
        
        
        if PRSUC not in diccionario_sucursales:
            diccionario_sucursales[PRSUC] = {'unidades': 0}
            productos_sucursal[PRSUC] = []
        
        
        diccionario_sucursales[PRSUC]['unidades'] += PRCANT
        
        
        productos_sucursal[PRSUC].append({
            'producto': PRCOD,
            'pesos': pesos_compra
        })

print("=" * 100)
print("INFORME DE COMPRAS POR SUCURSAL")
print("=" * 100)
print(f"{'SUCURSAL':<12} {'TOTSUC':<12} {'MYPROD':<12} {'MYIMPOR':<20} {'MNPRO':<12} {'MNIMPOR':<20}")
print("-" * 100)

for sucursal in sorted(diccionario_sucursales.keys()):
    totsuc = diccionario_sucursales[sucursal]['unidades']
    
    
    productos = productos_sucursal[sucursal]
    max_producto = max(productos, key=lambda x: x['pesos'])
    min_producto = min(productos, key=lambda x: x['pesos'])
    
    myprod = max_producto['producto']
    myimpor = max_producto['pesos']
    mnpro = min_producto['producto']
    mnimpor = min_producto['pesos']
    
    print(f"{sucursal} {totsuc} {myprod} {myimpor} {mnpro} {mnimpor}")

print("=" * 100)

# C)
cansuc = 0
totalimp = 0

with open(route, mode='r', encoding='utf-8') as archivo:
    lector_csv = csv.reader(archivo)
    next(lector_csv)
    
    sucursales_unicas = set()
    
    for fila in lector_csv:
        PRSUC = fila[0]
        PRCANT = int(fila[4])
        PRPRE = float(fila[5])
        
        sucursales_unicas.add(PRSUC)
        pesos_compra = PRCANT * PRPRE
        totalimp += pesos_compra
    
    cansuc = len(sucursales_unicas)

print("RESUMEN TOTAL")
print(f"CANSUC: {cansuc}")
print(f"TOTALIMP: {totalimp}")