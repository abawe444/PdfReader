#!/usr/bin/env python3
"""
Demo script to show PDF Invoice Reader capabilities
This creates a sample invoice scenario without requiring actual PDF files
"""
from pdf_invoice_reader import PDFInvoiceReader, InvoiceData
import pandas as pd


def create_sample_data():
    """Create sample invoice data to demonstrate the tool"""
    reader = PDFInvoiceReader()
    
    # Sample Invoice 1: English format
    invoice1 = InvoiceData()
    invoice1.invoice_number = "INV-2024-001"
    invoice1.invoice_date = "01/15/2024"
    invoice1.customer_name = "Acme Corporation"
    invoice1.subtotal = 1000.00
    invoice1.tax_amount = 150.00
    invoice1.total_amount = 1150.00
    
    # Sample Invoice 2: Arabic format
    invoice2 = InvoiceData()
    invoice2.invoice_number = "INV-2024-002"
    invoice2.invoice_date = "02/20/2024"
    invoice2.customer_name = "شركة الاختبار"
    invoice2.subtotal = 2000.00
    invoice2.tax_amount = 300.00
    invoice2.total_amount = 2300.00
    
    # Sample Invoice 3: Mixed data
    invoice3 = InvoiceData()
    invoice3.invoice_number = "INV-2024-003"
    invoice3.invoice_date = "03/10/2024"
    invoice3.customer_name = "Global Tech Solutions"
    invoice3.subtotal = 5000.00
    invoice3.tax_amount = 750.00
    invoice3.total_amount = 5750.00
    
    # Add invoices to reader
    reader.invoices = [invoice1, invoice2, invoice3]
    
    return reader


def demo_text_parsing():
    """Demonstrate text parsing capabilities"""
    print("\n" + "="*70)
    print("DEMO: Text Parsing from Invoice Content")
    print("="*70)
    
    reader = PDFInvoiceReader()
    
    # Sample English invoice text
    sample_text_en = """
    INVOICE
    
    Invoice #: INV-2024-999
    Date: 12/25/2023
    
    Bill To: John Doe Company
    123 Business Street
    
    Items:
    - Product A: $500.00
    - Product B: $300.00
    
    Subtotal: $800.00
    Tax (15%): $120.00
    Total: $920.00
    """
    
    print("\nSample Invoice Text (English):")
    print("-" * 70)
    print(sample_text_en.strip())
    
    invoice_en = reader.parse_invoice_data(sample_text_en, "sample_en.pdf")
    
    print("\nExtracted Data:")
    print(f"  Invoice Number: {invoice_en.invoice_number}")
    print(f"  Date: {invoice_en.invoice_date}")
    print(f"  Customer: {invoice_en.customer_name}")
    print(f"  Subtotal: ${invoice_en.subtotal}")
    print(f"  Tax: ${invoice_en.tax_amount}")
    print(f"  Total: ${invoice_en.total_amount}")
    
    # Sample Arabic invoice text
    sample_text_ar = """
    فاتورة
    
    رقم الفاتورة: INV-AR-555
    التاريخ: 15/01/2024
    
    العميل: شركة النجاح للتجارة
    
    المجموع الفرعي: 3000
    الضريبة: 450
    الإجمالي: 3450
    """
    
    print("\n" + "="*70)
    print("\nSample Invoice Text (Arabic):")
    print("-" * 70)
    print(sample_text_ar.strip())
    
    invoice_ar = reader.parse_invoice_data(sample_text_ar, "sample_ar.pdf")
    
    print("\nExtracted Data:")
    print(f"  Invoice Number: {invoice_ar.invoice_number}")
    print(f"  Date: {invoice_ar.invoice_date}")
    print(f"  Customer: {invoice_ar.customer_name}")
    print(f"  Total: ${invoice_ar.total_amount}")


def demo_excel_export():
    """Demonstrate Excel export functionality"""
    print("\n" + "="*70)
    print("DEMO: Excel Export")
    print("="*70)
    
    reader = create_sample_data()
    
    print("\nSample Invoices:")
    print("-" * 70)
    for i, invoice in enumerate(reader.invoices, 1):
        print(f"\n{i}. Invoice: {invoice.invoice_number}")
        print(f"   Date: {invoice.invoice_date}")
        print(f"   Customer: {invoice.customer_name}")
        print(f"   Subtotal: ${invoice.subtotal}")
        print(f"   Tax: ${invoice.tax_amount}")
        print(f"   Total: ${invoice.total_amount}")
    
    # Export to Excel
    output_file = "demo_output.xlsx"
    reader.export_to_excel(output_file)
    
    print("\n" + "="*70)
    print(f"✓ Data exported to: {output_file}")
    print("="*70)


def demo_data_analysis():
    """Demonstrate data analysis capabilities"""
    print("\n" + "="*70)
    print("DEMO: Data Analysis")
    print("="*70)
    
    reader = create_sample_data()
    
    # Calculate statistics
    total_revenue = sum(inv.total_amount for inv in reader.invoices if inv.total_amount)
    total_tax = sum(inv.tax_amount for inv in reader.invoices if inv.tax_amount)
    avg_invoice = total_revenue / len(reader.invoices) if reader.invoices else 0
    
    print(f"\nInvoice Summary:")
    print(f"  Total Invoices: {len(reader.invoices)}")
    print(f"  Total Revenue: ${total_revenue:,.2f}")
    print(f"  Total Tax Collected: ${total_tax:,.2f}")
    print(f"  Average Invoice Value: ${avg_invoice:,.2f}")
    
    # Create summary DataFrame
    data = []
    for invoice in reader.invoices:
        data.append({
            'Invoice': invoice.invoice_number,
            'Date': invoice.invoice_date,
            'Customer': invoice.customer_name,
            'Total': invoice.total_amount
        })
    
    df = pd.DataFrame(data)
    print("\nInvoice DataFrame:")
    print(df.to_string(index=False))


def main():
    """Run all demos"""
    print("\n" + "="*70)
    print(" PDF INVOICE READER - DEMO")
    print(" قارئ فواتير PDF - عرض توضيحي")
    print("="*70)
    
    # Run demos
    demo_text_parsing()
    demo_excel_export()
    demo_data_analysis()
    
    print("\n" + "="*70)
    print("Demo completed successfully!")
    print("To use with real PDF files, run:")
    print("  python pdf_invoice_reader.py your_invoice.pdf")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
