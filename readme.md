# 💰 Gestor de Gastos Personales (Consola)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Terminado-success?style=for-the-badge)

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
