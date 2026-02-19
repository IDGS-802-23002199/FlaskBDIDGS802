from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField
from wtforms import validators
from wtforms import Form, IntegerField, StringField, RadioField
from wtforms.validators import DataRequired, NumberRange

class UserForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre', [validators.DataRequired(message="El campo es requerido"),
                                        validators.NumberRange(min=100, max=1000, message='Ingrese un valor valido')
                                        ])
    nombre=StringField('Nombre', [validators.DataRequired(message="El campo es requerido"),
                                        validators.length(min=3, max=10, message='Ingrese nombre valido')
                                        ])
    apaterno=StringField('Apaterno',[validators.DataRequired(message="El campo es requerido")
                                        ])
    amaterno=StringField('Amaterno',[validators.DataRequired(message="El campo es requerido")
                                        ])
    correo=EmailField('Correo',[validators.Email(message="Ingrese un correo valido")
                                        ])