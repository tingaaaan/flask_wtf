from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError
from wtforms.fields.html5 import EmailField

class FormRegister(Form):
   """ 依照Model來建置相對應的Form  """
   username = StringField('使用者名稱', validators=[
       validators.DataRequired(),
       validators.Length(8, 30)
   ])
   email = EmailField('Email', validators=[
       validators.DataRequired(),
       validators.Length(1, 50),
       validators.Email()
   ])
   password = PasswordField('密碼', validators=[
       validators.DataRequired(),
       validators.Length(5, 10),
       validators.EqualTo('password2', message='密碼需要符合上欄輸入')
   ])
   password2 = PasswordField('密碼（請重複一次）', validators=[
       validators.DataRequired()
   ])
   submit = SubmitField('建立帳號')