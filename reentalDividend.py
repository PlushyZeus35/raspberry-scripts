import pandas as pd 
from notionHelper import NotionUtils
from reentalUtils import ReentalToken
route = 'dividentosNoviembre2023.csv'
data = {}
properties = []
dividends = []
month = 'Noviembre'
year = '2023'
tags = [{'name': month}, {'name': year}]
# Lee el archivo CSV en un DataFrame de Pandas
dataframe = pd.read_csv(route)
data = dataframe.to_dict()
dataLength = len(data['Inmuebles'])
for i in range(dataLength):
    dividendo = data['Div x Token'][i]
    nombre = data['Inmuebles'][i]
    if isinstance(dividendo, str) and dividendo.startswith("$"):
        dividendo = float(dividendo.lstrip("$").replace(',', '.'))
    properties.append({'Inmueble': nombre, 'Dividendo': dividendo})

for prop in properties:
    propAux = NotionUtils.getReentalToken(prop['Inmueble'])
    if isinstance(propAux, ReentalToken):
        dividends.append({'Inmueble': propAux.name, 'notionId': propAux.notionId, 'rendimiento': round(propAux.amount*prop['Dividendo'],2), 'rendimiento final': round(propAux.amount*prop['Dividendo']*propAux.getEurValue(),2)})
        NotionUtils.createReentalDividend(propAux.name, round(propAux.amount*prop['Dividendo'],2), round(propAux.amount*prop['Dividendo']*propAux.getEurValue(),2), propAux.notionId, tags)