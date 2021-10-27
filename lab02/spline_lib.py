import numpy as np
import matplotlib.pyplot as plt

def knot_pad(Xi,p):
    """
    Repeats first and last knots of Xi 
    """
    return np.hstack((np.ones([p]) * Xi[0], Xi, np.ones([p]) * Xi[0]))

def bspline(i, p, Xi, s):
    """
    Evaluation of univariate B-Splines by Cox-DeBoor recursion 

    [1] Cox, M. G. (Oct. 1972). “The numerical evaluation of B-splines”. In: Journal of
        the Institute of Mathematics and its Applications 10.2, pp. 134–149. ISSN:
        0020-2932.
    [2] De Boor, C. (1972). “On calculating with B-splines”. In: Journal of
        Approximation Theory 6. Collection of articles dedicated to J. L. Walsh on
        his 75th birthday, V (Proc. Internat. Conf. Approximation Theory, Related
        Topics and their Applications, Univ. Maryland, College Park, Md., 1970),
        pp. 50–62. ISSN: 0021-9045.
    """


    b = np.zeros(np.shape(s))

    return b

p = 3
Xi = np.linspace(0, 1, 5)

print(type(Xi))

# bspline(1, p, Xi, 0)