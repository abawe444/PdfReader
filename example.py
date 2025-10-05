#!/usr/bin/env python3
"""
Example usage of the PDF Invoice Reader
"""
from pdf_invoice_reader import PDFInvoiceReader
import os


def example_single_file():
    """Example: Process a single PDF invoice"""
    reader = PDFInvoiceReader()
    
    # Process a single PDF file
    pdf_path = "sample_invoice.pdf"
    
    if os.path.exists(pdf_path):
        reader.process_pdf(pdf_path)
        reader.export_to_excel("single_invoice_output.xlsx")
    else:
        print(f"Please place a PDF invoice at: {pdf_path}")


def example_directory():
    """Example: Process all PDFs in a directory"""
    reader = PDFInvoiceReader()
    
    # Process all PDF files in a directory
    directory = "invoices"
    
    if os.path.exists(directory):
        reader.process_directory(directory)
        reader.export_to_excel("all_invoices_output.xlsx")
    else:
        print(f"Please create a directory named '{directory}' with PDF invoices")


def example_programmatic():
    """Example: Using the reader programmatically"""
    reader = PDFInvoiceReader()
    
    # Process multiple specific files
    pdf_files = ["invoice1.pdf", "invoice2.pdf", "invoice3.pdf"]
    
    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            reader.process_pdf(pdf_file)
    
    # Export all processed invoices
    if reader.invoices:
        reader.export_to_excel("programmatic_output.xlsx")
        
        # You can also access the data programmatically
        print("\nInvoice Summary:")
        for invoice in reader.invoices:
            print(f"  {invoice.invoice_number}: {invoice.total_amount}")


if __name__ == "__main__":
    print("PDF Invoice Reader - Examples")
    print("=" * 50)
    
    print("\nExample 1: Processing a single file")
    example_single_file()
    
    print("\nExample 2: Processing a directory")
    example_directory()
    
    print("\nExample 3: Programmatic usage")
    example_programmatic()
