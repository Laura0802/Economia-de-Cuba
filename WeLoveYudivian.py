import json
import matplotlib.pyplot as plt
import numpy as np
"""-----------------------------------------------------------------------------------------------------------------"""
def abrir():
    with open("Estipendios.json", "r", encoding="utf-8") as h:
        estipendios = json.load(h)
    return estipendios
    # Abrir el json de Estipendios estudiantiles
estipendios = abrir()

"""-----------------------------------------------------------------------------------------------------------------"""
def abrirjson():
    with open("Tasa_Cambio.json", "r", encoding="utf-8") as g:
        info = json.load(g)

    return info
    #Abrir el json de Tasa de Cambio del toque
infor = abrirjson()

"""-----------------------------------------------------------------------------------------------------------------"""
def openjson():
   with open("Mipymes.json", "r", encoding="utf-8") as f:
        datas = json.load(f)

   return datas
   # Abrir el json de las Mipymes
data = openjson()

"""-----------------------------------------------------------------------------------------------------------------"""
def opentiendas():
     with open("Tiendas_Dolares.json", "r", encoding="utf-8") as l:
         usd = json.load(l)

     return usd
     #Abrir el json de las tiendas en dolares
usd = opentiendas()

"""-----------------------------------------------------------------------------------------------------------------"""

def opensalario_dis():
    with open("Distribución_sector_salario.json", "r", encoding="utf-8") as d:
        salario_distribucion = json.load(d)

    return salario_distribucion
    # Abrir el json de distribucion por sector del los salarios en 2022

salario_distribucion = opensalario_dis()

"""-----------------------------------------------------------------------------------------------------------------"""
def opensalary():
    with open("Salarios.json", "r", encoding="utf-8") as y:
        salary = json.load(y)

    return salary
    #Abrir el json de los salarios en Cuba
salary = opensalary()

"""-----------------------------------------------------------------------------------------------------------------"""
def workers():
    with open("Trabajadores.json", "r", encoding="utf-8") as y:
        trabajadores = json.load(y)

    return trabajadores
    #Abrir el json de la cantidad de trabajadores en La Habana
trabajadores = workers()

"""-----------------------------------------------------------------------------------------------------------------"""
def openprod():
    with open("Productos.json", "r", encoding="utf-8") as p:
        products = json.load(p)

    return products
    #Abrir el json de los salarios en Cuba
products = openprod()

"""-----------------------------------------------------------------------------------------------------------------"""
# Agrega elementos a una lista
def ele_list(p, q):
  b = []
  for i in estipendios.get(p):
     a = i[q]
     b.append(a)
  return b

"""-------------------------------------------------------------------------------------"""
#Sumar elementos
def sumador(num1):
    sum = 0
    for i in num1:
        sum += i
    return sum

"""-------------------------------------------------------------------------------------"""
#Hallar promedio de estipendio
def average1():
    return sumador(ele_list("Student_Stipend", "Quantity")) / len(ele_list("Student_Stipend", "Quantity"))

"""-------------------------------------------------------------------------------------"""
#Hallar promedio
def average(k, p):
    return sumador(k, p) / len(k,p)

"""-------------------------------------------------------------------------------------"""
#Hallar la cantidad de productos
def promedio_prod(abcd):
    l = []
    for mipyme in data["Mipymes"]:
        productos = mipyme["Places"]["Products"]
        for producto in productos:
            if abcd in producto:
                ele = producto[abcd]
                l.append(ele)
    return len(l)

"""-------------------------------------------------------------------------------------"""
#Distribucion de productos
def distri_prod():
    n = []
    q = []
    for i in products.get("Productos"):
        n.append(i["Nombre"])
        q.append(i["Quantity"])
    return n, q


"""-------------------------------------------------------------------------------------"""
#Hallar promedio de precio de productos
def promedio_pri(abc):
    m = []
    for mipyme in data["Mipymes"]:
        productos = mipyme["Places"]["Products"]
        for producto in productos:
            if abc in producto:
                el = producto[abc]["Price"]
                m.append(el)

    if m:
        return round(sum(m) / len(m), 0)
    else:
        return 0

