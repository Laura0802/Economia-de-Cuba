# Análisis de la Economía Cubana 
## Subtema: La Vida de un Graduado

---
Este proyecto nació de una inquietud: Comprobar con datos si el sueldo con el que un joven profesional empieza su vida en La Habana le alcanza para lo indispensable: alimentación e higiene. No es una teoría, es la realidad cotidiana.

### Tabla de Contenidos:

1. Introducción

2. Objetivos del Proyecto

3. Fuentes de Datos

4. Estructura del Análisis

5. Resultados Obtenidos

6. Conclusiones

7. ¿Cómo ejecutar el proyecto?

8. Notas Finales
---

### 1. Introducción
Este estudio analiza la relación cuantitativa entre el salario inicial promedio de profesionales en La Habana y el costo real de los productos básicos de alimentación e higiene disponibles en el mercado minorista durante el período 2020-2025. A partir de datos recopilados sobre precios, salarios y tasas de cambio, el proyecto evalúa de forma concreta cuánto puede adquirir un recién graduado con su ingreso mensual en las mipymes, identificando brechas y patrones en la capacidad adquisitiva y ofreciendo una visualización referencial del impacto económico en su vida diaria.

---
### 2. Objetivos del Proyecto

#### 2.1 Objetivo Principal:
Demostrar cómo los precios de los productos básicos en mipymes impactan la vida económica de un recién graduado en La Habana y elaborar una guía visual que ilustre su capacidad adquisitiva actual y potencial.



##### 2.2 Objetivos Secundarios:
* Cuantificar el impacto de los precios de alimentos y productos de higiene en el presupuesto mensual de un egresado.

* Crear una herramienta visual clara que muestre qué puede adquirir con su salario actual en el mercado minorista.

* Visualizar la frecuencia y disponibilidad de productos esenciales en las mipymes, destacando aquellos de más difícil acceso.

* Analizar la mejor manera de obtener los productos de primera necesidad utilizando distintas vías de pago

