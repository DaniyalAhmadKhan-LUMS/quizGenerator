## PDF Quiz
PDF Quiz Application is divided into two parts `React-Fronend` and `Flask-Backend`. 
`Flask-Backed` is further divided into two parts:
### PDF Preprocessing:
PDF Quiz generator app takes a PDF as input breaks the whole PDF into chunks and generates a quiz from each chunk. PDF Quiz uses `PyPDF2`, and `langchain.document_loader.PyPDFLoader` to read the PDF. After reading the PDF `langchain.text_splitter.RecursiveCharacterTextSplitter` is used to break the whole PDF into small chunks which are then processed further. 
