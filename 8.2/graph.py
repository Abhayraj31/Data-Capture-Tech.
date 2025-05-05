# accelerometer_dashboard.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# Configuration
DATA_DIR = "accelerometer_data"
CSV_FILENAME = "all_accelerometer_data.csv"
DATA_PATH = os.path.join(DATA_DIR, CSV_FILENAME)
REFRESH_INTERVAL = 1000  # Update every 1 second

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real-time Accelerometer Data Dashboard", 
           style={'textAlign': 'center', 'color': '#2c3e50'}),
    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='interval-component',
        interval=REFRESH_INTERVAL,
        n_intervals=0
    )
])

def load_accelerometer_data():
    """Load data from CSV file with error handling"""
    if not os.path.exists(DATA_PATH):
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(DATA_PATH)
        # Convert timestamp to datetime and sort
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.sort_values('Timestamp', inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return pd.DataFrame()

@app.callback(
    Output('live-graph', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    df = load_accelerometer_data()
    
    if df.empty:
        return px.scatter(title="Waiting for data...")
    
    # Create interactive plot
    fig = px.line(df, 
                 x='Timestamp', 
                 y=['X', 'Y', 'Z'],
                 title='Real-time Accelerometer Data',
                 labels={'value': 'Acceleration (m/s²)', 'variable': 'Axis'},
                 template='plotly_white')
    
    # Customize layout
    fig.update_layout(
        hovermode='x unified',
        legend_title_text='Axis',
        xaxis_title='Time',
        yaxis_title='Acceleration',
        margin=dict(l=40, r=40, t=60, b=40),
        plot_bgcolor='rgba(240,240,240,0.9)'
    )
    
    # Customize lines
    colors = {'X': '#3498db', 'Y': '#e74c3c', 'Z': '#2ecc71'}
    for trace in fig.data:
        trace.update(line=dict(color=colors[trace.name], width=1.5))
    
    return fig

if __name__ == '__main__':
    # Create data directory if it doesn't exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    print("Starting Dash server...")
    print(f"Monitoring data file: {DATA_PATH}")
    app.run_server(debug=False, port=8050)