"""
Fix script: Corrects all PDFs with wrong coordinates using exact block positions from inspection.
Strategy: Redact the wrong existing text blocks we added (by position), then write at correct coords.
"""
import fitz
import sys
import shutil
import os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BASE = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

def redact_rects(page, rects, fill=(1,1,1)):
    """Draw white rectangles over specified areas to erase existing content."""
    for r in rects:
        page.draw_rect(fitz.Rect(r), color=(1,1,1), fill=fill, overlay=True)

def add_text(page, x, y, text, fontsize=9, bold=False, color=(0,0,0), max_width=None):
    """Insert text at exact position."""
    fontname = "helv" if not bold else "hebo"
    if max_width and len(text) > 0:
        # Insert with auto line-break using textbox
        rc = page.insert_textbox(
            fitz.Rect(x, y, x + max_width, y + 80),
            text,
            fontsize=fontsize,
            fontname=fontname,
            color=color,
        )
    else:
        page.insert_text(
            (x, y),
            text,
            fontsize=fontsize,
            fontname=fontname,
            color=color,
        )

# ============================================================
# 1. FIX: Brainstorming & Idea Prioritization
# ============================================================
def fix_brainstorming():
    path = os.path.join(BASE, "1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection, the rows are at y positions:
    # Row 1: y0=349.9  Row 2: y0=374.0  Row 3: y0=398.1  Row 4: y0=422.2  Row 5: y0=446.4  Row 6: y0=470.5
    # Team Member block spans x 174-490, with names already filled at x=174
    # Category already filled in same block
    # We need to add "Idea / Suggestion" column - the header shows it at approx x=290-380 area
    # Looking at header block: 'S.No \nTeam Member \nIdea / Suggestion \nCategory \nGroup \nNo.'
    # The header is at [78.0,309.9,522.0,339.1]
    # S.No ~78-110, Team Member ~120-210, Idea/Suggestion ~220-340, Category ~350-430, Group ~440-522
    # But the data block [174.0,344.8,490.3,360.7] has 'Thrivedh Reddy\nAI/ML\n1'
    # So team member is at ~174, category at ~380, group at ~465
    # Idea/Suggestion column is at approx x=265-355 (between team member and category)

    # Erase wrong old "idea" text if any was added incorrectly
    # The ideas for each member:
    ideas = [
        "AI-powered icebreaker generator",
        "Real-time topic suggestion engine",
        "Event theme classifier using NLP",
        "Voice-guided networking prompts",
        "Fact-checking conversation helper",
        "",  # Row 6 empty
    ]
    row_y = [349.9, 374.0, 398.1, 422.2, 446.4, 470.5]

    # For Step 2 (Idea Prioritization) - Final Idea column
    # Header block [129.8,562.0,292.8,607.0] -> 'Final Idea \nFeasibility \n...'
    # The Final Idea column spans x ~130-200, Feasibility ~200-290
    # Data rows: y ~617, 641, 666
    # From inspection: '1\nMedium\nMedium\n3\nNo' at [78.0,612.8,498.1,625.8]
    # Group No at x=78, Final Idea at x~130, Feasibility at ~200, Importance at ~315, Priority ~430, Selected ~455
    final_ideas = [
        "Networking Prompt Generator",
        "Event Theme Classifier",
        "Live Fact Checker",
    ]
    step2_row_y = [612.8, 636.8, 661.8]

    # Erase the area where idea/suggestion text should go (rows 1-5)
    for i, y in enumerate(row_y[:5]):
        redact_rects(page, [(265, y-2, 355, y+14)])
        if ideas[i]:
            add_text(page, 267, y+10, ideas[i], fontsize=7.5, max_width=85)

    # Erase and fill Final Idea column for step 2
    for i, y in enumerate(step2_row_y):
        redact_rects(page, [(130, y-2, 220, y+14)])
        add_text(page, 132, y+10, final_ideas[i], fontsize=7.5, max_width=85)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Brainstorming & Idea Prioritization.pdf")

# ============================================================
# 2. FIX: Customer Journey Map - Page 1 (empty cells)
# ============================================================
def fix_cjm():
    path = os.path.join(BASE, "2. Requirement Analysis", "Customer Journey Map.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection page 1, the table has coloured header rows with Stage 1/2/3
    # But the action/touchpoint/thought/feeling rows have only bullet points (•)
    # We need to add text next to the bullets
    # The bullet points are at approx x=232, 414, 594 (for stages 1,2,3)
    # Let me look at actual positions by checking what we see on the image
    # Stage columns: Stage1=~232-385, Stage2=~390-575, Stage3=~580-760

    # Actions row: y~430-490 in the image at 100dpi → in PDF coords roughly y~543-600
    # Let me use approximate positions based on inspection

    # The CJM table structure (from visual inspection of the 100dpi render):
    # Row heights appear to be about 75px at 100dpi each
    # That = 75/100*72 = 54 pts per row
    # Header (Stage 1/2/3): y~300-355
    # Actions: y~355-430
    # Touchpoint: y~430-505
    # Customer Thought: y~505-580
    # Customer Feeling: y~580-640
    # (page 2 has Process Ownership and Opportunities)

    # Looking at the PDF which has bullets already, we just need to add text after bullets
    # Bullet positions: approximately y=375 for row 1 of Actions (first bullet)
    # Stage 1 x range: ~218-380, Stage 2: ~384-562, Stage 3: ~566-750

    # CJM content:
    # Stage 1: "Discovers the event" / "Event registration portal" / "Will I meet relevant people?" / "Nervous / Curious"
    # Stage 2: "Arrives at event venue" / "Networking app & event desk" / "Where should I stand?" / "Anxious / Hopeful"
    # Stage 3: "Engages with networking assistant" / "Streamlit app prompts" / "What topics should I discuss?" / "Confident / Engaged"

    stage_x = [220, 387, 567]  # Left x of each stage column

    # Row y positions (top of text area in each row) - estimated from visual
    rows = {
        "actions": [377, 397, 417],   # y positions for 3 bullet points in actions row
        "touchpoint": [453, 473, 493],
        "thought": [541, 561, 581],
        "feeling": [620],
    }

    content = {
        "actions": [
            ["Searches for networking events", "Signs up via registration portal", "Reviews event agenda online"],
            ["Arrives at event venue", "Checks in at reception desk", "Looks for familiar faces"],
            ["Opens Streamlit app on phone", "Enters event topic & interests", "Reviews AI-generated icebreakers"],
        ],
        "touchpoint": [
            ["Event discovery websites", "Email newsletter signup", "LinkedIn event page"],
            ["Physical event desk", "Badge scanner", "Welcome brochure"],
            ["Networking Assistant app", "FastAPI /generate endpoint", "AI response cards"],
        ],
        "thought": [
            ["Will I meet relevant people?", "Is the registration simple?", "Should I prepare talking points?"],
            ["Where should I stand?", "Who should I talk to first?", "How do I start a conversation?"],
            ["These prompts look helpful!", "I can use this to break the ice", "What if I save these for later?"],
        ],
        "feeling": [
            ["Nervous but curious"],
            ["Anxious but hopeful"],
            ["Confident and engaged"],
        ],
    }

    # Write content into cells - erase bullet area first then write text
    for stage_idx in range(3):
        sx = stage_x[stage_idx]

        # Actions
        for bi, act_text in enumerate(content["actions"][stage_idx]):
            y_pos = rows["actions"][bi]
            redact_rects(page, [(sx, y_pos-10, sx+170, y_pos+10)])
            add_text(page, sx+3, y_pos+2, act_text, fontsize=7, max_width=160)

        # Touchpoint
        for bi, tp_text in enumerate(content["touchpoint"][stage_idx]):
            y_pos = rows["touchpoint"][bi]
            redact_rects(page, [(sx, y_pos-10, sx+170, y_pos+10)])
            add_text(page, sx+3, y_pos+2, tp_text, fontsize=7, max_width=160)

        # Customer Thought
        for bi, ct_text in enumerate(content["thought"][stage_idx]):
            y_pos = rows["thought"][bi]
            redact_rects(page, [(sx, y_pos-10, sx+170, y_pos+10)])
            add_text(page, sx+3, y_pos+2, ct_text, fontsize=7, max_width=160)

        # Customer Feeling
        y_pos = rows["feeling"][0]
        feel_text = content["feeling"][stage_idx][0]
        redact_rects(page, [(sx, y_pos-10, sx+170, y_pos+18)])
        add_text(page, sx+3, y_pos+2, feel_text, fontsize=7.5, max_width=160)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Customer Journey Map.pdf page 1")

# ============================================================
# 3. FIX: Communication PDF - overlap issue
# ============================================================
def fix_communication():
    path = os.path.join(BASE, "8.Project Demonstration", "Communication.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection, the template rows at:
    # Row 1 (Team Standup Daily): y0=365.9
    # Row 2 (Progress Update Weekly): y0=397.4
    # Row 3 (Issue/Bug Discussion): y0=428.9
    # Row 4 (Stakeholder Review): y0=460.4
    # Row 5 (Final Demo Rehearsal): y0=491.9
    # Row 6: y0=523.4

    # Our added data blocks at y=343.0, 368.0, 392.0 are ABOVE the template rows
    # causing overlap. We need to erase our blocks and also erase the template's
    # row text that clashes, then rewrite cleanly.

    # Erase our incorrectly positioned text (y ~343-410)
    redact_rects(page, [(73, 340, 525, 420)])

    # Now erase the template pre-filled rows 1-2 text too to clean
    # Row 1 template: [45.2,365.9,195.9,376.0] -> '1 \nTeam Standup \nDaily'
    # Row 2 template: [45.2,397.4,205.2,407.5] -> '2 \nProgress Update \nWeekly'
    # We keep these but erase anything in Channel/Participants/Purpose columns of rows 1-2

    # Column x positions from header: S.No~45, CommType~73, Frequency~185,
    # Channel~225, Participants~330, Purpose~395
    # Actually from header: 'S.No Communication Type Frequency \nChannel / Tool \nParticipants \nPurpose'
    # From inspection [45.2,334.4,451.9,344.5]

    # Channel col ~x=225, Participants ~x=330, Purpose ~x=395
    # For rows 1 and 2 that already have template text, erase Channel/Part/Purpose:
    for row_y in [365.9, 397.4]:
        redact_rects(page, [(220, row_y-2, 540, row_y+13)])

    # Now write all 5 rows cleanly at the correct template row y positions:
    comm_data = [
        # (Type already in template for rows 1-2, Channel, Participants, Purpose)
        # Row 1: Team Standup Daily -> Channel=Discord, Participants=All 5, Purpose=Daily sync
        (365.9, "Discord", "All 5", "Daily sprint sync & story alignment"),
        # Row 2: Progress Update Weekly -> Channel=GitHub, Participants=All 5, Purpose=PR reviews
        (397.4, "GitHub", "All 5", "Feature branch merge & code reviews"),
        # Row 3: Issue/Bug Discussion As Needed
        (428.9, "WhatsApp", "As needed", "Debug & resolve blockers"),
        # Row 4: Stakeholder Review Bi-Weekly
        (460.4, "Google Meet", "All 5", "Share progress with mentor"),
        # Row 5: Final Demo Rehearsal Once
        (491.9, "Discord", "All 5", "Rehearse final demonstration"),
    ]

    for row_y, channel, parts, purpose in comm_data:
        add_text(page, 225, row_y+8, channel, fontsize=8, max_width=95)
        add_text(page, 325, row_y+8, parts, fontsize=8, max_width=70)
        add_text(page, 400, row_y+8, purpose, fontsize=7.5, max_width=125)

    # Fix Communication Challenges section - erase wrong text and redo
    # Challenge rows at y=632.7, 668.7, 704.7
    # Our data: [100.0,617.0,296.4,630.1] -> wrong position
    redact_rects(page, [(45, 615, 540, 635)])

    challenges = [
        (632.7, "Python 3.14 library compilation errors on Windows", "Downgraded to Python 3.10 venv; updated requirements.txt"),
        (668.7, "GPT-2 model slow on local CPU", "Batched generation; capped max tokens to 60"),
        (704.7, "Pytest failing on Windows file path separators", "Used pathlib.Path for cross-platform compatibility"),
    ]
    for row_y, chal, res in challenges:
        redact_rects(page, [(45, row_y-2, 540, row_y+14)])
        add_text(page, 50, row_y+10, chal, fontsize=7.5, max_width=180)
        add_text(page, 240, row_y+10, res, fontsize=7.5, max_width=290)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Communication.pdf")

# ============================================================
# 4. FIX: Problem-Solution Fit - Remove ONLINE/OFFLINE watermarks
# ============================================================
def fix_psf():
    path = os.path.join(BASE, "3. Project Design Phase", "Problem-Solution Fit.pdf")
    doc = fitz.open(path)
    page = doc[0]

    # ONLINE at [393.0,560.3,440.7,573.6] and OFFLINE at [393.0,591.8,445.3,605.1]
    # These are in box 8 (Channels of Behavior) - they are template labels
    # We keep them but add our content around them
    # Box 8 content at [390.0,524.0,495.8,535.7] -> 'Offline venues and meetups'
    # The ONLINE/OFFLINE labels are below that line
    # Erase them and replace with our channel text
    redact_rects(page, [(385, 555, 540, 615)])
    add_text(page, 390, 568, "ONLINE: LinkedIn, Discord", fontsize=8, max_width=145)
    add_text(page, 390, 585, "OFFLINE: Meetups, Events", fontsize=8, max_width=145)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Problem-Solution Fit.pdf")

# ============================================================
# 5. FIX: Define Problem Statements - Check if "Because" col needs data
# ============================================================
def fix_define_ps():
    path = os.path.join(BASE, "1. Brainstorming & Ideation", "Define Problem Statements .pdf")
    doc = fitz.open(path)
    page = doc[0]

    # From inspection:
    # PS-1 block: [84.0,504.8,443.3,535.2] -> 'PS-1\nAttendee\nNetwork easily\nSocial anxiety...\nblocks at events'
    # PS-1 "Which makes me feel": [456.0,504.8,537.8,517.8] -> 'Nervous / Awkward'
    # PS-2: [84.0,544.8,433.3,575.2] & [456.0,544.8,506.2,557.8] -> 'Unprepared'
    # The "Because" column seems to be missing from PS-1 and PS-2
    # Column x positions from header: Problem ~84-140, I am ~152-220, I'm trying ~239-295, But ~332, Because ~?, Which ~482
    # Header: [331.9,458.6,533.4,470.8] -> 'But  \nBecause \nWhich makes'
    # So But is at ~332, Because is at ~420, Which makes me feel ~482
    # Data block for PS-1 has: PS-1 | Attendee | Network easily | Social anxiety & starting conv blocks | Nervous/Awkward
    # The "Because" field should be between "But" and "Which makes me feel"
    # But text is "Social anxiety & starting conversation blocks at events" which occupies x=332 area
    # "Because" would be at x~420 area
    # Need to check what's missing - the data block spans 84-443 and includes all 5 fields
    # PS-1 data: PS-1, Attendee, Network easily, [But: Social anxiety...], [Because: ?], Nervous/Awkward
    # The "Because" field text is missing. Let's add it.

    # Erase the entire PS-1 and PS-2 data rows and rewrite cleanly
    redact_rects(page, [(84, 500, 545, 580)])

    fs = 7.5
    # PS-1 row at y=504.8
    add_text(page, 84, 515, "PS-1", fontsize=fs, bold=True)
    add_text(page, 152, 510, "Attendee", fontsize=fs, max_width=80)
    add_text(page, 239, 510, "Network easily", fontsize=fs, max_width=80)
    add_text(page, 295, 505, "Social anxiety &\nconversation blocks", fontsize=fs, max_width=85)
    add_text(page, 385, 510, "AI gives pre-event\ntopics", fontsize=fs, max_width=85)
    add_text(page, 464, 510, "Nervous /\nAwkward", fontsize=fs, max_width=80)

    # PS-2 row at y=544.8
    add_text(page, 84, 555, "PS-2", fontsize=fs, bold=True)
    add_text(page, 152, 555, "Presenter", fontsize=fs, max_width=80)
    add_text(page, 239, 555, "Share details", fontsize=fs, max_width=80)
    add_text(page, 295, 550, "Struggles to link\nthemes to interests", fontsize=fs, max_width=85)
    add_text(page, 385, 550, "Fact-checker maps\ntopics to events", fontsize=fs, max_width=85)
    add_text(page, 464, 555, "Unprepared", fontsize=fs, max_width=80)

    doc.save(path, incremental=True, encryption=fitz.PDF_ENCRYPT_KEEP)
    doc.close()
    print("Fixed: Define Problem Statements.pdf")

# Run all fixes
fix_brainstorming()
fix_cjm()
fix_communication()
fix_psf()
fix_define_ps()

print("\nAll fixes applied!")
