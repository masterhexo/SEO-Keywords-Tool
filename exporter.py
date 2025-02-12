import pandas as pd

def export_to_csv(keywords, filename="output/results.csv"):
    """Export keywords to a CSV file."""
    # Create a DataFrame with dummy search volume data
    data = [{"Keyword": keyword, "Search Volume": len(keyword) * 100} for keyword in keywords]
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv(filename, index=False)
    print(f"Keywords saved to {filename}")
