from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class SimpleLinearModel:
    def __init__(self):
        self.model = LinearRegression()

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Function for input validation with integer values
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to collect data for a given number of samples and dimensions
def collect_data(num_samples, num_dimensions, sample_type):
    data = []
    Y=[]
    print(f"Enter {num_dimensions} space-separated integer values for {sample_type} data.")
    for j in range(num_samples):
        print("------------------")
        x_values_list = [get_int_input(f"Enter x{i+1} for {sample_type} sample {j+1}: ") for i in range(num_dimensions)]
        data.append(x_values_list)
        print("------------------")
        if sample_type=="training":
            y_value = get_int_input(f"Enter corresponding integer y value for {x_values_list}: ")
            Y.append(y_value)
            print("------------------")
            print(f"Entered {sample_type} sample {j+1}: X = {x_values_list}, y = {y_value}")
            print("------------------")
    if sample_type=="training":
        return data,Y
    return data
while(True):
    # Get number of training samples and dimensions
    num_train_samples = get_int_input("Enter the number of training samples: ")
    num_dimensions = get_int_input("Enter the dimensionality of X feature vector: ")
    
    # Collect training data
    X_train,y_train = collect_data(num_train_samples, num_dimensions, "training")
    
    # Train the model
    ML_model = SimpleLinearModel()
    ML_model.fit(np.array(X_train), np.array(y_train))
    
    # Get number of test samples
    num_test_samples = get_int_input("Enter the number of test samples: ")
    
    # Collect test data
    X_test = collect_data(num_test_samples, num_dimensions, "test")
    
    # Make predictions
    predictions = ML_model.predict(np.array(X_test))
    print(f"\nPredictions for test samples: {predictions}\n")
    
    # Visualization
    if num_dimensions == 1:
        plt.scatter(np.array(X_train), np.array(y_train), color='blue', label='Training Data')
        plt.scatter(np.array(X_test), predictions, color='green', label='Test Data')
        plt.plot(np.concatenate([np.array(X_train), np.array(X_test)]), np.concatenate([np.array(y_train), predictions]), color='red', label='Linear Regression Prediction')
        plt.xlabel('X')
        plt.ylabel('y')
        plt.legend()
        plt.show()
