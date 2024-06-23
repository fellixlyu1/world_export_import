import matplotlib.pyplot as plt


# The 'get_scatter_plot' method will return an image of the scatter plot graph. By importing this file to main.py,
# the user will be able to provide the necessary options to create the scatter plot from the data provided
# by the database.
def get_scatter_plot(data, years, data_type, country):
    plt.figure(figsize=(40, 20))
    plt.plot(years, data, marker='o')
    plt.xlabel('Year')
    plt.ylabel(data_type)
    plt.title(f'{data_type}')
    plt.grid(True)

    # Save the plot as an image file
    image_path = f"{country}_{data_type}_scatter.png"
    plt.savefig(image_path)

    # Close the plot to free memory
    plt.close()

    return image_path


# The 'get_pie_chart' method returns an image of the pie chart data according to the country and data type.
def get_pie_chart(country, year, data, data_type):
    fig, ax = plt.subplots()
    ax.pie(data, labels=country)

    pie_path = f"{data_type}_{year}_pie.png"
    plt.savefig(pie_path)

    plt.close()

    return pie_path
