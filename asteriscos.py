class OperaAst:
  #declaración de propiedades
    num1=0
    ast = ""
  #declaración o definicion del constructor de la clase
    def __init__(self,a) -> None:
        self.num1=a
        self.ast="*"
        self.total=""
  #declaración de los metodos de la clase
    def construir(self):
        i = self.num1+1
        while i > 0:
          print(self.total)
          self.total = self.total + self.ast
          i -= 1

def main():
  obj=OperaAst(6)
  obj.construir()

if __name__=="__main__":
  main()
  