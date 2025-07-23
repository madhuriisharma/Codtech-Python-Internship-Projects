import pandas as pd
from fpdf import FPDF

# Step 1: Read CSV data
df = pd.read_csv('data.csv')

# Step 2: Analyze the data
average_score = df['Score'].mean()
topper = df.loc[df['Score'].idxmax()]
departments = df['Department'].value_counts()

# Step 3: Create a PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 16)
        self.cell(0, 10, "Student Report", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, text):
        self.set_font("Arial", '', 12)
        self.multi_cell(0, 10, text)
        self.ln()

pdf = PDF()
pdf.add_page()

# Section 1: Summary
pdf.chapter_title("1. Summary")
pdf.chapter_body(f"Average Score: {average_score:.2f}")
pdf.chapter_body(f"Topper: {topper['Name']} ({topper['Department']}) - {topper['Score']}")

# Section 2: Students per Department
pdf.chapter_title("2. Students per Department")
for dept, count in departments.items():
    pdf.chapter_body(f"{dept}: {count} students")

# Section 3: Full Data Table
pdf.chapter_title("3. Full Data Table")
pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", 1)
pdf.cell(60, 10, "Department", 1)
pdf.cell(60, 10, "Score", 1)
pdf.ln()

pdf.set_font("Arial", '', 12)
for index, row in df.iterrows():
    pdf.cell(60, 10, row['Name'], 1)
    pdf.cell(60, 10, row['Department'], 1)
    pdf.cell(60, 10, str(row['Score']), 1)
    pdf.ln()

# Save the PDF
pdf.output("student_report.pdf")
print("✅ PDF Report Created Successfully!")