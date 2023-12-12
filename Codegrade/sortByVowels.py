def get_num_of_vowels(inp: str) -> int:
    vowel_count = 0
    vowels = 'aeiou'
    for char in inp:
        if char in vowels:
            vowel_count += 1
    return vowel_count


def sort_basedon_vowels():
    cases = ['code', 'programming', 'description', 'fly', 'free']
    print(sorted(cases, key=lambda word: get_num_of_vowels(word)))


if __name__ == "__main__":
    sort_basedon_vowels()
