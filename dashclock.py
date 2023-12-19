from dash import Dash, html
import dash_daq as daq
import pendulum
import dash_bootstrap_components as dbc

# cidades no mundo
cidades = [
    ["São Paulo", pendulum.now(tz='America/Sao_Paulo')],
    
    
    ["Melbourne", pendulum.now(tz='Australia/Melbourne')],
    ["Vancouver", pendulum.now(tz='America/Vancouver')],
    ["New York", pendulum.now(tz='America/New_York')],
    ["London", pendulum.now(tz='Europe/London')],
    ["Paris", pendulum.now(tz='Europe/Paris')],
    ["Calcutta", pendulum.now(tz='Asia/Calcutta')],
    ["Shanghai", pendulum.now(tz='Asia/Shanghai')],
    ["Tokyo", pendulum.now(tz='Asia/Tokyo')],
]

# ---- layout ---- #
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

topo = dbc.Row(
    [    
        dbc.Col(
            [html.H1("Horários no mundo")], width=12),
        dbc.Col(
            [html.H5("by @italomarcelogit")], width=12),
        dbc.Col(
            [html.Div("Find current time around the world. By @italomarcelogit")], width=12),
        
    ], justify='center')
cores = ["#689F38"]
[cores.append("#455A64") for x in range(1, len(cidades))]
bgcores = ["#F1F8E9"]
[bgcores.append("#fff") for x in range(1, len(cidades))]
relogios  =dbc.Row(
    [
        dbc.Col(
            [
                daq.LEDDisplay
                (
                    color=cores[field],
                    backgroundColor=bgcores[field],
                    label=cidades[field][0],
                    labelPosition='bottom',
                    value=cidades[field][1].strftime("%H:%M")
                )
            ], width=4
        ) for field in range(0, len(cidades))
        
    ])
   

app.layout = dbc.Container(
[
    topo,
    dbc.Row(
    [
        dbc.Col([html.Br(), ], width=12) for field in range(3)
    ]),
    
    relogios
])


if __name__ == '__main__':
    app.run(debug=True)
