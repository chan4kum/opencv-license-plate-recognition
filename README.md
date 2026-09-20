# License Plate Recognition

Locates number plates with OpenCV's bundled Haar cascade and reads them with Tesseract OCR.

Part of a series of beginner-friendly OpenCV projects.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
brew install tesseract   # macOS; apt install tesseract-ocr on Linux
python main.py --image car.jpg
```

Press `q` to quit any live window.

## License

MIT
