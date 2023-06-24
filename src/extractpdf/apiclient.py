import os.path
import logging
from zipfile import ZipFile
from . utils import get_time_stamp

from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation


logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

class ApiClient:
    # get the base path
    __base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
    __execution_context: ExecutionContext = ExecutionContext()
    __extract_pdf_operation: ExtractPDFOperation = ExtractPDFOperation.create_new()

    def __init__(self, api_key):
        try:
            # Create a Credentials instance.
            credentials = Credentials.service_account_credentials_builder() \
                .from_file(api_key) \
                .build()

             # Create an ExecutionContext instance using credentials
            self.__execution_context = ExecutionContext.create(credentials)

        except Exception:
            logging.exception("Exception encountered while creating ApiClient")


    def extract_info_from_pdf(self, file_name):
        try:
            # Create a FileRef instance using path/to/source_file and set operation input
            source = FileRef.create_from_local_file(file_name)
            self.__extract_pdf_operation.set_input(source)

            # Create ExtractPDFOptions and set them into operation
            extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
                .with_element_to_extract(ExtractElementType.TEXT) \
                .build()
            self.__extract_pdf_operation.set_options(extract_pdf_options)

            # Execute the operation.
            result: FileRef = self.__extract_pdf_operation.execute(self.__execution_context)

            # Save the results to the specified location.
            ts = str(get_time_stamp())
            file_name = f'{os.path.split(file_name)[1].split(".")[0]}({ts})'
            result.save_as(self.__base_path + f"/output/{file_name}.zip")

            with ZipFile(f'{self.__base_path}/output/{file_name}.zip', 'r') as zip_file:
                return zip_file.read('structuredData.json')
            
        except (ServiceApiException, ServiceUsageException, SdkException):
            logging.exception("Exception encountered while executing operation")
