def calculate_list_size(combinations):
    return len(combinations)

def display_sample_output(combinations, sample_size):
    print(f"Sample of generated passwords (showing {sample_size} of {len(combinations)}):")
    sample = list(combinations)[:sample_size]
    for password in sample:
        print(password)

def save_to_file(combinations, filename):
    with open(filename, 'w') as f:
        for password in combinations:
            f.write(f"{password}\n")
