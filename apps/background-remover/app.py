import datapane as dp
from rembg import remove
from PIL import Image
from pathlib import Path


def process_image(upload: Path) -> dp.Group:
    image = Image.open(upload)
    fixed = remove(image)
    image.save("original.png", "PNG")
    fixed.save("fixed.png", "PNG")

    return dp.Group(
        dp.Group(
            "Original Image 📷",
            dp.Media(file="original.png"),
            dp.Attachment(file="original.png"),
        ),
        dp.Group("Fixed Image 🔧", dp.Media(file="fixed.png"), dp.Attachment(file="fixed.png")),
        columns=2,
    )


heading = """
## Remove the background from your image
🐶 Try uploading an image to watch the background magically removed. 
Special thanks to the <a href="https://github.com/danielgatis/rembg">rembg</a> library 😁
"""
v = dp.View(
    dp.Group(
        heading,
        dp.Form(on_submit=process_image, target="results", controls=dp.Controls(upload=dp.File())),
        columns=2,
    ),
    dp.Group(process_image(upload=Path("zebra.jpg")), name="results"),
)

dp.serve_app(v)
