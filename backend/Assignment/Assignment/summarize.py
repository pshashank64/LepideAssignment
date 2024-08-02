import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def summarize(text, cache_dir="E:/lepide software/models/gpt-2"):
    """
    Summarizes the given text using a pre-trained GPT-2 model.

    Args:
        text (str): The text to be summarized.
        cache_dir (str): Directory where the GPT-2 model is stored.

    Returns:
        str: The generated summary.
    """
    # Load the tokenizer and model from the specified cache directory
    tokenizer = GPT2Tokenizer.from_pretrained(cache_dir)
    model = GPT2LMHeadModel.from_pretrained(cache_dir)
    
    # Set the padding token to the end-of-sequence token
    tokenizer.pad_token = tokenizer.eos_token

    # Encode the input text to obtain input IDs
    input_ids = tokenizer.encode(text, return_tensors="pt")
    
    # Create an attention mask (1 for actual tokens, 0 for padding tokens)
    attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

    # Generate the summary
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=30,  # Generate up to 30 new tokens
        num_return_sequences=1,  # Generate a single sequence
        pad_token_id=tokenizer.eos_token_id,  # Set padding token ID to eos_token_id
        no_repeat_ngram_size=2,  # No repeating n-grams of size 2
        early_stopping=True  # Stop early when end-of-sequence token is generated
    )

    # Decode the generated tokens into a string, skipping special tokens
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

if __name__ == "__main__":
    # Get the file path from command line arguments
    file_path = sys.argv[1]
    
    # Read the content of the file
    with open(file_path, 'r') as file:
        text = file.read()
    
    # Generate the summary of the text
    summary = summarize(text)
    
    # Print the generated summary
    print(summary)
