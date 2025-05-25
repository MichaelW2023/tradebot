import argparse
from pathlib import Path
import markdown

CARD_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
.card {{
  max-width: 600px;
  margin: 20px auto;
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  padding: 20px;
  font-family: Arial, sans-serif;
}}
</style>
</head>
<body>
<div class="card">
{content}
</div>
</body>
</html>
'''


def markdown_to_card(md_text: str, title: str) -> str:
    html_body = markdown.markdown(md_text)
    return CARD_TEMPLATE.format(title=title, content=html_body)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown file to an HTML card")
    parser.add_argument("input", help="Path to the input Markdown file")
    parser.add_argument("-o", "--output", default="card.html", help="Output HTML file")
    parser.add_argument("--title", default="Markdown Card", help="Title for the card")
    args = parser.parse_args()

    md_path = Path(args.input)
    md_text = md_path.read_text(encoding="utf-8")
    card_html = markdown_to_card(md_text, args.title)
    output_path = Path(args.output)
    output_path.write_text(card_html, encoding="utf-8")
    print(f"Card written to {output_path}")


if __name__ == "__main__":
    main()