"""-------------------------------------------------------------------------------------"""
# Crear series
def serie():
    m = []
    n = []
    k = []
    for i in trabajadores.get("Work"):
       m.append(i["Year"])
       n.append(i["Women"])
       k.append(i["Men"])
    return m, n, k

"""-------------------------------------------------------------------------------------"""
#Leer json de trabajadores
def work(w):
    lista = []
    for i in trabajadores.get("Work"):
        lista.append(i[w])
    return lista

"""-------------------------------------------------------------------------------------"""
#Grafica de distribucion de trabajadores
def graf_distribucion_trabajo():
   years = work("Year")
   valores1 = work("Women")
   valores2 = work("Men")
   grosor = 0.5
   fig, ax = plt.subplots()

# Gráfico de barras apiladas
   ax.bar(years, valores1, width=grosor, color="#FF1493", edgecolor="#FFFFFF", linewidth=2, label="Mujeres")
   ax.bar(years, valores2, width=grosor, color="#00BFFF", edgecolor="#FFFFFF", linewidth=2, bottom=valores1,
       label="Hombres")

   ax.set_facecolor('#FFFFFF')

   for bar in ax.patches:
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2 + bar.get_y(),
            round(bar.get_height()), ha='center',
            color='w', weight='bold', size=10)


    total_values = np.add(valores1, valores2)

# Etiquetas con el total
    for i, total in enumerate(total_values):
       ax.text(i, total + 0.5, round(total),
            ha='center', weight='bold', color='black')

   ax.legend(loc='upper right')
   ax.set_title("Distribución de trabajadores por sexo, en el rango de edad de 20-29 años ")
   ax.set_xlabel('Años')
   ax.set_ylabel('Miles de trabajadores ')

   plt.show()

"""-------------------------------------------------------------------------------------"""
#Hallar las cantidades de los salarios
def quantity_salary():
    y = []
    for i in salario_distribucion.get("Money"):
        y.append(i["Amount"])
    return y

#Hallar promedio de salario con la funcion anterior
def promedio_salario(deb):
    for i in deb:
        return sumador(deb) / len(deb)

"""-------------------------------------------------------------------------------------"""
#Salario por dia
def salario_dia():
    if promedio_salario(quantity_salary()) == 0:
       return 0
    else:
       return promedio_salario(quantity_salary()) // 30

"""-------------------------------------------------------------------------------------"""
#Salario por semana
def salario_semana():
    if promedio_salario(quantity_salary()) == 0:
        return 0
    else:
        return promedio_salario(quantity_salary()) // 4

"""-------------------------------------------------------------------------------------"""
#Hallar promedio de productos en tiendas de dolares
def dolar(usa):
    u = []
    for tiendas in usd["Dolares"]:
        productos = tiendas["Places"]["Products"]
        for producto in productos:
            u.append(producto)
    return len(u)

"""-------------------------------------------------------------------------------------"""
def estipendio():
    m = []
    n= []
    for i in estipendios.get("Student_Stipend"):
       m.append(i["Academic_Year"])
       n.append(i["Quantity"])
    return m, n

"""-------------------------------------------------------------------------------------"""
# Estipendio estudiantil en relación con el año académico
import matplotlib.pyplot as plt

def estipendio_estudiantil():
   x = (estipendio()[0])
   y = (estipendio()[1])

   fig, ax = plt.subplots()
   ax.bar(x=x, height=y, width=0.6, color="#FF69B4", edgecolor="w")
   plt.title('Estipendio estudiantil en relación con el año académico', style="italic")
   ax.set_xlabel('Año')
   ax.set_ylabel('Cantidad de dinero')
   plt.xticks(rotation=45)
   plt.show()

"""-------------------------------------------------------------------------------------"""
#Sector y promedio de salarios en 2022
def sector_salary():
    m = []
    n= []
    for i in salario_distribucion.get("Money"):
       m.append(i["Activity"])
       n.append(i["Amount"])
    return m, n

