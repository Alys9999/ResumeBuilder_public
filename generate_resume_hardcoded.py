

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_TAB_ALIGNMENT, WD_TAB_LEADER


def describe_run(run):
    f = run.font
    attrs = []
    if f.name:        attrs.append(f.name)
    if f.size:        attrs.append(f"{f.size.pt:g} pt")
    if f.bold:        attrs.append("bold")
    if f.italic:      attrs.append("italic")
    if f.underline:   attrs.append("underline")
    if f.color and f.color.rgb:
        attrs.append(f"color=#{f.color.rgb}")
    return ", ".join(attrs) or "default"
def fmt_len(val):
    """Return a human-readable string for a Length, float, or None."""
    if val is None:
        return "inherit"
    # Length objects (Pt, Inches, etc.) expose .pt
    if hasattr(val, "pt"):
        return f"{val.pt:g} pt"
    # A float means “multiple of single-spacing”
    if isinstance(val, (float, int)):
        return f"{val}×"
    # Twips (an int) from the underlying XML
    return f"{val/20:g} pt"
res = []
with open('Zhaoyang_Lu_02_02_2025_sde.docx', 'rb') as resume_file:
    doc = Document(resume_file)
    for para in doc.paragraphs:
        pf = para.paragraph_format
        res.append(f"\n {para.text!r}")
        res.append(f"   style = {para.style.name}, align = {pf.alignment}")
        for run in para.runs:
            res.append(f" {run.text!r:25} [{describe_run(run)}]")
        ls_val   = fmt_len(pf.line_spacing)
        ls_rule  = pf.line_spacing_rule or "inherit"
        res.append(f"   line-spacing   = {ls_val}  (rule: {ls_rule})")
        res.append(f"   space-before   = {fmt_len(pf.space_before)}")
        res.append(f"   space-after    = {fmt_len(pf.space_after)}")
        res.append(f"   left-indent    = {fmt_len(pf.left_indent)}")
        res.append(f"   right-indent   = {fmt_len(pf.right_indent)}")
        res.append(f"   first-line ind = {fmt_len(pf.first_line_indent)}")

    for i, section in enumerate(doc.sections):
        res.append(f"\nSECTION {i}")
        res.append(f"  Page width: {section.page_width.pt:g} pt"
                   f"  ({section.page_width.inches:.2f} in)")
        res.append(f"  Page height: {section.page_height.pt:g} pt"
                   f"  ({section.page_height.inches:.2f} in)")
        res.append(f"  Header space: {section.header_distance.pt:g} pt"
                   f"  ({section.header_distance.inches:.2f} in)")
        res.append(f"  Footer space: {section.footer_distance.pt:g} pt"
                   f"  ({section.footer_distance.inches:.2f} in)")
        res.append(f"  Left   margin: {section.left_margin.pt:g} pt"
                   f"  ({section.left_margin.inches:.2f} in)")
        res.append(f"  Right  margin: {section.right_margin.pt:g} pt"
                   f"  ({section.right_margin.inches:.2f} in)")
        res.append(f"  Top    margin: {section.top_margin.pt:g} pt"
                   f"  ({section.top_margin.inches:.2f} in)")
        res.append(f"  Bottom margin: {section.bottom_margin.pt:g} pt"
                   f"  ({section.bottom_margin.inches:.2f} in)")


with open("formats.txt", 'w', encoding='utf-8') as f:
    for row in res:
        f.writelines(row)