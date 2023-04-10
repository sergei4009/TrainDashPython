import  dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output


app = dash.Dash(__name__)

app.layout = html.Div([
                        dcc.Dropdown( id = 'color_dropdown',
                                      options=[ {'label': color, 'value':color} for color in ['red','green','blue']
                                             ]),
                        html.Div(id = 'color_output')
                      ])

@app.callback(Output('color_output','children'),
              Input('color_dropdown','value'))

def display_selected_color(color):
    if color is None:
        color = 'nothing'
    return 'Вы выбрали цвет:',color

if __name__ == '__main__':
    app.run_server(debug = True)