"""-------------------------------------------------------------------------------------"""
#Grafica de sector y su salario
import numpy as np
import matplotlib.pyplot as plt

def graf_sector_salary():

   xpoints = np.array(sector_salary()[1])
   ypoints = np.array(sector_salary()[0])

   plt.figure(figsize=(14, 10))
   plt.plot(ypoints, xpoints, color='#FF00FF', linewidth=5, marker='*', markerfacecolor='#FF00FF', markersize=14)
   plt.yticks(fontsize=14)
   plt.xticks(rotation=45, ha='right', fontsize=12)
   plt.xlabel('Actividad económica', fontsize=16)
   plt.ylabel('Salario mensual ($)', fontsize=16)
   plt.title('Distribución por sector y su salario en 2023', fontsize=20)
   plt.grid(True, alpha=0.3)
   plt.tight_layout()

   plt.show()

"""-------------------------------------------------------------------------------------"""
#Grafica de la evolucion de las tasas de cambio del mercado informal
import numpy as np
import matplotlib.pyplot as plt

def tasa_cambio():
    tas = []
    cam = []
    bio = []
    for i in infor.get("Tasa_de_Cambio"):
        europe = i["Day"]["EUR"]
        america = i["Day"]["USD"]
        centro = i["Day"]["MLC"]
        tas.append(europe)
        cam.append(america)
        bio.append(centro)
    x = np.arange(30)
    y = np.vstack([tas, cam, bio])
    cols = ['#C71585', '#DB7093', '#FFC0CB']
    fig, ax = plt.subplots()
    ax.stackplot(x, y, labels=["EUR", "USD", "MLC"], colors=cols)
    plt.title('Tasa de cambio en el mercado informal durante 30 dias (21-10-2025 - 21-11-2025)', style="italic")
    ax.set_xlabel('Dias')
    ax.set_ylabel('Cambio')
    ax.legend(loc='upper left')
    ax.stackplot(x, y, colors=cols)
    plt.show()

