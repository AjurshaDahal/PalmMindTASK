from app.services.pdf_service import extract_text


text = extract_text("uploads/AjurshaDahalCV (1).pdf")

print(text[:2000])
