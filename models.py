import ast

def open_doc():
    doc = open("input.txt", "r")
    return doc

def quita_simbolos(texto):
    simbols=(",.:""[]'`'")
    return "". join(char for char in texto if char not in simbols)

def read_linea(doc):
    lineas= []
    simbols= (",.:""[]'`'")
    
    for linea in doc:
        linea = linea.split('\n')
        
        linea = str(linea)
        for i in linea:
            if i in simbols:
                linea=linea.replace(i,"")

        linea = linea.split()
        lineas.append(linea)
      
    return lineas    

def cuenta_linea(lineas):
    green = []
    red = []
    blue = []
    suma_jugadasko= []
    suma_jugadasok = []

    for linea in lineas:
        linea = linea
        num_juego = int(linea[1])
        
        
        
        for i in linea:
    
            if i == "green" or i == "green;":
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                green.append(num)
                linea.pop(pos)
                if num > 13:
                    suma_jugadasko.append(num_juego)
                    print(num_juego)
                    print ("Este juego no cumple porque green es:",num)
                    break
                else:
                    if num_juego in suma_jugadasok:
                        break
                    else:
                        suma_jugadasok.append(num_juego)
                        break
                

            elif i == "red" or i == "red;": 
                if num_juego == 43:
                    print("Ahora")
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                red.append(num)
                linea.pop(pos) 
                if num > 12:
                    suma_jugadasko.append(num_juego)
                    print(num_juego)
                    print ("Este juego no cumple porque red es:",num)
                    break
                else:
                    if num_juego in suma_jugadasok:
                        break
                    else:
                        suma_jugadasok.append(num_juego)
                        break
                
                
                

            elif i == "blue" or i == "blue;":
                pos = linea.index(i)
                pos_num = int(pos)-1
                num = linea[pos_num]
                num = int(num)
                blue.append(num)
                linea.pop(pos)
                if num > 14:
                    suma_jugadasko.append(num_juego)
                    print(num_juego)
                    print ("Este juego no cumple porque blue es:",num)
                    break
                else:
                    if num_juego in suma_jugadasok:
                        break
                    else:
                        suma_jugadasok.append(num_juego)
                        break

            
        continue
    
    print("Juegos que no cumplen son: ",suma_jugadasko)
    print("Juegos que si cumplen son: ",suma_jugadasok)
    solucion = sum(suma_jugadasok)
    print(solucion)
    return suma_jugadasko, suma_jugadasok  
        
    
        
        

       
                 
        
                


        
        
        
            
                
                
               
                   

    
    


    
        
             

        

    





doc = open_doc()
leer = read_linea(doc)
contar = cuenta_linea(leer)




