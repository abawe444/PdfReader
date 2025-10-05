# PdfReader

قارئ فواتير PDF - استخراج المعلومات من فواتير PDF وتنظيمها في جدول Excel

PDF Invoice Reader - Extract information from PDF invoices and organize them in Excel spreadsheets

## Features | المميزات

- 📄 Extract data from PDF invoices | استخراج البيانات من فواتير PDF
- 📊 Export to Excel format (.xlsx) | التصدير إلى صيغة Excel
- 🔍 Automatic detection of invoice fields | الكشف التلقائي عن حقول الفاتورة
- 📁 Process single files or entire directories | معالجة ملف واحد أو مجلدات كاملة
- 🌍 Support for Arabic and English invoices | دعم الفواتير العربية والإنجليزية

## Extracted Information | المعلومات المستخرجة

The tool automatically extracts the following information:
- Invoice Number | رقم الفاتورة
- Invoice Date | تاريخ الفاتورة
- Customer Name | اسم العميل
- Subtotal | المجموع الفرعي
- Tax Amount | قيمة الضريبة
- Total Amount | المبلغ الإجمالي

## Installation | التثبيت

1. Clone the repository:
```bash
git clone https://github.com/abawe444/PdfReader.git
cd PdfReader
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage | الاستخدام

### Command Line | سطر الأوامر

#### Process a single PDF file | معالجة ملف PDF واحد
```bash
python pdf_invoice_reader.py invoice.pdf
```

#### Process all PDFs in a directory | معالجة جميع ملفات PDF في مجلد
```bash
python pdf_invoice_reader.py invoices/
```

#### Specify custom output file | تحديد ملف إخراج مخصص
```bash
python pdf_invoice_reader.py invoices/ -o output.xlsx
```

### Programmatic Usage | الاستخدام البرمجي

```python
from pdf_invoice_reader import PDFInvoiceReader

# Create reader instance
reader = PDFInvoiceReader()

# Process a single PDF
reader.process_pdf("invoice.pdf")

# Or process entire directory
reader.process_directory("invoices/")

# Export to Excel
reader.export_to_excel("output.xlsx")

# Access data programmatically
for invoice in reader.invoices:
    print(f"Invoice: {invoice.invoice_number}")
    print(f"Total: {invoice.total_amount}")
```

## Examples | أمثلة

See `example.py` for more usage examples.

```bash
python example.py
```

## Requirements | المتطلبات

- Python 3.7+
- PyPDF2
- pdfplumber
- openpyxl
- pandas

## Project Structure | هيكل المشروع

```
PdfReader/
├── pdf_invoice_reader.py    # Main script | البرنامج الرئيسي
├── example.py                # Usage examples | أمثلة الاستخدام
├── requirements.txt          # Dependencies | التبعيات
└── README.md                 # Documentation | التوثيق
```

## Output Format | صيغة المخرجات

The Excel output includes the following columns:
| Column | Description |
|--------|-------------|
| Invoice Number | Unique invoice identifier |
| Invoice Date | Date of invoice |
| Customer Name | Customer/client name |
| Subtotal | Amount before tax |
| Tax Amount | Tax/VAT amount |
| Total Amount | Final total amount |

## Supported Invoice Formats | صيغ الفواتير المدعومة

The tool supports various invoice formats including:
- Standard business invoices
- Arabic invoices (فواتير عربية)
- English invoices
- Mixed language invoices

## Tips for Best Results | نصائح للحصول على أفضل النتائج

1. Ensure PDFs contain text (not just scanned images)
2. Use clear, well-formatted invoice PDFs
3. Check the extracted data in Excel for accuracy
4. Customize patterns in the code if needed for specific invoice formats

## Troubleshooting | استكشاف الأخطاء

If data is not extracted correctly:
1. Check that the PDF contains extractable text (not just images)
2. Verify the invoice format matches common patterns
3. Review the console output for any error messages
4. Consider customizing the regex patterns for your specific invoice format

## Contributing | المساهمة

Contributions are welcome! Please feel free to submit issues or pull requests.

## License | الترخيص

This project is open source and available under the MIT License.