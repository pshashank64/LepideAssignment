from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Define model name and cache directory
model_name = "gpt2"
cache_dir = "E:\lepide software\models"

# Load the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = GPT2LMHeadModel.from_pretrained(model_name, cache_dir=cache_dir)

# Save the model and tokenizer
model.save_pretrained(cache_dir)
tokenizer.save_pretrained(cache_dir)

print("Model and tokenizer saved to E:\lepide software\models\gpt-2")