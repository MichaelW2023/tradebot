# tradebot

## Markdown Card Generator

This repository includes `card_generator.py`, a small tool that converts Markdown files into a simple HTML card with basic styling.

Install dependencies first:
```bash
pip install -r requirements.txt
```

### Usage

Run the script with your Markdown file as input:
```bash
python card_generator.py samples/example.md -o example_card.html --title "Example Card"
```
Open `example_card.html` in your browser to view the result.
You can specify a custom title for the card using `--title`.
