import streamlit as st import numpy as np import pandas as pd import plotly.graph_objects as go

st.set_page_config(page_title="AI Energy-Adaptive Data Center", layout="wide")

st.title("⚡ AI-Powered Energy-Adaptive Data Center Demo") st.markdown("Simulating how AI balances grid fluctuations with compute workloads")

--- Sidebar Controls ---
st.sidebar.header("Simulation Controls") steps = st.sidebar.slider("Time Steps", 50, 200, 100) base_workload = st.sidebar.slider("Base Workload", 50, 150, 80) battery_capacity = st.sidebar.slider("Battery Capacity", 50, 200, 100) ai_enabled = st.sidebar.toggle("Enable AI Control", True)

--- Generate Energy Data ---
time = np.arange(steps) solar = np.sin(time/10) * 40 + 50 wind = np.random.normal(40, 8, size=steps)

Introduce disturbance
wind[int(steps0.4):int(steps0.6)] *= 0.3

--- Simulation Variables ---
workload = base_workload battery = battery_capacity

solar_series = [] wind_series = [] workload_series = [] battery_series = [] grid_stability = []

for t in range(steps): total_energy = solar[t] + wind[t] + battery * 0.1

# AI Decision
if ai_enabled:
    if total_energy < workload:
        workload *= 0.9
    elif total_energy > workload:
        workload *= 1.05

# Battery response
deficit = workload - (solar[t] + wind[t])
if deficit > 0:
    discharge = min(deficit, battery)
    battery -= discharge
else:
    battery += min(abs(deficit)*0.3, battery_capacity - battery)

stability = 1 - abs(deficit)/100

solar_series.append(solar[t])
wind_series.append(wind[t])
workload_series.append(workload)
battery_series.append(battery)
grid_stability.append(stability)
--- Charts ---
col1, col2 = st.columns(2)

with col1: st.subheader("Energy vs Workload") fig1 = go.Figure() fig1.add_trace(go.Scatter(y=solar_series, name="Solar")) fig1.add_trace(go.Scatter(y=wind_series, name="Wind")) fig1.add_trace(go.Scatter(y=workload_series, name="Workload")) st.plotly_chart(fig1, use_container_width=True)

with col2: st.subheader("Battery Level") fig2 = go.Figure() fig2.add_trace(go.Scatter(y=battery_series, name="Battery")) st.plotly_chart(fig2, use_container_width=True)

st.subheader("Grid Stability Index") fig3 = go.Figure() fig3.add_trace(go.Scatter(y=grid_stability, name="Stability")) st.plotly_chart(fig3, use_container_width=True)

--- KPI Metrics ---
col3, col4, col5 = st.columns(3)

col3.metric("Final Workload", round(workload_series[-1], 2)) col4.metric("Final Battery", round(battery_series[-1], 2)) col5.metric("Grid Stability", f"{round(grid_stability[-1]*100,2)}%")

st.markdown("---") st.markdown("### 💡 Demo Insight")

if ai_enabled: st.success("AI dynamically adjusted workloads to stabilize the grid and optimize energy usage.") else: st.error("Without AI, the system is less stable and more prone to imbalance.")

st.markdown("---") st.caption("Prototype for Greenko & AM Green – AI-driven grid balancing for AI data centers")