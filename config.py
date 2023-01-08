from main import app

app.config['SECRET_KEY'] = '71a998e3507079eab097eda8bcd034aa'

SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{usuario}:{senha}@{servidor}/{database}".format(
    SGBD = "postgresql",
    usuario = "postgres",
    senha = "123456",
    servidor = "localhost:5432",
    database = "postgres"
)