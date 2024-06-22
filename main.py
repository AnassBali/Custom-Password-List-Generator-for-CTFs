import argparse
from combinator import generate_combinations
from utils import calculate_list_size, display_sample_output, save_to_file
import config

def main():
    parser = argparse.ArgumentParser(
        description="Generate a password list based on input words.")
    parser.add_argument(
        "-w", "--words", 
        nargs='+', 
        required=True, 
        help="List of words to combine. Example: -w word1 word2 word3"
    )
    parser.add_argument(
        "-d", "--depth", 
        type=int, 
        default=config.MAX_DEPTH, 
        help="Maximum depth of combinations (default is 2)."
    )
    parser.add_argument(
        "-s", "--special", 
        nargs='*', 
        default=config.SPECIAL_CHARACTERS, 
        help="Special characters to use as separators (default is ['!', '@', '#', '$', '%', '^', '&', '*'])."
    )
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        default="password_list.txt", 
        help="Output file to save the generated passwords (default is password_list.txt)."
    )
    parser.add_argument(
        "--sample-size", 
        type=int, 
        default=config.SAMPLE_SIZE, 
        help="Number of sample passwords to display (default is 10)."
    )
    
    args = parser.parse_args()
    
    words = args.words
    max_depth = args.depth
    special_chars = args.special
    output_file = args.output
    sample_size = args.sample_size

    print(f"Input words: {words}")
    print(f"Maximum depth: {max_depth}")
    print(f"Special characters: {special_chars}")

    # Generate combinations
    all_combinations = generate_combinations(words, max_depth, special_chars)

    # Calculate and display size
    size = calculate_list_size(all_combinations)
    print(f"Estimated total size of password list: {size}")

    # Display sample output
    display_sample_output(all_combinations, sample_size)

    # Save to file
    save_to_file(all_combinations, output_file)
    print(f"Password list saved to {output_file}")

if __name__ == "__main__":
    main()
