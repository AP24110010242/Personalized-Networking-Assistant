"""
Definitive CJM and Brainstorming fix - wipe larger redact areas to catch all layers.
"""
import fitz
import sys
import os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

def fix_pdf(folder, filename, fix_fn):
    path = os.path.join(BASE, folder, filename)
    doc = fitz.open(path)
    fix_fn(doc)
    tmp = path + ".tmp"
    doc.save(tmp, garbage=4, deflate=True, clean=True)
    doc.close()
    os.replace(tmp, path)
    print(f"Saved: {filename}")

def txt(page, x, y, text, size=8):
    page.insert_text((x, y), text, fontname="helv", fontsize=size, color=(0,0,0))

def redact(page, rects):
    for r in rects:
        page.add_redact_annot(fitz.Rect(r), fill=(1,1,1))
    page.apply_redactions()

# ============================================================
# FIX CJM: Wipe ENTIRE data area (all 3 stages) and rewrite
# ============================================================
def cjm_fix(doc):
    page = doc[0]

    # Wipe the entire data area of the table (everything right of the "Phase of Journey" label column)
    # Phase label col is x=78-215, data starts at x=216
    # Table rows start at y=370, end at y=645
    redact(page, [(216, 370, 756, 650)])

    # Rewrite all 3 stages, all 4 rows cleanly
    stage_x = [220, 332, 460]  # left x for each stage column

    all_content = {
        "actions": [
            ["Searches for networking events", "Signs up via registration portal", "Reviews event agenda online"],
            ["Arrives at event venue", "Checks in at reception", "Looks for familiar faces"],
            ["Opens Streamlit app", "Enters topic & interests", "Reviews AI icebreakers"],
        ],
        "touchpoint": [
            ["Event discovery websites", "Email newsletter signup", "LinkedIn event page"],
            ["Physical event desk", "Badge scanner", "Welcome brochure"],
            ["Networking Assistant app", "FastAPI /generate API", "AI response cards"],
        ],
        "thought": [
            ["Will I meet relevant people?", "Is the registration simple?", "Should I prepare talking?"],
            ["Where should I stand?", "Who should I talk to?", "How do I start a conv?"],
            ["These prompts are helpful!", "I can break ice with this", "What if I save these?"],
        ],
        "feeling": ["Nervous but curious", "Anxious but hopeful", "Confident and engaged"],
    }

    for si, sx in enumerate(stage_x):
        col_w = 110  # width per column
        # Actions (bullet y: 388, 408, 428)
        for bi, line in enumerate(all_content["actions"][si]):
            txt(page, sx+3, 388 + bi*20, line, size=7.5)
        # Touchpoint (bullet y: 464, 484, 504)
        for bi, line in enumerate(all_content["touchpoint"][si]):
            txt(page, sx+3, 464 + bi*20, line, size=7.5)
        # Thought (bullet y: 552, 572, 592)
        for bi, line in enumerate(all_content["thought"][si]):
            txt(page, sx+3, 552 + bi*20, line, size=7.5)
        # Feeling
        txt(page, sx+3, 631, all_content["feeling"][si], size=7.5)

# ============================================================
# FIX Brainstorming: Wipe entire idea/suggestion and final idea columns
# ============================================================
def brainstorm_fix(doc):
    page = doc[0]

    # Wipe entire idea/suggestion column (x=262-365, y=340-475) - all rows
    redact(page, [(262, 340, 365, 475)])
    # Wipe final idea column (x=130-215, y=608-682)
    redact(page, [(130, 608, 215, 682)])

    # Write Step 1 ideas per row
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

    # Write Step 2 final ideas
    final_ideas = ["Networking Prompt Gen", "Event Theme Classifier", "Live Fact Checker"]
    step2_y0 = [612.8, 636.8, 661.8]
    for i, y0 in enumerate(step2_y0):
        txt(page, 132, y0+11, final_ideas[i], size=7.5)

# Run
fix_pdf("2. Requirement Analysis", "Customer Journey Map.pdf", cjm_fix)
fix_pdf("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", brainstorm_fix)
print("Done!")
