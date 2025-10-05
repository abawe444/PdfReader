#!/usr/bin/env python3
"""
PDF Invoice Reader - Extract information from PDF invoices and organize in Excel
"""
import re
import os
from typing import List, Dict, Optional
import pdfplumber
import pandas as pd
from datetime import datetime


class InvoiceData:
    """Class to store invoice information"""
    def __init__(self):
        self.invoice_number: Optional[str] = None
        self.invoice_date: Optional[str] = None
        self.customer_name: Optional[str] = None
        self.total_amount: Optional[float] = None
        self.items: List[Dict] = []
        self.tax_amount: Optional[float] = None
        self.subtotal: Optional[float] = None


class PDFInvoiceReader:
    """Extract invoice data from PDF files"""
    
    def __init__(self):
        self.invoices: List[InvoiceData] = []
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract all text from a PDF file"""
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
                return text
        except Exception as e:
            print(f"Error reading PDF {pdf_path}: {e}")
            return ""
    
    def parse_invoice_data(self, text: str, filename: str) -> InvoiceData:
        """Parse invoice information from extracted text"""
        invoice = InvoiceData()
        
        # Extract invoice number (common patterns)
        invoice_patterns = [
            r'Invoice\s*#\s*:?\s*([A-Z0-9\-]+)',
            r'Invoice\s+Number\s*:?\s*([A-Z0-9\-]+)',
            r'رقم\s+الفاتورة\s*:?\s*([A-Z0-9\-]+)',
            r'INV[:\-\s]*([A-Z0-9\-]+)',
        ]
        for pattern in invoice_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                invoice.invoice_number = match.group(1).strip()
                break
        
        # Extract date (common patterns)
        date_patterns = [
            r'Date\s*:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
            r'Invoice\s+Date\s*:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
            r'التاريخ\s*:?\s*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
            r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        ]
        for pattern in date_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                invoice.invoice_date = match.group(1).strip()
                break
        
        # Extract customer name (common patterns)
        customer_patterns = [
            r'Bill\s+To\s*:?\s*([^\n]+)',
            r'Customer\s*:?\s*([^\n]+)',
            r'العميل\s*:?\s*([^\n]+)',
        ]
        for pattern in customer_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                invoice.customer_name = match.group(1).strip()
                break
        
        # Extract total amount (common patterns)
        total_patterns = [
            r'Total\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'Grand\s+Total\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'المجموع\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'الإجمالي\s*:?\s*\$?\s*([\d,]+\.?\d*)',
        ]
        for pattern in total_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    amount_str = match.group(1).replace(',', '')
                    invoice.total_amount = float(amount_str)
                    break
                except ValueError:
                    continue
        
        # Extract tax amount
        tax_patterns = [
            r'Tax\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'VAT\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'الضريبة\s*:?\s*\$?\s*([\d,]+\.?\d*)',
        ]
        for pattern in tax_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    amount_str = match.group(1).replace(',', '')
                    invoice.tax_amount = float(amount_str)
                    break
                except ValueError:
                    continue
        
        # Extract subtotal
        subtotal_patterns = [
            r'Subtotal\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'Sub\s+Total\s*:?\s*\$?\s*([\d,]+\.?\d*)',
            r'المجموع\s+الفرعي\s*:?\s*\$?\s*([\d,]+\.?\d*)',
        ]
        for pattern in subtotal_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                try:
                    amount_str = match.group(1).replace(',', '')
                    invoice.subtotal = float(amount_str)
                    break
                except ValueError:
                    continue
        
        # If no invoice number found, use filename
        if not invoice.invoice_number:
            invoice.invoice_number = os.path.splitext(os.path.basename(filename))[0]
        
        return invoice
    
    def process_pdf(self, pdf_path: str):
        """Process a single PDF invoice"""
        if not os.path.exists(pdf_path):
            print(f"File not found: {pdf_path}")
            return
        
        print(f"Processing: {pdf_path}")
        text = self.extract_text_from_pdf(pdf_path)
        
        if text:
            invoice = self.parse_invoice_data(text, pdf_path)
            self.invoices.append(invoice)
            print(f"  - Invoice: {invoice.invoice_number}")
            print(f"  - Date: {invoice.invoice_date}")
            print(f"  - Customer: {invoice.customer_name}")
            print(f"  - Total: {invoice.total_amount}")
    
    def process_directory(self, directory_path: str):
        """Process all PDF files in a directory"""
        if not os.path.exists(directory_path):
            print(f"Directory not found: {directory_path}")
            return
        
        pdf_files = [f for f in os.listdir(directory_path) if f.lower().endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in {directory_path}")
            return
        
        print(f"Found {len(pdf_files)} PDF file(s)")
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(directory_path, pdf_file)
            self.process_pdf(pdf_path)
    
    def export_to_excel(self, output_path: str):
        """Export extracted invoice data to Excel"""
        if not self.invoices:
            print("No invoice data to export")
            return
        
        # Prepare data for DataFrame
        data = []
        for invoice in self.invoices:
            row = {
                'Invoice Number': invoice.invoice_number,
                'Invoice Date': invoice.invoice_date,
                'Customer Name': invoice.customer_name,
                'Subtotal': invoice.subtotal,
                'Tax Amount': invoice.tax_amount,
                'Total Amount': invoice.total_amount,
            }
            data.append(row)
        
        # Create DataFrame and export to Excel
        df = pd.DataFrame(data)
        
        try:
            df.to_excel(output_path, index=False, engine='openpyxl')
            print(f"\nData exported successfully to: {output_path}")
            print(f"Total invoices exported: {len(self.invoices)}")
        except Exception as e:
            print(f"Error exporting to Excel: {e}")


def main():
    """Main function to demonstrate usage"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Extract invoice information from PDF files and export to Excel'
    )
    parser.add_argument(
        'input',
        help='Path to PDF file or directory containing PDF files'
    )
    parser.add_argument(
        '-o', '--output',
        default='invoices_data.xlsx',
        help='Output Excel file path (default: invoices_data.xlsx)'
    )
    
    args = parser.parse_args()
    
    reader = PDFInvoiceReader()
    
    # Check if input is a file or directory
    if os.path.isfile(args.input):
        reader.process_pdf(args.input)
    elif os.path.isdir(args.input):
        reader.process_directory(args.input)
    else:
        print(f"Error: {args.input} is not a valid file or directory")
        return
    
    # Export to Excel
    if reader.invoices:
        reader.export_to_excel(args.output)
    else:
        print("No invoices were processed successfully")


if __name__ == "__main__":
    main()
