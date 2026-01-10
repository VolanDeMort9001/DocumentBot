from docx import Document
from docx.shared import Pt, Inches
from typing import Iterable


def create_document(text: Iterable[str]):
    doc = Document()