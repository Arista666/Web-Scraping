#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "========================================"
echo "   🕷️  EASYSCRAPER AUTO SETUP  🕷️"
echo "========================================"
echo -e "${NC}"

echo "Installer ini akan:"
echo "✓ Mengecek Python installation"
echo "✓ Menginstall Python jika belum ada (Linux/Mac)"
echo "✓ Menginstall dependencies yang diperlukan"
echo "✓ Membuat launcher script"
echo ""
read -p "Tekan Enter untuk melanjutkan..."

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check Python installation
echo -e "${YELLOW}[1/4] Mengecek Python installation...${NC}"
if command_exists python3; then
    echo -e "${GREEN}✅ Python3 sudah terinstall!${NC}"
    PYTHON_CMD="python3"
    python3 --version
elif command_exists python; then
    PYTHON_VERSION=$(python -c "import sys; print(sys.version_info.major)")
    if [ "$PYTHON_VERSION" = "3" ]; then
        echo -e "${GREEN}✅ Python3 sudah terinstall!${NC}"
        PYTHON_CMD="python"
        python --version
    else
        echo -e "${RED}❌ Python2 detected, need Python3!${NC}"
        NEED_PYTHON=true
    fi
else
    echo -e "${RED}❌ Python belum terinstall!${NC}"
    NEED_PYTHON=true
fi

# Install Python if needed
if [ "$NEED_PYTHON" = true ]; then
    echo ""
    echo "Python3 diperlukan untuk menjalankan EasyScraper."
    echo ""
    
    # Detect OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Detected: Linux"
        echo "Installing Python3..."
        
        if command_exists apt; then
            sudo apt update
            sudo apt install -y python3 python3-pip python3-tk
        elif command_exists yum; then
            sudo yum install -y python3 python3-pip python3-tkinter
        elif command_exists dnf; then
            sudo dnf install -y python3 python3-pip python3-tkinter
        elif command_exists pacman; then
            sudo pacman -S python python-pip tk
        else
            echo -e "${RED}Package manager tidak dikenali. Silakan install Python3 manual.${NC}"
            exit 1
        fi
        
        PYTHON_CMD="python3"
        
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Detected: macOS"
        
        if command_exists brew; then
            echo "Installing Python3 via Homebrew..."
            brew install python python-tk
            PYTHON_CMD="python3"
        else
            echo -e "${YELLOW}Homebrew tidak ditemukan.${NC}"
            echo "Silakan install Homebrew terlebih dahulu:"
            echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
            echo ""
            echo "Atau download Python dari: https://www.python.org/downloads/"
            exit 1
        fi
    else
        echo -e "${RED}OS tidak didukung untuk auto-install.${NC}"
        echo "Silakan install Python3 manual dari: https://www.python.org/downloads/"
        exit 1
    fi
fi

# Check pip
echo -e "${YELLOW}[2/4] Mengecek pip...${NC}"
if command_exists pip3; then
    echo -e "${GREEN}✅ pip3 sudah tersedia!${NC}"
    PIP_CMD="pip3"
elif command_exists pip; then
    echo -e "${GREEN}✅ pip sudah tersedia!${NC}"
    PIP_CMD="pip"
else
    echo -e "${RED}❌ pip tidak ditemukan!${NC}"
    echo "Installing pip..."
    $PYTHON_CMD -m ensurepip --upgrade
    PIP_CMD="$PYTHON_CMD -m pip"
fi

# Install dependencies
echo -e "${YELLOW}[3/4] Installing dependencies...${NC}"
echo "📦 Installing required packages..."

$PIP_CMD install --user requests beautifulsoup4 selenium pandas lxml openpyxl pillow

echo ""
echo -e "${YELLOW}[4/4] Membuat launcher script...${NC}"

# Create run script
cat > run_easyscraper.sh << 'EOF'
#!/bin/bash

# Get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$DIR"

# Run EasyScraper
if command -v python3 >/dev/null 2>&1; then
    python3 easyscraper.py
elif command -v python >/dev/null 2>&1; then
    python easyscraper.py
else
    echo "Python tidak ditemukan!"
    exit 1
fi
EOF

chmod +x run_easyscraper.sh

# Create desktop file for Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    DESKTOP_FILE="$HOME/Desktop/EasyScraper.desktop"
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=EasyScraper
Comment=Web Scraping Made Easy
Exec=$PWD/run_easyscraper.sh
Icon=applications-internet
Terminal=false
Categories=Network;WebDevelopment;
EOF
    chmod +x "$DESKTOP_FILE"
    echo -e "${GREEN}✅ Desktop shortcut created!${NC}"
fi

echo ""
echo -e "${GREEN}"
echo "========================================"
echo "        ✅ SETUP COMPLETED! ✅"
echo "========================================"
echo -e "${NC}"
echo ""
echo "🚀 Cara menjalankan EasyScraper:"
echo "   1. ./run_easyscraper.sh"
echo "   2. Atau: $PYTHON_CMD easyscraper.py"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "   3. Double-click EasyScraper di Desktop"
fi
echo ""
echo "📁 File yang dibuat:"
echo "   ✓ run_easyscraper.sh (launcher script)"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "   ✓ EasyScraper.desktop (desktop shortcut)"
fi
echo ""
echo "🎉 Selamat! EasyScraper siap digunakan!"
echo ""

# Test run
read -p "🧪 Mau test run sekarang? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "🚀 Launching EasyScraper..."
    $PYTHON_CMD easyscraper.py
fi