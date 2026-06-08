def calcular_total(productos):
    """Calcula el total de la compra aplicando un 10% de descuento si supera los $10000."""
    if not isinstance(productos, list):
        raise ValueError("Los productos deben ser una lista")
        
    total = 0
    for p in productos:
        if "precio" not in p or "cantidad" not in p:
            raise ValueError("Producto con formato inválido")
        if p["precio"] < 0 or p["cantidad"] < 0:
            raise ValueError("El precio y la cantidad no pueden ser negativos")
        total += p["precio"] * p["cantidad"]
        
    if total > 10000:
        total *= 0.90  
    return round(total, 2)

def producto_mas_vendido(productos):
    """Devuelve el nombre del producto con mayor cantidad de unidades vendidas."""
    if not productos:
        return None
    
    mas_vendido = productos[0]
    for p in productos:
        if p["cantidad"] > mas_vendido["cantidad"]:
            mas_vendido = p
    return mas_vendido["nombre"]