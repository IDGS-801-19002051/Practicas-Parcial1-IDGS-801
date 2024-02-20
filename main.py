from flask import Flask, render_template, request
import forms
import math
from io import open
app=Flask(__name__)


@app.route("/")
def operas():
  return render_template("OperaBas.html")

@app.route("/textos", methods=["GET","POST"])
def textos():
  texto_clase=forms.TextForm1(request.form)
  texto_clase2=forms.TextForm2(request.form)
  
  if request.method=="POST" and texto_clase.validate():
    val1=texto_clase.text1.data
    val2=texto_clase.text2.data
    arg=val1+" "+val2+"\n"
    archivo1=open("archivo.txt","a")
    archivo1.write(arg)
    archivo1.close()
  return render_template("texto.html",form=texto_clase, form2=texto_clase2)

@app.route("/textosb", methods=["GET","POST"])
def textosb():
  texto_clase=forms.TextForm1(request.form)
  texto_clase2=forms.TextForm2(request.form)
  val = "valor no encontrado"
  sep = ""
  if request.method=="POST" and texto_clase2.validate():
    val1=texto_clase2.busc.data
    val2=texto_clase2.rad.data
    archivo1=open("archivo.txt","r")
    for line in archivo1.readlines():
      if line.find(val1) != -1:
        sep = line.split(sep=" ")
        print(sep[val2-1])
        val = sep[val2-1]
    archivo1.close()
  return render_template("texto.html",form=texto_clase, form2=texto_clase2, val=val)

@app.route("/resistencia", methods=["GET","POST"])
def resistencia(): 
  resistencia_clase=forms.ResisForm(request.form)
  if request.method=="POST":
    val1=resistencia_clase.val1.data
    val2=resistencia_clase.val2.data
    val3=resistencia_clase.val3.data
    val4=resistencia_clase.val4.data
    colors=["Negro","Cafe","Rojo","Naranja","Amarillo","Verde","Azul","Violeta","Gris","Blanco"]
    colors2={1:"Negro",10:"Cafe",100:"Rojo",1000:"Naranja",10000:"Amarillo",100000:"Verde",1000000:"Azul",10000000:"Violeta",100000000:"Gris",1000000000:"Blanco"}  
    colorseng = ["Black","Brown","Red","Orange","yellow","Green","Blue","Violet","Grey","White"]
    colors2eng={1:"Black",10:"Brown",100:"Red",1000:"Orange",10000:"yellow",100000:"Green",1000000:"Blue",10000000:"Violet",100000000:"Grey",1000000000:"White"}
    coltol={5:"Gold",10:"Silver"}
    valt= int(str(val1)+str(val2)) * int(val3)
    valmin= valt - ((valt*val4)/100)
    valmax= valt + ((valt*val4)/100)
    valtem=val4
    if val4==5:
      val4= "Dorado "+str(val4)+"%"
    elif val4==10:
      val4= "Plateado "+str(val4)+"%"
    return render_template("resistencia.html", form=resistencia_clase, val1=colors[val1],val2=colors[val2],val4=val4, val3=colors2[val3], valt=valt, valmin=valmin, valmax=valmax, bg1=colorseng[val1],bg2=colorseng[val2],bg3=colors2eng[val3],bg4=coltol[valtem])
  else:
    return render_template("resistencia.html", form=resistencia_clase)

@app.route("/distancia", methods=["GET","POST"])
def distancia():
  distancia_clase=forms.UserForm(request.form)
  if request.method=="POST":
    dis1=distancia_clase.x1.data
    dis2=distancia_clase.x2.data
    dis3=distancia_clase.y1.data
    dis4=distancia_clase.y2.data
    dist=math.sqrt(((dis2-dis1)** 2) + ((dis4-dis3)** 2))
    print(dist)
    return render_template("distancia.html", form=distancia_clase, dist=dist)
  else:
    return render_template("distancia.html", form=distancia_clase)


@app.route("/resultado", methods=["GET","POST"])
def result():
    if request.method=="POST":
      num1=request.form.get("n1")
      num2=request.form.get("n2")
      opt=request.form.get("tipo")
      if opt == "1":
        return"la suma de {} + {} es: {}".format(num1, num2, str(int(num1)+int(num2)))
      elif opt== "2":
        return"la resta de {} - {} es: {}".format(num1, num2, str(int(num1)-int(num2)))
      elif opt== "3":
        return"la multiplicación de {} * {} es: {}".format(num1, num2, str(int(num1)*int(num2)))
      elif opt== "4":
        return"la division de {} entre {} es: {}".format(num1, num2, str((int(num1)/int(num2))))
      elif opt== "5":
        return"la division exacta de {} entre {} es: {}".format(num1, num2, str(int(num1)//int(num2)))
      elif opt== "6":
        return"la potencia de {} sobre {} es: {}".format(num1, num2, str(int(num1)**int(num2)))
      else:
        return"error"
      
    
if __name__=="__main__":
  app.run(debug=True)
  