
def open_doc():
    doc = open("input.txt").read().strip()
    return doc

def read_lines(doc):
    colores = ["red","green","blue", "red;","green;","blue;"]
    no_posible = []
    solucion = []
    for line in doc.split('\n'):
        id_game,line = line.split(":")
        jugada = line.split(";")
        juego = line.split(",")
        id_game = id_game.split()
        
        for i in (juego):
            i = i.split()
            for c in i:
                pos = i.index(c)
                value = pos -1
                if c in colores:
                    if c == "red" or c == "red;":
                        if int(i[value]) > 12:
                            if int(id_game[1]) not in no_posible:
                                no_posible.append(int(id_game[1]))
                            
                        

                    elif c == "green" or c == "green;":
                        if int(i[value]) > 13:
                            if int(id_game[1]) not in no_posible:
                                no_posible.append(int(id_game[1]))
                           
                        
                       
                    elif c == "blue" or c == "blue;":
                        if int(i[value]) > 14:
                            if int(id_game[1]) not in no_posible:
                                no_posible.append(int(id_game[1]))
                            

    print(no_posible)
    print(solucion)
    print (sum(no_posible))   
    print(sum(solucion))                   
    return sum(no_posible)                    
        
    
                                 
                       
        

        

    
        
        

    




       
doc = open_doc()
solucion = read_lines(doc)