from pathlib import Path
from pypdf import PdfReader


root: Path = Path(__file__).resolve().parents[2]
pdf_path: Path = Path(r"C:\Users\panze\Downloads\测试台Guide.pdf")
output_dir: Path = root / "tmp" / "pdfs" / "extracted"
output_dir.mkdir(parents=True, exist_ok=True)

reader: PdfReader = PdfReader(pdf_path)
for page_number, page in enumerate(reader.pages, start=1):
    for image_number, image_file in enumerate(page.images, start=1):
        suffix: str = Path(image_file.name).suffix or ".bin"
        output_path: Path = output_dir / f"page-{page_number:02d}-image-{image_number:02d}{suffix}"
        output_path.write_bytes(image_file.data)
        print(f"{output_path.name}\t{len(image_file.data)}")
