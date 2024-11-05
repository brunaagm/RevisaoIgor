from flask import Blueprint, render_template, request, redirect, url_for, session

questionarioController = Blueprint("questoes", __name__) #criação blueprint

@questionarioController.route("/")
def index():
    return render_template("index.html")

@questionarioController.route("/verifica", methods = ["POST"])
def verifica():
    nome = request.form.get("nome")
    email = request.form["email"]
    if nome != "":
        if email.split("@") [1] == "aluno.isfp.edu.br":
            session["nome"] = nome #Criação da sessão
            session["email"] = email
            return redirect(url_for("questoes.questionario"))
    return redirect (url_for("questoes.index"))

@questionarioController.route("/questionario")
def questionario():
    if "nome" in session :
        return render_template("questionario.html")
    return redirect(url_for("questoes.index"))

@questionarioController.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("nome", None)
    return redirect(url_for("questoes.index"))



