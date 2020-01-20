import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer
import os


def load_libpono():
    """Carlo De Franchis's load_config function adapted to this wrapper.
    """

    working_directory_path = os.path.realpath(__file__)
    path = '/'.join(working_directory_path.split('/')[:-1])

    paths = {'libpono': os.path.join(path, 'ponomarenko', 'libpono.so')}

    for lib in paths.values():
        if not os.path.isfile(lib):
            raise FileNotFoundError(
                'Cannot find lib %s, please check this path' % lib)


    libpono = ctypes.CDLL(paths['libpono'])
    libpono.ponomarenko_c.argtypes = (
            ndpointer(dtype=ctypes.c_float, flags='C_CONTIGUOUS'),  # image
            ctypes.c_int,  # width
            ctypes.c_int,  # height
            ctypes.c_int,  # w: block side
            ctypes.c_float,  # p: percentile
            ctypes.c_int,  # num_bins: number of bins
            ctypes.c_int,  # D: filtering distance
            ctypes.c_int,  # curve_filter_iterations: filter curve iterations
            ctypes.c_int,  # mean_method: Mean computation method
            ctypes.c_bool,  # remove_equal_pixels_blocks: Flag to remove them
            ndpointer(dtype=ctypes.c_float),
            ndpointer(dtype=ctypes.c_float))

    return libpono


def estimate_noise(image, w=8, p=0.005, remove_equal_pixels_blocks=False,
                   num_bins=3, D=7, curve_filter_iterations=5, mean_method=2,
                   libpono=load_libpono()):
    """Ponomarenko. Python wraper around Miguel Colom code.

    C implementation: (c) 2012 Miguel Colom. Under license GNU GPL.
    Command-line program gives the following indications:

        ponomarenko: Ponomarenko SD noise estimation algorithm

        usage: ponomarenko [-w w] [-p p] [-r] [-b b] [-D D] [-g g] [-m m] input
                -w  w    Block side (Default: 8)
                -p  p    Percentile (Default: 0.005)
                -r       Flag to remove equal pixels
                -b  b    Number of bins (Default: 0)
                -D  D    Filtering distance (Default: 7)
                -g  g    Filter curve iterations (Default: 5)
                -m  m    Mean computation method (Default: 2)
                input    input file

    Args:
        image (2D np array): image on which to estimate the noise
        w (int) block side
        p (float): percentile
        remove_equal_pixels_blocks (bool): flag to remove equal pixels blocks
        num_bins (int): number of bins
        D (int): filtering distance
        curve_filter_iterations (int): filter curve iterations
        mean_method (int): mean computation method
        libpono (str): don't touch!

    Return:
        (bin_mean, bin_std): tuple with two lists. bin_mean contains the center
                of the bins and bin_std the standard-deviation of the noise in
                the bin.
    """

    assert image.ndim == 2, 'input must be a gray image'

    image = image.astype(np.float32)
    height, width = image.shape

    bin_mean = np.zeros((num_bins,), dtype=np.float32, order='C')
    bin_std = np.zeros(bin_mean.shape, dtype=np.float32, order='C')

    libpono.ponomarenko_c(image, width, height, w, p, num_bins, D,
                          curve_filter_iterations, mean_method,
                          remove_equal_pixels_blocks,
                          bin_mean, bin_std)

    return bin_mean, bin_std

