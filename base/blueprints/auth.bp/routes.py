from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from flask_login import login_required, login_user, logout_user

from database import *

auth_bp = Blueprint("auth", __name__)
auth_bp.secret_key = 'acai'

login_manager.init_app(auth_bp)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get('nome')
        email = request.form.get('email')

        senha = request.form.get('senha')
        hash = generate_password_hash(senha)

        conexao = sqlite3.connect('banco.db')
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO usuarios(nome, email, senha)
            VALUES (?, ?, ?)
        """, (nome, email, hash))

        conexao.commit()
        conexao.close()

        flash("Complete o cadastro usando database.py e generate_password_hash.")
        return redirect(url_for("auth.registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
@login_required
def login():
    if request.method == "POST":
        email = request.form.get('login')
        senha = request.form.get('senha')
        flash("Complete o login usando check_password_hash e session.")
        return redirect(url_for("auth.login"))

    return render_template("login.html")



@auth_bp.route("/logout")
@login_required
def logout(): 
    flash("Complete o logout removendo os dados da session.")
    return redirect(url_for("auth.login"))