import ast

def open_doc():
    doc = open("./day2/input.txt", "r")
    return doc

def read_linea(doc):
    for linea in doc:
        linea = linea.split('\n')  
    return linea

 #continuar con  creacion de diccionario por cada juego         
def linea_dic(linea):
    linea_dic = ast.literal_eval(linea)
    print(linea_dic)
    return linea_dic


doc = open_doc()
linea = read_linea(doc)
print(linea)
