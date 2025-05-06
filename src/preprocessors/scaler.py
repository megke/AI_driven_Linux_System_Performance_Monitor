from sklearn.preprocessing import MinMaxScaler

class Scaler:
    """
    Class for scaling data using Min-Max scaling.
    """

    def __init__(self):
        self.scaler = MinMaxScaler()

    def fit_transform(self, data):
        """
        Fits the scaler on the data and transforms it.

        Args:
            data: Input data.

        Returns:
            array: Scaled data.
        """
        return self.scaler.fit_transform(data)

    def transform(self, data):
        """
        Transforms the data using the fitted scaler.

        Args:
            data: Input data.

        Returns:
            array: Scaled data.
        """
        return self.scaler.transform(data)

    def inverse_transform(self, data):
        """
        Inverts the scaling to get the original data.

        Args:
            data: Scaled data.

        Returns:
            array: Original data.
        """
        return self.scaler.inverse_transform(data)

# Example usage
if __name__ == "__main__":
    data = [[1, 2], [3, 4], [5, 6]]
    scaler = Scaler()
    scaled_data = scaler.fit_transform(data)
    print("Scaled data:", scaled_data)

    original_data = scaler.inverse_transform(scaled_data)
    print("Original data:", original_data)