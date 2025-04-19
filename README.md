# Smart Search-Summarizer

An AI-powered tool designed to assist users with real-time searches and concise summaries of their interests. Leveraging advanced language models, this application streamlines information retrieval and distillation, enhancing productivity and comprehension.

---

## 🧠 Features

- **Real-Time Search**:Fetches up-to-date information based on user queries
- **Automated Summarization**:Generates concise summaries of retrieved content using large language models
- **User-Friendly Interface**:Intuitive design facilitating seamless interaction
- **Modular Architecture**:Separation of concerns with distinct frontend and backend components

---

## 🏗️ Architecture Overview

1. **Frontend**:
    Handles user interactions and displays result.
2. **Backend**:
    Processes search queries and interfaces with language models for summarization.
3. **Integration**:
    Frontend communicates with backend APIs to deliver real-time search and summarization functionalities.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higer- Node.js and npm (for frontend developmet)- OpenAI API key (or equivalet)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Aarushi232005/Smart_Search-Summarizer.git
   cd Smart_Search-Summarizer
   ``


2. **Set up the backend**:

   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ``


3. **Set up the frontend**:

   ```bash
   cd ../frontend
   npm install
   ``


4. **Configure environment variables**:

  - Create a `.env` file in the backend directory.
  - Add your API keys and other necessary configurations.

---

## 🧪 Usage

1. **Start the backend server**:

   ```bash
   cd backend
   python app.py
   ``


2. **Start the frontend development server**:

   ```bash
   cd frontend
   npm start
   ``


3. **Access the application**:

  - Open your browser and navigate to `http://localhost:3000` to interact with the Smart Search-Summarizer.

---

## 📁 Project Structre


```bash
Smart_Search-Summarizer/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── package.json
│   ├── src/
│   └── ...
├── README.md
└── ...```


---

## 🤝 Contribuing

Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.


## 📬 Contact

For any inquiries or feedback, please contact Aarush232005.
