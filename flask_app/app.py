from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Aluno
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def index():
    alunos = Aluno.query.all()
    return render_template("index.html", alunos=alunos)

@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        ra = request.form["ra"]
        if not nome or not ra:
            flash("Todos os campos são obrigatórios!")
            return redirect(url_for("cadastrar"))

        aluno = Aluno(nome=nome, ra=ra)
        try:
            db.session.add(aluno)
            db.session.commit()
            flash("Aluno cadastrado com sucesso!")
            return redirect(url_for("index"))
        except:
            db.session.rollback()
            flash("Erro ao cadastrar aluno. Verifique se o RA é único.")
            return redirect(url_for("cadastrar"))

    return render_template("cadastrar.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
