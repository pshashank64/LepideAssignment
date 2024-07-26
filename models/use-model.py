from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Define the cache directory
cache_dir = "E:/lepide software/models/gpt-2"

# Load the tokenizer and model from the cache directory
tokenizer = GPT2Tokenizer.from_pretrained(cache_dir)
model = GPT2LMHeadModel.from_pretrained(cache_dir)

# Set pad_token_id to eos_token_id
tokenizer.pad_token = tokenizer.eos_token

# Generate a sample text
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors="pt")

# Create the attention mask (1 for actual tokens, 0 for padding tokens)
attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

# Generate the text
output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=50,
    num_return_sequences=1,
    pad_token_id=tokenizer.eos_token_id  # Set pad_token_id to eos_token_id
)

# Decode and print the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
