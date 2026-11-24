# 💰 Gestor de Gastos Personales (Consola)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow?style=for-the-badge)

Aplicación de línea de comandos desarrollada en **Python** puro (sin librerías externas) que funciona como una libreta de gastos personales. Permite registrar, consultar, filtrar y analizar gastos diarios mediante un menú interactivo en consola, aplicando validación de datos y manejo de errores.

---

## ✨ Características principales

* **📝 Registro de gastos:** Guarda descripción, monto (validado como número positivo) y categoría normalizada.
* **📋 Listado ordenado:** Muestra todos los gastos registrados de forma numerada y clara.
* **🔍 Filtrado por categoría:** Permite buscar y visualizar únicamente los gastos pertenecientes a una categoría específica.
* **📊 Resumen financiero:** Calcula automáticamente el gasto total acumulado y el desglose detallado por cada categoría.
* **🛡️ Validación robusta:** Manejo de excepciones (`try/except`) para evitar cierres inesperados ante entradas inválidas.

---

## 🚀 Cómo ejecutar el proyecto

1. Asegúrate de tener **Python 3** instalado en tu computadora.
2. Clona este repositorio o descarga el archivo `.py`.
3. Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python gestor_gastos.py


=== GESTOR DE GASTOS ===
1. Registrar gasto
2. Ver todos los gastos
3. Filtrar por categoría
4. Ver resumen total
5. Salir
Elige una opción: 1
Descripción del gasto: Boleto de autobús
Monto ($): 12.50
Categoría (Comida/Transporte/Ocio/Otros): Transporte
-> Gasto registrado con éxito.


📌 Historial de Versiones
Versión 0.1: Se crea el código para que imprima y muestre el menú y los botones, y hacer que solo salgas si escribes 5.

Versión 0.2: Se hace funcionar la lista de guardado de gastos, pero aún no la muestra.

Versión 0.3: Se terminan de hacer los otros 3 botones: el de filtrado, el de ver gastos y el de ver los resultados totales.
