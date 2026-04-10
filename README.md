# 🛒 Estadísticas de Compras — Supermercado
### Computación I - Universidad Austral
**Estudiante:** Bernardo Di Rienzo

---

## 📋 Descripción del problema
Este proyecto analiza el archivo `COMPRAS_supermercado.csv` con las compras realizadas en las distintas sucursales del supermercado durante un período de tiempo. El objetivo es procesar la información para obtener métricas de ventas por sucursal y producto.

---

## 🧮 Estructura del archivo CSV
El programa procesa los datos basados en los siguientes campos técnicos:

| Campo | Descripción |
|-------|-------------|
| **PRSUC** | Código de sucursal |
| **PRCOD** | Código de producto |
| **PRFEC** | Fecha de compra |
| **PRPROV** | Proveedor |
| **PRCANT** | Cantidad comprada |
| **PRPRE** | Precio unitario |

---

## 📂 Estructura del Proyecto
* **app/**: Contiene el script principal de ejecución (`principal.py`).
* **data/**: Carpeta con los archivos de datos (`.csv`).
* **src/**: Scripts auxiliares de desarrollo.

---

## 🛠️ Funcionalidades Principales

### 1. Algoritmo de Ordenamiento (Burbuja)
Se incluye una implementación propia del **Algoritmo de Burbuja (Bubble Sort)** para diccionarios. Esta función ordena los registros por código de sucursal (`PRSUC`) para permitir el correcto funcionamiento de los cortes de control. 
* **Nota:** No se utilizaron funciones nativas como `.sort()` o `sorted()` siguiendo los requerimientos de la cátedra.

### 2. Menú Interactivo
El script cuenta con una interfaz de consola que solicita:
* El **path** del archivo CSV.
* El **estado** de orden del archivo (Y/N).
En caso de no estar ordenado, el sistema genera un archivo **temporal** (`temp_ordenado.csv`) y comienza la ejecución desde allí.

---

## 🚀 Instrucciones de Ejecución

Para ejecutar el proyecto en macOS:

1. **Abrir la terminal** en la carpeta raíz del proyecto.
2. **Ejecutar el script principal:**

   ```bash
   python3 app/principal.py
