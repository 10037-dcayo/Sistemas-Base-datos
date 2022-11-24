#importamos modulo y creamos un excel vacio
import glob
import pandas as pd
import csv
data_null={}
df_null=pd.DataFrame(data_null)
df_null.to_excel('DatosS.xlsx', index=False)

from faker import Faker
#Cargar y modificar el archivo 
writer=pd.ExcelWriter('DatosS.xlsx') 

fake=Faker('es-ES')
personas = [fake.unique.name() for b in range(5000)]

fake=Faker('es-ES')
empleados = [fake.unique.name() for b in range(5000)]

fake=Faker('es-ES')
bomberos = [fake.unique.name()  for b in range(5000)]

fake=Faker('es-ES')
policia = [fake.unique.name() for b in range(5000)]

data1= {'Personas':[personas],'Empleados':[empleados],'Bomberos':[bomberos],'Policia':[policia]}

df1 = pd.DataFrame(data1)

df1.to_excel(writer,'Hoja 1',index=False)

writer.save()
writer.close()