import numpy as np
import matplotlib.pyplot as plt

def knot_pad(Xi,p):
    """
    Repeats first and last knots of Xi 
    """
    # Check on types
    assert isinstance(Xi,np.ndarray)
    # Pad knot vector with due repretitions
    return np.hstack((np.ones([p]) * Xi[0], Xi, np.ones([p]) * Xi[-1]))

def bspline(i, p, Xi, s):
    """
    Evaluation of univariate B-Splines by Cox-DeBoor recursion 
    
    i: index of the B-spline
    p: B-spline degree
    Xi: knot vector
    s: evaluation point

    [1] Cox, M. G. (Oct. 1972). “The numerical evaluation of B-splines”. In: Journal of
        the Institute of Mathematics and its Applications 10.2, pp. 134–149. ISSN:
        0020-2932.
    [2] De Boor, C. (1972). “On calculating with B-splines”. In: Journal of
        Approximation Theory 6. Collection of articles dedicated to J. L. Walsh on
        his 75th birthday, V (Proc. Internat. Conf. Approximation Theory, Related
        Topics and their Applications, Univ. Maryland, College Park, Md., 1970),
        pp. 50–62. ISSN: 0021-9045.
    """

    # Check types
    assert isinstance(i,int)
    assert isinstance(p,int)
    assert isinstance(Xi,np.ndarray)

    # Initialize output to zero
    b = np.zeros(np.shape(s))

    # Define degree zero
    if p==0:
        if Xi[i+1] < Xi[-1]:
            # Internal nodes 
            b[(Xi[i] <= s) & (s < Xi[i+1])] = 1
        else:
            # Last subinterval
            b[(Xi[i] <= s) & (s <= Xi[-1])] = 1
    else:
        d = Xi[i+p]-Xi[i] # side sx
        if d > 0:
            b = b + (s - Xi[i]) * bspline(i,p-1,Xi,s)/d
        
        d = Xi[i+p+1]-Xi[i+1] # side dx
        if d > 0:
            b = b + (Xi[i+p+1] - s) * bspline(i+1,p-1,Xi,s)/d

    return b

def bspline_space_dim(p,Xi):
    """
    Computes dimension of B-spline space span
    """
    assert isinstance(p,int)
    assert isinstance(Xi,np.ndarray)

    return np.size(Xi) - p - 1

def plot_bspline_basis(p,Xi):
    """
    Plots all B-spline basis functions
    """
    assert isinstance(p,int)
    assert isinstance(Xi,np.ndarray)

    # Evaluation points
    x = np.linspace(Xi[0],Xi[-1],20*np.size(Xi))

    for fdx in range(0,bspline_space_dim(p,Xi)):
        plt.plot(x,bspline(fdx,p,Xi,x))
    
    plt.show()

p = 6
# Xi = np.linspace(0, 1, 5)
Xi = np.sort(np.random.rand(5))
Xi = knot_pad(Xi,p)

# plot_bspline_basis(p,Xi)
