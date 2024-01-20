# use dictioneries  to counting the frequency of words in a text document.

def count_word_frequency(text):
    """
    Count the frequency of each word in a text document.

    Parameters:
    - text: String representing the text document.

    Returns:
    - Dictionary with words as keys and their frequencies as values.
    """
    word_frequency = {}

    # Split the text into words
    words = text.split()

    # Count the frequency of each word
    for word in words:
        # Remove punctuation and convert to lowercase for better matching
        cleaned_word = word.strip('.,!?()[]{}":;')
        cleaned_word = cleaned_word.lower()

        # Update word frequency in the dictionary
        if cleaned_word:
            word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1

    return word_frequency

# Example usage:
document = """
Python is a powerful programming language. It is widely used for web development,
data science, artificial intelligence, and more. Python has a simple and
readable syntax, making it an excellent choice for both beginners and experienced
developers.
"""

frequency_dict = count_word_frequency(document)

# Print word frequencies
for word, frequency in frequency_dict.items():
    print(f"{word}: {frequency} times")
