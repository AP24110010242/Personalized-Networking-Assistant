"""
FINAL FIX: Uses proper PDF redaction to permanently erase content,
then writes clean text once. Saves as a new file to avoid incremental stacking.
"""
import fitz
import sys
import os
import shutil
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"
BACKUP = os.path.join(BASE, "pdf_backups_final")
os.makedirs(BACKUP, exist_ok=True)

def fix_pdf(folder, filename, fix_fn):
    """Load PDF, apply fix function, save to new file (replacing original)."""
    path = os.path.join(BASE, folder, filename)
    # Back up if not already backed up
    bk = os.path.join(BACKUP, folder.replace(" ", "_").replace("&","and") + "_" + filename)
    if not os.path.exists(bk):
        shutil.copy2(path, bk)

    doc = fitz.open(path)
    fix_fn(doc)
    # Save to temp path first, then replace original
    tmp = path + ".tmp"
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)
    print(f"Fixed: {filename}")

def txt(page, x, y, text, size=8, bold=False):
    fn = "hebo" if bold else "helv"
    page.insert_text((x, y), text, fontname=fn, fontsize=size, color=(0,0,0))

def tbox(page, rect, text, size=8, bold=False, align=0):
    fn = "hebo" if bold else "helv"
    page.insert_textbox(fitz.Rect(rect), text, fontname=fn, fontsize=size, align=align, color=(0,0,0))

def redact(page, rects):
    """Apply permanent redactions to erase text in specified rectangles."""
    for r in rects:
        page.add_redact_annot(fitz.Rect(r), fill=(1,1,1))
    page.apply_redactions()

# ============================================================
# FIX 1: Brainstorming
# ============================================================
def brainstorming_fix(doc):
    page = doc[0]

    # Redact the "Idea/Suggestion" column area in step 1 (x=262-365, rows y=342-460)
    redact(page, [(262, 342, 365, 462)])

    # Redact "Final Idea" column area in step 2 (x=130-210, rows y=610-680)
    redact(page, [(130, 610, 210, 680)])

    # Step 1: write idea per row
    ideas = [
        "AI icebreaker generator",
        "Real-time topic suggester",
        "Event theme classifier",
        "Voice networking prompts",
        "Fact-check conv. helper",
    ]
    step1_y0 = [344.8, 369.8, 393.8, 417.8, 441.8]
    for i, y0 in enumerate(step1_y0):
        txt(page, 264, y0+11, ideas[i], size=7.5)

    # Step 2: write final idea per row
    final_ideas = [
        "Networking Prompt Gen",
        "Event Theme Classifier",
        "Live Fact Checker",
    ]
    step2_y0 = [612.8, 636.8, 661.8]
    for i, y0 in enumerate(step2_y0):
        txt(page, 132, y0+11, final_ideas[i], size=7.5)

# ============================================================
# FIX 2: Customer Journey Map Page 1 - fix Stage 3 column
# ============================================================
def cjm_fix(doc):
    page = doc[0]

    # Stage 3 data currently truncated. Redact all stage 3 column content area.
    # Stage 3 column x range: 457-612
    # Content rows: Actions y~370-435, Touchpoint y~440-510, Thought y~525-600, Feeling y~612-650
    redact(page, [(457, 370, 614, 650)])

    # Rewrite stage 3 content
    s3x = 460

    # Actions row (~y=378, 398, 418)
    for i, line in enumerate(["Opens Streamlit app", "Enters topic & interests", "Reviews AI icebreakers"]):
        txt(page, s3x, 388 + i*20, line, size=7.5)

    # Touchpoint row (~y=454, 474, 494)
    for i, line in enumerate(["Networking Assistant app", "FastAPI /generate API", "AI response cards"]):
        txt(page, s3x, 464 + i*20, line, size=7.5)

    # Thought row (~y=542, 562, 582)
    for i, line in enumerate(["These prompts look helpful!", "I can use this to break ice", "What if I save these?"]):
        txt(page, s3x, 552 + i*20, line, size=7.5)

    # Feeling row (~y=621)
    txt(page, s3x, 631, "Confident and engaged", size=7.5)

