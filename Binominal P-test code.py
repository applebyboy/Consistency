import pandas as pd
import scipy.stats as stats

def calculate_p_values(cp_values, final_values, n=100):
    """
    Calculate p-values for each pair of CP and Final values using a binomial test.

    Parameters:
    cp_values (list): List of checkpoint (CP) percentages.
    final_values (list): List of final outcome percentages.
    n (int): Hypothetical number of trials (default: 100 for percentage-based data).

    Returns:
    list: A list of formatted p-values for each pair.
    """
    p_values = []
    for cp, final in zip(cp_values, final_values):
        observed_successes = round(cp * n / 100)
        test_result = stats.binomtest(observed_successes, n, final / 100, alternative='two-sided')
        p_value = test_result.pvalue
        formatted_p_value = f"{p_value:.7f}"
        p_values.append(formatted_p_value)
    return p_values

if __name__ == "__main__":
    # Data definitions from the provided table
    cp_values = [100, 100, 100, 100, 100, 100, 91, 100, 94.8, 97, 73]
    final_values = [100, 100, 100, 100, 100, 100, 97, 97, 97, 97, 73]
    
    # Hypothetical number of trials
    n = 100

    # Calculate p-values
    individual_p_values = calculate_p_values(cp_values, final_values, n)

    # Create results DataFrame
    results_df = pd.DataFrame({
        'CP (%)': cp_values,
        'Final (%)': final_values,
        'P-value': individual_p_values
    })

    # Display results
    print(results_df)
