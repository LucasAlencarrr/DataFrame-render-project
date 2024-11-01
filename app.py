from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/tabela/<nome>')
def tabela(nome):
    # Definindo dataframes com base no nome
    dataframes = {
        'clientes': pd.DataFrame({
            'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
            'Idade': [23, 35, 29, 42],
            'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador']
        }),
        'produtos': pd.DataFrame({
            'Produto': ['Notebook', 'Celular', 'Tablet', 'Monitor'],
            'Preço': ['R$ 3000', 'R$ 1500', 'R$ 700', 'R$ 800']
        })
    }

    # Obtendo o dataframe correspondente ao parâmetro
    df = dataframes.get(nome)
    if df is None:
        return "<h1>Erro: Tabela não encontrada</h1>", 404
    
    table_html = df.to_html(classes='table table-striped')
    return render_template('index.html', table=table_html, title=nome.capitalize())


if __name__ == '__main__':
    app.run(debug=True)