# ============================================================
# FIX 3: Communication
# ============================================================
def communication_fix(doc):
    page = doc[0]

    # Redact all table rows content area (keep headers)
    # Header row at y=334-356, rows start at y=358
    redact(page, [(44, 356, 540, 536)])

    # Write all 6 rows
    rows = [
        (1, "Team Standup",         "Daily",      "Discord",      "All 5",     "Daily sprint sync & story alignment"),
        (2, "Progress Update",      "Weekly",     "GitHub",       "All 5",     "Feature branch merge & code reviews"),
        (3, "Issue/Bug Discussion", "As Needed",  "WhatsApp",     "As needed", "Debug & resolve blockers"),
        (4, "Stakeholder Review",   "Bi-Weekly",  "Google Meet",  "All 5",     "Share progress with mentor"),
        (5, "Final Demo Rehearsal", "Once",       "Discord",      "All 5",     "Rehearse final demonstration"),
        (6, "",                     "",           "",             "",          ""),
    ]
    row_height = 31.5
    y0 = 366.0

    for i, (sno, comm_type, freq, channel, parts, purpose) in enumerate(rows):
        y = y0 + i * row_height
        txt(page, 47, y+10, str(sno), size=8)
        tbox(page, (73, y+2, 184, y+29), comm_type, size=7.5)
        tbox(page, (185, y+2, 253, y+29), freq, size=7.5)
        tbox(page, (255, y+2, 338, y+29), channel, size=7.5)
        tbox(page, (340, y+2, 418, y+29), parts, size=7.5)
        tbox(page, (420, y+2, 535, y+29), purpose, size=7)

    # Redact challenge rows area and rewrite
    redact(page, [(44, 620, 540, 725)])
    challenges = [
        (632.7, "Python 3.14 library compilation errors on Windows",
                "Downgraded to Python 3.10 venv; updated requirements.txt"),
        (668.7, "GPT-2 model slow on local CPU",
                "Batched generation; capped max tokens to 60"),
        (704.7, "pytest failing on Windows file path separators",
                "Used pathlib.Path for cross-platform compatibility"),
    ]
    for ry, chal, res in challenges:
        tbox(page, (50, ry, 235, ry+18), chal, size=7.5)
        tbox(page, (240, ry, 535, ry+18), res, size=7.5)

# ============================================================
# FIX 4: Define Problem Statements
# ============================================================
def define_ps_fix(doc):
    page = doc[0]

    # Redact PS-1 and PS-2 rows completely
    redact(page, [(83, 498, 545, 582)])

    fs = 7.5
    # PS-1 row
    y1 = 504.8
    txt(page, 85, y1+8, "PS-1", size=fs, bold=True)
    tbox(page, (152, y1, 237, y1+32), "Attendee", size=fs)
    tbox(page, (239, y1, 293, y1+32), "Network\neasily", size=fs)
    tbox(page, (295, y1, 380, y1+32), "Social anxiety\n& conv. blocks", size=fs)
    tbox(page, (382, y1, 450, y1+32), "AI suggests\nice-breakers", size=fs)
    tbox(page, (452, y1, 540, y1+32), "Nervous /\nAwkward", size=fs)

    # PS-2 row
    y2 = 544.8
    txt(page, 85, y2+8, "PS-2", size=fs, bold=True)
    tbox(page, (152, y2, 237, y2+32), "Presenter", size=fs)
    tbox(page, (239, y2, 293, y2+32), "Share\ndetails", size=fs)
    tbox(page, (295, y2, 380, y2+32), "Struggles to\nlink themes to\ninterests", size=fs)
    tbox(page, (382, y2, 450, y2+32), "Fact-checker\nmaps topics", size=fs)
    tbox(page, (452, y2, 540, y2+32), "Unprepared", size=fs)

# ============================================================
# Run all fixes
# ============================================================
fix_pdf("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", brainstorming_fix)
fix_pdf("2. Requirement Analysis", "Customer Journey Map.pdf", cjm_fix)
fix_pdf("8.Project Demonstration", "Communication.pdf", communication_fix)
fix_pdf("1. Brainstorming & Ideation", "Define Problem Statements .pdf", define_ps_fix)

print("\nAll PDFs fixed with proper redactions!")
