from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/clientes')
def clientes():
    # Criando um dataframe de exemplo
    data = {
        'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
        'Idade': [23, 35, 30, 42],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador']
    }
    df = pd.DataFrame(data)
    
    # Renomeando colunas
    df = df.rename(columns={
        'Nome': 'Cliente',
        'Idade': 'Anos de Vida',
        'Cidade': 'Localização'
    })
    
    # Renomeando os índices das linhas (opcional)
    df.index = [f'ID-{i+1}' for i in df.index]

    # Convertendo o dataframe para HTML
    table_html = df.to_html(classes='table table-striped')

    # Renderizando o template com o dataframe modificado
    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
