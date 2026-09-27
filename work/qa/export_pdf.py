"""Export a .pptx to PDF through PowerPoint COM, then render each PDF page to PNG.

LibreOffice and poppler are not installed on this machine, so PowerPoint does the
PDF export and PyMuPDF does the page rendering for visual checks.

Usage:
    python work/qa/export_pdf.py <deck.pptx> [--png-dir <folder>] [--dpi 110]
The PDF is written next to the .pptx with the same name.
"""

import argparse
import sys
from pathlib import Path


def export(pptx: Path) -> Path:
    import pythoncom
    import win32com.client

    pdf = pptx.with_suffix(".pdf")
    pythoncom.CoInitialize()
    app = win32com.client.DispatchEx("PowerPoint.Application")
    try:
        pres = app.Presentations.Open(str(pptx.resolve()), ReadOnly=True, Untitled=False, WithWindow=False)
        try:
            pres.SaveAs(str(pdf.resolve()), 32)  # 32 = ppSaveAsPDF
        finally:
            pres.Close()
    finally:
        app.Quit()
        pythoncom.CoUninitialize()
    return pdf


def render(pdf: Path, out_dir: Path, dpi: int) -> list[Path]:
    import fitz

    out_dir.mkdir(parents=True, exist_ok=True)
    for old in out_dir.glob(pdf.stem + "-p*.png"):
        old.unlink()
    paths = []
    doc = fitz.open(str(pdf))
    for i, page in enumerate(doc, 1):
        pix = page.get_pixmap(dpi=dpi)
        p = out_dir / f"{pdf.stem}-p{i:02d}.png"
        pix.save(str(p))
        paths.append(p)
    return paths


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--png-dir", default=None)
    ap.add_argument("--dpi", type=int, default=110)
    a = ap.parse_args()
    pptx = Path(a.pptx)
    pdf = export(pptx)
    print("pdf", pdf)
    if a.png_dir:
        for p in render(pdf, Path(a.png_dir), a.dpi):
            print("png", p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
