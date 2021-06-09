import sys,os
class basicdb:
    def write_from_to(self,name,array,X1,Y1,X2,Y2):
        db = basicdb()
        relleno = []
        inicio = array[Y1 - 1][0:db.sizeX(name) + 1]
        print(inicio)
        for f in range(0,db.sizeY(name) - 2):
            relleno.append([])
        print(relleno)
        for w in range(1,db.sizeY(name) - 1):
            for v in range(0,db.sizeX(name)):
                relleno[w - 1].append(array[w][v])
        final = array[Y2 - 1][0:X2]
        for i in range(0,db.sizeX(name) - 1):
            print(i)
            db.write_cordinate(name, inicio[i], i + X1, Y1)
        print(relleno)
        for j in range(0,Y2 - 2):
            for t in range(0,db.sizeX(name)):
                print(j,"n",t)
                db.write_cordinate(name, relleno[j][t], t + 1, j + 2)
        print(final)
        for e in range(0, X2):
            db.write_cordinate(name, final[e], e + 1, Y2)
        
    def read_from_to(self,name,X1,Y1,X2,Y2):
        db = basicdb()
        array = []
        for i in range(0,db.sizeY(name)):
            array.append([])
        otherarray = list(db.read_database(name).splitlines())
        for j in range(0 , db.sizeY(name)):
            for t in range(0,db.sizeX(name)):
                array[j].append(otherarray[j].split("|")[t])
        relleno = []
        inicio = array[Y1 - 1][X1 - 1:db.sizeX(name) + 1]
        for w in range(1,db.sizeY(name) - 1):
            for v in range(0,db.sizeX(name)):
                relleno.append(array[w][v])
        final = array[Y2 - 1][0:X2]
        end = inicio + relleno + final
        return end
    
    
    
    
    def append(self,name,array):
        filename = name + ".senior"
        #inicia#comprobar si el tamaño de la base de datos coincide con el tamaño del array
        file1 = open(filename,"r")
        lines1 = file1.read()
        file1.close()
        AsizeX = len(array)
        FsizeX = lines1.split("\n")[0].count("|")
     
        if not AsizeX == FsizeX:
           sys.exit(1)
        
        file = open(filename,"a")
        

        finalArray = []
          
        for i in range(0, AsizeX):
            val = str(array[i]) + "|"
            finalArray.append(val)
            file.write(finalArray[i])
        file.write("\n") 
        file.close()                 
        
    def delete_database(self,name):
        os.remove(name+".senior")
    
    
    
    
    def create_database(self,name,sizeX,sizeY):
        
        
        filename = name+".senior"
        if os.path.isfile(filename)==True:
            sys.exit(2)
        file = open(filename,"w")
        array = []
        for j in range(0,sizeY):
            array.append([])
        for i in range(0,len(array)):
            
            
            for t in range(0,sizeX):
                array[i].append(" | ")
        
        for n in range(0,len(array)):
            for m in range(0,sizeX):
                file.write(array[n][m])
            file.write("\n")
        
        file.close()
        
    def sizeY(self,name):
        filename = name + ".senior"
        file = open(filename,"r")
        lines1 = file.read()
        file.close()
        resultado1=lines1.splitlines()
        numn1 = len(resultado1)
        return numn1
    def sizeX(self,name):
        filename = name + ".senior"
        file = open(filename,"r")
        lines1 = file.read()
        file.close()
        FsizeX = lines1.split("\n")[0].count("|")
        return FsizeX
        
        
        
    def read_database(self,name,mode):
        db = basicdb()
        filename = name + ".senior"
        file = open(filename,"r")
        read = file.read()
        file.close()
        text = ""
        if mode == "text n":
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,db.sizeX(name) + 1):
                    text += db.read_cordinate(name, j,i) + " "
               text += "\n"
           return text
        if mode == "text wn":
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,db.sizeX(name) + 1):
                    text += db.read_cordinate(name, j,i) + " "
           return text
        if mode == "list wn":
           
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,db.sizeX(name) + 1):
                    text += db.read_cordinate(name, j,i)
           text2 = list(text)
           return list(text2)
        if mode == "list n":
           
           for i in range(1, db.sizeY(name) + 1):
               for j in range(1,db.sizeX(name) + 1):
                    text += db.read_cordinate(name, j,i)
               text += "\n"     
           text2 = list(text)
           return list(text2)
        return read  
    
    def write_array(self,name,array):
        filename = name + ".senior"
        #inicia#comprobar si el tamaño de la base de datos coincide con el tamaño del array
        file1 = open(filename,"r")
        lines1 = file1.read()
        file1.close()
        resultado1=lines1.splitlines()
        numn1 = len(resultado1)
        AsizeY = len(array)
        AsizeX = len(array[0])
        FsizeY = numn1
        FsizeX = lines1.split("\n")[0].count("|")
     
        if not AsizeY == FsizeY and AsizeX == FsizeX:
            sys.exit(1)
        #termina#comprobar si el tamaño de la base de datos coincide con el tamaño del array
        
       
        file = open(filename,"w") 
        finalArray = []
        
        for i in range(0,FsizeY):
            finalArray.append([])
        for n in range(0,FsizeY):
            for m in range(0,AsizeX):
               val = str(array[n][m])+"|" 
               finalArray[n].append(val)
            
        
        for s in range(0,len(array)):
            for r in range(0,FsizeX):
                file.write(finalArray[s][r])
            file.write("\n")
        file.close()
    def read_cordinate(self,name,X,Y):
        filename = name+".senior"
        file = open(filename,"r")
     
        line = file.readlines()[Y - 1]
        line = line.split("|")[X - 1]
        return line
    def write_cordinate(self,name,val,X,Y):
        filename = name+".senior"
        file1 = open(filename,"r")
        lines1 = file1.read()
        file = open(filename,"w")
        finalArray = []
        resultado1=lines1.splitlines()
        numn1 = len(resultado1)
        FsizeY = numn1
        FsizeX = lines1.split("\n")[0].count("|")
      
        array = []
        if not X > FsizeX and Y > FsizeY:
            sys.exit(1)   
        for i in range(0,FsizeY):
            finalArray.append([])
            array.append([])
        

        vas = lines1
        
        
        
        for y in range(0,FsizeY):
            for x in range(0,FsizeX):
                var = vas.split("\n")[y]
               
                
                array[y].append(var.split("|")[x])
            array[y].append("\n")    
       
        
        array[Y - 1].pop(X - 1)
        array[Y - 1].insert(X - 1, val)
        
        for n in range(0,len(array)):
            for m in range(0,FsizeX):
               val = str(array[n][m])+"|" 
               finalArray[n].append(val)
        for s in range(0,FsizeY):
            for r in range(0,FsizeX):
                file.write(finalArray[s][r])
            file.write("\n")               
         
        file1.close()
        file.close()
      
      
        
      
        
      
        