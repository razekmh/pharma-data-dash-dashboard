# import pandas as pd
from dash import Dash, dcc, html, page_container, dcc, clientside_callback, ClientsideFunction, Output, Input

class MainApplication:
    def __init__(self):
        self.__app = Dash(
            __name__,
            update_title="Loading...",
            use_pages=True,
        )


    @property
    def app(self):
        return self.__app


Application = MainApplication()
app = Application.app.server








# data = (
#     pd.read_csv("pharma_data.csv")
#     .query("type == 'conventional' and region == 'Albany'")
#     .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
#     .sort_values(by="Date")
# )

# app = Dash(__name__)

# app.layout = html.Div(
#     children=[
#         html.H1(children="Avocado Analytics",
#                 style={"fontSize": "48px", "color": "red"},
#                 ),
        
#         html.P(
#             children=(
#                 "Analyze the behavior of avocado prices and the number"
#                 " of avocados sold in the US between 2015 and 2018"
#             ),
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": data["Date"],
#                         "y": data["AveragePrice"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Average Price of Avocados"},
#             },
#         ),
#         dcc.Graph(
#             figure={
#                 "data": [
#                     {
#                         "x": data["Date"],
#                         "y": data["Total Volume"],
#                         "type": "lines",
#                     },
#                 ],
#                 "layout": {"title": "Avocados Sold"},
#             },
#         ),
#     ]
# )

# if __name__ == "__main__":
#     app.run_server(debug=True)