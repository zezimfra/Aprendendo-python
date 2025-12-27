from flask import Flask, render_template, request

app = Flask(__name__)

# Criamos as listas fora da função para elas não "resetarem" a cada clique
itens = []
valores = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário HTML
        item = request.form.get('item')
        valor = float(request.form.get('valor'))
        
        # Armazena nas listas (Igual você fez no treino!)
        itens.append(item)
        valores.append(valor)
    
    # Cálculos (Igual você fez no treino!)
    total = sum(valores)
    quantidade = len(itens)
    
    # Envia os dados para o HTML
    return render_template('index.html', lista_itens=itens, lista_valores=valores, total=total, qtd=quantidade)

if __name__ == '__main__':
    app.run(debug=True)
valores = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Captura os dados do formulário HTML
        item = request.form.get('item')
        valor = float(request.form.get('valor'))
        
        # Armazena nas listas (Igual você fez no treino!)
        itens.append(item)
        valores.append(valor)
    
    # Cálculos (Igual você fez no treino!)
    total = sum(valores)
    quantidade = len(itens)
    
    # Envia os dados para o HTML
    return render_template('index.html', lista_itens=itens, lista_valores=valores, total=total, qtd=quantidade)

if __name__ == '__main__':
    app.run(debug=True)