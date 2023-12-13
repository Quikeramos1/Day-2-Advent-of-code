import ast

def open_doc():
    doc = open("input.txt", "r")
    return doc



def read_linea(doc):
    simbols= (",.;:""[]'`'")
    
    for linea in doc:
        linea = linea.split('\n')
        
        linea = str(linea)
        for i in linea:
            if i in simbols:
                linea=linea.replace(i,"")

        linea = linea.split()
                  
        green = []
        red = []
        blue = []
        num_juego = int(linea[1])
        
        
        for i in linea:
            
            if i == "green":
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                green.append(num)
                
                linea.pop(pos)

            elif i == "red": 
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                red.append(num)
                
                linea.pop(pos)  

            elif i == "blue":
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                blue.append(num)
                
                linea.pop(pos)

        green = sum(green)
        red = sum(red)
        blue = sum(blue)            

        print("Juego Nº: ",num_juego)
        print("green= ",green)
        print("red= ",red)
        print("blue= ",blue)

#revisar esta oprecion que suma jugadas que no cumplen
        suma_jugadas= []

        if red > 12:
            suma_jugadas.append(num_juego)
        elif green > 13:
            suma_jugadas.append(num_juego)
        elif blue > 14:
            suma_jugadas.append(num_juego)

        print(suma_jugadas)
         
             

        

    return suma_jugadas





doc = open_doc()
solucion = read_linea(doc)
print(solucion)

