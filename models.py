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
        num_juego = linea[1]
        print("Juego Nº: ",num_juego)
        
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
                    

        
        print("green= ",sum(green))
        print("red= ",sum(red))
        print("blue= ",sum(blue))
         
             
         

            
        
        
        
        
        

    return 

 #continuar con  creacion de diccionario por cada juego         
#def linea_dic(linea):
#    linea_dic = ast.literal_eval(linea)
#    print(linea_dic)
#    return linea_dic


doc = open_doc()
linea = read_linea(doc)

