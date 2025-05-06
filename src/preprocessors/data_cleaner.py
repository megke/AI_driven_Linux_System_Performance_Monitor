import numpy as np

def remove_outliers(data, threshold=3):
    """
    Removes outliers using the IQR method.

    Args:
        data: The input data.
        threshold: The multiplier for the IQR.

    Returns:
        array: The data without outliers.
    """
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (threshold * iqr)
    upper_bound = q3 + (threshold * iqr)
    return data[(data >= lower_bound) & (data <= upper_bound)]

# Example usage
if __name__ == "__main__":
    data = ... 
    cleaned_data = remove_outliers(data)