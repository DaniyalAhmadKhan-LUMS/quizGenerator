# PDF Quiz
PDF Quiz Application is divided into two parts `React-Fronend` and `Flask-Backend`. 
## Flask-Backend
`Flask-Backend` is further divided into two parts:
### PDF Preprocessing:
PDF preprocessing involves reading the PDF and dividing the whole PDF into smaller chunks that can be processed further: 
* `PyPDF2`, and `langchain.document_loader.PyPDFLoader` is used to read the PDF.
* `langchain.text_splitter.RecursiveCharacterTextSplitter` is then used to break the whole PDF into small chunks. 