"""-------------------------------------------------------------------------------------"""
#Grafica de tasa de cambio y productos de primera necesidad
def graf_tasa_product():
    productos = ['Aceite', 'Pechuga', 'Arroz', 'Huevos', 'Cafe']
    precio_cup = [promedio_pri("Aceite"), promedio_pri("Pollo_Pechuga"), promedio_pri("Arroz"), promedio_pri("Huevos"),
              promedio_pri("Cafe")]
    tasa_informal = 435.0
    tasa_oficial = 24.0

    precio_cup_informal = [m // tasa_informal for m in precio_cup]
    precio_cup_formal = [f // tasa_oficial for f in precio_cup]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Gráfico mercado formal
    ax1.bar(productos, precio_cup_formal, color='#EE82EE')
    ax1.set_title(f'Precios con tasa de cambio formal (Tasa: {tasa_oficial})\n Fecha: 19-11-2025')
    ax1.set_ylabel('Precio en USD')
    ax1.tick_params(axis='x', rotation=45)

   # Gráfico mercado informal
    ax2.bar(productos, precio_cup_informal, color='#DDA0DD')
    ax2.set_title(f'Precios con tasa de cambio informal (Tasa: {tasa_informal})\n Fecha: 19-11-2025')
    ax2.set_ylabel('Precio en USD')
    ax2.tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

"""-------------------------------------------------------------------------------------"""
#Evolucion del promedio de salarios
def evolucion_salario():
    e = []
    s = []
    for i in salary.get("Salary"):
        e.append(i["Date"])
        s.append(i["Amount"])
    return e, s

"""-------------------------------------------------------------------------------------"""
#Grafica de evolucion de los salarios
import numpy as np
import matplotlib.pyplot as plt


def graf_salario():
    xpoints = np.array(evolucion_salario()[1])
    ypoints = np.array(evolucion_salario()[0])


    plt.figure(figsize=(10, 6))
    plt.plot(ypoints, xpoints, color='#e377c2', linewidth=5, marker='*', markersize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.xlabel('Salario mensual ($)', fontsize=16)
    plt.ylabel('Año', fontsize=16)
    plt.title('Evolución de salarios del 2018- 2023', fontsize=20)
    plt.tight_layout()

    plt.show()

"""-------------------------------------------------------------------------------------"""
import folium
from folium.map import Icon

map = folium.Map(location=(23.1136, -82.3666), tiles = "cartodb positron", zoom_start=12)
map.save('Mapa_Habana.html')
contenido_id_1 = "<h2>Neptuno entre Aramburu y Soledad</h2> <br/> <b>Direccion:</b> Neptuno entre Aramburu y Soledad <br/"
contenido_id_2 = "<h2>Belascuain entre Neptuno y San Miguel</h2> <br/> <b>Dirección:</b>Belascuain entre Neptuno y San Miguel<br/"
contenido_id_3 ="<h2>Infanta esquina Neptuno</h2> <br/> <b>Dirección:</b>Infanta esquina Neptuno<br/"
contenido_id_4 ="<h2>La Casita</h2> <br/> <b>Dirección:</b>San lazaro entre Aramburu e Hospital<br/"
contenido_id_5 ="<h2>La Farola</h2> <br/> <b>Dirección:</b>San Lazaro entre Aramburu e Hospital<br/"
contenido_id_6 ="<h2>San Rafael entre Marquez Gonzalez y Lucena</h2> <br/> <b>Dirección:</b>San Rafael entre Marquez Gonzalez y Lucena<br/"
contenido_id_7 ="<h2>Santys</h2> <br/> <b>Dirección:</b>San Rafael entre Marques Gonzalez y Lucena<br/"
contenido_id_8 ="<h2>Stella Artois</h2> <br/> <b>Dirección:</b>San Rafael entre Aramburu y Soledad <br/"
contenido_id_9 ="<h2>Bodeguita</h2> <br/> <b>Dirección:</b>Calle F entre 26 y Cuba<br/"
contenido_id_10 ="<h2>Kalifa</h2> <br/> <b>Dirección:</b>Calle Real entre More y Marcos <br/"
contenido_id_11 ="<h2>La Pampa</h2> <br/> <b>Dirección:</b>Paseo Panamericano entre 5taA y 5taC<br/"
contenido_id_12 ="<h2>Merk2 Marino</h2> <br/> <b>Dirección:</b>Avenida 7ma entre Calle 46 y 7maA<br/"
contenido_id_13 ="<h2>23 entre J e I</h2> <br/> <b>Dirección:</b>23 entre J e I<br/"
contenido_id_14 ="<h2>Gran Pizzero</h2> <br/> <b>Dirección:</b>Calle J entre 25 y 27 <br/"
contenido_id_15 ="<h2>La Nenita</h2> <br/> <b>Dirección:</b>Calle 17 entre M y L<br/"
contenido_id_16 ="<h2>Que Cookie!</h2> <br/> <b>Dirección:</b>Calle N entre 23 y 25<br/"
contenido_id_17 ="<h2>La Patron Cita</h2> <br/> <b>Dirección:</b>Carretera de Berroa<br/"
contenido_id_18 ="<h2>El Tren de Playa</h2> <br/> <b>Dirección:</b>Calle 42 entre 19 y 21<br/"
contenido_id_19 ="<h2>Es Aqui</h2> <br/> <b>Dirección:</b>Calle 5ta entre J e I<br/"
contenido_id_20 ="<h2>27 entre N y O</h2> <br/> <b>Dirección:</b>27 entre N y O<br/"
contenido_id_21 ="<h2>Bodegon D'K</h2> <br/> <b>Dirección:</b>San Martin 235 <br/"
contenido_id_22 ="<h2>Bodegon Las Duras</h2> <br/> <b>Dirección:</b>Calle 23 entre 24 y 26<br/"
contenido_id_23 ="<h2>Mercadito Hakuna Matata</h2> <br/> <b>Dirección:</b>Cuchiillo de Avenida Sexta y Calle 21B<br/"
contenido_id_24 ="<h2>Mercadito M&G</h2> <br/> <b>Dirección:</b>Calle Jovellar entre L y M<br/"
contenido_id_25 ="<h2>May May Mercadito</h2> <br/> <b>Dirección:</b>Calle J entre 19 y 21<br/"
contenido_id_26 ="<h2>Mercadito 112</h2> <br/> <b>Dirección:</b>9na entre 5taF y 110<br/"
contenido_id_27 ="<h2>La Nave</h2> <br/> <b>Dirección:</b>Desvio Naval entre Carretera del Asilo y Carretera Naval<br/"
contenido_id_28 ="<h2>Bodegon Oasis</h2> <br/> <b>Dirección:</b>Calle J entre Linea y 11<br/"
contenido_id_29 ="<h2>Bodegon Wawa</h2> <br/> <b>Dirección:</b>Calle 1ra entre 16 y 18<br/"
contenido_id_30 ="<h2>Kaluch Market</h2> <br/> <b>Dirección:</b>Calle 12 entre 1ra y 3ra<br/"
contenido_id_31 ="<h2>Market Rey</h2> <br/> <b>Dirección:</b>Carretera del Asilo entre Naval y los Pinos<br/"
contenido_id_32 ="<h2>Don Pancho</h2> <br/> <b>Dirección:</b>Calle Los Pinos entre Cuba y 29<br/"
contenido_id_33 ="<h2>Xalxa</h2> <br/> <b>Dirección:</b>Calle L entre Linea y 15<br/"
contenido_id_34 ="<h2>Ten Cen Mercado</h2> <br/> <b>Dirección:</b>Avenida Carlos III entre Soledad y Castillejo<br/"
contenido_id_35 ="<h2>Ko Minimercado</h2> <br/> <b>Dirección:</b>Calle 98 entre 5ta y 3ra<br/"

folium.Marker(
    location=[23.136670, -82.378462],
    tooltip="Click me!",
    popup= contenido_id_1,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136978, -82.378452],
    tooltip="Click me!",
    popup= contenido_id_2,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136670, -82.378462],
    tooltip="Click me!",
    popup= contenido_id_3,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.139172, --82.375413],
    tooltip="Click me!",
    popup= contenido_id_4,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.139312, -82.374955],
    tooltip="Click me!",
    popup= contenido_id_5,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136067, -82.371610],
    tooltip="Click me!",
    popup= contenido_id_6,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136072, -82.371438],
    tooltip="Click me!",
    popup= contenido_id_7,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.135885, -82.374399],
    tooltip="Click me!",
    popup= contenido_id_8,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.160816, -82.298762],
    tooltip="Click me!",
    popup= contenido_id_9,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.1677199, -82.2958790],
    tooltip="Click me!",
    popup= contenido_id_10,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.1615429, -82.3060070],
    tooltip="Click me!",
    popup= contenido_id_11,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.112360, -82.430514],
    tooltip="Click me!",
    popup= contenido_id_12,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.138261, -82.385447],
    tooltip="Click me!",
    popup= contenido_id_13,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136743, -82.383931],
    tooltip="Click me!",
    popup= contenido_id_14,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.142646, -82.385271],
    tooltip="Click me!",
    popup= contenido_id_15,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.13992, -82.38087],
    tooltip="Click me!",
    popup= contenido_id_16,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.145390, -82.267267],
    tooltip="Click me!",
    popup= contenido_id_17,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.11291, -82.42327],
    tooltip="Click me!",
    popup= contenido_id_18,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.161456, -82.303290],
    tooltip="Click me!",
    popup= contenido_id_19,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.139277, -82.379336],
    tooltip="Click me!",
    popup= contenido_id_20,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.14178, -82.38665],
    tooltip="Click me!",
    popup= contenido_id_21,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.12275, -82.40522],
    tooltip="Click me!",
    popup= contenido_id_22,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.143574, -82.311805],
    tooltip="Click me!",
    popup= contenido_id_23,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.137987, -82.380839],
    tooltip="Click me!",
    popup= contenido_id_24,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.139864, -82.386700],
    tooltip="Click me!",
    popup= contenido_id_25,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.096684, -82.448197],
    tooltip="Click me!",
    popup= contenido_id_26,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.154132, -82.331793],
    tooltip="Click me!",
    popup= contenido_id_27,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.142825, -82.389349],
    tooltip="Click me!",
    popup= contenido_id_28,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.126657, -82.422274],
    tooltip="Click me!",
    popup= contenido_id_29,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.136082, -82.407619],
    tooltip="Click me!",
    popup= contenido_id_30,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.154693, -82.333464],
    tooltip="Click me!",
    popup= contenido_id_31,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.160597, -82.297689],
    tooltip="Click me!",
    popup= contenido_id_32,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.14326, -82.38677],
    tooltip="Click me!",
    popup= contenido_id_33,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.13172, -82.37345],
    tooltip="Click me!",
    popup= contenido_id_34,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

