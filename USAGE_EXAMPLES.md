# Usage Examples | أمثلة الاستخدام

## Quick Start | البدء السريع

### 1. Process a Single Invoice | معالجة فاتورة واحدة
```bash
# English invoice
python pdf_invoice_reader.py invoice.pdf

# Arabic invoice | فاتورة عربية
python pdf_invoice_reader.py فاتورة.pdf
```

### 2. Process Multiple Invoices | معالجة عدة فواتير
```bash
# Process all PDFs in a directory
python pdf_invoice_reader.py invoices/

# Specify output file name
python pdf_invoice_reader.py invoices/ -o monthly_invoices.xlsx
```

## Programmatic Usage | الاستخدام البرمجي

### Basic Example | مثال أساسي
```python
from pdf_invoice_reader import PDFInvoiceReader

# Create reader instance
reader = PDFInvoiceReader()

# Process a PDF
reader.process_pdf("invoice.pdf")

# Export to Excel
reader.export_to_excel("output.xlsx")
```

### Processing Multiple Files | معالجة ملفات متعددة
```python
from pdf_invoice_reader import PDFInvoiceReader
import os

reader = PDFInvoiceReader()

# Process all PDFs in a directory
invoice_dir = "invoices"
for filename in os.listdir(invoice_dir):
    if filename.endswith('.pdf'):
        filepath = os.path.join(invoice_dir, filename)
        reader.process_pdf(filepath)

# Export all invoices
reader.export_to_excel("all_invoices.xlsx")
```

### Accessing Extracted Data | الوصول إلى البيانات المستخرجة
```python
from pdf_invoice_reader import PDFInvoiceReader

reader = PDFInvoiceReader()
reader.process_directory("invoices/")

# Access individual invoices
for invoice in reader.invoices:
    print(f"Invoice: {invoice.invoice_number}")
    print(f"Date: {invoice.invoice_date}")
    print(f"Customer: {invoice.customer_name}")
    print(f"Total: ${invoice.total_amount}")
    print("-" * 40)
```

### Custom Processing | معالجة مخصصة
```python
from pdf_invoice_reader import PDFInvoiceReader
import pandas as pd

reader = PDFInvoiceReader()
reader.process_directory("invoices/")

# Create custom DataFrame
data = []
for invoice in reader.invoices:
    # Add custom calculations
    tax_percentage = 0
    if invoice.subtotal and invoice.tax_amount:
        tax_percentage = (invoice.tax_amount / invoice.subtotal) * 100
    
    data.append({
        'Invoice': invoice.invoice_number,
        'Date': invoice.invoice_date,
        'Customer': invoice.customer_name,
        'Amount': invoice.total_amount,
        'Tax %': round(tax_percentage, 2)
    })

df = pd.DataFrame(data)
df.to_excel("custom_report.xlsx", index=False)
```

## Expected Output | المخرجات المتوقعة

The Excel file will contain the following columns:

| Column | Description (EN) | الوصف (AR) |
|--------|------------------|------------|
| Invoice Number | Unique invoice identifier | رقم الفاتورة |
| Invoice Date | Date of the invoice | تاريخ الفاتورة |
| Customer Name | Customer or company name | اسم العميل |
| Subtotal | Amount before tax | المبلغ قبل الضريبة |
| Tax Amount | Tax or VAT amount | قيمة الضريبة |
| Total Amount | Final total | المبلغ الإجمالي |

## Supported Invoice Formats | أنواع الفواتير المدعومة

The tool can extract data from invoices with the following patterns:

### English Invoices
- Invoice #: INV-001
- Invoice Number: 12345
- Date: 01/15/2024
- Bill To: Customer Name
- Customer: Customer Name
- Subtotal: $1000.00
- Tax: $150.00
- Total: $1150.00

### Arabic Invoices | الفواتير العربية
- رقم الفاتورة: 12345
- التاريخ: 15/01/2024
- العميل: اسم العميل
- المجموع الفرعي: 1000
- الضريبة: 150
- الإجمالي: 1150

## Tips for Best Results | نصائح للحصول على أفضل النتائج

1. **Use Text-Based PDFs** | استخدم ملفات PDF نصية
   - Ensure PDFs contain selectable text
   - Scanned images won't work without OCR

2. **Standard Formats** | التنسيقات القياسية
   - Standard invoice layouts work best
   - Common field labels are recognized

3. **Check Results** | تحقق من النتائج
   - Always verify extracted data
   - Some invoices may need manual correction

4. **Batch Processing** | المعالجة الجماعية
   - Process similar invoices together
   - Organize PDFs by vendor/format

## Troubleshooting | استكشاف الأخطاء

### Problem: No data extracted
**Solution**: Check if PDF contains text (not just images)

### Problem: Wrong data extracted
**Solution**: The invoice format may be unusual. Check the patterns in the code.

### Problem: Missing fields
**Solution**: Some invoices may not have all fields. Check the original PDF.

### Problem: Arabic text not recognized
**Solution**: Ensure the PDF has proper UTF-8 encoding for Arabic text.
