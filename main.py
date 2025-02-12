# SEO Keywords Tool
# Created by: Master Jay
# Telegram: @jaymali841


from keyword_analysis import generate_combinations
from exporter import export_to_csv
import os


output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def main():
    print("Welcome to the SEO Keywords Tool!")
    
  
    column1 = input("Enter keywords for Column 1 (comma-separated): ").split(",")
    column2 = input("Enter keywords for Column 2 (comma-separated): ").split(",")
    column3 = input("Enter keywords for Column 3 (comma-separated): ").split(",")


    keywords = generate_combinations(column1, column2, column3)
    
    
    print("\nGenerated Keywords:")
    for keyword in keywords:
        print(keyword)
    
   
    export_to_csv(keywords)
    print("\nKeywords saved successfully in 'output/results.csv'.")

if __name__ == "__main__":
    main()
