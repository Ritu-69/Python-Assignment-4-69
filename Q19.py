def is_palindrome(text):
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]

# Example usage:
print(is_palindrome("madam"))  # Output: True
