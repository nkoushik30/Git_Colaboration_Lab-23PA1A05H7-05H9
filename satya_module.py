"""
Satya Module - Data Processing Features
This module handles data processing and analytics.
"""

class DataProcessor:
    """Class to handle data processing operations"""
    
    def __init__(self):
        self.data = []
        print("DataProcessor initialized by Satya")
    
    def add_data(self, item):
        """Add data item to the processor"""
        self.data.append(item)
        print(f"Data item added: {item}")
        return True
    
    def process_data(self):
        """Process all data items"""
        print("\nProcessing data...")
        print("-" * 40)
        for idx, item in enumerate(self.data, 1):
            print(f"Processing item {idx}: {item}")
        print("-" * 40)
        return len(self.data)
    
    def get_statistics(self):
        """Get statistics about the data"""
        stats = {
            'total_items': len(self.data),
            'data_types': {}
        }
        
        for item in self.data:
            item_type = type(item).__name__
            stats['data_types'][item_type] = stats['data_types'].get(item_type, 0) + 1
        
        return stats

def analyze_data(data_list):
    """Analyze a list of data"""
    print(f"\nAnalyzing {len(data_list)} items...")
    
    if not data_list:
        print("No data to analyze")
        return None
    
    # Calculate basic statistics
    numeric_data = [item for item in data_list if isinstance(item, (int, float))]
    
    if numeric_data:
        avg = sum(numeric_data) / len(numeric_data)
        print(f"Average of numeric values: {avg:.2f}")
        print(f"Min: {min(numeric_data)}, Max: {max(numeric_data)}")
        return avg
    
    return None

if __name__ == "__main__":
    print("Satya Module - Data Processing System")
    print("=" * 50)
    
    # Demo usage
    processor = DataProcessor()
    processor.add_data(100)
    processor.add_data(200)
    processor.add_data("Sample text")
    processor.add_data(300)
    
    count = processor.process_data()
    print(f"\nProcessed {count} items")
    
    stats = processor.get_statistics()
    print(f"\nStatistics: {stats}")
    
    analyze_data([100, 200, 300])
