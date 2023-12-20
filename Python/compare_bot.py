import pandas as pd

def compare_and_write_results(file_path, column1_index, column2_index):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)

        # Input validation
        if column1_index < 0 or column1_index >= df.shape[1] or column2_index < 0 or column2_index >= df.shape[1]:
            print("Invalid column indices. Please provide valid indices.")
            return

        # Create a new DataFrame with True/False values for exact match
        exact_match = df.iloc[:, column1_index].str.strip() == df.iloc[:, column2_index].str.strip()

        # Create a new DataFrame with differences
        differences = df.apply(lambda row: ''.join([char2 for char1, char2 in zip(str(row[column1_index]), str(row[column2_index])) if char1 != char2])[:20], axis=1)
        
        result_df = pd.DataFrame({
            'Exact Match': exact_match,
            'Differences': differences
        })

        # Write the result to a new Excel file
        result_df.to_excel('result.xlsx', index=False)
        print("Saved successfully.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'your_file.xlsx', 0, and 1 with your actual file path, column1_index, and column2_index
    compare_and_write_results('deneme.xlsx', 0, 1)
