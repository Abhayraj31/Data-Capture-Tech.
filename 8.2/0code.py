import sys 
import traceback 
import time 
import random 
import pandas as pd 
import plotly.graph_objs as go 
import dash 
from dash import dcc, html 
from dash.dependencies import Input, Output 
from threading import Thread 

# ------------------------------- 
# Simulation parameters 
# ------------------------------- 
WINDOW_SIZE = 100 
SIMULATION_INTERVAL = 0.05  # seconds 

# ------------------------------- 
# Global buffer and figure 
# ------------------------------- 
data_buffer = {'x': [], 'y': [], 'z': [], 'time': []} 
latest_fig = go.Figure() 

# ------------------------------- 
# Smooth update function (Reusable API) 
# ------------------------------- 
def create_smooth_dash_update(data, window_size, trace_names, title, 
                              xaxis_title, yaxis_title): 
    fig = go.Figure() 
    time_axis = data.get('time', list(range(len(next(iter(data.values())))))) 

    for axis, values in data.items(): 
        if axis == 'time': 
            continue 
        fig.add_trace(go.Scatter( 
            x=time_axis[-window_size:], 
            y=values[-window_size:], 
            mode='lines', 
            name=trace_names.get(axis, axis) 
        )) 

    fig.update_layout( 
        title=title, 
        xaxis_title=xaxis_title, 
        yaxis_title=yaxis_title, 
        uirevision='constant', 
        template='plotly_dark' 
    ) 
    return fig 

# ------------------------------- 
# Dash App Layout 
# ------------------------------- 
app = dash.Dash(__name__) 
app.layout = html.Div([ 
    html.H1("Real-time Accelerometer Data (Simulation Mode)"), 

    html.Label("Select Axis to Display:"), 
    dcc.Dropdown( 
        id='axis-selector', 
        options=[ 
            {'label': 'X', 'value': 'x'}, 
            {'label': 'Y', 'value': 'y'}, 
            {'label': 'Z', 'value': 'z'}, 
            {'label': 'All Axes', 'value': 'all'} 
        ], 
        value='all', 
        multi=False, 
        style={'width': '50%'} 
    ), 

    dcc.Graph(id='accelerometer-graph', figure=latest_fig), 
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0) 
]) 

# ------------------------------- 
# Dash Callbacks 
# ------------------------------- 
@app.callback( 
    Output('accelerometer-graph', 'figure'), 
    [Input('interval-component', 'n_intervals'), 
     Input('axis-selector', 'value')] 
) 
def update_graph(n, selected_axis): 
    return update_plot(selected_axis) 

# ------------------------------- 
# Plot Update Logic 
# ------------------------------- 
def update_plot(selected_axis='all'): 
    trace_names = {'x': 'Accelerometer X', 'y': 'Accelerometer Y', 'z': 'Accelerometer Z'} 

    if selected_axis == 'all': 
        filtered_data = { 
            'time': data_buffer['time'], 
            'x': data_buffer['x'], 
            'y': data_buffer['y'], 
            'z': data_buffer['z'] 
        } 
    else: 
        filtered_data = { 
            'time': data_buffer['time'], 
            selected_axis: data_buffer[selected_axis] 
        } 

    return create_smooth_dash_update(filtered_data, WINDOW_SIZE, trace_names, 
                                     title="Accelerometer Data (Smooth Update)", 
                                     xaxis_title="Time", yaxis_title="Acceleration") 

# ------------------------------- 
# Simulated Accelerometer Stream 
# ------------------------------- 
def simulate_data(): 
    while True: 
        timestamp = time.time() 
        data_buffer['x'].append(random.uniform(-10, 10)) 
        data_buffer['y'].append(random.uniform(-10, 10)) 
        data_buffer['z'].append(random.uniform(-10, 10)) 
        data_buffer['time'].append(timestamp) 

        # Limit buffer length 
        for key in data_buffer: 
            if len(data_buffer[key]) > 1000: 
                data_buffer[key] = data_buffer[key][-1000:] 

        time.sleep(SIMULATION_INTERVAL) 

# ------------------------------- 
# Main Entrypoint 
# ------------------------------- 
if __name__ == '__main__': 
    try: 
        # Run Dash in a separate thread 
        def run_dash(): 
            app.run(debug=False, use_reloader=False, host='0.0.0.0', port=8050) 

        dash_thread = Thread(target=run_dash) 
        dash_thread.start() 

        # Start simulation thread 
        simulate_thread = Thread(target=simulate_data) 
        simulate_thread.daemon = True 
        simulate_thread.start() 

    except Exception as e: 
        print("Error occurred:", e) 
        traceback.print_exc()
