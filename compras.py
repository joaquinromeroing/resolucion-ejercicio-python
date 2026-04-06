import os
import csv 

with open('COMPRAS_supermercado.csv', 'r') as file:
   lines = file.readlines()
   lines.pop(0)
   i=0
   n=len(lines) 
    # datos[0] -> SUCURSAL
    # datos[1] -> PRODUCTO
    # datos[4] -> CANTIDAD
    # datos[5] -> PRECIO


TOTALIMP=0
CANSUC=0
while i < n:
   datos = lines[i].strip().split(',')
   suc_actual=datos[0]
   CANSUC +=1
   TOTSUC_UNI = 0
   TOTSUC_PESOS = 0
   MYPROD = ""
   MYIMPOR = -1
   MNPROD = ""
   MNIPOR = 999999

   while i < n and lines[i].strip().split(',')[0] == suc_actual:
         datos = lines[i].strip().split(',') 
         prod_actual=datos[1]

         TOTUNI=0
         TOTPES=0

         while i<n and lines[i].strip().split(',')[0] == suc_actual \
          and lines[i].strip().split(',')[1] == prod_actual:
             datos = lines[i].strip().split(',')
             cant = int(datos[4])
             precio = float(datos[5])
             importe = cant * precio

             TOTUNI += cant
             TOTPES += importe

             i +=1
         print(f"Sucursal: {suc_actual} | Producto: {prod_actual} | Cantidad: {TOTUNI} | Total: ${TOTPES:.2f}")    
         
         TOTSUC_UNI += TOTUNI
         TOTSUC_PESOS += TOTPES

         if TOTPES > MYIMPOR:
             MYIMPOR = TOTPES
             MYPROD = prod_actual

         if TOTPES < MNIPOR:
            MNIPOR = TOTPES
            MNPROD = prod_actual     

         print("-" * 50)
         print(f"INFORME SUCURSAL {suc_actual}:")
         print(f"Total Unidades Vendidas: {TOTSUC_UNI}")
         print(f"Producto Mayor Compra: {MYPROD} (${MYIMPOR:.2f})")
         print(f"Producto Menor Compra: {MNPROD} (${MNIPOR:.2f})")
         print("-" * 50)        
         
         TOTALIMP += TOTSUC_PESOS
print("=" * 50)
print("ESTADÍSTICA GENERAL DEL SUPERMERCADO")
print(f"Total de Sucursales procesadas: {CANSUC}")
print(f"Importe Total General: ${TOTALIMP:.2f}")
print("=" * 50)         