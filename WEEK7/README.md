# WEEK7 – Next-Token Probability Inspector

**CO Mapping:** CO2

## Aim
To inspect next-token logits and top-k token candidates from a small open language model using Hugging Face Transformers.

## Description
This program uses the `distilgpt2` causal language model. After entering a prompt, it:
1. Tokenizes the input text.
2. Runs the model and reads the logits at the final input position.
3. Applies softmax to convert logits into probabilities.
4. Displays the top-k next-token candidates and their probabilities.

## Project structure

```text
WEEK7/
├── main.py
├── requirements.txt
└── README.md
```

## Requirements
- Python 3.9 or later
- Internet connection for the first model download
- VS Code (recommended)

## Run in VS Code (Windows PowerShell)

Open the WEEK7 folder in VS Code, then run:

```powershell
py -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again.

Install dependencies:

```powershell
py -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the program:

```powershell
py main.py
```

The first run downloads `distilgpt2` from Hugging Face, so it can take a little time. Later runs can reuse the downloaded model.

## Example prompts
- The future of artificial intelligence is
- Once upon a time
- Machine learning helps computers

The exact candidates and probabilities depend on the model and prompt.

## Important concepts
- **Token:** A unit of text processed by the model. It may be a word, part of a word, or punctuation.
- **Logits:** Raw, unnormalized scores produced by the model for possible next tokens.
- **Softmax:** Converts logits into a probability distribution.
- **Top-k:** Selects the k candidates with the highest probabilities.

## Expected output
The program prints the entered prompt and a ranked list of five candidate next tokens with their probabilities. It then explains logits, softmax, and top-k.

Type `exit` to close the program.
