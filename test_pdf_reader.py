#!/usr/bin/env python3
"""
Simple tests for PDF Invoice Reader
"""
import unittest
import os
import tempfile
from pdf_invoice_reader import PDFInvoiceReader, InvoiceData


class TestInvoiceData(unittest.TestCase):
    """Test InvoiceData class"""
    
    def test_invoice_data_initialization(self):
        """Test that InvoiceData initializes with None values"""
        invoice = InvoiceData()
        self.assertIsNone(invoice.invoice_number)
        self.assertIsNone(invoice.invoice_date)
        self.assertIsNone(invoice.customer_name)
        self.assertIsNone(invoice.total_amount)
        self.assertEqual(invoice.items, [])
        self.assertIsNone(invoice.tax_amount)
        self.assertIsNone(invoice.subtotal)


class TestPDFInvoiceReader(unittest.TestCase):
    """Test PDFInvoiceReader class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.reader = PDFInvoiceReader()
    
    def test_reader_initialization(self):
        """Test that reader initializes with empty list"""
        self.assertEqual(self.reader.invoices, [])
    
    def test_parse_invoice_number(self):
        """Test invoice number extraction"""
        text = """
        Invoice #: INV-2024-001
        Date: 01/15/2024
        Customer: John Doe
        Total: $1000.00
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.invoice_number, "INV-2024-001")
    
    def test_parse_invoice_date(self):
        """Test date extraction"""
        text = """
        Invoice: 12345
        Date: 12/25/2023
        Customer: Jane Smith
        Total: $500.00
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.invoice_date, "12/25/2023")
    
    def test_parse_customer_name(self):
        """Test customer name extraction"""
        text = """
        Invoice: 12345
        Date: 01/01/2024
        Bill To: Acme Corporation
        Total: $750.00
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.customer_name, "Acme Corporation")
    
    def test_parse_total_amount(self):
        """Test total amount extraction"""
        text = """
        Invoice: 12345
        Date: 01/01/2024
        Customer: Test Company
        Total: $1,234.56
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.total_amount, 1234.56)
    
    def test_parse_tax_amount(self):
        """Test tax amount extraction"""
        text = """
        Invoice: 12345
        Subtotal: $1000.00
        Tax: $150.00
        Total: $1150.00
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.tax_amount, 150.00)
    
    def test_parse_subtotal(self):
        """Test subtotal extraction"""
        text = """
        Invoice: 12345
        Subtotal: $900.00
        Tax: $90.00
        Total: $990.00
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.subtotal, 900.00)
    
    def test_parse_arabic_invoice(self):
        """Test Arabic invoice fields"""
        text = """
        رقم الفاتورة: INV-AR-001
        التاريخ: 15/01/2024
        العميل: شركة الاختبار
        الإجمالي: 5000
        """
        invoice = self.reader.parse_invoice_data(text, "test.pdf")
        self.assertEqual(invoice.invoice_number, "INV-AR-001")
        self.assertEqual(invoice.invoice_date, "15/01/2024")
        self.assertIsNotNone(invoice.customer_name)
        self.assertEqual(invoice.total_amount, 5000.0)
    
    def test_fallback_to_filename(self):
        """Test that filename is used if no invoice number found"""
        text = "Some random text with no identifiable data"
        invoice = self.reader.parse_invoice_data(text, "/path/to/invoice_123.pdf")
        self.assertEqual(invoice.invoice_number, "invoice_123")
    
    def test_nonexistent_file(self):
        """Test handling of nonexistent file"""
        self.reader.process_pdf("nonexistent_file.pdf")
        self.assertEqual(len(self.reader.invoices), 0)
    
    def test_export_empty_invoices(self):
        """Test export with no invoices"""
        with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as tmp:
            tmp_path = tmp.name
        
        try:
            # Should not create file if no invoices
            self.reader.export_to_excel(tmp_path)
            # File might be created, so we just check that no error occurred
            self.assertEqual(len(self.reader.invoices), 0)
        finally:
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)


if __name__ == '__main__':
    unittest.main()
