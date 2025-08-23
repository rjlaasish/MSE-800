import pandas as pd

class ColumnStats:
    def __init__(self, values):
        self.values = values
    
    def get_max(self):
        return max(self.values)
    
    def get_min(self):
        return min(self.values)
    
    def get_mean(self):
        return sum(self.values) / len(self.values)
    
    def get_abs_max(self):
        return max([abs(v) for v in self.values])


def main():
    df = pd.read_csv('./files/data.csv')  
    
    df.to_parquet('./files/output_data.parquet', engine='pyarrow')
    column_name = ' Operating Profit Rate'  
    
    values = df[column_name].dropna().tolist()
    
    stats = ColumnStats(values)
        
    print(f"\nAnalyzing column: {column_name}")
    print(f"Max: {stats.get_max()}")
    print(f"Min: {stats.get_min()}")
    print(f"Mean: {stats.get_mean()}")
    print(f"Absolute Max: {stats.get_abs_max()}\n")


if __name__ == "__main__":
    main()
