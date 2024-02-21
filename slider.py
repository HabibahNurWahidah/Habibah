import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Pilih rentang', 0.0, 2.0, (.2, .5))
st.write('nilai x:', x)
y = st.slider('Set nilai',0.0, 10.0, 5.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
u = np.sin(y*t)

# Calculate f(x) = 2x^2 + 9x - 2
def f(x):
    return 2*x**2 + 9*x - 2

v = f(t)

# Compute integral using trapezoidal rule
integral = np.trapz(v, t)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(t, u, label='sin(t)', color='b')  # Plotting sin(t) curve
ax.plot(t, v, label='f(t)', color='r')     # Plotting f(t) curve
ax.fill_between(t, 0, v, alpha=0.2, color='r', label='Integral')  # Fill the area under the curve for integral
ax.set_ylabel("")
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)
plt.grid(color='green', linestyle='-.', linewidth=.5)
plt.legend()  # Show legend
st.pyplot(fig)

st.write(f'Integral (using trapezoidal rule): {integral}')