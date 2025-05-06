from src.models.lstm_model import create_lstm_model
from src.preprocessors.data_cleaner import remove_outliers
from sklearn.model_selection import train_test_split

def train_model(data):
    """
    Trains an LSTM model on the given data.

    Args:
        data: The input data.

    Returns:
        model: The trained model.
    """
    # Preprocess data (e.g., remove outliers, create time series windows)
    cleaned_data = remove_outliers(data)
    # ... (create time series windows)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        cleaned_data, 
        # ... (target variable), 
        test_size=0.2, 
        shuffle=False 
    )

    # Create and train the model
    model = create_lstm_model(X_train.shape)
    model.fit(X_train, y_train, epochs=50, batch_size=32) 

    return model

# Example usage
if __name__ == "__main__":
    data = ... 
    trained_model = train_model(data)