import os

# The exact structure you asked for
structure = {
    "data/raw": [],
    "data/processed": [],
    "src/collectors": ["__init__.py", "reddit_scraper.py", "news_scraper.py"],
    "src/processing": ["__init__.py", "cleaner.py", "chunker.py"],
    "src/rag_engine": ["__init__.py", "vector_store.py", "retriever.py"],
    "src/analysis": ["__init__.py", "sentiment.py", "topics.py"],
    "src/ui": ["app.py"],
    ".": [".env", "requirements.txt", "README.md", "main.py"]
}

def create_structure():
    print("🚀 Starting Project Setup...")
    
    for folder, files in structure.items():
        # Create the folder
        os.makedirs(folder, exist_ok=True)
        print(f"   📂 Created Folder: {folder}")
        
        # Create the files inside that folder
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding='utf-8') as f:
                    f.write("") # Create empty file
                print(f"      📄 Created File: {file}")
            else:
                print(f"      ✅ File exists: {file}")

    print("\n🎉 Success! Your project structure is ready.")
    print("👉 Next step: Open 'requirements.txt' and paste your libraries.")

if __name__ == "__main__":
    create_structure()
