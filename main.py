import argparse
import json
from pathlib import Path
from src.extractor import extract_policy

def main():
    parser = argparse.ArgumentParser(description="Extract structured insurance policy details.")
    parser.add_argument("document", help="Path to PDF, DOCX, or TXT policy document")
    parser.add_argument("--output", default="outputs/extraction.json", help="Output JSON path")
    args = parser.parse_args()

    result = extract_policy(args.document)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.model_dump_json(indent=2), encoding="utf-8")
    print(result.model_dump_json(indent=2))
    print(f"\nSaved validated extraction to: {output_path}")

if __name__ == "__main__":
    main()
