from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def make_contact_sheet(paths: list[Path], output_path: Path, columns: int, width: int) -> None:
    thumbnails: list[tuple[Path, Image.Image]] = []
    for path in paths:
        with Image.open(path) as source:
            image: Image.Image = source.convert("RGB")
            ratio: float = width / image.width
            resized: Image.Image = image.resize((width, int(image.height * ratio)))
            thumbnails.append((path, resized))

    label_height: int = 34
    row_heights: list[int] = []
    for row_start in range(0, len(thumbnails), columns):
        row: list[tuple[Path, Image.Image]] = thumbnails[row_start : row_start + columns]
        row_heights.append(max(image.height for _, image in row) + label_height)

    sheet_width: int = columns * width
    sheet_height: int = sum(row_heights)
    sheet: Image.Image = Image.new("RGB", (sheet_width, sheet_height), "white")
    draw: ImageDraw.ImageDraw = ImageDraw.Draw(sheet)
    font: ImageFont.ImageFont = ImageFont.load_default(size=22)

    y: int = 0
    for row_index, row_start in enumerate(range(0, len(thumbnails), columns)):
        row = thumbnails[row_start : row_start + columns]
        for column_index, (path, image) in enumerate(row):
            x: int = column_index * width
            draw.text((x + 8, y + 5), path.name, fill="black", font=font)
            sheet.paste(image, (x, y + label_height))
        y += row_heights[row_index]

    sheet.save(output_path)


root: Path = Path(__file__).resolve().parents[2]
pdf_pages: list[Path] = sorted((root / "tmp" / "pdfs").glob("test-bench-guide-*.png"))
asset_images: list[Path] = sorted(
    (root / "docs" / "src" / "assets" / "Test_Bench").glob("pic (*).PNG"),
    key=lambda path: int(path.stem.removeprefix("pic (").removesuffix(")")),
)
make_contact_sheet(pdf_pages, root / "tmp" / "pdfs" / "pdf-pages-contact-sheet.jpg", 4, 360)
make_contact_sheet(asset_images, root / "tmp" / "pdfs" / "assets-contact-sheet.jpg", 4, 360)
