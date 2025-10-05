# PDF Invoice Reader - Project Summary
# قارئ فواتير PDF - ملخص المشروع

## Overview | نظرة عامة

This project provides a complete solution for extracting invoice information from PDF files and organizing the data in Excel spreadsheets. It supports both Arabic and English invoices.

هذا المشروع يوفر حلاً متكاملاً لاستخراج معلومات الفواتير من ملفات PDF وتنظيم البيانات في جداول Excel. يدعم الفواتير العربية والإنجليزية.

## Features | المميزات

✅ **Multi-language Support** | دعم متعدد اللغات
- Extracts data from English and Arabic invoices
- Handles mixed language content

✅ **Automatic Field Detection** | الكشف التلقائي للحقول
- Invoice number/رقم الفاتورة
- Invoice date/تاريخ الفاتورة
- Customer name/اسم العميل
- Subtotal/المجموع الفرعي
- Tax amount/قيمة الضريبة
- Total amount/المبلغ الإجمالي

✅ **Flexible Processing** | معالجة مرنة
- Process single PDF files
- Batch process entire directories
- Programmatic API access

✅ **Excel Export** | تصدير Excel
- Clean, organized spreadsheet output
- Ready for further analysis
- Compatible with Excel, Google Sheets, etc.

## File Structure | هيكل الملفات

```
PdfReader/
├── pdf_invoice_reader.py    # Main script - البرنامج الرئيسي
├── example.py                # Usage examples - أمثلة الاستخدام
├── demo.py                   # Demo with sample data - عرض توضيحي
├── test_pdf_reader.py        # Unit tests - اختبارات الوحدة
├── requirements.txt          # Dependencies - المتطلبات
├── README.md                 # Main documentation - التوثيق الرئيسي
├── USAGE_EXAMPLES.md         # Detailed examples - أمثلة تفصيلية
└── .gitignore                # Git ignore rules - قواعد Git

```

## Quick Start | البدء السريع

### Installation | التثبيت
```bash
pip install -r requirements.txt
```

### Basic Usage | الاستخدام الأساسي
```bash
# Single file
python pdf_invoice_reader.py invoice.pdf

# Directory
python pdf_invoice_reader.py invoices/

# Custom output
python pdf_invoice_reader.py invoices/ -o output.xlsx
```

### Demo | العرض التوضيحي
```bash
python demo.py
```

## Testing | الاختبار

Run unit tests:
```bash
python -m unittest test_pdf_reader.py -v
```

All 12 tests pass successfully! ✅

## Dependencies | المتطلبات

- **PyPDF2** (3.0.1): PDF processing
- **pdfplumber** (0.10.3): Text extraction
- **openpyxl** (3.1.2): Excel file creation
- **pandas** (2.1.4): Data manipulation

All dependencies are verified and secure. ✅

## How It Works | كيف يعمل

1. **PDF Reading** | قراءة PDF
   - Opens PDF files using pdfplumber
   - Extracts all text content from pages

2. **Data Parsing** | تحليل البيانات
   - Uses regex patterns to identify invoice fields
   - Supports multiple formats and languages
   - Falls back to filename if no invoice number found

3. **Excel Export** | تصدير Excel
   - Organizes data in structured columns
   - Creates clean, professional spreadsheet
   - Easy to analyze and share

## Use Cases | حالات الاستخدام

✅ **Accounting & Bookkeeping** | المحاسبة ومسك الدفاتر
- Track all invoices in one place
- Calculate totals and taxes
- Generate reports

✅ **Business Analytics** | تحليلات الأعمال
- Analyze invoice patterns
- Customer spending analysis
- Revenue tracking

✅ **Automated Processing** | المعالجة التلقائية
- Batch process monthly invoices
- Integrate with existing systems
- Reduce manual data entry

## Customization | التخصيص

The tool can be customized for specific invoice formats by modifying the regex patterns in `pdf_invoice_reader.py`. See the code comments for guidance.

يمكن تخصيص الأداة لتنسيقات فواتير محددة عن طريق تعديل أنماط regex في `pdf_invoice_reader.py`. راجع تعليقات الكود للحصول على الإرشادات.

## Support & Documentation | الدعم والتوثيق

- **README.md**: General overview and installation
- **USAGE_EXAMPLES.md**: Detailed usage examples and patterns
- **demo.py**: Working demonstration with sample data
- **example.py**: Code examples for different scenarios

## Limitations | القيود

⚠️ **Text-based PDFs Only** | ملفات PDF نصية فقط
- Works with PDFs containing selectable text
- Scanned images require OCR (not included)

⚠️ **Format Variations** | اختلافات التنسيق
- Some invoice formats may need pattern adjustments
- Always verify extracted data for accuracy

## Future Enhancements | التحسينات المستقبلية

Potential improvements:
- OCR support for scanned invoices
- More invoice format patterns
- GUI interface
- Cloud integration
- Database storage
- Advanced analytics

## License | الترخيص

Open source - MIT License

## Contributing | المساهمة

Contributions welcome! Please feel free to:
- Report issues
- Suggest improvements
- Submit pull requests
- Add support for more invoice formats

---

**Ready to use!** | **جاهز للاستخدام!**

For questions or support, please open an issue on GitHub.
