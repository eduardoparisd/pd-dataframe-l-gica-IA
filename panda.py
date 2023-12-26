import pandas as pd
import sys

medida_pantalon_m = pd.Series(['Cintura-cm', 'Longitud-cm'])

datos_pantalones = [
    {'Medida': medida_pantalon_m, 'Talla': 'XXS', 'Ancho': 67, 'Longitud': 77},
    {'Medida': medida_pantalon_m, 'Talla': 'XS', 'Ancho': 71, 'Longitud': 78},
    {'Medida': medida_pantalon_m, 'Talla': 'S', 'Ancho': 79, 'Longitud': 79},
    {'Medida': medida_pantalon_m, 'Talla': 'M', 'Ancho': 87, 'Longitud': 82},
    {'Medida': medida_pantalon_m, 'Talla': 'L', 'Ancho': 96, 'Longitud': 84},
    {'Medida': medida_pantalon_m, 'Talla': 'XL', 'Ancho': 102, 'Longitud': 85},
    {'Medida': medida_pantalon_m, 'Talla': 'XXL', 'Ancho': 112, 'Longitud': 87},
]

medida_sueter = pd.Series(['Largo','Ancho','Largo de manga'])

datos_Sueter = [
    {'Medida': medida_sueter, 'Talla': 'XS', 'Largo': 74, 'Ancho': 66,'LargoManga':23},
    {'Medida': medida_sueter, 'Talla': 'S', 'Largo': 75, 'Ancho': 68,'LargoManga':24},
    {'Medida': medida_sueter, 'Talla': 'M', 'Largo': 77, 'Ancho': 71,'LargoManga':25},
    {'Medida': medida_sueter, 'Talla': 'L', 'Largo': 79, 'Ancho': 76,'LargoManga':26},
    {'Medida': medida_sueter, 'Talla': 'XL', 'Largo': 81, 'Ancho': 80,'LargoManga':27},
]

df = pd.DataFrame(datos_pantalones)
df_sueter = pd.DataFrame(datos_Sueter)


tipo_camisas = pd.Series(['Cuello', 'Altura', 'Longitud de Manga', 'Ancho de Pecho'])

datos_camisas = {
    'Camisa_Medidas': tipo_camisas,
    'XS': [36, 73, 61, 50],
    'Small': [36, 77, 63, 52],
    'Medium': [38, 77, 64, 55],
    'Large': [40, 78, 65, 58],
    'XL': [42, 79, 66, 61]
}

dt = pd.DataFrame(datos_camisas)
dt.set_index('Camisa_Medidas', inplace=True)  # Establece 'Camisa_Medidas' como el índice del DataFrame



# Obtener medidas de pantalones para tallas 'XS', 'S', 'M'
medidas_pantalones = df.loc[df['Talla'].isin(['XS', 'S', 'M']), ['Talla', 'Ancho', 'Longitud']]
medidas_pantalones = medidas_pantalones.set_index('Talla')

# Obtener medidas de suéter para tallas 'XS', 'S', 'M'
medidas_sueter = df_sueter.loc[df_sueter['Talla'].isin(['XS', 'S', 'M']), ['Talla', 'Ancho', 'Largo', 'LargoManga']]
medidas_sueter = medidas_sueter.set_index('Talla')



# Acceder a las medidas para tallas 'XS'
longitud_xs, ancho_xs = medidas_pantalones.loc['XS', ['Longitud', 'Ancho']].astype(int).tolist()
longitud_s, ancho_s = medidas_pantalones.loc['S', ['Longitud', 'Ancho']].astype(int).tolist()
longitud_m, ancho_m = medidas_pantalones.loc['M', ['Longitud', 'Ancho']].astype(int).tolist()

# Acceder a las medidas de suéter para tallas 'XS'
longitud_sueter_xs, ancho_sueter_xs, largo_manga_sueter_xs = medidas_sueter.loc['XS', ['Largo', 'Ancho', 'LargoManga']].astype(int).tolist()

