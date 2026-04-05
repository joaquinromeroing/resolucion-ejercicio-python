#!/bin/env python3
import csv 

file = "COMPRAS_supermercado.csv"

with open(file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    
    data = list(reader)
    i = 0
    
    total_units_product = 0
    total_price_product = 0
    total_units_branch = 0
    total_price_branch = 0
    max_price_product = 0
    min_price_product = 999999999
    total_price = 0
    total_branch = 0
    
    while i < len(data):
        row = data[i]
        
        current_branch = row[0]
        
        print("-"*30 + f"Sucursal: {current_branch}" + "-"*30 + "\n")
        
        while i < len(data) and current_branch == row[0]:
            
            current_product = row[1]
            
            while i < len(data) and current_product == row[1]:
                row = data[i]
                
                units_product = int(row[4])
                price_product = float(row[5])
                total_units_product += units_product
                total_price_product += price_product * units_product
                
                
                i+=1
            
            print(f"Cod. Prod.: {current_product}, Total Uni.: {total_units_product}, Total precio: {total_price_product:.2f}")
            
            if total_price_product > max_price_product:
                max_product = current_product
                max_price_product = total_price_product
            
            if total_price_product < min_price_product:
                min_product = current_product
                min_price_product = total_price_product
            
            total_units_branch += total_units_product
            total_price_branch += total_price_product
            total_units_product = 0
            total_price_product = 0
        
        print(f"\nTotal Uni. de la sucursal: {total_units_branch}")
        print(f"Producto más comprado: {max_product}, Importe: {max_price_product:.2f}")
        print(f"Producto menos comprado: {min_product}, Importe: {min_price_product:.2f}\n")
        
        total_price += total_price_branch
        total_units_branch = 0
        total_price_branch = 0
        max_price_product = 0
        min_price_product = 999999999
        total_branch += 1
    
    print("-"*45)
    print(f"\nSucursales totales: {total_branch}, Compra total: {total_price:.2f}")
