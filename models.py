
def open_doc():
    doc = open("input.txt").read().strip()
    return doc

def read_lines(doc):
    colores = ["red","green","blue"]
    no_posible = []
    solucion = []
    read_games = []
    solucion_2 = []

    for line in doc.split('\n'):
        
        id_game,line = line.split(":")
        juego = line.split(",")
        id_game = id_game.split()
        red = []
        green =[]
        blue = []
        
            
        
        for i in (juego):
            
            
            i = i.split()
            if ";" in i:
                juego.replace(";", "")
            
            if id_game[1] not in read_games:
                read_games.append(id_game[1])
            i = list(i)

            
            #utilizo bucle for en vez de .index, para generar la posisción y evitar el error de reseteo de indice al estar el color duplicado
            for pos, c in enumerate(i):
                
                if pos >= 1:
                    value = pos -1
                else:
                    value = 0
                
                if c.endswith(';'):
                    c = c.rstrip(';')

                if c in colores:
                    
                    if c == "red":
                        red.append(int(i[value]))
                        
                        for n in red:
                            if int(n) > 12:
                                if int(id_game[1]) not in no_posible:
                                    no_posible.append(int(id_game[1]))
                                    
                    elif c == "green":
                        green.append(int(i[value]))

                        for n in green:
                            if int(n) > 13:
                                if int(id_game[1]) not in no_posible:
                                    no_posible.append(int(id_game[1]))
                                   
                    elif c == "blue":
                        blue.append(int(i[value]))
                        
                        for n in blue:
                            if int(n) > 14:
                                if int(id_game[1]) not in no_posible:
        
                                    no_posible.append(int(id_game[1]))
        
        red.sort()
        green.sort()
        blue.sort()

        resultado = red[-1]*green[-1]*blue[-1]
        solucion_2.append(int(resultado))
                                              
        for i in read_games:
            if int(i) not in no_posible and  int(i) not in solucion:
                solucion.append(int(i))                        
                            
                            
    return (sum(solucion)), (sum(solucion_2))                    
        