
# RAG-Based PDF Question Answering System

## Project Overview

This project demonstrates an end-to-end Retrieval-Augmented Generation (RAG) pipeline using LangChain and Google Gemini.

The application allows users to upload PDF documents and ask questions based on their content. It retrieves relevant information from the document using semantic search and generates context-based answers using a Large Language Model (LLM).

## Technologies Used

- Python
- Google Colab
- LangChain
- Google Gemini API
- Gemini Embeddings
- FAISS Vector Database
- PyPDF

## Project Workflow

1. **PDF Upload:** Upload a PDF document.
2. **Document Loading:** Extract text from the uploaded PDF.
3. **Text Splitting:** Divide the extracted text into smaller chunks using RecursiveCharacterTextSplitter.
4. **Text Embeddings:** Convert text chunks into vector representations using Gemini Embeddings.
5. **Vector Storage:** Store the embeddings in a FAISS vector database.
6. **Semantic Search:** Retrieve the four most relevant document chunks based on the user's question.
7. **Prompt Template:** Combine the retrieved context with the user's question using LangChain PromptTemplate.
8. **Answer Generation:** Generate context-based answers using Google Gemini.
9. **Source Tracking:** Display the source page numbers of retrieved document content.

## RAG Architecture

```text
       PDF Document
             |
             v
      Document Loading
             |
             v
       Text Extraction
             |
             v
        Text Chunking
             |
             v
     Gemini Embeddings
             |
             v
     FAISS Vector Store
             |
             v
       User Question
             |
             v
      Semantic Search
             |
             v
   Retrieve Relevant Chunks
             |
             v
      Prompt Template
             |
             v
       Google Gemini
             |
             v
      Generated Answer
             |
             v
     Source Page Numbers
```

## Key Features

- Upload PDF documents using Google Colab.
- Extract text from PDF documents.
- Split large documents into smaller text chunks.
- Generate embeddings using Gemini.
- Store document embeddings using FAISS.
- Retrieve relevant information through semantic search.
- Generate answers using Google Gemini.
- Display source page references.
- Ask multiple questions interactively.

## How to Run the Project

1. Open the `Ragpractice.ipynb` notebook in Google Colab.
2. Install the required Python libraries.
3. Configure your Gemini API key using Google Colab Secrets.
4. Run the notebook cells in sequence.
5. Upload your PDF document.
6. Wait for document processing and vector database creation.
7. Enter your questions.
8. View the generated answers and source page numbers.
9. Type `exit` to stop the question-answering session.

## Learning Outcomes

Through this project, I gained practical experience in:

- Understanding Retrieval-Augmented Generation (RAG).
- Working with LangChain components.
- PDF document loading and processing.
- Text chunking and embeddings.
- Vector database creation using FAISS.
- Semantic similarity search.
- Prompt engineering.
- Integrating Google Gemini API.
- Building an end-to-end RAG pipeline.

## Future Improvements

- Develop an interactive Streamlit web application.
- Support multiple PDF document uploads.
- Add conversation history for follow-up questions.
- Display retrieved source text with page references.
- Improve document retrieval accuracy.

---

**Project Category:** Artificial Intelligence | Generative AI | RAG

**Developed Using:** Python, LangChain, Google Gemini, FAISS and Google Colab.
