#Limpieza base de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:\Users\20344807257\Desktop\PERMISOS DE OBRA_2012-2021.xlsx", engine="openpyxl", sheet_name="base completa")
dict_cuatri = {'PRIMER': 1,
                     'SEGUNDO': 2,
                     'TERCER': 3,
                     'CUARTO': 4}
dict_meses = {'enero': 1, 'febrero': 2, 'marzo': 3, "abril": 4, "mayo": 5, 'junio': 6,
                'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11,
                'diciembre': 12}
#Convirtiendo a lowercase
df['MES'] = df['MES'].apply(str.lower)
#Remplazar meses por nums
df['MES'].replace(dict_meses, inplace=True)
#Remplazar cuatris x nums
df['TRIMESTRE'].replace(dict_cuatri, inplace=True)
df['TIPO_OBRA'] = df['TIPO_OBRA'].apply(str.lower)

#sort by year
df.sort_values(by='ANIO', inplace=True)
df["FECHA"] = pd.to_datetime(df["FECHA"],errors='coerce')
df = df[df["ANIO"] == 2022]
#df.to_excel("Base_limpia.xlsx",)
print(df)

