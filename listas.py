class Lista:
  #declaración de propiedades
    num1=0
    lista=[]
    c=0
    aux=0
  #declaración o definición del constructor de la clase
    def __init__(self,a) -> None:
        self.num1=a
        self.lista=[]
        self.par=[]
        self.impar=[]
        self.c=0
  #declaración de los métodos de la clase
    def obtener(self):
        
        i = self.num1
        print(i)
        while i > 0:
          self.lista.append(int(input("dame el numero {}: ".format(i))))
          print(i)
          if self.lista[self.c]%2 == 0:
            self.par.append(self.lista[self.c])
          else: 
             self.impar.append(self.lista[self.c])
          i -= 1
          self.c = self.c + 1
        
        self.lista.sort()
        self.par.sort()
        self.impar.sort()
        print("lista ordenada: {}".format(self.lista))
        print("lista con pares: {}".format(self.par))
        print("lista con impares: {}".format(self.impar))
        
        for n in self.lista:
            if n != self.aux:
              if self.lista.count(n) > 1:
                
                print("el numero {} se repite {} veces".format(n, self.lista.count(n)))
            self.aux = n; 

def main():
  obj=Lista(int(input("cuantos números?")))
  obj.obtener()

if __name__=="__main__":
  main()
  