import sys
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def summarize(text, cache_dir="E:/lepide software/models/gpt-2"):
    tokenizer = GPT2Tokenizer.from_pretrained(cache_dir)
    model = GPT2LMHeadModel.from_pretrained(cache_dir)
    tokenizer.pad_token = tokenizer.eos_token

    input_ids = tokenizer.encode(text, return_tensors="pt")
    attention_mask = input_ids.ne(tokenizer.pad_token_id).long()

    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=30, 
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id,
        no_repeat_ngram_size=2, 
        early_stopping=True
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text

if __name__ == "__main__":
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        text = file.read()
    summary = summarize(text)
    print(summary)