# Obtener medidas de suéter para tallas 'XS', 'S', 'M'
medidas_sueter = df_sueter.loc[df_sueter['Talla'].isin(['XS', 'S', 'M']), ['Talla', 'Largo', 'Ancho', 'LargoManga']]


medidas_sueter = medidas_sueter.set_index('Talla')

# Acceder a las medidas de suéter para tallas 'XS'
longitud_sueter_xs, ancho_sueter_xs, largo_manga_sueter_xs = medidas_sueter.loc['XS'].astype(int).tolist()

# Acceder a las medidas de suéter para tallas 'S'
longitud_sueter_s, ancho_sueter_s, largo_manga_sueter_s = medidas_sueter.loc['S'].astype(int).tolist()

# Acceder a las medidas de suéter para tallas 'M'
longitud_sueter_m, ancho_sueter_m, largo_manga_sueter_m = medidas_sueter.loc['M'].astype(int).tolist()

print(f"\nDATAFRAME SUETER: \n\n{medidas_sueter}")
print(f"\nDATAFRAME PANTALONES: \n\n{medidas_pantalones}")


# ---------------------------------DATOS--------------------------------

# VALORES FICTIOSIOS DESDE EL IA PANTALON

# datos anatomicos de la persona
ancho_pierna_persona = 82
longitud_pierna_persona = 80

# datos del pantalon de la persona
ancho_pantalon_persona = 70
longitud_pantalon_persona = 80

# condiciones
pantalon_roto = False
sport_Pantalon = False
# VALORES FICTISIOS DESDE EL IA PANTALON 

# variables globales
genero = "Masculino"
# variables globales


# Datos de la camisa a verificar
longitud_manga_camisa = 71

# VALORES FICTISIOS DESDE EL IA SUETER
longitud_torso_persona = 78
ancho_torso_persona = 75
sport_Sueter = False
longitud_sueter_persona = 70
ancho_sueter_persona = 50
largo_manga_sueter = 30

escote = False

# VALORES FICTISIOS DESDE EL IA SUETER


#-----------------------------------FUNCIONES -----------------------------

#FUNCION PARA CAMISAS
def es_manga_permitida(longitud_manga, longitud_permitida):
    return not (longitud_manga < longitud_permitida or pd.isnull(longitud_manga))

def verificar_manga_permitida(dataframe, longitud_manga):
    resultados = {}

    for talla in dataframe.columns:
        if talla != 'Camisa_Medidas':
            manga_permitida = es_manga_permitida(longitud_manga, dataframe.loc['Longitud de Manga', talla])
            resultados[talla] = manga_permitida

    return resultados

resultados = verificar_manga_permitida(dt, longitud_manga_camisa)



# FUNCION ASIGNAR TALLA DE SUETER A PERSONA

def talla_sueter(altura,ancho):
  if altura >= longitud_sueter_xs and altura <= longitud_sueter_s and ancho >= ancho_sueter_xs and ancho <= ancho_sueter_s:
    return 'XS'
  elif altura >= longitud_sueter_s and altura <= longitud_sueter_m and ancho >= ancho_sueter_s and ancho <= ancho_sueter_m:
    return 'S'
  elif altura >= longitud_sueter_m and ancho >= ancho_sueter_m:
    return 'M'
  else:
    return 'Error'

talla_sueter_persona = talla_sueter(longitud_torso_persona, ancho_torso_persona)

if talla_sueter_persona == 'Error':
  print('Los datos no son correctos')
  sys.exit("Detenido por el usuario")



# FUNCION VALIDAR TALLA DE SUETER

def validar_sueter(longitud,deportivo,manga,escotado):
  manga_longitud = 7
  if talla_sueter_persona == "XS":
    
    minimo_talla_longitud = 50

    if longitud < minimo_talla_longitud or deportivo==True or manga < manga_longitud or escotado == True:
      return "no valido."
    else:
      return "válido"

  elif talla_sueter_persona == "S":
    minimo_talla_longitud = 60

    if longitud < minimo_talla_longitud or deportivo==True or manga < manga_longitud or escotado == True:
      return "no valido." 
    else:
      return("válido")
  elif talla_sueter_persona == "M":

    minimo_talla_longitud = 70

    if longitud < minimo_talla_longitud or deportivo==True or manga < manga_longitud or escotado == True:
      return "no valido." 
    else:
      return "válido" 
  
