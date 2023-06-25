# PDF Invoice Data Extractor

This program is designed to extract information from PDF invoices using the Adobe PDF Services Extract API. It provides a convenient way to automate the extraction process, allowing users to process a large number of invoices quickly and efficiently.

## Getting Started

To use this program, you'll need an Adobe PDF Services account. If you don't have one already, you can sign up for a free trial on the [Adobe PDF Services website](https://developer.adobe.com/document-services/apis/pdf-extract/).

Once you have your Adobe PDF Services credentials, you can clone this repository and follow the instructions below to set up the program.
<br></br>
# Installation

* Open Command Prompt.

* Clone the repository.

```Shell
git clone https://github.com/Bhanuteja917/ExtractInvoice.git
```
1. Change directory to ExtractInvoice directory.

```Shell
cd ExtractInvoice
```

2. Create a virtual environment. 

```Shell
virtualenv venv
```

3. Activate the virtual environment.

```Shell
# Windows
venv\Scripts\activate

# Linux
source venv/bin/activate
```

4. Install the required dependencies.

```Shell
pip install -r requirements.txt
```
<br>

# For Adobe Hackathon

1. Use the following command to run the program.

```Shell
python3 src/cli.py -d ./InvoicesData/TestDataSet

# or

python src/cli.py -d ./InvoicesData/TestDataSet
```

### The data from the TestDataSet PDFs will be extracted to a file placed in the directory ExtractedData
<br>

### Note:
If the 1000 free transactions are completed. Please sign up for a free trial on the [Adobe PDF Services website](https://developer.adobe.com/document-services/apis/pdf-extract/).<br>
Place the `pdfservices-api-credentials.json` and `private.key` files in root directory of the project or specify the path to the `pdfservices-api-credentials.json` as a command line argument.

```Shell
python3 src/cli.py -d ./InvoicesData/TestDataSet -k /path/to/api-key

# or

python src/cli.py -d ./InvoicesData/TestDataSet -k /path/to/api-key
```

<br>

# Usage

1. Run the program, specifying the input folder or file and output file path as command-line arguments.

```Shell
python3 src/cli.py -d /path/to/input/folder -o /path/to/output/file

# or

python3 src/cli.py -i /path/to/input/file -o /path/to/output/file
```

### Note
```Shell
# Use the following command to know about CLI
python3 src/cli.py --help
```






