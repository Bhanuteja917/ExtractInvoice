import os.path
import logging

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

try:
    # get base path.
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(base_path)
    # Create a Credentials instance .
    credentials = Credentials.service_account_credentials_builder() \
        .from_file(base_path + "/pdfservices-api-credentials.json") \
        .build()
    
    # Create an ExecutionContext instance using credentials
    execution_context = ExecutionContext.create(credentials)

    # Create ExtractPDFOperation instance
    extract_pdf_operation = ExtractPDFOperation.create_new()

    # Create a FileRef instance using path/to/source_file and set operation input
    source = FileRef.create_from_local_file(base_path + "/InvoicesData/TestDataSet/output1.pdf")
    extract_pdf_operation.set_input(source)

    # Create ExtractPDFOptions and set them into operation
    extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
        .with_element_to_extract(ExtractElementType.TEXT) \
        .build()
    extract_pdf_operation.set_options(extract_pdf_options)

    # # Execute the operation.
    # result: FileRef = extract_pdf_operation.execute(execution_context)

    # # Save the results to the specified location.
    # result.save_as("C:Users/bhanu/output/ExtractTextInfoFromPDF.zip")
except (ServiceApiException, ServiceUsageException, SdkException):
    logging.exception("Exception encountered while executing operation")