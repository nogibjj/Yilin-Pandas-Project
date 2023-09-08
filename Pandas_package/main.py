import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def descriptive_statistics(data):
    return data.describe()

if __name__ == "__main__":
    data = load_data("data/data_sample.csv")
    stats = descriptive_statistics(data)
    print(stats)
