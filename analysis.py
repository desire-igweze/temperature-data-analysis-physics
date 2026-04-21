import numpy as np
import matplotlib.pyplot as plt

# Generate time (0–24 hours)
time = np.linspace(0, 24, 100)

# Simulated temperature data (sinusoidal + noise)
temperature = 25 + 5*np.sin((2*np.pi/24)*time) + np.random.normal(0, 0.5, len(time))

# Line plot (temperature vs time)
plt.figure()
plt.plot(time, temperature)
plt.title("Temperature Variation Over Time")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.savefig("temperature_plot.png")
plt.show()

# Histogram (distribution)
plt.figure()
plt.hist(temperature, bins=15)
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.grid()
plt.savefig("histogram.png")
plt.show()

# Statistics
mean_temp = np.mean(temperature)
max_temp = np.max(temperature)
min_temp = np.min(temperature)

print("Mean Temperature:", mean_temp)
print("Max Temperature:", max_temp)
print("Min Temperature:", min_temp)
