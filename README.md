# 🕷️ EasyScraper - Web Scraping Made Easy

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/31b28a64-58bb-4ce5-888e-96b868ccbc93" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/2fd578e1-4198-406e-9cc6-ea3d3c368f59" />

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/683dc6a0-9f51-4b21-9724-c3d400847f38" />


**EasyScraper** is a user-friendly web scraping application with a graphical interface, designed to be used by anyone without coding knowledge.

---

## 🌍 Language / Bahasa
- [🇺🇸 English](#-english)
- [🇮🇩 Bahasa Indonesia](#-bahasa-indonesia)

---

# 🇺🇸 English

## ✨ Key Features

### 🎯 Simple Scraper
- **One-Click Scraping**: Just enter URL and select data type
- **Multiple Data Types**: Text, links, images, tables, and custom CSS selectors
- **Real-time Results**: View scraping results instantly
- **Example URLs**: Built-in template URLs for testing
- **Progress Tracking**: Visual progress bars and status updates

### ⚙️ Advanced Scraper
- **Batch Processing**: Scrape multiple websites simultaneously
- **Custom Headers**: Configure User-Agent and other headers
- **Request Delay**: Control scraping speed to avoid rate limiting
- **Load from File**: Import URL lists from text files
- **Multiple URL Support**: Process hundreds of URLs in one session

### 📊 Data Management
- **Interactive Data Viewer**: Sortable table for viewing results
- **Multiple Export Formats**: CSV, Excel, JSON
- **Data Summary**: Statistics and overview of scraped data
- **Search & Filter**: Find specific data within results
- **Data Validation**: Automatic data cleaning and formatting

### 🔧 User-Friendly Features
- **Auto-Installer**: Automatic scripts for Python and dependencies installation
- **GUI Interface**: No command line required
- **Built-in Help**: Comprehensive tutorials and tips
- **Error Handling**: Clear and helpful error messages
- **Cross-Platform**: Works on Windows, Linux, and macOS

## 🚀 Quick Start

### For Beginners (No Python/Programming Experience Required)

#### Windows:
1. Download all files to a folder
2. **Option A**: Double-click `setup_simple.bat` (for older Windows)
3. **Option B**: Double-click `setup.bat` (for newer Windows)
4. Follow installer instructions
5. Double-click "EasyScraper" shortcut on Desktop

#### Linux/Mac:
1. Download all files to a folder
2. Open terminal in the folder
3. Run: `chmod +x setup.sh && ./setup.sh`
4. Follow installer instructions
5. Run: `./run_easyscraper.sh`

### For Developers

```bash
# Clone or download files
git clone <repository-url>
cd easyscraper

# Install dependencies
pip install -r requirements.txt

# Run application
python easyscraper.py
```

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 7+, Linux (Ubuntu 16.04+), macOS 10.12+
- **Python**: 3.6 or newer
- **RAM**: 512MB minimum, 1GB recommended
- **Storage**: 100MB free space
- **Internet**: Required for scraping and initial setup

### Python Dependencies
```txt
requests>=2.25.0          # HTTP requests
beautifulsoup4>=4.9.0     # HTML parsing
selenium>=3.141.0         # Browser automation
pandas>=1.3.0             # Data manipulation
lxml>=4.6.0               # XML/HTML parser
openpyxl>=3.0.0           # Excel file support
pillow>=8.0.0             # Image processing
```

## 🎮 How to Use

### 1. Simple Scraping

#### Step 1: Enter URL
- Type the target website URL
- Or select from provided example URLs
- URL validation is automatic

#### Step 2: Select Data Type
- 📝 **All Text**: Extract all text content from the page
- 🔗 **All Links**: Extract all hyperlinks with URLs
- 🖼️ **All Images**: Extract all image URLs and alt text
- 📊 **Tables**: Extract data from HTML tables
- 📋 **Custom CSS**: Use custom CSS selectors for specific data

#### Step 3: Start Scraping
- Click "🚀 Start Scraping" button
- Monitor progress in real-time
- View results in "Data Viewer" tab

### 2. Advanced Scraping

#### Configuration
- **User-Agent**: Set custom user agent to avoid blocking
- **Request Delay**: Set delay between requests (recommended: 1-3 seconds)
- **Headers**: Configure additional HTTP headers

#### Multiple URLs
- Enter multiple URLs (one per line)
- Load URLs from text file
- Support for bulk processing

#### Batch Processing
- Click "🚀 Scrape Multiple URLs"
- Monitor progress for each URL
- Automatic error handling for failed requests

### 3. Data Export

#### Export Formats
- **CSV**: For data analysis in Excel/Google Sheets
- **Excel**: .xlsx format with proper formatting
- **JSON**: For developers and API integration

#### Export Process
- Select desired format
- Choose save location
- Files are automatically saved with timestamps

## 📖 CSS Selector Guide

| Target | CSS Selector | Description |
|--------|-------------|-------------|
| All headings | `h1, h2, h3, h4, h5, h6` | Extract all heading elements |
| Specific class | `.product-name` | Elements with class "product-name" |
| Specific ID | `#main-content` | Element with ID "main-content" |
| Attribute contains | `a[href*="product"]` | Links containing "product" in href |
| Nested elements | `.container .item .price` | Price within item within container |
| Multiple classes | `.product.featured` | Elements with both classes |
| First child | `.list > li:first-child` | First list item |
| Text contains | `span:contains("Sale")` | Spans containing "Sale" text |

### Advanced CSS Selectors
```css
/* All external links */
a[href^="http"]:not([href*="yourdomain.com"])

/* Images with specific extensions */
img[src$=".jpg"], img[src$=".png"]

/* Form inputs */
input[type="text"], input[type="email"]

/* Tables with specific content */
table:has(th:contains("Price"))
```

## ⚠️ Ethics & Legal Guidelines

### ✅ Best Practices:
- **Check robots.txt** before scraping any website
- **Use reasonable delays** between requests (minimum 1 second)
- **Respect rate limits** and terms of service
- **Scrape only public data** that's freely accessible
- **Test with small data** before large-scale scraping
- **Monitor server response** and adjust accordingly

### ❌ Avoid These:
- **Don't spam requests** to servers
- **Don't scrape personal/sensitive data** without permission
- **Don't ignore rate limiting** or blocking mechanisms
- **Don't scrape copyrighted content** for commercial use
- **Don't overload servers** with excessive requests
- **Don't ignore website terms of service**

### Legal Considerations:
- Web scraping legality varies by jurisdiction
- Always respect website terms of service
- Consider reaching out to website owners for permission
- Be aware of data protection laws (GDPR, CCPA, etc.)

## 🔧 Troubleshooting

### Common Issues & Solutions

#### "Python not found"
**Solutions:**
- **Windows**: Run `setup_simple.bat` again
- **Linux**: Install Python3: `sudo apt install python3 python3-pip`
- **Mac**: Install via Homebrew: `brew install python`
- **All**: Download from [python.org](https://python.org/downloads)

#### "Module not found"
**Solutions:**
```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt

# Install specific package
pip install requests beautifulsoup4 pandas
```

#### "Website blocking requests"
**Solutions:**
- Increase delay between requests (5-10 seconds)
- Change User-Agent string
- Use different IP address or proxy
- Check if website allows scraping in robots.txt

#### "No data extracted"
**Solutions:**
- Check if website loads JavaScript content
- Verify CSS selectors using browser developer tools
- Ensure website structure hasn't changed
- Try different data extraction methods

#### "Permission denied errors"
**Solutions:**
- Run command prompt as Administrator (Windows)
- Use `sudo` for installation commands (Linux/Mac)
- Check file permissions and ownership

### Advanced Troubleshooting

#### Memory Issues
- Reduce batch size for multiple URLs
- Clear data regularly during long scraping sessions
- Increase virtual memory/swap space

#### Network Issues
- Check internet connection stability
- Configure proxy settings if behind corporate firewall
- Use VPN if geographical restrictions apply

## 🆕 Version History & Updates

### v1.0.0 (Current) - Stable Release
- ✅ Complete GUI interface with Tkinter
- ✅ Simple & Advanced scraping modes
- ✅ Multiple export formats (CSV, Excel, JSON)
- ✅ Auto-installer scripts for all platforms
- ✅ Cross-platform compatibility
- ✅ Built-in help and example URLs
- ✅ Error handling and progress tracking
- ✅ Data validation and cleaning

### Planned Features (v1.1.0):
- 🔄 Scheduled scraping with cron jobs
- 🌐 Proxy support and rotation
- 📱 Web-based interface option
- 🤖 AI-powered content extraction
- 📈 Data visualization charts
- 🔍 Advanced filtering and search
- 📧 Email notifications for completed jobs
- 🗃️ Database storage options

### Future Roadmap:
- Browser extension version
- Cloud-based scraping service
- Machine learning for content recognition
- API for third-party integration

## 📁 Project Structure

```
easyscraper/
├── easyscraper.py          # Main application
├── setup.bat               # Windows installer (new)
├── setup_simple.bat        # Windows installer (compatible)
├── setup.sh                # Linux/Mac installer
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── INSTALL_MANUAL.txt      # Manual installation guide
├── LICENSE                 # MIT license
└── examples/               # Example files and tutorials
    ├── sample_urls.txt     # Sample URLs for testing
    ├── css_selectors.md    # CSS selector examples
    └── tutorials/          # Step-by-step tutorials
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute:
1. **Bug Reports**: Report issues with detailed descriptions
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with enhancements
4. **Documentation**: Improve documentation and tutorials
5. **Testing**: Test on different platforms and configurations
6. **Translations**: Add support for more languages

### Development Setup:
```bash
# Fork and clone repository
git clone https://github.com/yourusername/easyscraper.git
cd easyscraper

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/

# Start development
python easyscraper.py
```

### Contribution Guidelines:
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation for changes
- Use meaningful commit messages
- Create feature branches for new development

## 📞 Support & Community

### Getting Help:
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/easyscraper/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/easyscraper/discussions)
- **Email Support**: easyscraper.support@gmail.com
- **Documentation**: Built-in help and online wiki

### Community:
- **Discord Server**: [Join our community](https://discord.gg/easyscraper)
- **Reddit**: r/EasyScraper
- **Stack Overflow**: Tag questions with `easyscraper`

### Commercial Support:
- Priority email support
- Custom feature development
- Training and consultation
- Enterprise deployment assistance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No warranty provided
- ❌ No liability accepted

## 🙏 Acknowledgments

### Libraries & Tools:
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)**: HTML/XML parsing
- **[Requests](https://docs.python-requests.org/)**: HTTP library
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation and analysis
- **[Selenium](https://selenium-python.readthedocs.io/)**: Browser automation
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: GUI framework

### Community:
- Contributors and beta testers
- Feature suggestions and feedback
- Bug reports and issue discussions
- Documentation improvements

## 🎯 Quick Examples

### Example 1: Scrape News Headlines
```
URL: https://news.ycombinator.com
Target: Custom CSS
Selector: .storylink
```

### Example 2: Extract Product Information
```
URL: https://books.toscrape.com
Target: Custom CSS
Selector: .product_pod h3 a, .price_color
```

### Example 3: Social Media Posts
```
URL: https://reddit.com/r/programming
Target: Custom CSS
Selector: .title a, .score
```

### Example 4: Job Listings
```
URL: https://stackoverflow.com/jobs
Target: Custom CSS
Selector: .job-link, .salary, .location
```

---

# 🇮🇩 Bahasa Indonesia

## ✨ Fitur Utama

### 🎯 Simple Scraper
- **Scraping Satu Klik**: Cukup masukkan URL dan pilih jenis data
- **Berbagai Jenis Data**: Teks, link, gambar, tabel, dan CSS selector khusus
- **Hasil Real-time**: Lihat hasil scraping secara langsung
- **Contoh URL**: Template URL bawaan untuk testing
- **Tracking Progress**: Progress bar visual dan update status

### ⚙️ Advanced Scraper
- **Batch Processing**: Scrape banyak website sekaligus
- **Custom Headers**: Konfigurasi User-Agent dan header lainnya
- **Request Delay**: Kontrol kecepatan scraping untuk menghindari rate limiting
- **Load dari File**: Import daftar URL dari file teks
- **Support Multiple URL**: Proses ratusan URL dalam satu sesi

### 📊 Manajemen Data
- **Data Viewer Interaktif**: Tabel yang bisa diurutkan untuk melihat hasil
- **Multiple Format Export**: CSV, Excel, JSON
- **Ringkasan Data**: Statistik dan overview data yang di-scrape
- **Search & Filter**: Cari data spesifik dalam hasil
- **Validasi Data**: Pembersihan dan formatting data otomatis

### 🔧 Fitur User-Friendly
- **Auto-Installer**: Script otomatis untuk instalasi Python dan dependencies
- **Interface GUI**: Tidak perlu command line
- **Help Bawaan**: Tutorial dan tips yang komprehensif
- **Error Handling**: Pesan error yang jelas dan membantu
- **Cross-Platform**: Berjalan di Windows, Linux, dan macOS

## 🚀 Memulai Cepat

### Untuk Pemula (Tidak Perlu Pengalaman Python/Programming)

#### Windows:
1. Download semua file ke satu folder
2. **Opsi A**: Double-click `setup_simple.bat` (untuk Windows lama)
3. **Opsi B**: Double-click `setup.bat` (untuk Windows baru)
4. Ikuti instruksi installer
5. Double-click shortcut "EasyScraper" di Desktop

#### Linux/Mac:
1. Download semua file ke satu folder
2. Buka terminal di folder tersebut
3. Jalankan: `chmod +x setup.sh && ./setup.sh`
4. Ikuti instruksi installer
5. Jalankan: `./run_easyscraper.sh`

### Untuk Developer

```bash
# Clone atau download files
git clone <repository-url>
cd easyscraper

# Install dependencies
pip install -r requirements.txt

# Jalankan aplikasi
python easyscraper.py
```

## 📋 Kebutuhan Sistem

### Kebutuhan Minimum
- **OS**: Windows 7+, Linux (Ubuntu 16.04+), macOS 10.12+
- **Python**: 3.6 atau lebih baru
- **RAM**: 512MB minimum, 1GB direkomendasikan
- **Storage**: 100MB ruang kosong
- **Internet**: Diperlukan untuk scraping dan setup awal

### Dependencies Python
```txt
requests>=2.25.0          # HTTP requests
beautifulsoup4>=4.9.0     # HTML parsing
selenium>=3.141.0         # Browser automation
pandas>=1.3.0             # Data manipulation
lxml>=4.6.0               # XML/HTML parser
openpyxl>=3.0.0           # Excel file support
pillow>=8.0.0             # Image processing
```

## 🎮 Cara Penggunaan

### 1. Simple Scraping

#### Langkah 1: Masukkan URL
- Ketik URL website target
- Atau pilih dari contoh URL yang disediakan
- Validasi URL otomatis

#### Langkah 2: Pilih Jenis Data
- 📝 **Semua Teks**: Ekstrak semua konten teks dari halaman
- 🔗 **Semua Link**: Ekstrak semua hyperlink dengan URLs
- 🖼️ **Semua Gambar**: Ekstrak semua URL gambar dan alt text
- 📊 **Tabel**: Ekstrak data dari tabel HTML
- 📋 **Custom CSS**: Gunakan CSS selector khusus untuk data spesifik

#### Langkah 3: Mulai Scraping
- Klik tombol "🚀 Mulai Scraping"
- Monitor progress real-time
- Lihat hasil di tab "Data Viewer"

### 2. Advanced Scraping

#### Konfigurasi
- **User-Agent**: Set custom user agent untuk menghindari blocking
- **Request Delay**: Set delay antar request (direkomendasikan: 1-3 detik)
- **Headers**: Konfigurasi HTTP headers tambahan

#### Multiple URLs
- Masukkan multiple URLs (satu per baris)
- Load URLs dari file teks
- Support untuk bulk processing

#### Batch Processing
- Klik "🚀 Scrape Multiple URLs"
- Monitor progress untuk setiap URL
- Error handling otomatis untuk request yang gagal

### 3. Export Data

#### Format Export
- **CSV**: Untuk analisis data di Excel/Google Sheets
- **Excel**: Format .xlsx dengan formatting yang proper
- **JSON**: Untuk developer dan integrasi API

#### Proses Export
- Pilih format yang diinginkan
- Pilih lokasi penyimpanan
- File otomatis tersimpan dengan timestamp

## 📖 Panduan CSS Selector

| Target | CSS Selector | Deskripsi |
|--------|-------------|-----------|
| Semua heading | `h1, h2, h3, h4, h5, h6` | Ekstrak semua elemen heading |
| Class spesifik | `.product-name` | Elemen dengan class "product-name" |
| ID spesifik | `#main-content` | Elemen dengan ID "main-content" |
| Attribute contains | `a[href*="product"]` | Link yang mengandung "product" di href |
| Nested elements | `.container .item .price` | Price dalam item dalam container |
| Multiple classes | `.product.featured` | Elemen dengan kedua class |
| Child pertama | `.list > li:first-child` | Item list pertama |
| Text contains | `span:contains("Sale")` | Span yang mengandung teks "Sale" |

### CSS Selectors Advanced
```css
/* Semua external links */
a[href^="http"]:not([href*="yourdomain.com"])

/* Gambar dengan ekstensi spesifik */
img[src$=".jpg"], img[src$=".png"]

/* Form inputs */
input[type="text"], input[type="email"]

/* Tabel dengan konten spesifik */
table:has(th:contains("Harga"))
```

## ⚠️ Etika & Panduan Legal

### ✅ Best Practices:
- **Cek robots.txt** sebelum scraping website apapun
- **Gunakan delay yang wajar** antar request (minimum 1 detik)
- **Hormati rate limits** dan terms of service
- **Scrape hanya data publik** yang bisa diakses bebas
- **Test dengan data kecil** sebelum scraping besar-besaran
- **Monitor response server** dan sesuaikan accordingly

### ❌ Hindari Ini:
- **Jangan spam request** ke server
- **Jangan scrape data pribadi/sensitif** tanpa izin
- **Jangan abaikan rate limiting** atau mekanisme blocking
- **Jangan scrape konten berhak cipta** untuk kepentingan komersial
- **Jangan overload server** dengan request berlebihan
- **Jangan abaikan terms of service website**

### Pertimbangan Legal:
- Legalitas web scraping bervariasi per jurisdiksi
- Selalu hormati terms of service website
- Pertimbangkan untuk menghubungi pemilik website untuk izin
- Sadar akan undang-undang perlindungan data (GDPR, dll.)

## 🔧 Troubleshooting

### Masalah Umum & Solusi

#### "Python tidak ditemukan"
**Solusi:**
- **Windows**: Jalankan `setup_simple.bat` lagi
- **Linux**: Install Python3: `sudo apt install python3 python3-pip`
- **Mac**: Install via Homebrew: `brew install python`
- **Semua**: Download dari [python.org](https://python.org/downloads)

#### "Module tidak ditemukan"
**Solusi:**
```bash
# Reinstall semua dependencies
pip install --upgrade -r requirements.txt

# Install package spesifik
pip install requests beautifulsoup4 pandas
```

#### "Website memblokir request"
**Solusi:**
- Tambah delay antar request (5-10 detik)
- Ganti User-Agent string
- Gunakan IP address atau proxy berbeda
- Cek apakah website mengizinkan scraping di robots.txt

#### "Tidak ada data yang diekstrak"
**Solusi:**
- Cek apakah website memuat konten JavaScript
- Verifikasi CSS selector menggunakan browser developer tools
- Pastikan struktur website tidak berubah
- Coba metode ekstraksi data yang berbeda

#### "Permission denied errors"
**Solusi:**
- Jalankan command prompt sebagai Administrator (Windows)
- Gunakan `sudo` untuk perintah instalasi (Linux/Mac)
- Cek permission dan ownership file

### Troubleshooting Advanced

#### Masalah Memory
- Kurangi batch size untuk multiple URLs
- Clear data secara regular selama sesi scraping panjang
- Tambah virtual memory/swap space

#### Masalah Network
- Cek stabilitas koneksi internet
- Konfigurasi proxy settings jika di balik corporate firewall
- Gunakan VPN jika ada geographical restrictions

## 🆕 Riwayat Versi & Update

### v1.0.0 (Current) - Stable Release
- ✅ Interface GUI lengkap dengan Tkinter
- ✅ Mode scraping Simple & Advanced
- ✅ Multiple format export (CSV, Excel, JSON)
- ✅ Script auto-installer untuk semua platform
- ✅ Kompatibilitas cross-platform
- ✅ Help bawaan dan contoh URLs
- ✅ Error handling dan progress tracking
- ✅ Validasi dan pembersihan data

### Fitur yang Direncanakan (v1.1.0):
- 🔄 Scheduled scraping dengan cron jobs
- 🌐 Support proxy dan rotasi
- 📱 Opsi interface berbasis web
- 🤖 Ekstraksi konten bertenaga AI
- 📈 Chart visualisasi data
- 🔍 Advanced filtering dan search
- 📧 Notifikasi email untuk job selesai
- 🗃️ Opsi penyimpanan database

### Roadmap Masa Depan:
- Versi browser extension
- Cloud-based scraping service
- Machine learning untuk content recognition
- API untuk integrasi third-party

## 📁 Struktur Project

```
easyscraper/
├── easyscraper.py          # Aplikasi utama
├── setup.bat               # Windows installer (baru)
├── setup_simple.bat        # Windows installer (kompatibel)
├── setup.sh                # Linux/Mac installer
├── requirements.txt        # Python dependencies
├── README.md               # File ini
├── INSTALL_MANUAL.txt      # Panduan instalasi manual
├── LICENSE                 # MIT license
└── examples/               # File contoh dan tutorial
    ├── sample_urls.txt     # Sample URLs untuk testing
    ├── css_selectors.md    # Contoh CSS selector
    └── tutorials/          # Tutorial step-by-step
```

## 🤝 Berkontribusi

Kami menyambut kontribusi! Begini cara Anda bisa membantu:

### Cara Berkontribusi:
1. **Bug Reports**: Laporkan masalah dengan deskripsi detail
2. **Feature Requests**: Sarankan fitur baru atau perbaikan
3. **Kontribusi Kode**: Submit pull request dengan enhancement
4. **Dokumentasi**: Perbaiki dokumentasi dan tutorial
5. **Testing**: Test di platform dan konfigurasi berbeda
6. **Terjemahan**: Tambah dukungan untuk lebih banyak bahasa

### Setup Development:
```bash
# Fork dan clone repository
git clone https://github.com/yourusername/easyscraper.git
cd easyscraper

# Buat virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Jalankan tests
python -m pytest tests/

# Mulai development
python easyscraper.py
```

### Guidelines Kontribusi:
- Ikuti guidelines style PEP 8
- Tambah tests untuk fitur baru
- Update dokumentasi untuk perubahan
- Gunakan commit message yang bermakna
- Buat feature branch untuk development baru

## 📞 Support & Komunitas

### Mendapatkan Bantuan:
- **GitHub Issues**: [Buat issue](https://github.com/yourusername/easyscraper/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/easyscraper/discussions)
- **Email Support**: easyscraper.support@gmail.com
- **Dokumentasi**: Help bawaan dan wiki online

### Komunitas:
- **Discord Server**: [Bergabung dengan komunitas kami](https://discord.gg/easyscraper)
- **Reddit**: r/EasyScraper
- **Stack Overflow**: Tag pertanyaan dengan `easyscraper`

### Commercial Support:
- Priority email support
- Custom feature development
- Training dan konsultasi
- Enterprise deployment assistance

## 📄 Lisensi

Project ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

### Arti dari ini:
- ✅ Penggunaan komersial diizinkan
- ✅ Modifikasi diizinkan
- ✅ Distribusi diizinkan
- ✅ Penggunaan pribadi diizinkan
- ❌ Tidak ada warranty yang diberikan
- ❌ Tidak ada liability yang diterima

## 🙏 Acknowledgments

### Libraries & Tools:
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)**: HTML/XML parsing
- **[Requests](https://docs.python-requests.org/)**: HTTP library
- **[Pandas](https://pandas.pydata.org/)**: Data manipulation dan analysis
- **[Selenium](https://selenium-python.readthedocs.io/)**: Browser automation
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: GUI framework

### Komunitas:
- Contributors dan beta testers
- Saran fitur dan feedback
- Bug reports dan diskusi issue
- Perbaikan dokumentasi

## 🎯 Contoh Cepat

### Contoh 1: Scrape News Headlines
```
URL: https://news.detik.com
Target: Custom CSS
Selector: .media__title a
```

### Contoh 2: Ekstrak Informasi Produk
```
URL: https://tokopedia.com/search?st=product&q=laptop
Target: Custom CSS
Selector: .prd_link-product-name, .prd_link-product-price
```

### Contoh 3: Social Media Posts
```
URL: https://reddit.com/r/indonesia
Target: Custom CSS
Selector: .title a, .score
```

### Contoh 4: Job Listings
```
URL: https://www.jobstreet.co.id/id/job-search/
Target: Custom CSS
Selector: .job-title, .company-name, .salary
```

---

**Disclaimer**: EasyScraper adalah tool untuk educational dan research purposes. Pengguna bertanggung jawab untuk mematuhi terms of service website yang di-scrape dan hukum yang berlaku.

**Happy Scraping! 🕷️✨**
