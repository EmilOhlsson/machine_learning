#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    l = len(predictions)
    errs = [(a[0], nw[0], abs(nw[0] - p[0])) for a, nw, p in zip(ages, net_worths, predictions)]
    cleaned_data = sorted(errs, key=lambda v: v[2])[0:l - l/10]
    
    return cleaned_data

