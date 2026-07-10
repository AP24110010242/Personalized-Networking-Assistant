"""
Final micro-fixes for brainstorming row 5 and CJM Stage 2 truncation.
"""
import fitz
import sys
import os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"
BACKUP = os.path.join(BASE, "pdf_backups_final")

def fix_pdf(folder, filename, fix_fn):
    path = os.path.join(BASE, folder, filename)
    doc = fitz.open(path)
    fix_fn(doc)
    tmp = path + ".tmp"
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)
    print(f"Fixed: {filename}")

def txt(page, x, y, text, size=8):
    page.insert_text((x, y), text, fontname="helv", fontsize=size, color=(0,0,0))

def redact(page, rects):
    for r in rects:
        page.add_redact_annot(fitz.Rect(r), fill=(1,1,1))
    page.apply_redactions()

# ============================================================
# FIX Brainstorming: Row 5 idea text y position
# ============================================================
def brainstorm_fix(doc):
    page = doc[0]
    # Redact both idea/suggestion column and the row 6 area where it spilled
    redact(page, [(262, 437, 365, 480)])  # Row 5 and 6 area
    # Write row 5 idea within bounds of row 5 (y0=441.8, row height ~24pt)
    txt(page, 264, 452, "Fact-check conv. helper", size=7.5)
    # Row 6 stays empty

def cjm_fix(doc):
    page = doc[0]
    # Stage 2 column: bullet points at x=304-327, text starts at x=330
    # But text is being cut off. Stage 2 column width = 434-327 = 107 pts
    # Text was originally written starting at x=390 in a previous pass, but column needs x=330
    # Redact stage 2 column content area
    redact(page, [(328, 370, 435, 640)])

    s2x = 330
    # Actions
    for i, line in enumerate(["Arrives at event venue", "Checks in at reception", "Looks for familiar faces"]):
        txt(page, s2x, 388 + i*20, line, size=7.5)
    # Touchpoint
    for i, line in enumerate(["Physical event desk", "Badge scanner", "Welcome brochure"]):
        txt(page, s2x, 464 + i*20, line, size=7.5)
    # Thought
    for i, line in enumerate(["Where should I stand?", "Who should I talk to?", "How do I start a conv?"]):
        txt(page, s2x, 552 + i*20, line, size=7.5)
    # Feeling
    txt(page, s2x, 631, "Anxious but hopeful", size=7.5)

fix_pdf("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", brainstorm_fix)
fix_pdf("2. Requirement Analysis", "Customer Journey Map.pdf", cjm_fix)
print("\nMicro-fixes done!")
