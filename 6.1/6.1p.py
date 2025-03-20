import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import plotly.express as px

# Load gyroscope data from CSV
DATA_FILE = "gyroscope_data.csv"  # Change to your actual file

def load_data():
    return pd.read_csv(DATA_FILE)

df = load_data()

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the Dash app
app.layout = html.Div([
    html.H1("Gyroscope Data Visualization"),
    
    # Dropdown for selecting graph type
    html.Label("Select Graph Type:"),
    dcc.Dropdown(
        id="graph-type",
        options=[
            {"label": "Scatter Plot", "value": "scatter"},
            {"label": "Line Chart", "value": "line"},
            {"label": "Distribution Plot", "value": "histogram"}
        ],
        value="line",
        clearable=False
    ),
    
    # Dropdown for selecting data variables
    html.Label("Select Gyroscope Data Variables:"),
    dcc.Dropdown(
        id="axis-selection",
        options=[
            {"label": "X-Axis", "value": "x"},
            {"label": "Y-Axis", "value": "y"},
            {"label": "Z-Axis", "value": "z"}
        ],
        value=["x", "y", "z"],
        multi=True
    ),
    
    # Input box for number of samples
    html.Label("Number of Samples to Display:"),
    dcc.Input(id="num-samples", type="number", value=100, min=10, step=10),
    
    # Navigation buttons
    html.Button("Previous", id="prev-btn", n_clicks=0),
    html.Button("Next", id="next-btn", n_clicks=0),
    
    # Graph output
    dcc.Graph(id="gyro-graph"),
    
    # Data Summary Table
    html.H2("Statistical Summary"),
    html.Div(id="summary-table")
])

# Callback to update graph and summary
df_index = 0  # Global index to track data window

@app.callback(
    [Output("gyro-graph", "figure"), Output("summary-table", "children")],
    [Input("graph-type", "value"),
     Input("axis-selection", "value"),
     Input("num-samples", "value"),
     Input("prev-btn", "n_clicks"),
     Input("next-btn", "n_clicks")]
)
def update_graph(graph_type, selected_axes, num_samples, prev_clicks, next_clicks):
    global df_index
    
    # Determine slice of data to show
    total_samples = len(df)
    df_index = max(0, min(df_index + (next_clicks - prev_clicks) * num_samples, total_samples - num_samples))
    data_subset = df.iloc[df_index:df_index + num_samples]
    
    # Create graph
    if graph_type == "scatter":
        fig = px.scatter(data_subset, x=data_subset.index, y=selected_axes, title="Gyroscope Data Scatter Plot")
    elif graph_type == "line":
        fig = px.line(data_subset, x=data_subset.index, y=selected_axes, title="Gyroscope Data Line Chart")
    else:  # Histogram
        fig = px.histogram(data_subset, x=selected_axes, title="Gyroscope Data Distribution")
    
    # Compute summary statistics
    summary = data_subset[selected_axes].describe().round(2).to_html()
    return fig, html.Div([html.Table([html.Tr([html.Td(summary)])])])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)