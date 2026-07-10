import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

source_dir = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

def inspect_pdf(folder, filename, page_nums=None):
    path = f"{source_dir}\\{folder}\\{filename}"
    doc = fitz.open(path)
    total_pages = len(doc)
    if page_nums is None:
        page_nums = list(range(min(2, total_pages)))
    for pn in page_nums:
        if pn >= total_pages:
            continue
        page = doc[pn]
        print(f"\n=== {filename} | Page {pn+1} ===")
        blocks = page.get_text("blocks")
        for b in blocks:
            x0, y0, x1, y1, text, block_no, block_type = b
            text = text.strip()
            if text:
                print(f"  [{x0:.1f},{y0:.1f},{x1:.1f},{y1:.1f}] -> {repr(text[:100])}")

# Check all remaining PDFs
pdfs = [
    ("1. Brainstorming & Ideation", "Define Problem Statements .pdf", [0]),
    ("2. Requirement Analysis", "Solution Requirements.pdf", [0]),
    ("2. Requirement Analysis", "Technology Stack.pdf", [0,1]),
    ("3. Project Design Phase", "Problem-Solution Fit.pdf", [0]),
    ("3. Project Design Phase", "Solution Architecture.pdf", [0,1]),
    ("4. Project Planning Phase", "Project Planning.pdf", [0]),
    ("5. Project Development Phase", "Code-Layout, Readability and Reusability.pdf", [0,1]),
    ("5. Project Development Phase", "Coding & Solution.pdf", [0,1]),
    ("5. Project Development Phase", "No. of Functional Features Included in the Solution.pdf", [0,1]),
    ("6.Project Testing", "Performance Testing.pdf", [0,1]),
    ("7.Project Documentation", "Project Executable Files.pdf", [0]),
    ("8.Project Demonstration", "Demonstration of Proposed Features.pdf", [0]),
    ("8.Project Demonstration", "Project Demo Planning.pdf", [0]),
    ("8.Project Demonstration", "Scalability & Future Plan.pdf", [0]),
    ("8.Project Demonstration", "Team Involvement in Demonstration.pdf", [0]),
]

for folder, filename, pnums in pdfs:
    inspect_pdf(folder, filename, pnums)
