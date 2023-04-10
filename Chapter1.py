import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.DARKLY])

# app.layout=html.Div([
#     html.H1('Hello world!')
# ])

app.layout = (
              dbc.Col([
                       html.Div(children=[
                                          html.H1("App_0: Hello world",
                                           style = {
                                                'fontSize':'40px',
                                                # 'color':'red',
                                                'text-align':'center',
                                                'font-style':'italic',
                                                'marginTop':'20px'
                                             }),

                                           html.H2(children=" Example:The world Bank",
                                                   style={
                                                          'fontSize':'40px',
                                                          'color':'red',
                                                          'text-align':'center',
                                                          'font-style': 'italic'
                                                          }),

                                           dbc.Tabs([
                                                        dbc.Tab([
                                                            html.Ol([
                                                                html.Br(),
                                                                html.Li("Number of economies: 170"),
                                                                html.Li("Temporal Coverage: 1974 - 2019"),
                                                                html.Li('Update Frequency: Quarterly'),
                                                                html.Li('Last Updated: March 18, 2020'),
                                                                html.Li('Example from book:'),
                                                                html.A( 'Элиас Даббас.Интерактивные дашборды и приложения с Plotly и Dash.2022',
                                                                    href='https://paraknig.me/view/1836817')
                                                            ]),
                                                            html.P('Source:'),
                                                            html.A( 'https://datacatalog.worldbank.org/dataset/poverty-andequity-database',
                                                                    href='https://datacatalog.worldbank.org/dataset/povertyand-equity-database')
                                                        ],label="Some Facts about World Bank"),
                                                       dbc.Tab([
                                                           html.Ul([
                                                               html.Br(),
                                                               html.Li("Created: 08/03/2023 "),
                                                               html.Li("Creator:Shtefko Sergey"),
                                                               html.Li('Social link:'),
                                                               html.A('VK',
                                                                       href='http://vk.com/geone')
                                                           ])
                                                       ], label="Project Info"),
                                               ])
                                          ])


             ],lg = {'size':8,'offset':2},md =12)  # Div кладется в Col и редактируется позиция на экране по 12 равным столбцам (md,lg -размеры экранов)
)

if __name__ == '__main__':
    app.run_server(debug = True)