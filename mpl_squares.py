import matplotlib.pyplot as plt
plt.style.available

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)
# Assigning a Chart Title and Axis Labels
ax.set_title('Square Numbers', fontsize = 24)
ax.set_xlabel('Value', fontsize = 14)
ax.set_ylabel('Square of Value', fontsize = 14)

# Assigning the font size of divisions on the axes
ax.tick_params(axis='both', labelsize = 14)

plt.show()