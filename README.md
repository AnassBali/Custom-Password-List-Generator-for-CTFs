# Custom Password List Generator for CTFs

## EXAMPLE
python3 main.py -w word1 word2 word3 -d 2 -s '!' '@' -o output.txt --sample-size 10

## Overview

This project is a Python script designed to help generate password lists for cracking purposes. It combines words in various ways, includes special characters, and changes case to create a comprehensive list of potential passwords.

## Features

- Combines words in different orders and depths.
- Includes permutations with special characters as separators.
- Creates variations with uppercase and lowercase letters.
- Calculates and displays the size of the generated password list before creating it.
- Displays a sample of the generated password list.

## Installation

Ensure you have Python 3.7+ installed. Clone the repository and navigate to the project directory.

```sh
git clone https://github.com/AnassBali/password-list-generator.git
cd Custom-wordlists-for-CTF
