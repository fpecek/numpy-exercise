import matplotlib.pyplot as plt
import numpy as np


# Define a main() function that prints a data statistics.
def main():
    data = np.loadtxt('data/populations.txt')
    year, hares, lynxes, carrots = data.T  # trick: columns to variables

    plt.axes([0.1, 0.1, 0.5, 0.8])
    plt.plot(year, hares, year, lynxes, year, carrots)
    plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
    plt.show()

    # calculate mean and std population for each species (column) separately is slower.
    # calculating separately takes ~3.06 µs for each mean operation and on array
    # that contains all the data by axis=0 takes ~4.68 µs
    populations = data[:, 1:]
    print("Means by species: {}".format(populations.mean(axis=0)))
    print("Standard deviation by species: {}".format(populations.std(axis=0)))

    # calculate year when each species had the larges population
    max_populations = np.argmax(populations, axis=0)
    print("Max populations in years: {}".format(year[max_populations]))

    # calculate species that has larges population for each year
    max_species_idx = np.argmax(populations, axis=1)
    max_species = np.array(['H', 'L', 'C'])[max_species_idx]
    print("Max species: {}".format(tuple(zip(year, max_species))))

    # calculate years when any of the populations is above 50000
    above_mask = np.any(np.greater(populations, 50000), axis=1)
    print("Years any population above 50000: {}".format(year[above_mask]))

    # find the top 2 years for each species when they had the lowest populations
    sorted_indices = populations.argsort(axis=0)
    years_sorted = year[sorted_indices]
    print("Two smallest years: {}".format(years_sorted[:2, :]))

    # compare (plot) the change in hare population and the number of lynxes
    hare_gradients = np.gradient(hares)
    plt.axes([0.1, 0.1, 0.7, 0.8])
    plt.plot(year, hare_gradients, year, lynxes)
    plt.legend(('Hare', 'Lynx'), loc=(1.05, 0.5))
    plt.show()

    # calculate correlation
    print("Hares and lynxes correlation: {}".format(np.corrcoef(hare_gradients, lynxes)[0, 1]))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
