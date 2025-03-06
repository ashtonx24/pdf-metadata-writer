from PyPDF2 import PdfReader, PdfWriter

input_pdf = "path/to/your/original_pdf.pdf"  # Full path to your PDF
output_pdf = "path/to/your/updated_pdf.pdf"    # Where you want to save the updated file

reader = PdfReader(input_pdf)
writer = PdfWriter()

# Copy pages
for page in reader.pages:
    writer.add_page(page)

# Add metadata as per your requirement.
writer.add_metadata({
    "/Title": "",
    "/Author": "",
    "/Subject": "",
    "/Keywords": "",
    "/Creator": "",
    "/Producer": "",
    "/CreationDate": "",
    "/ModDate": ""
})

# Save the new PDF
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print("Metadata updated successfully!")