from wtforms import Form
from wtforms import StringField, FloatField, SelectField, RadioField

class UserForm(Form):
  x1=FloatField("x1")
  x2=FloatField("x2")
  y1=FloatField("y1")
  y2=FloatField("y2")
  
class ResisForm(Form):
  val1 = SelectField('Primera banda', choices=[(0,'Negro'), (1,'Cafe'), (2,'Rojo'),(3,'Naranja'),(4,'Amarillo'),(5,'Verde'),(6,'Azul'),(7,'Violeta'),(8,'Gris'),(9,'Blanco')],default=1,coerce=int)
  val2 = SelectField('Segunda Banda', choices=[(0,'Negro'), (1,'Cafe'), (2,'Rojo'),(3,'Naranja'),(4,'Amarillo'),(5,'Verde'),(6,'Azul'),(7,'Violeta'),(8,'Gris'),(9,'Blanco')],default=1,coerce=int)
  val3 = SelectField('Tercera banda', choices=[(1,'Negro'), (10,'Cafe'), (100,'Rojo'),(1000,'Naranja'),(10000,'Amarillo'),(100000,'Verde'),(1000000,'Azul'),(10000000,'Violeta'),(100000000,'Gris'),(1000000000,'Blanco')],default=1,coerce=int)
  val4 =  RadioField('Tolerancia', choices=[
        (5,'Oro'), (10,'Plata')],
        default=1, coerce=int)
  