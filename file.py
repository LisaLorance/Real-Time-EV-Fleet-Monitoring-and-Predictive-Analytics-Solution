import pandas as pd
import plotly.graph_objects as go

data = {
    'Date': pd.date_range(start='2011-01-01', end='2018-01-01', freq='ME'),
    'Energy_Consumption': [i * 0.01 for i in range(1, 85)],  # Simulated small values
    'Operational_Costs': [30 + (i % 10) for i in range(1, 85)]  # Simulated large values
}
df = pd.DataFrame(data)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Energy_Consumption'],
    mode='lines+markers',
    name='Energy Consumption (MW)',
    line=dict(color='cyan', width=2),
    marker=dict(size=5),
    hovertemplate='<b>Energy Consumption:</b> %{y:.2f} MW<br><b>Date:</b> %{x}<extra></extra>'
))

fig.add_trace(go.Scatter(
    x=df['Date'], 
    y=df['Operational_Costs'],
    mode='lines+markers',
    name='Operational Costs ($)',
    line=dict(color='orange', width=2, dash='dash'),
    marker=dict(size=5),
    hovertemplate='<b>Operational Costs:</b> %{y:.2f} $<br><b>Date:</b> %{x}<extra></extra>'
))

fig.update_layout(
    title={
        'text': "Energy Consumption and Operational Costs Over Time",
        'x': 0.5,
        'xanchor': 'center',
        'font': dict(size=18, color='white')
    },
    xaxis=dict(
        title="Date",
        showgrid=False,
        tickformat='%Y-%m',
        color='white'
    ),
    yaxis=dict(
        title="Energy Consumption (MW)",
        showgrid=True,
        gridcolor='#444',
        color='white'
    ),
    yaxis2=dict(
        title="Operational Costs ($)",
        overlaying='y',
        side='right',
        showgrid=False,
        color='white'
    ),
    paper_bgcolor='black',
    plot_bgcolor='black',
    legend=dict(
        font=dict(color='white'),
        x=0.02, y=0.98
    ),
    hovermode="x unified"  # Makes hover appear for both traces at once
)

# Show the interactive graph
fig.show()


