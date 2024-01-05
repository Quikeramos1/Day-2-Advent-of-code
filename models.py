
def open_doc():
    doc = open("input.txt").read().strip()
    return doc

def read_lines(doc):
    colores = ["red","green","blue", "red;","green;","blue;"]
    no_posible = []
    solucion = []
    read_games = []
    for line in doc.split('\n'):
        id_game,line = line.split(":")
        juego = line.split(",")
        id_game = id_game.split()
        red = []
        green =[]
        blue = []
        
        for i in (juego):
            i = i.split()
            if id_game[1] not in read_games:
                read_games.append(id_game[1])
            for c in i:
                pos = i.index(c)
                value = pos -1
                if c in colores:
                    if c == "red" or c == "red;":
                        red.append(int(i[value]))
                        
                        for n in red:
                            if int(n) > 12:
                                if int(id_game[1]) not in no_posible:
                                    no_posible.append(int(id_game[1]))
                                    
                    elif c == "green" or c == "green;":
                        green.append(int(i[value]))

                        for n in green:
                            if int(n) > 13:
                                if int(id_game[1]) not in no_posible:
                                    no_posible.append(int(id_game[1]))
                                   
                    elif c == "blue" or c == "blue;":
                        blue.append(int(i[value]))
                        
                        for n in blue:
                            if int(n) > 14:
                                if int(id_game[1]) not in no_posible:
                                    no_posible.append(int(id_game[1]))
        for i in read_games:
            if int(i) not in no_posible and  int(i) not in solucion:
                solucion.append(int(i))                        
                            
                
                   
        
    
                   
    return (sum(solucion))                     
        