folium.Marker(
    location=[23.10020, -82.44860],
    tooltip="Click me!",
    popup= contenido_id_35,
    icon=folium.Icon(icon = "shopping-cart", color='pink'),
).add_to(map)

"""-------------------------------------------------------------------------------------"""
#Grafica de cantidad de Mipymes por municipio
import matplotlib.pyplot as plt

def graf_cant_muni():
    labels = ["Plaza", "Playa", "Habana del Este", "Centro Habana"]
    value = [12, 6, 9, 9]
    colors = ["#FFC0CB", "#FF69B4", "#DB7093", "#C71585"]

    fig, ax = plt.subplots()
    ax.pie(value, labels = labels, colors = colors, autopct='%1.1f%%', wedgeprops= {'linewidth': 1, "edgecolor": "black"})
    ax.axis('equal')
    plt.title("Cantidad de Mipymes por municipio")

    plt.show()

"""-------------------------------------------------------------------------------------"""
#Grafica de distribucion de productos
import matplotlib.pyplot as plt
import squarify


def graf_distri_product():
    values = distri_prod()[1]
    labels = distri_prod()[0]
    colors = ["#FF1493", "#FF00FF", "#FF69B4", "#FFB6C1", "#C71585", "#DA70D6", "#DB7093", "#FFC0CB", "#EE82EE",
              "#e377c2"]

    plt.figure(figsize=(18, 12))
    squarify.plot(sizes=values, pad=0.25, label=labels, text_kwargs={"fontsize": 13, "color": "black"}, ec='black',
                  color=colors, alpha=0.7)
    plt.axis('off')
    plt.show()


