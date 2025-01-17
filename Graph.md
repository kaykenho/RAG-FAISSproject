# RAG Chatbot Knowledge Graph

This is the knowledge graph for a Retrieval-Augmented Generation (RAG) chatbot using vector databases, Hugging Face GPT-2, and a GUI.

```mermaid
graph TD
  %% User Interaction and GUI Layer
  A[User] -->|Interacts via| B[GUI]
  B[GUI] -->|Sends query to| C[Input Preprocessor]
  C[Input Preprocessor] -->|Cleans and formats input| D[Query Handler]

  %% Query Handling Layer
  D[Query Handler] -->|Retrieves context from| E[Contextual Database]
  D[Query Handler] -->|Searches vector embeddings from| F[Vector Database]
  E[Contextual Database] -->|Stores contextual information from| G[Knowledge Base]
  F[Vector Database] -->|Stores vectorized text| H[Document Embeddings]

  %% Vector Database Interaction
  H[Document Embeddings] -->|Mapped to| I[Text Data/Articles]
  F[FAISS] -->|Retrieves top-k most similar vectors| J[Relevant Document Embeddings]
  F[FAISS] -->|Performs similarity search using| K[Embedding Search Algorithm]

  %% GPT-2 Model Layer
  D[Query Handler] -->|Sends query to| L[Hugging Face GPT-2 Model]
  L[Hugging Face GPT-2 Model] -->|Generates text response using context| M[Response Generator]
  M[Response Generator] -->|Returns final response| N[Output Postprocessor]

  %% Post-Processing Layer
  N[Output Postprocessor] -->|Formats final response| B[GUI]

  %% Dataflow and Optimization Layers
  K[Embedding Search Algorithm] -->|Optimizes by filtering relevant docs| J
  J[Relevant Document Embeddings] -->|Feeds contextual info into| L
  L[Hugging Face GPT-2 Model] -->|Tuned with domain-specific knowledge| O[Fine-Tuning Dataset]
  O[Fine-Tuning Dataset] -->|Updates GPT-2 model weights| P[GPT-2 Fine-Tuning Process]
  P[GPT-2 Fine-Tuning Process] -->|Improves accuracy and relevance| L

  %% External Data Sources
  G[Knowledge Base] -->|Contains| I[Text Data/Articles]
  G[Knowledge Base] -->|Prepares knowledge for retrieval| H

  %% Optional Features
  D -->|Uses NLP techniques to enhance query| Q[Named Entity Recognition]
  D -->|Identifies keywords for better matching| R[Keyword Extraction]
  D -->|Manages user sessions| S[Session Management]

  %% GUI Feedback Loop
  B[GUI] -->|Collects feedback| T[User Feedback]
  T[User Feedback] -->|Improves query handling| D[Query Handler]

  %% Connections to External Data
  I[Text Data/Articles] -->|Retrieves| U[External APIs/Knowledge Sources]

  %% Labels and Relationships
  A -->|Provides input through| T
  T -->|Improves system performance via feedback| L
  K -->|Improves retrieval quality| F
