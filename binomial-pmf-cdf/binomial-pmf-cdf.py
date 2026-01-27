import numpy as np
from scipy.special import comb

def pmf(n,k,p):
    return comb(n,k)*(p**k)*((1-p)**(n-k))
def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    ans = pmf(n,k,p) 
    cdf = 0
    for i in range(0,k+1):
        cdf += pmf(n,i,p)
    return (ans,cdf)
    pass