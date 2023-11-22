def add(x, y):
    """Add two parameters, which must be of compatible types.

    Parameters
    ----------
    x: float or str or list
        The first parameter.
    y: float or str or list
        The second parameter

    Returns
    -------
    float or str or list
        The "sum" (depending on type) of the two parameters.

    Raises
    ------
    TypeError
        If the types of the two parameters are not compatible.
    """
    return x + y
