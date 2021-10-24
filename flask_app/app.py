import os
from flask import Flask, render_template, g, flash, request, session, url_for,send_file,make_response
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from db import close_db, get_db

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/', methods=('GET', 'POST'))
@app.route('/login', methods=('GET', 'POST'))
def login():
    # return render_template('Mockup1.html')
    #TODO
    try:
        if request.method == 'POST':
            print("Antes de db")
            db = get_db()
            error = None
            username = request.form['username']
            password = request.form['password']
            if not username:
                error = 'Debes ingresar el username'
                flash(error)
                return render_template('Mockup1.html')

            if not password:
                error = 'Contraseña requerida'
                flash(error)
                return render_template('Mockup1.html')
            print("Antes de base de datos")
            # user = db.execute(
            #     'SELECT * FROM usuario WHERE username = ?', (username)).fetchone()
            user = db.execute(
                'SELECT * FROM usuario WHERE username = ? AND contrasena = ? ', (username, password)
            ).fetchone()
            
            contrasena_almacenada=user[3]
            # resultado=check_password_hash(contrasena_almacenada,password)
            # flash(resultado)
            print("Antes del if")
            if (user is None or contrasena_almacenada != password):
                error = 'Consulta realizada: Usuario o contraseña inválidos'
                print('Consulta realizada: Usuario o contraseña inválidos')
                return render_template('Mockup2.html')
            else:
                error = 'Consulta realizada: Usuario valido'
                session.clear()
                session["user_id"]=user[1]
            #     resp = make_response( redirect( url_for('inicio')))
            #     resp.set_cookie( 'username', username )
            # flash(error)
        return render_template('Mockup1.html')
    except:
        return render_template('Mockup1.html')


@app.route('/registro', methods=('GET', 'POST'))
def registro():
    #TODO
    try:
        if request.method=='POST':
            print("inicia")
            nombre=request.form['fullname']
            username=request.form['username']
            password=request.form['password']
            celular=request.form['phonenumber']
            correo=request.form['email']
            # pais=request.form['country']
            # ciudad=request.form['city']
            direccion=request.form['address']
            # informacion_adicional=request.form['aditional_information']
            error=None
            db = get_db()
            print("base de datos conectada")
            
            if error is not None:
                return render_template("Mockup1.html")
            else:
                db.execute(
                     'INSERT INTO usuario (nombre_completo, username, contrasena, celular, correo, direccion) VALUES (?,?,?,?,?,?)',
                     (nombre, username, generate_password_hash (password), celular, correo, direccion,) 
                )
                db.commit()
                # yag = yagmail.SMTP('wpprueba.prueba0123456@gmail.com', 'prue0123%&/')
                # yag.send(to=correo, subject='Activa tu cuenta',
                #        contents='Bienvenido, usa este link para activar tu cuenta y ser parte de nuestros huespedes del Hotel Swissotel The Stamford')
                # flash('Revisa tu correo para activar tu cuenta')
                # return render_template('Mockup1.html')
        return render_template('Mockup2.html')
    except:
       return render_template('Mockup2.html')


@app.route('/inicio', methods=('GET', 'POST'))
def inicio():
    #TODO
    return render_template('Mockup3.html')

@app.route('/producto/añadir', methods=('GET', 'POST'))
def añadirProducto():
    #TODO
    return render_template('Mockup4.html')

@app.route('/producto/editar', methods=('GET', 'POST'))
def editarProducto():
    #TODO
    return render_template('Mockup5.html')

@app.route('/producto/eliminar', methods=('GET', 'POST'))
def eliminarProducto():
    #TODO
    return render_template('Mockup6.html')

@app.route('/producto/calificar', methods=('GET', 'POST'))
def calificarProducto():
    #TODO
    return render_template('Mockup7.html')

@app.route('/administrar', methods=('GET', 'POST'))
def administrar():
    #TODO
    return render_template('Mockup8.html')

@app.route('/lista/deseos', methods=('GET', 'POST'))
def listaDeseos():
    #TODO
    return render_template('Mockup9.html')

@app.route('/comentarios', methods=('GET', 'POST'))
def comentarios():
    #TODO
    return render_template('Mockup10.html')

if __name__=='__main__':
    app.run(debug=True)