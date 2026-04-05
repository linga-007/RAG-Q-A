# PDF Q&A (RAG with Pinecone + Ollama)

This project is a simple Retrieval-Augmented Generation (RAG) pipeline for asking questions about a PDF file.

It works by:
- Loading a PDF
- Splitting it into chunks
- Converting chunks to embeddings
- Storing embeddings in Pinecone
- Retrieving relevant chunks for a user query
- Sending query + context to a local LLM (Ollama)

## Project Structure

- `app.py`: Entry point. Builds index from PDF and starts chat loop.
- `config.py`: All configuration values (Pinecone, model names, chunk settings).
- `rag/loader.py`: Loads PDF documents.
- `rag/chunker.py`: Splits documents into chunks.
- `rag/embedder.py`: Creates embeddings using Sentence Transformers.
- `rag/vectordb.py`: Handles Pinecone index creation, insert, and search.
- `rag/retriever.py`: Embeds user query and retrieves top-k matching chunks.
- `utils/helper.py`: Formats retrieved chunks into context text.
- `prompts/prompt_template.py`: Builds prompt with selected response mode.
- `llm/llm_client.py`: Sends prompt to Ollama and returns answer.
- `data/sample.pdf`: Sample input document.

## How It Works

1. `app.py` calls `setup_pipeline()`.
2. PDF is loaded from `data/sample.pdf`.
3. Text is chunked using `CHUNK_SIZE` and `CHUNK_OVERLAP`.
4. Chunk text is embedded using `EMBEDDING_MODEL`.
5. Embeddings + text are upserted to Pinecone index (`INDEX_NAME`).
6. In chat mode:
   - User asks question
   - Query is embedded
   - Top `TOP_K` relevant chunks are retrieved from Pinecone
   - Context + question + mode instruction are sent to Ollama
   - Final answer is displayed

## Requirements

- Python 3.10+
- Pinecone account and API key
- Ollama installed locally
- Ollama model pulled (default: `gemma3:1b`)

Python packages:

```bash
pip install sentence-transformers langchain pypdf pinecone-client requests
```

## Configuration

Edit `config.py`:

- `PINECONE_API_KEY`: Your Pinecone API key
- `PINECONE_ENV`: Pinecone region (example: `us-east-1`)
- `INDEX_NAME`: Pinecone index name
- `EMBEDDING_MODEL`: SentenceTransformer model id
- `CHUNK_SIZE`, `CHUNK_OVERLAP`: Chunking controls
- `TOP_K`: Number of retrieved chunks
- `OLLAMA_URL`: Usually `http://localhost:11434/api/generate`
- `MODEL_NAME`: Ollama model name (example: `gemma3:1b`)

## Run

From the `PDF Q&A` folder:

```bash
python app.py
```

Then in terminal:
- Ask a question
- Choose mode: `beginner`, `interview`, or `summary`
- Type `exit` to stop

## Example Session

```text
Ask a question (or type 'exit'): What is this PDF about?
Mode (beginner/interview/summary): beginner
Answer:
...model response...
```

## Troubleshooting

- Error: `File path data/sample.pdf is not a valid file or url`
  - `app.py` now uses an absolute path based on script location. Keep PDF at `data/sample.pdf`.

- Pinecone connection/index issues
  - Verify `PINECONE_API_KEY`, `PINECONE_ENV`, and internet access.

- Ollama not responding
  - Start Ollama server and ensure model is available:
    - `ollama run gemma3:1b`

- Empty/weak answers
  - Increase `TOP_K`, adjust chunk size, or use a stronger embedding/LLM model.

## Security Note

Your current `config.py` stores secrets in plain text. For production or shared code:
- Move `PINECONE_API_KEY` to environment variables
- Keep `config.py` free of sensitive credentials
- Add secret files to `.gitignore`
