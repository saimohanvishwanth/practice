#Matplotlib for Sensor Trend Visualization
#used for creating static , interactive nad animated visualization.
#trends, helping engineers analyze real-time data like temperature, speed / fuel levels

#key Feautres of MatplotLib

'''
1. Customizable Plots -> Adjust axes, labels, styles, colors, etc, o suit your data.
2. Support for Multiple Plot types -> Line Plots, scatter, plots, bar charts, histograms, etc.
3. Integration with sensor data -> Easily visulaize trends from i;lve / logged sensor data
4. Interactive Features -> Zoom, pan, and save plots as images

Steps for using matplotlib
-----------------------------
1. Install Matplotlib: Use pip install matplotlib
2. Import required modules
3. import matplotlib.pyplot as plt
4. Prepare sensor data -> gather/ simulate sensor data, like temperature readings / speed
5. Create and customize the plot -> use various plotting functions and customize labels , titles and axes

Ex:Plotting sensor trends
-----------
Here's an ex to plot vehicle temperature trends:

import matplotlib.pyplot as plt
#Simulated sensor data
time =[1,2,3,4,5]# time intervals(Seconds)
temperature = [30,35,40,42,48]#temperature readings celsius
#Create the plot
plt.plot(time, temperature, marker = 'o', color = 'blue', label = 'Temperature Trends')
plt.xlabel("Time(s)")
plt.ylabel("Temperature(celsius)")
plt.title("Engine Temperature trends")
plt.legend()
#show the plot
plt.show()

Ex: Comparing Multiple Sensor Trends
--------------------------------

Comapre different sensor readings(EX: temperature vs pressure) on same plot

import matplotlib.pyplot as plt
#simulated sensor data
time = [1,2,3,4,5]# time intervals(Seconds)
temperature = [30, 35, 40, 42, 38]#temperature readings celsius
pressure = [2,3,4,5,3] # pressure readings(bars)
#create plot
plt.plot(time, pressure, marker="o", color = "green")
plt.xlabel("Time(s)")
plt.ylabel("Pressure")
plt.title("Rate of change in pressure w.r.t Time")
plt.show()
'''