# filename: crypto_report.py
import requests
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch

def fetch_top_cryptocurrencies():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def create_pdf_report(data):
    if not data:
        print("No data to create report.")
        return
    
    doc = SimpleDocTemplate("top_10_cryptocurrencies.pdf", pagesize=letter)
    elements = []
    
    styles = getSampleStyleSheet()
    title = Paragraph("Top 10 Cryptocurrencies by Market Cap", styles['Title'])
    elements.append(title)
    
    table_data = [["Rank", "Name", "Symbol", "Price (USD)", "Market Cap (USD)", "24h Change (%)"]]
    for i, crypto in enumerate(data, 1):
        table_data.append([
            i,
            crypto['name'],
            crypto['symbol'].upper(),
            f"${crypto['current_price']:,.2f}",
            f"${crypto['market_cap']:,.0f}",
            f"{crypto['price_change_percentage_24h']:.2f}%"
        ])
    
    table = Table(table_data, colWidths=[0.5*inch, 1.5*inch, 1*inch, 1.5*inch, 2*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    elements.append(table)
    doc.build(elements)
    print("PDF report created successfully: top_10_cryptocurrencies.pdf")

def main():
    crypto_data = fetch_top_cryptocurrencies()
    if crypto_data:
        create_pdf_report(crypto_data)

if __name__ == "__main__":
    main()

print("Script executed successfully.")