import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class FeatureEngineer:
    """
    Class for performing feature engineering on system performance data.
    """

    def __init__(self):
        self.scaler = MinMaxScaler()

    def create_time_windows(self, data, window_size):
        """
        Creates time windows from the given data.

        Args:
            data: Input data (pandas DataFrame).
            window_size: Size of the time window.

        Returns:
            tuple: X (input features) and y (target variable).
        """
        X = []
        y = []
        for i in range(len(data) - window_size):
            X.append(data[i:i+window_size])
            y.append(data[i+window_size])
        return np.array(X), np.array(y)

    def scale_data(self, data):
        """
        Scales the data using Min-Max scaling.

        Args:
            data: Input data.

        Returns:
            array: Scaled data.
        """
        return self.scaler.fit_transform(data)

    def engineer_features(self, data, window_size):
        """
        Performs feature engineering on the given data.

        Args:
            data: Input data (pandas DataFrame).
            window_size: Size of the time window.

        Returns:
            tuple: X (input features) and y (target variable).
        """
        # Create time windows
        X, y = self.create_time_windows(data, window_size)

        # Scale the data
        X = self.scale_data(X)

        return X, y

# Example usage
if __name__ == "__main__":
    # Assuming 'data' is a pandas DataFrame containing system performance data
    data = pd.DataFrame({'cpu_utilization': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})

    feature_engineer = FeatureEngineer()
    X, y = feature_engineer.engineer_features(data['cpu_utilization'].values, window_size=3)

    print(X)
    print(y)