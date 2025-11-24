Librería Nacional

Este proyecto implementa un sistema de consola para gestionar el inventario y registrar ventas de una librería.

Características Principales

El sistema cumple con los siguientes requisitos funcionales:

1. Gestión de Inventario
CRUD Completo: Permite 
1. Registrar 
2. Consultar 
3. Actualizar  
4. Eliminar 

Cada libro almacena: Título, Autor, Categoría, Precio y Cantidad en Stock.

Registro y Consulta de Ventas
+ Permite el registro detallado de ventas (cliente, producto, cantidad, fecha, descuento).
+ Validación de Stock: Valida automáticamente el stock antes de registrar una venta.

Actualización Automática: Reduce la cantidad en stock después de cada venta exitosa.

Módulo de Reportes 
Top Productos: Muestra el Top 3 de productos más vendidos por cantidad.
Ventas por Autor: Genera un reporte detallado de las ventas totales agrupadas por autor

Buenas Prácticas
Validaciones: Asegura que las entradas sean números positivos, formatos correctos y que se cumplan los campos.
Manejo de Excepciones: El programa maneja errores sin detenerse abruptamente, guiando al usuario de vuelta al menú.

Uso de Lambdas: Implementación de funciones lambda para cálculos agregados.

Cómo Ejecutar el Sistema?

Requisitos
* Tener instalado Python 3.x en tu sistema.
