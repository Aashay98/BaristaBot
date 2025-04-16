from fpdf import FPDF
import os

def generate_pdf(order_items, eta, session_id):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="BaristaBot Receipt", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Session ID: {session_id}", ln=True)
    pdf.cell(200, 10, txt=f"Estimated Time of Arrival: {eta} minutes", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Order Summary:", ln=True)
    for item in order_items:
        pdf.cell(200, 10, txt=f"- {item}", ln=True)

    os.makedirs("receipts", exist_ok=True)
    file_path = f"receipts/receipt_{session_id}.pdf"
    pdf.output(file_path)
    return file_path
