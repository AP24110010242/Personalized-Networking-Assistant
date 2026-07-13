import os
import fitz

source_dir = r"C:\Users\vijay\Desktop\Personalized Networking Assistant"

pdfs_to_check = [
    ("1. Brainstorming & Ideation", "Brainstorming & Idea Prioritization.pdf", 0),
    ("1. Brainstorming & Ideation", "Define Problem Statements .pdf", 0),
    ("1. Brainstorming & Ideation", "Empathy Map.pdf", 0),
    ("2. Requirement Analysis", "Customer Journey Map.pdf", 0),
    ("2. Requirement Analysis", "Customer Journey Map.pdf", 1),
    ("2. Requirement Analysis", "Data Flow Diagram.pdf", 0),
    ("2. Requirement Analysis", "Solution Requirements.pdf", 0),
    ("2. Requirement Analysis", "Technology Stack.pdf", 0),
    ("3. Project Design Phase", "Problem-Solution Fit.pdf", 0),
    ("3. Project Design Phase", "Proposed Solution.pdf", 0),
    ("3. Project Design Phase", "Solution Architecture.pdf", 0),
    ("4. Project Planning Phase", "Project Planning.pdf", 0),
    ("5. Project Development Phase", "Code-Layout, Readability and Reusability.pdf", 0),
    ("5. Project Development Phase", "Coding & Solution.pdf", 0),
    ("5. Project Development Phase", "No. of Functional Features Included in the Solution.pdf", 0),
    ("6.Project Testing", "Performance Testing.pdf", 0),
    ("7.Project Documentation", "Project Executable Files.pdf", 0),
    ("8.Project Demonstration", "Communication.pdf", 0),
    ("8.Project Demonstration", "Demonstration of Proposed Features.pdf", 0),
    ("8.Project Demonstration", "Project Demo Planning.pdf", 0),
    ("8.Project Demonstration", "Scalability & Future Plan.pdf", 0),
    ("8.Project Demonstration", "Team Involvement in Demonstration.pdf", 0),
]

out_dir = r"C:\Users\vijay\Desktop\Personalized Networking Assistant\page_previews"
os.makedirs(out_dir, exist_ok=True)

for folder, filename, page_num in pdfs_to_check:
    pdf_path = os.path.join(source_dir, folder, filename)
    if not os.path.exists(pdf_path):
        print(f"MISSING: {folder}/{filename}")
        continue
    doc = fitz.open(pdf_path)
    if page_num >= len(doc):
        print(f"Page {page_num} out of range for: {filename}")
        continue
    page = doc[page_num]
    pix = page.get_pixmap(dpi=100)
    safe_name = filename.replace(" ", "_").replace("&", "and").replace(".", "_")
    out_path = os.path.join(out_dir, f"{safe_name}_p{page_num+1}.png")
    pix.save(out_path)
    print(f"Rendered: {out_path}")
    doc.close()

print("Done.")
