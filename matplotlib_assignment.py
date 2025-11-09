import matplotlib.pyplot as plt
import numpy as np


x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]
plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")   
plt.close()


students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]
plt.bar(students, marks, color=['green', 'blue', 'purple', 'orange'])
plt.title("Marks Scored by Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("bar_graph.png")
plt.close()


regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]
explode = [0.1 if r == max(revenue) else 0 for r in revenue]
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Company Revenue Distribution")
plt.savefig("pie_chart.png")
plt.close()

data = np.random.randint(1, 101, 1000)
plt.hist(data, bins=20, edgecolor='black')
plt.title("Frequency Distribution of Random Integers (1–100)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.close()