"""-------------------------------------------------------------------------------------"""
#Imprimir los nombres de todos los productos
def names_prod():
    p = []
    for i in data.get("Mipymes"):
        for j in i["Places"]["Products"][0]:
            if '_1' in j:
                continue
            if '_2' in j:
                continue
            if '_3' in j:
                continue
            if '_4' in j:
                continue
            if '_5' in j:
                continue
                continue
            if j not in p:
                p.append(j)
    return p

"""-------------------------------------------------------------------------------------"""
#Graficos de salario y productos
def graf_salario_prod():
    A = ["Arroz", "Pechuga", "Aceite", "Cafe", "Huevo"]
    B = [promedio_pri("Arroz"), promedio_pri("Pollo_Pechuga"),
         promedio_pri("Aceite"), promedio_pri("Cafe"), promedio_pri("Huevos")]

    salario = promedio_salario(quantity_salary())
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.arange(len(A))
    ax.bar(x=x, height=B, width=0.6, color="#FF69B4", edgecolor="w")
    ax.axhline(y=salario, color='magenta', linestyle='--', linewidth=2,
               label=f'Salario: ${salario:,.0f}')
    plt.title('Productos que puedes comprar con el salario', style="italic")
    ax.set_xlabel('Productos')
    ax.set_ylabel('Promedio de precio')
    ax.set_xticks(x)
    ax.set_xticklabels(A, rotation=45)
    ax.legend()
    plt.tight_layout()
    plt.show()

