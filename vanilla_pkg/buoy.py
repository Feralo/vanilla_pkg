import numpy as np
from urllib.request import urlretrieve
import logging


URL = "https://www.ndbc.noaa.gov/data/realtime2/{}.data_spec"
DEST = "data/{}.data_spec"


class Buoy:
    def __init__(self, identifier):
        self.identifier = identifier
        self.dates = []
        self.E = np.array([])
        self.f = np.array([])

    def get_data(self, dest=None):
        url = URL.format(self.identifier)
        if dest is None:
            dest = DEST.format(self.identifier)

        urlretrieve(url, dest)
        self.dest = dest
        return dest

    def read_data(self, dest):
        dates = []
        energies = []
        frequencies = []

        with open(dest) as fp:
            for _ in range(3):
                next(fp)

            for l in fp:
                dates.append(l.split()[0:5])
                energies.append([float(e) for e in l.split()[6::2]])
                freqs = l.split()[7::2]
                frequencies.append([float(i[1:-1]) for i in freqs])

            fp.close()

            E = np.array(energies)
            f = np.array(frequencies)
        return (E, f)

    def bootstrap(self):
        self.Emid = self.calc_midpoint(self.E)
        self.fmid = self.calc_midpoint(self.f)
        self.df = np.diff(self.f)

    def calc_swh(self):
        product = self.df * self.Emid
        return 4 * np.sqrt(product.sum(axis=1))

    def calc_midpoint(self, series):
        nofirst = series[:, 1:]
        nolast = series[:, :-1]
        mid = 0.5 * (nolast + nofirst)
        return mid
