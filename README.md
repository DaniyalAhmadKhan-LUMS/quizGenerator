# PDF Quiz Application

The PDF Quiz Application is an innovative tool designed to transform PDF documents into interactive quizzes, enhancing the learning and assessment process. This application seamlessly integrates a `React-Frontend` for user interaction with a `Flask-Backend` for processing, creating a dynamic and engaging educational experience.

## Features

- **PDF Preprocessing:** Efficiently parses and segments PDF documents into manageable chunks for further processing.
- **Quiz Generation:** Automatically generates multiple-choice and open-ended questions from the PDF content, complete with correct answers and detailed explanations.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm/yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone [repository-url]

   
## Flask-Backend
`Flask-Backend` is further divided into two parts:
### PDF Preprocessing:
PDF preprocessing involves reading the PDF and dividing the whole PDF into smaller chunks that can be processed further: 
* `PyPDF2`, and `langchain.document_loader.PyPDFLoader` is used to read the PDF.
* `langchain.text_splitter.RecursiveCharacterTextSplitter` is then used to break the whole PDF into small chunks.

### Quiz Generation:
This comprises steps involving the generation of the Questions their choices/answers, and then grading them once the user has solved a question:
* Generate the summary of the text chunk to show the user before he moves on to the questions.
* Generate multiple-choice questions from the chunk along with choices and the correct choice.
* Generate open-ended questions along with the answers.
* Grade the answers of the user and tell them, why a particular choice is correct and why a particular choice is incorrect.
