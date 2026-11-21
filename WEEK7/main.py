import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "distilgpt2"
TOP_K = 5

def load_model():
    print(f"Loading model: {MODEL_NAME}")
    print("The first run may download the model from Hugging Face.")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    model.eval()
    return tokenizer, model

def inspect_next_tokens(prompt, tokenizer, model, top_k=TOP_K):
    inputs = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        # Logits at the final input position predict the next token.
        logits = outputs.logits[0, -1, :]
        probabilities = torch.softmax(logits, dim=-1)

    k = min(top_k, probabilities.numel())
    top_probs, top_ids = torch.topk(probabilities, k)

    print("\nPrompt:", repr(prompt))
    print("\nTop next-token candidates:")
    print("-" * 55)
    print(f"{'Rank':<8}{'Token':<25}{'Probability':>15}")
    print("-" * 55)

    for rank, (token_id, probability) in enumerate(zip(top_ids, top_probs), start=1):
        token = tokenizer.decode([token_id.item()])
        print(f"{rank:<8}{repr(token):<25}{probability.item() * 100:>14.4f}%")

    print("-" * 55)
    print("\nExplanation:")
    print("Logits are the model's raw scores for every possible next token.")
    print("Softmax converts those scores into probabilities that sum to 1.")
    print(f"Top-k displays the {k} tokens with the highest probabilities.")

def main():
    tokenizer, model = load_model()
    print("\nNEXT-TOKEN PROBABILITY INSPECTOR")
    print("Model:", MODEL_NAME)
    print("Enter a sentence or prompt to inspect its next-token predictions.")
    print("Type 'exit' to stop.\n")

    while True:
        prompt = input("Enter prompt: ").strip()
        if prompt.lower() in {"exit", "quit"}:
            print("Program ended.")
            break
        if not prompt:
            print("Please enter a non-empty prompt.\n")
            continue

        try:
            inspect_next_tokens(prompt, tokenizer, model)
        except Exception as error:
            print("Could not process this prompt:", error)
        print()

if __name__ == "__main__":
    main()
