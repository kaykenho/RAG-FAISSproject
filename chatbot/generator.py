from transformers import GPT2LMHeadModel, GPT2Tokenizer


class ResponseGenerator:
    def __init__(self):
        self.model_name = "gpt2"
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)

    def generate_response(self, user_input, documents):
        # Combine user input with retrieved documents as context
        context = user_input + "\n" + "\n".join(documents)

        inputs = self.tokenizer.encode(context, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response
