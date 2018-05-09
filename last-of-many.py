import numpy as np

def filter(ins,outs):
    rn = ins['ReturnNumber']
    nr = ins['NumberOfReturns']

    rets = np.logical_and(np.equal(rn, nr),
        np.greater(nr, 1))

    outs['Mask'] = rets
    return True