from flask import Blueprint, request 
from flask import render_template 

blue = Blueprint("print", "__name__")

@blue.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        # getting the user data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')

        return render_template('display.html',
            name = name, email = email, phone = phone
        )
        
    return render_template('index.html')
