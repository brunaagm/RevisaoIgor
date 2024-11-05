from flask import Flask, session, render_template, redirect, request, url_for
from controllers.questionarioController import questionarioController

app = Flask(__name__)
app.secret_kay = "brunalinda"

rotas_publicas = ["questoes.index", "questoes.verifica"]

@app.before_request #criação do middleware
def verificarIdentificação():
    if request.endpoint in rotas_publicas: # O endpoint é basicamente a junção das questoes (blueprint) com a função
        return
    
app.register_blueprint(questionarioController)

if __name__ == "__main__":
    app.run(debug=True)