# SE INICIA FUNCION
validacion_sueter = validar_sueter(longitud_sueter_persona,sport_Sueter,largo_manga_sueter,escote)



# FUNCION ASIGNAR TALLA PANTALON A PERSONA

def talla_pantalon(altura,ancho):
  if altura >= longitud_xs and altura <= longitud_s and ancho >=ancho_xs and ancho <= ancho_s:
    return 'XS'
  elif altura >= longitud_s and altura <= longitud_m and ancho >= ancho_s and ancho <= ancho_m:
    return 'S'
  elif altura >= longitud_m and ancho >= ancho_m:
    return 'M'
  

# FUNCION VALIDAD PANTALON A PERSONA
def validar_pantalon(longitud,roto,sexo,deportivo):
  if tallaPersona == "XS":
    if(sexo =="Masculino"):
      minimo_talla_longitud = 40
    elif(sexo =="Femenino"):
      minimo_talla_longitud = 31


    if longitud <= minimo_talla_longitud or roto == True or deportivo == True:
      return "válido"
    else:
      return "válido"
  
  elif tallaPersona == "S":
    if(sexo =="Masculino"):
      minimo_talla_longitud = 50
    elif(sexo =="Femenino"):
      minimo_talla_longitud = 42


    if longitud <= minimo_talla_longitud or roto == True or deportivo == True:
      return "no valido"
    else:
      return "válido"

  elif tallaPersona == "M":
    if(sexo =="Masculino"):
      minimo_talla_longitud = 56
    elif(sexo =="Femenino"):
      minimo_talla_longitud = 45

    if longitud <= minimo_talla_longitud or roto == True or deportivo == True:
      return "no valido"
    else:
      return "válido"
  # elif tallaPersona == "M":



tallaPersona = talla_pantalon(longitud_pierna_persona,ancho_pierna_persona)
validacion_pantalon = validar_pantalon(longitud_pantalon_persona,pantalon_roto,genero,sport_Pantalon)

validacion = ""

# Verificar si la manga es permitida
if resultados['XS']:
    print("La camisa es permitida")
    print("Puede entrar a la UIP.")
    validacion = "válido"
else:
    print("La camisa no es permitida")
    print("No puede entrar a la UIP.")
    validacion = "no valido"


if(sport_Pantalon==True):
  esSportpant = 'Si'
else:
  esSportpant ='No'

if(sport_Sueter==True):
  esSportsueter = 'Si'
else:
  esSportsueter ='No'

if(pantalon_roto ==True):
  esRoto = 'Roto'
else:
  esRoto ='Normal'

if(escote == True):
  escotePrnt = 'Escotado'
else:
  escotePrnt = 'Normal'


# SE IMPRIMEN RESULTADOS
print('\n------INFORMACION DE PANTALONES---------')


tallaPersona = print(f"\nLa talla de pantalon es:{talla_pantalon(longitud_pierna_persona,ancho_pierna_persona)}\nGenero: {genero}\nDeportivo: {esSportpant}\nEstado: {esRoto}")

print('\n------Información de sueter--------')
print(f"\nLa talla de sueter es: {talla_sueter_persona}\nGenero: {genero}\nDeportivo: {esSportsueter}\nEstado: {escotePrnt}")

print('\n-------Información de camisa')
print(f"Longitud de manga: {longitud_manga_camisa}")


print(f"\n------Resultado-------\n\nEl pantalon es: {validacion_pantalon} y el sueter es: {validacion_sueter} y la camisa es: {validacion}")

if(validacion_pantalon == "válido" and validacion_sueter == "válido" and validacion=="válido"):
  print('\n¡Puede entrar a la UIP! :)\n')
else:
  print('\n¡No puede entrar a la UIP! :(')




  


  



