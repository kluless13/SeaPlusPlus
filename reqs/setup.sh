#!/bin/bash

echo "🌊 Welcome to Sea++ setup! 🌊"

# Check for required tools
check_command() {
    if ! command -v $1 &> /dev/null; then
        echo "❌ $1 is not installed."
        case $1 in
            "python3")
                echo "Please install Python 3.8 or later from https://www.python.org/"
                ;;
            "pip3")
                echo "Please install pip3 using: python3 -m ensurepip --upgrade"
                ;;
            "pandoc")
                if [[ "$OSTYPE" == "linux-gnu"* ]]; then
                    echo "Install using: sudo apt-get install pandoc"
                elif [[ "$OSTYPE" == "darwin"* ]]; then
                    echo "Install using: brew install pandoc"
                else
                    echo "Install from: https://pandoc.org/installing.html"
                fi
                ;;
        esac
        exit 1
    fi
}

# Check for required commands
echo "🔍 Checking required tools..."
check_command "python3"
check_command "pip3"
check_command "pandoc"

# Create Python virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create project structure
echo "📁 Creating project structure..."
python3 folders.py

# Function to convert README.md to PDF
convert_md_to_pdf() {
    local dir="$1"
    if [ -f "$dir/README.md" ]; then
        echo "📄 Converting README in $dir to PDF..."
        pandoc "$dir/README.md" -o "$dir/README.pdf" --pdf-engine=xelatex
    fi
}

# Convert READMEs to PDF
echo "📚 Converting documentation..."
find . -type f -name "README.md" -exec dirname {} \; | while read dir; do
    convert_md_to_pdf "$dir"
done

# Set up pre-commit hooks
echo "🔧 Setting up git hooks..."
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# Run tests
python3 -m pytest

# Run linting
python3 -m flake8 marine_science
python3 -m black --check marine_science
python3 -m isort --check-only marine_science
EOF

chmod +x .git/hooks/pre-commit

echo "✨ Setup complete! Dive into Sea++! 🐠"
echo "
To get started:
1. Activate the virtual environment: source venv/bin/activate
2. Run tests: pytest
3. Check out the documentation in docs/
"