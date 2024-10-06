# 🌍 Earthquake Data Processor

This project is a simple web application built with Flask that allows users to upload CSV files containing earthquake data. The application cleans and transforms the data, saving it in JSON format, and allows users to download the resulting file.

## 🚀 Features

- **CSV File Upload**: Allows users to upload CSV files containing earthquake information.
- **Data Cleaning**: Removes rows with null values and duplicates, and renames columns for clarity.
- **JSON Conversion**: Saves the cleaned data in a JSON file that can be downloaded.
- **Automatic File Deletion**: JSON files are automatically deleted 10 seconds after being downloaded.

## 🛠️ Technologies Used

- **Flask**: A microframework for Python that allows for quick and easy web application development.
- **Pandas**: A Python library for data analysis that facilitates data manipulation and cleaning.

## 📥 Installation

1. Clone the repository:
   ``` bash
   git clone https://github.com/repo_uri.git
   cd earthquake-data-processor
   ``` 

2. Create a virtual environment (optional but recommended):
   ``` bash
   python -m venv venv
   source venv/bin/activate  # On Linux or Mac
   venv\Scripts\activate     # On Windows
   ``` 

3. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ``` 

## ⚙️ Usage

1. Run the application:
   ``` bash
   python src/main.py
   ``` 

2. Open your web browser and go to \`http://127.0.0.1:5000\`.

3. Use the interface to upload a CSV file containing earthquake data. Ensure the file has the following columns:

| **Column**                                         | **Description**                                  |
|---------------------------------------------------|--------------------------------------------------|
| FECHA - HORA (UTC)día-mes-año hora:min:seg      | Date and time of the earthquake in UTC format   |
| LATgrados                                        | Latitude of the earthquake in degrees            |
| LONgrados                                        | Longitude of the earthquake in degrees           |
| MAGexplicado abajo                               | Magnitude of the earthquake                       |
| PROFkm                                           | Depth of the earthquake in kilometers            |
| LOCALIDADhaga clic para ver mapa                 | Name of the locality of the earthquake           |

### Example CSV File

``` csv
FECHA - HORA (UTC)día-mes-año hora:min:seg,LATgrados,LONgrados,MAGexplicado abajo,PROFkm,LOCALIDADhaga clic para ver mapa
04-OCT-2024 03:24:52,70.64,-14.34,4.5,10,ISLA DE JAN MAYEN REGIÓN
04-OCT-2024 03:06:29,52.14,178.00,4.5,172,"ISLAS RATA, ALEUTIANAS"
04-OCT-2024 01:49:12,58.61,-154.72,4.3,3,ALASKA PENINSULA
``` 

4. Once the file is uploaded, the application will clean the data and provide a JSON file for download.

---

# 🌍 Procesador de Datos de Sismos

Este proyecto es una aplicación web simple construida con Flask que permite a los usuarios cargar archivos CSV que contienen datos sobre sismos. La aplicación limpia y transforma los datos, guardándolos en formato JSON, y permite a los usuarios descargar el archivo resultante.

## 🚀 Características

- **Carga de archivos CSV**: Permite a los usuarios cargar archivos CSV que contengan información sobre sismos.
- **Limpieza de datos**: Elimina filas con valores nulos y duplicados, y renombra las columnas para mayor claridad.
- **Conversión a JSON**: Guarda los datos limpios en un archivo JSON que se puede descargar.
- **Eliminación automática de archivos**: Los archivos JSON se eliminan automáticamente después de 10 segundos de haber sido descargados.

## 🛠️ Tecnologías Utilizadas

- **Flask**: Un microframework para Python que permite crear aplicaciones web de manera rápida y sencilla.
- **Pandas**: Una biblioteca de Python para el análisis de datos que facilita la manipulación y limpieza de datos.

## 📥 Instalación

1. Clona el repositorio:
   ``` bash
   git clone https://github.com/tu_usuario/earthquake-data-processor.git
   cd earthquake-data-processor
   ``` 

2. Crea un entorno virtual (opcional pero recomendado):
   ``` bash
   python -m venv venv
   source venv/bin/activate  # En Linux o Mac
   venv\Scripts\activate     # En Windows
   ``` 

3. Instala las dependencias:
   ``` bash
   pip install -r requirements.txt
   ``` 

## ⚙️ Uso

1. Ejecuta la aplicación:
   ``` bash
   python src/main.py
   ``` 

2. Abre tu navegador web y ve a \`http://127.0.0.1:5000\`.

3. Utiliza la interfaz para cargar un archivo CSV que contenga datos sobre sismos. Asegúrate de que el archivo tenga las siguientes columnas:

| **Columna**                                         | **Descripción**                                  |
|-----------------------------------------------------|--------------------------------------------------|
| FECHA - HORA (UTC)día-mes-año hora:min:seg        | Fecha y hora del sismo en formato UTC           |
| LATgrados                                          | Latitud del sismo en grados                      |
| LONgrados                                          | Longitud del sismo en grados                     |
| MAGexplicado abajo                                 | Magnitud del sismo                               |
| PROFkm                                             | Profundidad del sismo en kilómetros              |
| LOCALIDADhaga clic para ver mapa                   | Nombre de la localidad del sismo                 |

### Ejemplo de archivo CSV

``` csv
FECHA - HORA (UTC)día-mes-año hora:min:seg,LATgrados,LONgrados,MAGexplicado abajo,PROFkm,LOCALIDADhaga clic para ver mapa
04-OCT-2024 03:24:52,70.64,-14.34,4.5,10,ISLA DE JAN MAYEN REGIÓN
04-OCT-2024 03:06:29,52.14,178.00,4.5,172,"ISLAS RATA, ALEUTIANAS"
04-OCT-2024 01:49:12,58.61,-154.72,4.3,3,ALASKA PENINSULA
``` 

4. Una vez cargado el archivo, la aplicación limpiará los datos y te proporcionará un archivo JSON para descargar.

