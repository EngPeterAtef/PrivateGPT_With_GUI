# privateGPT

Ask questions about your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!

Built with [LangChain](https://github.com/hwchase17/langchain), [GPT4All](https://github.com/nomic-ai/gpt4all), [LlamaCpp](https://github.com/ggerganov/llama.cpp), [Chroma](https://www.trychroma.com/) and [SentenceTransformers](https://www.sbert.net/).

![image](https://github.com/EngPeterAtef/PrivateGPT_With_GUI/assets/75852529/dc3df8b1-05dc-4fca-a8a5-66dbf2954229)
![image](https://github.com/EngPeterAtef/PrivateGPT_With_GUI/assets/75852529/a431e7a0-ba3c-4aee-87fc-67caa3968bac)


# Environment Setup

In order to set your environment up to run the code here, first install all requirements:

```shell
pip3 install -r requirements.txt
```

Then, download the LLM model and place it in a directory of your choice:

- LLM: default to [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). If you prefer a different GPT4All-J compatible model, just download it and reference it in your `.env` file.

Copy the `example.env` template into `.env`

```shell
cp example.env .env
```

and edit the variables appropriately in the `.env` file.

```
MODEL_TYPE: supports LlamaCpp or GPT4All
PERSIST_DIRECTORY: is the folder you want your vectorstore in
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for the LLM model
MODEL_N_BATCH: Number of tokens in the prompt that are fed into the model at a time. Optimal value differs a lot depending on the model (8 works well for GPT4All, and 1024 is better for LlamaCpp)
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
```

Note: because of the way `langchain` loads the `SentenceTransformers` embeddings, the first time you run the script it will require internet connection to download the embeddings model itself.

## Test dataset

You can upload any file using the webstie. The uploaded file will get copied in source_documents folder.

## Instructions for ingesting your own dataset

Put any and all your files into the `source_documents` directory

The supported extensions are:

- `.csv`: CSV,
- `.docx`: Word Document,
- `.doc`: Word Document,
- `.enex`: EverNote,
- `.eml`: Email,
- `.epub`: EPub,
- `.html`: HTML File,
- `.md`: Markdown,
- `.msg`: Outlook Message,
- `.odt`: Open Document Text,
- `.pdf`: Portable Document Format (PDF),
- `.pptx` : PowerPoint Document,
- `.ppt` : PowerPoint Document,
- `.txt`: Text file (UTF-8),

Run the following command to open the website.

```shell
streamlit run privateGPT.py
```

## Upload The files you want to chat with

1. Click on Browse button
2. Choose your files"in the listed extenstions"
3. Click on Process Documents button
4. after ingesting your documents you are ready to ask your questions

## Ask questions to your documents, locally!

```plaintext
> Enter a query:
```

Hit enter. You'll need to wait 20-30 seconds (depending on your machine) while the LLM model consumes the prompt and prepares the answer. Once done, it will print the answer and the 4 sources it used as context from your documents; you can then ask another question without re-running the script, just wait for the prompt again.

Note: you could turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

# How does it work?

Selecting the right local models and the power of `LangChain` you can run the entire pipeline locally, without any data leaving your environment, and with reasonable performance.

- `ingest.py` uses `LangChain` tools to parse the document and create embeddings locally using `HuggingFaceEmbeddings` (`SentenceTransformers`). It then stores the result in a local vector database using `Chroma` vector store.
- `privateGPT.py` uses a local LLM based on `GPT4All-J` or `LlamaCpp` to understand questions and create answers. The context for the answers is extracted from the local vector store using a similarity search to locate the right piece of context from the docs.
- `GPT4All-J` wrapper was introduced in LangChain 0.0.162.

# System Requirements

## Python Version

To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

## C++ Compiler

If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

### For Windows 10/11

To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
   * Universal Windows Platform development
   * C++ CMake tools for Windows
3. Download the MinGW installer from the [MinGW website](https://sourceforge.net/projects/mingw/).
4. Run the installer and select the `gcc` component.

## Demo video For Small .txt File

https://github.com/EngPeterAtef/PrviateGPT_With_GUI/assets/75852529/a701f727-b236-47d3-a770-c78fe9e9bfe3

## Demo video For Large .txt File

https://github.com/EngPeterAtef/PrivateGPT_With_GUI/assets/75852529/ecb55179-b313-4778-973d-7dfae4d72cb6

## Demo video For .csv File

https://github.com/EngPeterAtef/PrivateGPT_With_GUI/assets/75852529/4f0afb25-6bb9-4a6e-8297-b77eec9b4c10

## Demo video For .pdf File

https://github.com/EngPeterAtef/PrivateGPT_With_GUI/assets/75852529/d4789cd7-0978-42a7-880e-42d208df2c34

###### Notion document [Link](https://mmsrashid.notion.site/Data-Science-Technical-Test-PrviateGPT-Clone-7146933e552f41549c819c58a85249d8)
