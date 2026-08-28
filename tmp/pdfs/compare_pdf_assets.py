from pathlib import Path
from PIL import Image, ImageChops, ImageStat


def normalized(path: Path) -> Image.Image:
    with Image.open(path) as source:
        image: Image.Image = source.convert("RGB")
        bbox: tuple[int, int, int, int] | None = ImageChops.difference(
            image, Image.new("RGB", image.size, "white")
        ).getbbox()
        if bbox is not None:
            image = image.crop(bbox)
        image.thumbnail((256, 256))
        canvas: Image.Image = Image.new("L", (256, 256), "white")
        grayscale: Image.Image = image.convert("L")
        x: int = (256 - grayscale.width) // 2
        y: int = (256 - grayscale.height) // 2
        canvas.paste(grayscale, (x, y))
        return canvas


def score(first: Image.Image, second: Image.Image) -> float:
    difference: Image.Image = ImageChops.difference(first, second)
    return ImageStat.Stat(difference).rms[0]


root: Path = Path(__file__).resolve().parents[2]
extracted: list[Path] = sorted((root / "tmp" / "pdfs" / "extracted").glob("*.png"))
assets: list[Path] = sorted(
    (root / "docs" / "src" / "assets" / "Test_Bench").glob("pic (*).PNG"),
    key=lambda path: int(path.stem.removeprefix("pic (").removesuffix(")")),
)
asset_images: dict[Path, Image.Image] = {path: normalized(path) for path in assets}
for extracted_path in extracted:
    extracted_image: Image.Image = normalized(extracted_path)
    matches: list[tuple[float, Path]] = sorted(
        (score(extracted_image, asset_image), asset_path)
        for asset_path, asset_image in asset_images.items()
    )
    print(
        f"{extracted_path.name}\t"
        + "\t".join(f"{path.name}:{value:.2f}" for value, path in matches[:3])
    )
