import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Dados de exemplo (vendas por mês)
dados = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'],
    'Vendas': [10000, 12000, 11000, 13000, 11500, 14000]
}

# Criar DataFrame com os dados
df_vendas = pd.DataFrame(dados)

# Inicializar a aplicação Dash
app = dash.Dash(__name__)

# Layout da dashboard
app.layout = html.Div([
    html.H1('Dashboard de Vendas'),
    dcc.Graph(
        id='grafico-vendas',
        figure=px.bar(df_vendas, x='Mês', y='Vendas', title='Vendas por Mês')
    ),
    html.Div([
        html.Label('Selecione o mês:'),
        dcc.Dropdown(
            id='dropdown-mes',
            options=[
                {'label': 'Janeiro', 'value': 'Janeiro'},
                {'label': 'Fevereiro', 'value': 'Fevereiro'},
                {'label': 'Março', 'value': 'Março'},
                {'label': 'Abril', 'value': 'Abril'},
                {'label': 'Maio', 'value': 'Maio'},
                {'label': 'Junho', 'value': 'Junho'}
            ],
            value='Janeiro'
        ),
        html.Div(id='selecao-mes')
    ])
])

# Callback para atualizar a seleção do mês
@app.callback(
    dash.dependencies.Output('selecao-mes', 'children'),
    [dash.dependencies.Input('dropdown-mes', 'value')]
)
def atualizar_vendas_mes(mes_selecionado):
    vendas_mes = df_vendas[df_vendas['Mês'] == mes_selecionado]['Vendas'].values[0]
    return f'As vendas em {mes_selecionado} foram de ${vendas_mes}.'

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
