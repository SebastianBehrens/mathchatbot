import fitz
def pdf_to_png(file_path):
    with fitz.open(file_path) as doc:
        page = doc.load_page(0)
        pixmap = page.get_pixmap(dpi=300)
        img = pixmap.tobytes()
    return img