---
### 3. Fuentes de Datos
Para fundamentar el análisis, este estudio integró varios tipos de evidencia:
* Los precios recolectados en más de 30 establecimientos locales (mipymes)
* Tiendas que operan en divisa
* Datos y referenciales publicados por:
  * [Estipendio Estudiantil](https://noticias.upr.edu.cu/2020/12/resolucion-no-108-20-de-la-educacion-superior-que-implementa-la-tarea-ordenamiento-sobre-otorgamiento-del-estipendio-prestamos-pago-como-alumno-ayudante-y-practica-laboral-a-los-estudiantes/) 
  * ONEI [Link1](https://www.onei.gob.cu/sites/default/files/datos-estadisticos/2023-10/7.4-salario-medio-mensual-en-las-entidades-estatales-y-mixtas-por-clase-de-actividad-economica.xls), [Link2](https://www.onei.gob.cu/aep-la-habana-2023)
  * [Gaceta Oficial](https://www.gacetaoficial.gob.cu/sites/default/files/goc-2020-ex69.pdf)
  * [ElToque](https://eltoque.com/tasas-de-cambio-de-moneda-en-cuba-hoy#informal-diaria-1)

---
### 4. Estructura del Análisis

#### 4.1 Estructura de los JSON:
###### 4.1.1 Archivo `Mipymes.json`:

Este archivo contiene el registro estructurado de las MiPymes visitadas durante el estudio. Incluye la información de cada establecimiento y el listado completo de productos comercializados, con sus respectivos precios y datos como categoría, unidad de medida y marca.

Su propósito es servir como fuente primaria para el análisis de precios, permitiendo calcular valores promedio, estudiar la variación entre tiendas y establecer comparaciones objetivas dentro del mercado minorista analizado.
La estructura se puede observar en `Template.json`
````
{
  "Mipymes": [
    {
      "Places": {
        "id": str,
        "Name": str,
        "Date": str,
        "Municipality": str,
        "Location": {
          "Latitud": float,
          "Longitud": float
        },
        "Products": [
          {
            "Producto": {
              "Brand": str,
              "Cuantity": str,
              "Weight": float,
              "Price": float
            }
          }
        ]
      }
    }
  ]
}
````

###### 4.1.2 Archivo `Estipendios.json`:

Contiene los montos actuales de estipendios estudiantiles universitarias. Sirve como referencia de ingresos durante la etapa de formación para contrastarlos con el salario profesional posterior.
````
{
  "Student_Stipend": [
    {
      "Academic_Year": str,
      "Quantity": float,
      "Teaching_Aids": float
    }
  ]
}
````    

###### 4.1.3 Archivo `Tasa_Cambio.json`:

Contiene los datos diarios de tasas de cambio informales recopilados del portal El Toque durante 30 días consecutivos. Este registro permite analizar la variación y el valor promedio de la tasa de cambio en el mercado paralelo durante el período de estudio.
````
{
  "Tasa_de_Cambio": [
    {
      "Day": {
        "id": int,
        "Date": str,
        "EUR": float,
        "USD": float,
        "MLC": float
      }
    }
  ]
}    
````    

###### 4.1.4 Archivo `Tiendas_Dolares.json`:

Contiene el registro de tiendas en La Habana que comercian exclusivamente en dólares (USD), con información sobre productos, precios y ubicaciones. Permite analizar el mercado en divisas y compararlo con el mercado en pesos cubanos (CUP).
````
{
  "Dolares": [
    {
      "Places": {
        "id": str,
        "Name": str,
        "Date": str,
        "Curancy": str,
        "Municipality": str,
        "Location": {
          "Latitud": float,
          "Longitud": float
        },
        "Products": [
          {
            "Producto": {
              "Brand": str,
              "Cuantity": str,
              "Weight": float,
              "Price": float
            }
          }
        ]
      }
    }
  ]
}
````

###### 4.1.5 Archivo `Distribución_sector_salario.json`:

Contiene los datos de distribución salarial organizados por sectores económicos y categorías laborales en Cuba. Permite analizar las diferencias de ingresos según la actividad profesional y ubicar el salario de entrada promedio de un egresado dentro del panorama laboral general.
````
{
  "Money": [
    {
      "Activity": str,
      "Amount": int
    }
  ]
}
````    

###### 4.1.6 Archivo `Salarios.json`:

Contiene la serie histórica de los salarios promedio mensuales en Cuba desde 2018 hasta 2024, desglosada por año. Este archivo permite observar la evolución nominal de los ingresos en el período analizado.
````
{
  "Salary": [
    {
      "Date": str,
      "Amount": float
    }
  ]
}
````    

###### 4.1.7 Archivo `Productos.json`:

Contiene los precios promedio calculados para cada producto básico en el mercado minorista, junto con la cantidad disponible y la frecuencia de aparición en las MiPymes analizadas. Permite un acceso rápido a los valores de referencia del estudio.
````
{
  "Productos": [
    {
      "Nombre": str,
      "Quantity": float
    }
  ]
}
````    

#### 4.2 Estructura de la Biblioteca Utilizada:
###### 4.2.1 Archivo `WeLoveYudivian.py`:

Organiza en funciones específicas todo el código necesario para el procesamiento, limpieza, transformación y visualización de los datos. Centraliza la lógica del análisis, asegurando consistencia y reutilización en cada etapa del proyecto. 

##### 4.3 Estructura del Notebook:

4.3.1 Archivo `Economia_en_Cuba.ipnub`:

Consolida todo el análisis en un solo lugar: incluye las visualizaciones generadas, desarrolla la narrativa (storytelling) paso a paso y presenta los hallazgos clave del proyecto.

---

### 5. Resultados Obtenidos

* Existe una variación significativa de precios para un mismo producto entre diferentes Mipymes y municipios.

* El salario promedio no cubre la totalidad de los productos básicos requeridos mensualmente, sin considerar otros gastos esenciales como servicios, transporte o comunicaciones.

* Varios productos básicos requieren uno o más días de salario para su adquisición, destacándose el arroz, pollo y aceite, lo que limita la compra simultánea de múltiples artículos.

* El acceso a divisas presenta resultados variables según el producto, ya que considerando las tasas de cambio, algunos artículos resultan más accesibles en moneda nacional mientras otros en divisas.

* La evolución salarial reciente muestra que los aumentos nominales han sido compensados por el incremento en los precios, manteniendo una capacidad de compra similar a periodos anteriores.


---
### 6. Conclusiones

El salario inicial de un egresado universitario frecuentemente resulta insuficiente para cubrir el costo completo de los alimentos básicos del hogar. Esta brecha se complica aún más en entornos donde conviven precios en moneda local y en dólares, ya que la persona debe realizar cálculos constantes de tipo de cambio y priorización para decidir dónde, cuánto y cómo realizar sus compras, lo que limita significativamente su capacidad de planificación y autonomía financiera.

---

### 7. ¿Cómo ejecutar el proyecto?

#### 7.1 Requisitos
* Jupyter
* Python 3
* Matplotlib
* Numpy
* Folium

#### 7.2 Pasos:
1. Abrir el archivo `Economia_en_Cuba.ipyub`
2. Ejecutar las celdas

---


### 8. Notas Finales

Agradezco profundamente su interés y tiempo dedicado a la revisión de este proyecto de análisis. Su atención es muy valiosa para el trabajo presentado.