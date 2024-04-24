import pandas as pd
import numpy as np

def data_analysis(csv_file_path):
    df = pd.read_csv(csv_file_path)
    
    # Initialize an empty dictionary to store the results
    analysis_results = {}
    
    # Basic statistics
    analysis_results['basic_statistics'] = df.describe().to_dict()
    
    # Exploratory Data Analysis (EDA)
    analysis_results['eda'] = {
        'data_types': df.dtypes.to_dict(),
        'null_counts': df.isnull().sum().to_dict(),
        'unique_counts': df.nunique().to_dict(),
        'first_five_rows': df.head().to_dict(orient='records')
    }
    
    # Correlation
    correlation_matrix = df.corr().to_dict()
    analysis_results['correlation'] = correlation_matrix
    
    # Columns
    analysis_results['columns'] = {
        'all_columns': df.columns.tolist(),
        'categorical_columns': df.select_dtypes(include=['object']).columns.tolist(),
        'numerical_columns': df.select_dtypes(include=['number']).columns.tolist()
    }
    
    return analysis_results