"""
Final comprehensive fix for all PDF issues.
"""
import fitz
import sys
import os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

def white_rect(page, rect):
    r = fitz.Rect(rect)
    shape = page.new_shape()
    shape.draw_rect(r)
    shape.finish(color=(1,1,1), fill=(1,1,1))
    shape.commit(overlay=True)

def txt(page, x, y, text, size=8, bold=False):
    fn = "hebo" if bold else "helv"
    page.insert_text((x, y), text, fontname=fn, fontsize=size, color=(0,0,0))

def tbox(page, rect, text, size=8, bold=False, align=0):
    fn = "hebo" if bold else "helv"
    rc = page.insert_textbox(fitz.Rect(rect), text, fontname=fn, fontsize=size, align=align, color=(0,0,0))
    return rc

# ============================================================
# FIX 1: Brainstorming - fix Y positions for idea column
# ============================================================
def fix_brainstorming():
    path = os.path.join(BASE, "1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # Step 1: From inspection, team member rows y0 values: 344.8, 369.8, 393.8, 417.8, 441.8
    # Text baseline is at y0+13 approx. 
    # Idea/Suggestion column: x range = 263-360 (between Team Member and Category)
    ideas = [
        "AI icebreaker generator",
        "Real-time topic suggester",
        "Event theme classifier",
        "Voice networking prompts",
        "Fact-check conv. helper",
    ]
    step1_y0 = [344.8, 369.8, 393.8, 417.8, 441.8]

    for i, y0 in enumerate(step1_y0):
        white_rect(page, (262, y0-1, 365, y0+16))
        txt(page, 264, y0+11, ideas[i], size=7.5)

    # Step 2: Final Idea column: x range = 130-210
    # Row y0 values: 612.8, 636.8, 661.8
    final_ideas = [
        "Networking Prompt Gen",
        "Event Theme Classifier",
        "Live Fact Checker",
    ]
    step2_y0 = [612.8, 636.8, 661.8]

    for i, y0 in enumerate(step2_y0):
        white_rect(page, (130, y0-1, 210, y0+16))
        txt(page, 132, y0+11, final_ideas[i], size=7.5)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Brainstorming.pdf")

# ============================================================
# FIX 2: Customer Journey Map Page 1 - fix Stage 3 truncation
# ============================================================
def fix_cjm():
    path = os.path.join(BASE, "2. Requirement Analysis", "Customer Journey Map.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # Stage 3 column: bullet points at x=434-456, content starts at x=460
    # But page max x ~ 615 and our text is being truncated
    # Fix: erase stage 3 column content and rewrite with shorter text

    stage3_x = 460
    col_w = 148  # width of stage 3 column (to x=608)

    # Row y positions (from inspection):
    # Actions: 378, 398, 418
    # Touchpoint: 454, 474, 494
    # Thought: 542, 562, 582
    # Feeling: 621

    # Erase current truncated stage 3 content
    white_rect(page, (457, 372, 612, 640))

    # Rewrite stage 3 content
    stage3_content = {
        "actions": ["Opens Streamlit app", "Enters event topic", "Reviews AI icebreakers"],
        "touchpoint": ["Networking Assistant app", "FastAPI /generate", "AI response cards"],
        "thought": ["These prompts look helpful!", "I can use this to break ice", "What if I save these?"],
        "feeling": "Confident and engaged",
    }

    for i, line in enumerate(stage3_content["actions"]):
        txt(page, stage3_x, 388 + i*20, line, size=7.5)

    for i, line in enumerate(stage3_content["touchpoint"]):
        txt(page, stage3_x, 464 + i*20, line, size=7.5)

    for i, line in enumerate(stage3_content["thought"]):
        txt(page, stage3_x, 552 + i*20, line, size=7.5)

    txt(page, stage3_x, 631, stage3_content["feeling"], size=7.5)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Customer Journey Map.pdf page 1 - Stage 3")

# ============================================================
# FIX 3: Communication PDF
# ============================================================
def fix_communication():
    path = os.path.join(BASE, "8.Project Demonstration", "Communication.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection, template has rows:
    # [45.2,365.9,195.9,376.0] -> '1 \nTeam Standup \nDaily'
    # [45.2,397.4,205.2,407.5] -> '2 \nProgress Update \nWeekly'
    # [45.2,428.9,220.4,439.0] -> '3 \nIssue / Bug Discussion As Needed'
    # [45.2,460.4,216.2,470.5] -> '4 \nStakeholder Review \nBi-Weekly'
    # [45.2,491.9,197.4,502.0] -> '5 \nFinal Demo Rehearsal \nOnce'
    # These template rows exist. Our previous fixes erased them. We need to restore them AND
    # add Channel/Participants/Purpose columns.

    # Erase our previous bad writes (all of rows area)
    white_rect(page, (44, 356, 540, 535))

    # Now write all rows with ALL columns
    # Cols: S.No=47, Type=73, Freq=185, Channel=255, Participants=340, Purpose=420
    rows = [
        (1, "Team Standup",        "Daily",     "Discord",     "All 5",    "Daily sprint sync & story alignment"),
        (2, "Progress Update",     "Weekly",    "GitHub",      "All 5",    "Feature branch merge & code reviews"),
        (3, "Issue/Bug Discussion","As Needed", "WhatsApp",    "As needed","Debug & resolve blockers"),
        (4, "Stakeholder Review",  "Bi-Weekly", "Google Meet", "All 5",    "Share progress with mentor"),
        (5, "Final Demo Rehearsal","Once",      "Discord",     "All 5",    "Rehearse final demonstration"),
        (6, "",                    "",          "",            "",         ""),
    ]
    row_height = 31.5
    y0 = 366.0

    for i, (sno, comm_type, freq, channel, parts, purpose) in enumerate(rows):
        y = y0 + i * row_height
        txt(page, 47, y+8, str(sno), size=8)
        tbox(page, (73, y, 184, y+30), comm_type, size=7.5)
        tbox(page, (185, y, 253, y+30), freq, size=7.5)
        tbox(page, (255, y, 338, y+30), channel, size=7.5)
        tbox(page, (340, y, 418, y+30), parts, size=7.5)
        tbox(page, (420, y, 535, y+30), purpose, size=7)

    # Fix challenge rows
    white_rect(page, (44, 620, 540, 725))
    challenges = [
        (632.7, "Python 3.14 library compilation errors on Windows",
                "Downgraded to Python 3.10 venv; updated requirements.txt"),
        (668.7, "GPT-2 model slow on local CPU",
                "Batched generation; capped max tokens to 60"),
        (704.7, "pytest failing on Windows file path separators",
                "Used pathlib.Path for cross-platform compatibility"),
    ]
    for row_y, chal, res in challenges:
        tbox(page, (50, row_y, 235, row_y+20), chal, size=7.5)
        tbox(page, (240, row_y, 535, row_y+20), res, size=7.5)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Communication.pdf")

# ============================================================
# FIX 4: Define Problem Statements
# ============================================================
def fix_define_ps():
    path = os.path.join(BASE, "1. Brainstorming & Ideation", "Define Problem Statements .pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection:
    # PS-1 data at y=504.8-535.2, PS-2 at y=544.8-575.2
    # Columns (from header inspection): PS~84, Iam~152, Itrying~239, But~295, Because~383, Whichmakes~452

    white_rect(page, (83, 498, 545, 582))

    fs = 7.5
    y1 = 504.8
    txt(page, 85, y1+8, "PS-1", size=fs, bold=True)
    tbox(page, (152, y1, 237, y1+32), "Attendee", size=fs)
    tbox(page, (239, y1, 293, y1+32), "Network\neasily", size=fs)
    tbox(page, (295, y1, 380, y1+32), "Social anxiety\n& conv. blocks\nat events", size=fs)
    tbox(page, (382, y1, 450, y1+32), "AI suggests\nice-breakers\nbefore event", size=fs)
    tbox(page, (452, y1, 540, y1+32), "Nervous /\nAwkward", size=fs)

    y2 = 544.8
    txt(page, 85, y2+8, "PS-2", size=fs, bold=True)
    tbox(page, (152, y2, 237, y2+32), "Presenter", size=fs)
    tbox(page, (239, y2, 293, y2+32), "Share\ndetails", size=fs)
    tbox(page, (295, y2, 380, y2+32), "Struggles to\nlink themes to\ninterests", size=fs)
    tbox(page, (382, y2, 450, y2+32), "Fact-checker\nmaps topics\nto events", size=fs)
    tbox(page, (452, y2, 540, y2+32), "Unprepared", size=fs)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Define Problem Statements.pdf")

# Run all
fix_brainstorming()
fix_cjm()
fix_communication()
fix_define_ps()
print("\nAll done!")
