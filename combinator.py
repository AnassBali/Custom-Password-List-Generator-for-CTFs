import itertools

def generate_combinations(words, max_depth, special_chars):
    combinations = set()
    
    for depth in range(1, max_depth + 1):
        for combo in itertools.product(words, repeat=depth):
            combinations.add("".join(combo))
            combinations.add("".join(combo).lower())
            combinations.add("".join(combo).upper())
            combinations.add("".join(combo).capitalize())
            
            for special_char in special_chars:
                combinations.add(special_char.join(combo))
                combinations.add(special_char.join(combo).lower())
                combinations.add(special_char.join(combo).upper())
                combinations.add(special_char.join(combo).capitalize())
                
    return combinations
