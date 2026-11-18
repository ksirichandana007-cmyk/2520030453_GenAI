# WEEK 6 – Generative AI Programming Practical

This folder implements the Week 6 practical from the supplied handout.

## Files
- `golden_set.json` – 30 golden questions, expected answers, keywords and source URLs.
- `main.py` – sends each question to the local Ollama model, scores keyword coverage and writes the results.
- `requirements.txt` – Python dependency.

## Prerequisites
1. Install Python 3.
2. Install Ollama: https://ollama.com/
3. Open PowerShell and download the model:
   ```powershell
   ollama pull llama3.2
   ```
4. Make sure the Ollama service is running. You can check with:
   ```powershell
   ollama --version
   ollama list
   ```

## Run in VS Code (Windows PowerShell)
Open this `WEEK6` folder in VS Code, then run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py main.py
```

If PowerShell blocks virtual-environment activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

The program evaluates all 30 questions using `llama3.2`. It creates `baseline_results.csv` in this folder. The CSV contains each model answer, expected answer, matched/missing keywords, score, status, source, model and release label (`v0.1`).

## Important
- Keep Ollama running while `main.py` executes.
- The first run may take time because the model generates an answer for each of the 30 questions.
- `PASS` means keyword coverage is at least 60%; otherwise the result is marked `REVIEW`.
- This is a keyword-coverage baseline, not a semantic or factuality evaluation.
