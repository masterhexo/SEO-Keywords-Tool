def generate_combinations(column1, column2, column3):
    """Generate meaningful keyword combinations."""
    combinations = []
    for word1 in column1:
        for word2 in column2:
            for word3 in column3:
                combinations.append(f"{word1.strip()} {word2.strip()} {word3.strip()}")
    return combinations
