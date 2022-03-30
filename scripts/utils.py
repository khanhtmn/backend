from datetime import datetime

# Function to create lists of data to inject to Models
"""
Take data and put to dictionary
"""
def create_list_of_data(data, data_cols, model_cols, default_cols=None, default_vals=None):
    """
    Input:
    dataframe data: Source of data
    list[str] data_cols: Column names from the df data
    list[str] model_cols: Column names from the db model
    list[str] default_cols: Default columns
    list[str] default_vals: Default values for the default columns

    Output:
    list[dict] table_to_insert: Table to insert to database
    """
    n = len(data_cols)
    table_to_insert = []

    for index, row in data.iterrows():
        row_data = dict()
        for i in range(n):
            model_col = model_cols[i]
            data_col = data_cols[i]
            row_value = row[data_col]
            if data_col == "timestamp":
                datetime_object = datetime.strptime(row_value, '%m/%d/%Y %H:%M:%S')
                row_data[model_col] = datetime_object
            else:
                # Do normal stuffs
                row_data[model_col] = row_value
        if default_cols:
            for i in range(len(default_cols)):
                row_data[default_cols[i]] = default_vals[i]
        table_to_insert.append(row_data)

    return table_to_insert