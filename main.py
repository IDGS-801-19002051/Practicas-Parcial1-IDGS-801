from flask import Flask, render_template, request
import forms
import math
app=Flask(__name__)


@app.route("/")
def operas():
  return render_template("OperaBas.html")

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
  