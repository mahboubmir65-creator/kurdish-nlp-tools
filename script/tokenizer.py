def kurdish_tokenizer(text):
    """A simple tokenizer for Kurdish text"""
    tokens = text.split()
    return tokens

# Example usage
if name == "__main__":
    sample_text = "دیسان من تاقەت گەورەم"
    tokens = kurdish_tokenizer(sample_text)
    print("Tokens:", tokens)
