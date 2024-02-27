# Python-payment-receipts-creator

## Overview
Python Payment Receipts Creator is a Python tool designed to generate payment receipts in PDF format. Leveraging the pdfkit library, this project offers a straightforward solution for businesses or individuals needing to create professional-looking receipts for transactions.

## Features
- **PDF Generation**: Utilize pdfkit to create high-quality PDF receipts for your transactions.
- **Customization Options**: Tailor receipts with customizable fields such as recipient name, payment amount, date, and more.
- **Ease of Use**: Simple and intuitive interface makes it easy to generate receipts quickly.
- **Save and Print**: Save generated receipts locally or print them directly from the application.

## Installation
Before using the Python Payment Receipts Creator, ensure you have pdfkit installed. You can install it via pip:

```bash
pip install pdfkit
```
Install wkhtmltopdf :

- Debian/Ubuntu :
```bash
sudo apt-get install wkhtmltopdf
```

- MacOs :
```bash
brew install homebrew/cask/wkhtmltopdf
```

Then, clone the Python Payment Receipts Creator repository:
```bash
git clone https://github.com/yourusername/python-payment-receipts-creator.git
```

## Usage
Navigate to the project directory and run the script:
```bash
cd python-payment-receipts-creator
python payment_receipts_creator.py
```
Follow the on-screen instructions to input payment details and generate a receipt.

## Documentation
For more details on using pdfkit, refer to the [pdfkit documentation](https://pypi.org/project/pdfkit/).

## Contribution
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request on [GitHub](https://github.com/mccartheney/Python-payment-receipts-creator).

## License 
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
