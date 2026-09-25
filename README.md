# PalmMind RAG API

A modular backend application built with **FastAPI** that implements document ingestion, semantic search, conversational Retrieval-Augmented Generation (RAG), Redis-based conversation memory, and LLM-powered interview booking.

The project was developed as a backend-focused implementation of the PalmMind technical assignment.

---

## Overview

PalmMind RAG API provides two primary capabilities:

1. **Document Ingestion**
   - Upload PDF and TXT documents
   - Extract document text
   - Apply selectable chunking strategies
   - Generate semantic embeddings
   - Store embeddings in Qdrant
   - Store document metadata in SQLite

2. **Conversational RAG & Interview Booking**
   - Ask questions about uploaded documents
   - Retrieve relevant document chunks using vector similarity
   - Generate answers using an LLM
   - Maintain multi-turn conversation history with Redis
   - Detect interview-booking requests
   - Extract booking information using an LLM
   - Validate and persist interview bookings in SQLite

---

## Features

### Document Ingestion

- PDF and TXT file support
- PDF text extraction using `pypdf`
- Two selectable chunking strategies:
  - Fixed-size chunking with overlap
  - Sentence-based chunking
- Sentence Transformer embeddings
- Qdrant vector storage
- SQLite document and chunk metadata

### Conversational RAG

- Custom RAG pipeline
- Semantic similarity search using Qdrant
- Context construction from retrieved document chunks
- Conversation history from Redis
- Multi-turn contextual questions
- LLM-generated answers
- No `RetrievalQAChain` or pre-built RAG chain

### Interview Booking

- Natural-language booking requests
- LLM-based extraction of:
  - Name
  - Email
  - Date
  - Time
- Multi-turn collection of missing information
- Email validation
- Date and time parsing
- Booking persistence in SQLite
- Temporary booking state stored in Redis
- Conversation-specific booking state

### API

- FastAPI REST API
- Automatic OpenAPI documentation
- Swagger UI
- Modular service-oriented structure
- Python type annotations throughout the application

---

## Architecture

```text
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │       REST API      │
                         └──────────┬──────────┘
                                    │
                 ┌──────────────────┴──────────────────┐
                 │                                     │
                 ▼                                     ▼
        ┌──────────────────┐                  ┌──────────────────┐
        │ Document Upload  │                  │   Chat Endpoint  │
        └────────┬─────────┘                  └────────┬─────────┘
                 │                                     │
                 ▼                                     ▼
        ┌──────────────────┐                  ┌──────────────────┐
        │ Text Extraction  │                  │ Intent Detection │
        └────────┬─────────┘                  └───────┬──────────┘
                 │                                    │
                 ▼                         ┌──────────┴──────────┐
        ┌──────────────────┐               │                     │
        │ Chunking         │               ▼                     ▼
        │ Fixed/Sentence   │        ┌──────────────┐     ┌──────────────┐
        └────────┬─────────┘        │ RAG Pipeline │     │    Booking   │
                 │                  └──────┬───────┘     └──────┬───────┘
                 ▼                         │                    │
        ┌──────────────────┐               ▼                    ▼
        │ Embeddings       │        ┌──────────────┐     ┌──────────────┐
        │ MiniLM           │        │    Qdrant    │     │    SQLite    │
        └────────┬─────────┘        │ Vector Store │     │   Bookings   │
                 │                  └──────────────┘     └──────────────┘
                 ▼
        ┌──────────────────┐
        │     Qdrant       │
        │  Vector Storage  │
        └──────────────────┘

                    Redis
                      │
                      ├── Conversation history
                      └── Temporary booking state
