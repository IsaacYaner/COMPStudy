import numpy as np
class GaussianFactor:
    def __init__(self, domain, mu=None, sigma=None, parents=None, beta=None, b_mean=None, b_var=None, K=None, h=None, g=None):
        '''
        There are three ways to initialize this object.
        1. As a multivariate gaussian
        domain:   A list or tuple of the names of each variable.
        mu:       The mean vector
        sigma:    The covariance matrix
        
        2. As a conditional distribution Y|X where Y = beta^T X + b
        domain:   List of names with the *child variable first*.
        beta:     The vector of parameters which define the scale each of the variables X_i
        b_mean:   The mean of b
        b_var:    The variance of b
        
        3. Directly with the cannonical form of the parameters
        domain:  A list or tuple of the names of each variable.
        K:       see cell above, (or Koller&Friedman textbook (section 14.2.1.1)) for definitions of these variables
        h:
        g:
        '''
        n = len(domain)
        self.domain = domain
        if mu is not None and sigma is not None:
            mu, sigma = np.array(mu).reshape((n,)), np.array(sigma).reshape((n,n))
            self.K = np.linalg.inv(sigma)
            self.h = self.K@mu
            self.g = -(1/2)*mu.T@self.K@mu - np.log(((2*np.pi)**(n/2))*np.linalg.det(sigma)**(1/2))
        elif K is not None and h is not None and g is not None:
            self.K = np.array(K).reshape((n,n))
            self.h = np.array(h).reshape((n,))
            self.g = np.array(g).reshape((1,))
        elif beta is not None and b_mean is not None and b_var is not None:
            # We will complete the function below in the next exercise
            K,h,g = self._init_as_conditional(domain[0],domain[1:], beta, b_mean, b_var)
            self.K = K
            self.h = h
            self.g = g
        else:
            raise ValueError("Insufficient arguments")
            
    def density(self, x):
        '''
        x:  ndarray of shape [..., len(domain)], to specifiy the set of 
        points in the domain space for which the density should be returned.
        
        returns: ndarray of shape [...], same as input but missing final dimension.
        '''
        x = np.array(x)
        if x.shape == tuple():
            x = x.reshape(-1)
        if len(self.domain) == 1 and x.shape[-1] != 1:
            x = x.reshape((*x.shape,1))
        assert(x.shape[-1] == len(self.domain))
        output_shape = x.shape[:-1]
        xT = np.array(x).reshape((*x.shape[:-1],1,len(self.domain)))
        x = np.array(x).reshape((*x.shape[:-1],len(self.domain),1))
        hT = self.h.reshape(1,len(self.domain))
        return np.exp(-(1/2)*xT@self.K@x+hT@x+self.g).reshape(output_shape)
    
    def plot(self):
        '''
        If mean() and covariance() are well defined (and sometimes when they aren't),
        this function will plot a graph or contour diagram of the distribution.
        Limited to 1 or 2 dimensional factors.
        '''
        try:
            mu = self.mean()
        except np.linalg.LinAlgError:
            raise np.linalg.LinAlgError("Can't plot conditional distributions")
            
        if len(self.domain) == 1:
            mu = self.mean()
            sigma = np.sqrt(self.covariance())[0,0]
            x = np.linspace(mu-5, mu+5, 100)
            y = self.density(x)
            plt.plot(x,y)
            plt.xlabel(f'Domain: {self.domain[0]}')
            plt.ylabel('density')
            plt.show()
        elif len(self.domain) == 2:
            mu = self.mean()
            x1 = np.linspace(mu[0]-5,mu[0]+5,200).reshape(-1,1)
            x2 = np.linspace(mu[1]-5,mu[1]+5,200).reshape(1,-1)
            a,b = np.meshgrid(x1,x2)
            x = np.dstack([a,b])
            y = self.density(x)
            plt.contour(a,b, y)
            plt.xlabel(f'Domain: {self.domain[0]}')
            plt.ylabel(f'Domain: {self.domain[1]}')
            plt.show()
        else:
            print("Error: Need 1 or 2 dimensional gaussian for plotting")
            
    def mean(self):
        '''
        Returns the mean of this gaussian distribution, assuming it is well defined (it isn't if conditional).
        '''
        return np.linalg.inv(self.K)@self.h
    
    def covariance(self):
        '''
        Returns the covariance matrix of this gaussian distribution, assuming it is well defined (it isn't if conditional).
        '''
        return np.linalg.inv(self.K)


    def copy(self):
        '''
        Creates a full copy of the object
        '''
        return copy.deepcopy(self)
            
    def __str__(self):
        '''
        Creates a string representation of the distribution.
        Tries to print the mean and covariance.
        If distribution is conditional, the covariance matrix isn't well defined, so it resorts
        to printing the cannonical form parameters.
        '''
        try:
            return f"Factor over {tuple(self.domain)},\nμ = {self.mean()},\nΣ = \n{self.covariance()}"
        except np.linalg.LinAlgError:
            return f"Factor over {tuple(self.domain)},\nK = \n{self.K},\nh = {self.h},\ng = {self.g}"
    
    def _init_as_conditional(self, child, parents, beta, mean, var):
        '''
        This function is only to be used by the __init__ function.
        This function initialises the factor as a conditional distribution P(Y|X),
        where Y = \beta^T X + b.
        Arguments:
        child: Name of Y
        parents: Names of each X
        beta: vector to multiply with X
        mean: mean of b
        var: variance of b
        Explanation and derivation of this function (advanced and out of scope material) is provided at the bottom of the notebook.
        '''
        n = len(beta)
        beta = np.array(beta).reshape((n,1)) # make sure beta is a column vector
        K = np.zeros((n+1,n+1))
        
        # top left section of K
        K[0,0] = 1/var
        # top right section of K
        K[0:1,1:] = -(1/var)*beta.T
        # bottom left section of K
        K[1:,0:1] = -(1/var)*beta
        # bottom right section of K
        K[1:,1:] = (1/var)*beta@beta.T
        
        h = np.zeros((n+1,1))
        # top section of h
        h[0,:] = mean/var
        # bottom section of h
        h[1:,:] = -(mean/var)*beta
        
        # reshape h to be row vector (for consistency with previous format)
        h = h.reshape(-1)
        
        g = -(1/2)*(mean**2/var) - (1/2)*np.log(2*np.pi*var)
        
        return K,h,g

    def evidence(self, **kwargs):
        '''
        Sets evidence which results in removal of the evidence variables
        This function must be used to set evidence on all factors before any are joined,
        because it removes the evidence variables from the factor
        
        Usage: fac.evidence(A=4.6,B=-0.3)
        This returns a factor which has set the variable 'A' to '.6 and 'B' to -0.3.
        '''
        evidence_dict = kwargs
        

        # remove any irrelevant evidence from evidence dict
        for var in list(evidence_dict.keys()):
            if var not in self.domain:
                del evidence_dict[var]
                
        if(len(evidence_dict) == 0):
            return self
        
        # work out new domain vars and evidence vars
        new_domain = list(self.domain)
        evidence_vars = []
        evidence_values = []
        for var,value in evidence_dict.items():
            new_domain.remove(var)
            evidence_vars.append(var)
            evidence_values.append(value)
            
        # rearrange the domain to put evidence vars last
        f = self._extend(new_domain+evidence_vars)
        
        # Split up K and h into sections
        n = len(evidence_vars)
        m = len(new_domain)
        K_xx = f.K[:m,:m]
        K_xy = f.K[:m,-n:]
        K_yy = f.K[-n:,-n:]
        h_x = f.h[:m]
        h_y = f.h[-n:]
        # put evidence variables into a vector called y
        y = np.array(evidence_values)
        
        # update variables
        new_K = K_xx
        new_h = h_x - K_xy@y
        new_g = f.g+h_y.T@y - (1/2)*y.T@K_yy@y
        return self.__class__(new_domain, K=new_K, h=new_h,g=new_g)

    def _extend(self, new_domain):
        '''
        This function is for adding variables to the domain, or reordering the variables in the domain
        Note that self.domain must be contain a subset of the variables in new_domain
        '''
        n = len(new_domain)
        
        # add zeros to K and h corresponding to the new variables
        new_K = np.zeros((len(new_domain),len(new_domain)))
        new_K[:len(self.domain), :len(self.domain)] = self.K
        new_h = np.zeros(len(new_domain))
        new_h[:len(self.domain)] = self.h
        new_g = self.g
        old_order = list(self.domain) + list(set(new_domain)-set(self.domain))
        # shuffle rows and columns of K according to new order
        new_order = []
        for v in new_domain:
            new_order.append(old_order.index(v))
        new_K = new_K[new_order,:]
        new_K = new_K[:,new_order]

        # shuffle h according to new order
        new_h = new_h[new_order]
        
        return self.__class__(new_domain, K=new_K, h=new_h, g=new_g)


    def sample(self, **kwargs):
        '''
        Draw a sample from this distribution, given evidence.
        output: dict containing a map from variable names to values
        '''
        f = self.evidence(**kwargs)
        sample = np.random.multivariate_normal(f.mean(), f.covariance())
        sample_dict = dict((var, sample[i]) for i,var in enumerate(f.domain))
        return sample_dict



