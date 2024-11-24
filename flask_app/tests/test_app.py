import pytest
import sys
import os

# Adiciona o diretório pai ao sys.path para garantir que o módulo app seja encontrado
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Aluno  # Importa o app, o banco de dados e o modelo Aluno

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Banco de dados em memória para testes
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Cria as tabelas no banco de dados
        yield client
        with app.app_context():
            db.drop_all()  # Limpa o banco de dados após os testes

def test_cadastro_aluno(client):
    # Testa o cadastro de um aluno válido
    response = client.post("/cadastrar", data={"nome": "João", "ra": "12345"})
    assert response.status_code == 302  # Redirecionamento após o cadastro
    assert Aluno.query.count() == 1  # Verifica se um aluno foi adicionado
    aluno = Aluno.query.first()
    assert aluno.nome == "João"  # Verifica o nome do aluno
    assert aluno.ra == "12345"  # Verifica o RA do aluno

def test_cadastro_ra_duplicado(client):
    # Testa o cadastro com RA duplicado
    client.post("/cadastrar", data={"nome": "João", "ra": "12345"})
    response = client.post("/cadastrar", data={"nome": "Maria", "ra": "12345"})
    assert response.status_code == 302  # Redirecionamento após tentativa de cadastro
    assert Aluno.query.count() == 1  # Verifica que apenas um aluno foi adicionado