"""-------------------------------------------------------------------------------------"""
#Guardar datos en un diccionario
def save_dicc():
    d ={}
    for i in data.get("Mipymes"):
        for j in i["Places"]["Products"]:
            print(j)

"""-------------------------------------------------------------------------------------"""
#Grafica de productos y dias necesarios
def graf_count_prod():

    x = ["Arroz", "Pechuga", "Aceite", "Cafe", "Huevo"]
    y = [promedio_pri("Arroz")/ salario_dia(), promedio_pri("Pollo_Pechuga")/ salario_dia(), promedio_pri("Aceite")/ salario_dia(), promedio_pri("Cafe")/ salario_dia(), promedio_pri("Huevos")/ salario_dia()]


    fig, ax = plt.subplots()
    ax.bar(x=x, height=y, width=0.6, color="#FF00FF", edgecolor="black")
    plt.title('Promedio adquisitivo diario', style="italic")
    ax.set_xlabel('Productos')
    ax.set_ylabel('Dias necesarios')
    plt.xticks(rotation=45)
    plt.show()

"""-------------------------------------------------------------------------------------"""
#Leer Tiendas en Dolares
def read_dolares(abc):
    d = []
    for i in usd.get("Dolares"):
        for j in i["Places"]["Products"]:
            if abc in j:
                d.append(j[abc])
    return d

"""-------------------------------------------------------------------------------------"""
#Leer productod de tiendas en dolares
def read_dolares(abc):
    d = []
    for i in usd.get("Dolares"):
        for j in i["Places"]["Products"]:
            if abc in j:
                d.append(j[abc])
    return d

"""-------------------------------------------------------------------------------------"""
#Promedio de precios en tiendas de dolares
def pri_dolar(dola):
    p = []
    for i in usd.get("Dolares"):
        for j in i["Places"]["Products"]:
            if dola in j:
               p.append(j[dola]["Price"])
    return round(sum(p)/len(p), 2)

"""-------------------------------------------------------------------------------------"""
#Ultima tasa de cambio en usd
def find_cambio():
    last_day = infor["Tasa_de_Cambio"][-1]["Day"]
    return last_day["USD"]

"""-------------------------------------------------------------------------------------"""
#Precio en moneda nacional de los productos en dolares
def pri_dolar_cambio(dola):
    p = []
    for i in usd.get("Dolares"):
        for j in i["Places"]["Products"]:
            if dola in j:
               p.append(j[dola]["Price"])
    ave = round((sum(p)/len(p))* find_cambio(), 2)
    return ave
"""-------------------------------------------------------------------------------------"""
# Grafica de comparacion de productos en tiendas de dolares vs mipymes
def graf_comp_usd_cup():
    import numpy as np
    import matplotlib.pyplot as plt

    productos = ["Arroz", "Cafe_1", "Pollo_Pechuga", "Leche_Polvo", "Lentejas"]
    x1 = [promedio_pri(producto) for producto in productos]
    x2 = [pri_dolar_cambio(producto) for producto in productos]

    fig, ax = plt.subplots(figsize=(10, 6))

    ancho_barra = 0.35
    indices = np.arange(len(productos))
    colors = ["#DA70D6", "#FF00FF"]

    ax.bar(indices - ancho_barra/2, x1, ancho_barra, label='CUP', alpha=0.8, color= colors[0])
    ax.bar(indices + ancho_barra/2, x2, ancho_barra, label='USD', alpha=0.8, color= colors[1])

    ax.set_xlabel('Productos')
    ax.set_ylabel('Precio')
    ax.set_title('Comparación de precios: CUP vs USD')
    ax.set_xticks(indices)
    ax.set_xticklabels(productos)
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

"""-------------------------------------------------------------------------------------"""