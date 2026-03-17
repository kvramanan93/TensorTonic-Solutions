import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """

    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    N,d = X.shape

    w = np.zeros(d)
    b = 0.0

    loss_history = []

    for step in range(1,steps+1):
        z = X@w + b
        p = _sigmoid(z)

        #p_clipped = np.clip(p,1e-12,1-1e-12)
        loss = -np.mean((y*np.log(p)) + (1-y)*np.log(1-p))
        loss_history.append(loss)

        error = p-y
        dw = (X.T @ error)/N
        db = np.mean(error)

        w -= lr*dw
        b -= lr*db

        if step % 500 == 0:
            print(f"Epoch {step:>4d} | Loss: {loss:.4f}")

    return (w,b)
    

    
    
    # Write code here
    pass