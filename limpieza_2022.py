#Limpieza base de datos
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\20344807257\Desktop\PERMISOS DE OBRA_2022.xlsx", engine="openpyxl")
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
#df['TIPO_OBRA'] = df['TIPO_OBRA'].apply(str.lower)
df.drop(['ID',"EXPEDIENTE","M2_SGU","SMP","SMP_UF","TRATA","DISTR_CPU_1","DISTR_CPU_2","DISTR_CUR"], axis=1, inplace=True)

#df.to_excel("Base_2022_limpia.xlsx",)
df["TIPO_OBRA"] = df["TIPO_OBRA"].astype(str).apply(str.lower)
replace_dict = {"├│": "o", "ó": "o"}
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("├│", "o")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("ó", "o")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("sin dato", "NaN")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("sin datos", "Nan")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("nan", "NaN")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace("NaNs", "NaN")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace(" y", ",")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace(" con ", ", ")
df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace(".", "")

dict = {"modificacion de obra en curso bajo responsabilidad profesional":"NaN" ,
        "obra nueva": "1","demolicion total":"2", "modificacion":"3",
        "demolicion parcial":"2", "ampliacion":"3",
        "regularizacion de obra en contravencion reglamentaria":"NaN"}
for key in dict:
   df["TIPO_OBRA"] = df["TIPO_OBRA"].str.replace(key, dict[key])

df["TIPO_OBRA"] = df["TIPO_OBRA"].str.split(", ")
df = df.explode("TIPO_OBRA")
df["TIPO_OBRA"] = df["TIPO_OBRA"].replace("NaN", np.nan)
df.dropna(inplace=True,subset="TIPO_OBRA")
df["BARRIOS"] = df["BARRIOS"].str.replace("NU├æEZ", "NUÑEZ")
df["BARRIOS"] = df["BARRIOS"].str.replace("MONTSERRAT","MONSERRAT" )

for trimestre in range(1,5):
    df_1 = df[df["TRIMESTRE"] == trimestre]
   # print(f"valores para el {trimestre} trimestre:")
   # print(df["TIPO_OBRA"].value_counts())
list = df["BARRIOS"].unique()
sup_barrio = df.groupby('BARRIOS')["SUP_CONST"].sum().sort_values()
df.to_excel("base_limpia.xlsx")
#print((a)
#print(df)