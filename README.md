# Academic Research Paper Information Retrieval System

Welcome to the **Academic Research Paper Information Retrieval System**. This system is designed to help researchers and students easily upload, process, and interact with academic PDFs. By using this tool, you can ask questions related to the content of the PDFs, and the system will retrieve relevant information for you using natural language processing (NLP) techniques powered by Google PaLm2.

![image](https://github.com/user-attachments/assets/ee5b764d-97ef-449c-980d-858dff3cb734)
Fig: Screenshot of the app at work

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Folder Structure](#folder-structure)

## Project Overview

The **Academic Research Paper Information Retrieval System** allows users to upload multiple PDF files and interact with the content through a conversational interface. This tool leverages modern NLP techniques, powered by Google Vertex AI, to extract and understand the content from academic papers.

### Features

- **Multi-PDF Upload**: Upload multiple academic papers at once.
- **Text Extraction**: Extracts text from uploaded PDFs.
- **Conversational Interface**: Ask questions about the content and receive relevant answers.
- **Google PaLm2 I**: Utilizes Google PaLm2 for advanced natural language processing.
- **Easy Integration**: Built with Streamlit, allowing easy deployment and usage.


## Installation

To get started, you need to clone this repository and install the necessary dependencies.

### Clone the repository

```bash
git clone https://github.com/your-username/research-paper-retrieval-system.git
cd research-paper-retrieval-system
```

### Install the requirements

```pip install -r requirements.txt```

### Add the GOOGLE_API_KEY in a .env file

```GOOGLE_API_KEY= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"```

### Run it in streamlit:
```streamlit run app.py```


## Folder Structure

```plaintext
.
├── research
│   └── trial.ipynb               # Jupyter notebook for experiments and trials
├── src
│   ├── __init__.py               # Initialization file for the src module
│   └── helper.py                 # Helper functions for text extraction and processing
├── .gitignore                    # Git ignore file
├── LICENSE                       # License file
├── README.md                     # Readme file for the project
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── setup.py                      # Setup file for the project
└── template.py                   # Template or example script (optional)
```

`src` Folder
- `__init__.py`: Initialization for the src module.
- `helper.py`: Contains functions for processing PDFs, extracting text, and managing the conversational interface.

`research` Folder
- `trial.ipynb`: Jupyter notebook used for testing and prototyping various parts of the system.



### Techstack Used:
- Python
- LangChain
- Streamlit
- PaLM2
- FAISS
