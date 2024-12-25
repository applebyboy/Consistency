import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def perform_statistical_analysis(all_data):
    """
    Perform statistical analysis (Pearson Correlation, RMSE, R-squared, and slope difference) 
    on input data and return results in a dictionary format.

    Parameters:
    all_data (dict): A dictionary where keys represent stages and values are lists of (x, y) tuples.

    Returns:
    dict: A dictionary containing statistical analysis results for each stage.
    """
    results = {}

    for stage, data in all_data.items():
        x_vals, y_vals = zip(*data)
        
        # Calculate Pearson Correlation Coefficient
        correlation = np.corrcoef(x_vals, y_vals)[0, 1]
        
        # Calculate RMSE
        if len(x_vals) > 1:
            predicted = np.poly1d(np.polyfit(x_vals, y_vals, 1))(x_vals)
        else:
            predicted = y_vals  # Default to the only available value if only one point
        rmse = np.sqrt(mean_squared_error(y_vals, predicted))
        
        # Calculate R-squared
        r_squared = r2_score(y_vals, predicted)
        
        # Calculate slope difference from 1 (ideal slope)
        slope, _ = np.polyfit(x_vals, y_vals, 1)
        slope_difference = abs(slope - 1)
        
        # Store results
        results[f'{stage + 1}st CP'] = {
            'Pearson Correlation': correlation,
            'RMSE': rmse,
            'R-squared': r_squared,
            'Slope Difference from 1': slope_difference
        }

    return results

# Example usage
if __name__ == "__main__":
    sample_data = {
        0: [(1, 2), (2, 3), (3, 5), (4, 7)],
        1: [(1, 1.5), (2, 2.8), (3, 3.7), (4, 4.9)],
    }
    analysis_results = perform_statistical_analysis(sample_data)
    print(analysis_results)

