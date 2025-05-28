
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# App title
st.title("Booking Window Bell Curve Visualizer")

# User inputs
checkin_date = st.date_input("Select Check-in Date", datetime.today())
median_window = st.slider("Median Booking Window (days)", min_value=5, max_value=60, value=20)

# Calculate range
start = median_window / 2
end = 2 * median_window
x = np.linspace(start, end, 300)
mu = median_window
sigma = (end - start) / 6
y = np.exp(-0.5 * ((x - mu)/sigma)**2)
y = y / max(y)

# Convert x values into actual dates
booking_dates = [checkin_date - timedelta(days=int(day)) for day in x]

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(booking_dates, y, label='Booking Likelihood')
ax.axvline(checkin_date - timedelta(days=median_window), color='red', linestyle='--', label='Median Booking Date')
ax.set_title(f'Booking Window Bell Curve (M={median_window}, Check-in: {checkin_date.strftime("%b %d")})')
ax.set_xlabel("Booking Date")
ax.set_ylabel("Relative Likelihood")
ax.grid(True)
ax.legend()
plt.xticks(rotation=45)

# Display plot in Streamlit
st.pyplot(fig)
