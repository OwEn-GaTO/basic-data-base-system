import sys,os
class basicdb:
    
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
        
        
        
    def read_database(self,name):
        filename = name + ".senior"
        file = open(filename,"r")
        read = file.read()
        file.close()
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
      
      
        
        
      
        
