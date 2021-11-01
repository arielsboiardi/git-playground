import numpy as np

from bspline_lib import *

def test_partition_of_unity():
    """
    Tests weather or not B-spline basis functions form a partition of unity 
    """
    # Tests the property for B-splines of random degree, below 15, on a random 
    # knot vector with a random (below 100) number of knots
    p = np.random.randint(0,15)
    nknots = np.random.randint(2,10)
    Xi = np.sort(np.random.rand(nknots))
    Xi = np.random.randint(0,100) + np.random.randint(0,100) * Xi
    Xi = knot_pad(Xi, p)

    # We now test the property in a random point (within knot span)
    l = np.random.rand(1)
    x = (1-l) * Xi[0] + l * Xi[-1]

    # Compute the sum of the valus of B-splines @ x
    S = sum(bspline(idx, p, Xi, x) for idx in range(bspline_space_dim(p,Xi)))

    error = np.abs(1-S)

    if error >= 1e-5:
        print(p,Xi)
        print(x,error)
        plot_bspline_basis(p,Xi)
        raise Exception("Partition of unity property not respected")
    else:
        return 0