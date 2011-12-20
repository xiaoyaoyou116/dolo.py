def asymptotic_variance( A, sigma, T=100 ):
    '''Computes asymptotic variance of the AR(1) process defined by:
    $X_t = A X_{t-1} + \epsilon_t$
    where the $\epsilon_t$ follows a random law with covariance sigma.
    '''
    import numpy
    p = A.shape[0] # number of variables
    Q = numpy.zeros( (p,p), dtype=numpy.float )
    for i in range(T):
        Q = numpy.dot( A.T, numpy.dot( Q, A)) + sigma
    return Q
