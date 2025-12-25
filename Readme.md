## **AI-Powered RAG Teaching Assistant**

### **Overview**

The AI-Powered RAG Teaching Assistant is an intelligent question-answering system designed to help learners efficiently navigate educational video content. The system leverages **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers by retrieving relevant video segments and generating human-like responses with precise timestamps.

The project processes course videos by converting them into audio, transcribing and translating subtitles, generating vector embeddings, and storing them for semantic retrieval. When a user asks a question, the system retrieves the most relevant video chunks using similarity search and guides the learner to the exact video and timestamp where the topic is explained. This project demonstrates the practical application of **NLP, embeddings, vector search, and LLMs** in the education domain.

---

### **Key Features**

* Question answering from educational video content
* Semantic search using vector embeddings
* Timestamp-based video guidance for precise learning
* Context-aware, human-like responses using an LLM
* Fully automated data processing pipeline (video → audio → text → vectors → answers)
* Local LLM inference for privacy and efficiency

---

### **Proposed Design**

The system follows a **Retrieval-Augmented Generation (RAG)** architecture. Video lectures are first converted into audio and transcribed using **Whisper**, followed by subtitle chunking. Each chunk is embedded using a sentence embedding model and stored in a vector database.

During inference, user queries are converted into embeddings and compared with stored vectors using **cosine similarity** to retrieve the most relevant video segments. These retrieved segments are then passed as context to a Large Language Model, which generates a clear, user-friendly response while referencing the appropriate video and timestamps.

This design improves answer accuracy, reduces hallucinations, and ensures responses are grounded in actual course material.

---

### **Requirements**

#### **Programming Languages**

* Python

#### **Libraries & Frameworks**

* OpenAI Whisper (Speech-to-Text)
* Scikit-learn (Cosine Similarity)
* Pandas, NumPy
* Joblib

#### **Models**

* bge-m3 (Text Embeddings)
* LLaMA (Local LLM for response generation)

#### **Tools & Technologies**

* FFmpeg (Video to Audio Conversion)

#### **Hardware (Optional)**

* GPU for faster transcription and embedding generation

---

# How to use this RAG AI Teaching assistant on your own data

## Step 1 - Collect your videos
Move all your video files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by running video_to_mp3

## Step 3 - Convert mp3 to json 
Convert all the mp3 files to json by running mp3_to_json

## Step 4 - Convert the json files to Vectors
Use the file preprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM


