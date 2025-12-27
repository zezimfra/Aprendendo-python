from flask import Flask, render_template, request

app = Flask(__name__)

itens = []
valores = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form.get('item')
        valor = float(request.form.get('valor'))
        

        itens.append(item)
        valores.append(valor)
    
    total = sum(valores)
    quantidade = len(itens)
    

    return render_template('index.html', lista_itens=itens, lista_valores=valores, total=total, qtd=quantidade)

if __name__ == '__main__':
    app.run(debug=True)
valores = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item = request.form.get('item')
        valor = float(request.form.get('valor'))
        
        itens.append(item)
        valores.append(valor)
    
    total = sum(valores)
    quantidade = len(itens)
    
    # Envia os dados para o HTML
    return render_template('index.html', lista_itens=itens, lista_valores=valores, total=total, qtd=quantidade)

if __name__ == '__main__':

    app.run(debug=True)
