from flask import Flask, render_template
from models import Restaurante, Especialista


app = Flask(__name__)

# Especialistas
junior = Especialista("Junior", "Demorou no atendimento, porém a comida é muito boa.")
nascimento = Especialista("Nascimento", "Restaurante nota 10.")
guimaraes = Especialista("Guimarães", "Comida boa e com preço justo.")

# Restaurantes
restaurante_sputnik = Restaurante(0, "Sputnik Vassouras", "../static/img/restaurante0.jpg", "Av. Exp.Osvaldo de Almeida Ramos, 86 Avenida expedicionário Osvaldo de Almeida Ramos 86, Vassouras, Estado do Rio de Janeiro 27700-000 Brasil", "07:00 / 18:00", junior)
restaurante_hipolito = Restaurante(1, "Hipolito", "../static/img/restaurante1.jpg", "Rua Barao de Tingua 33, Vassouras, Estado do Rio de Janeiro 27700-000 Brasil", "11:00 / 23:00", nascimento)
restaurante_varandas = Restaurante(2, "Varandas", "../static/img/restaurante2.jpg.", "Av Exp Oswaldo de Almeida Ramos 110, Vassouras, Estado do Rio de Janeiro 27700-000 Brasil", "12:00 / 00/00", guimaraes)

# Listas dos restaurantes
restaurante_lista = [restaurante_sputnik, restaurante_hipolito, restaurante_varandas]

# Rotas
@app.route('/')
def home():
    return render_template ('index.html', restaurantes=restaurante_lista)
    
    
@app.route('/restaurante/<int:id>')
def exibir_restaurante(id):
    for restaurante in restaurante_lista:
        if restaurante.get_id() == int(id):
            return render_template("restaurante.html", restaurante=restaurante_lista[int(id)])
    return render_template ('index.html', restaurantes=restaurante_lista)
