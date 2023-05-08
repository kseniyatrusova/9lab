from PIL import Image, ImageFilter
from pathlib import Path

current_dir = ""
a = Path(current_dir).glob('*')
Path('newfile').mkdir(parents=True, exist_ok=True)
for i in a:
    if i.suffix in ['.jpg', '.png']:
        with Image.open(a) as img:
            img.load()
            new_img = img.filter(ImageFilter.EDGE_ENHANCE)
            new_img.save(Path('newfile/filter-' + i))

