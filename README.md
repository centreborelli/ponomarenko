# Ponomarenko: noise curve estimation from a single image

Python bindings for Miguel Colom's implementation of the Ponomarenko et al.
method.

Version 0.0.4 -- March 23, 2020

By Charles Hessel <charles.hessel@ens-paris-saclay.fr>

The C++ code used in this repository has been peer-reviewed as part of the IPOL
publication:
> Miguel Colom, and Antoni Buades, Analysis and Extension of the Ponomarenko et
  al. Method, Estimating a Noise Curve from a Single Image, Image Processing On
  Line, 3 (2013), pp. 173–197. https://doi.org/10.5201/ipol.2013.45


## Installation

Run
```
pip install -e .
```
from the directory where `setup.py` is located.


## Usage


### As a Python module

```python
from ponomarenko import estimate_noise

bins, noise_std = estimate_noise(image)
```

The method estimates the standard-deviation of the noise (in `noise_std`) in
different intensity bins, which centers are given in the first output `bins`.

