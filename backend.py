import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import chromadb
from transformers import pipeline

client = chromadb.Client()
csv_path = "/Users/adityaab14/Documents/Projects/power-bi-dax-generator/KB-dax-formulas.csv"
model = SentenceTransformer('all-MiniLM-L6-v2')
collection_name = "dax_formulas"
collection = client.create_collection(collection_name)

def preprocess_input(operation, table_structure):
    if not operation:
        raise ValueError("Operation cannot be empty.")
    
    operation = operation.strip()
    operation = operation.lower()

    if not isinstance(table_structure, pd.DataFrame) or table_structure.empty:
        raise ValueError("Table structure must be a non-empty DataFrame.")

    table_structure.columns = table_structure.columns.str.strip()  # Strip column names
    table_structure = table_structure.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Strip string values

    return operation, table_structure

def store_embeddings_in_chroma():
    df = pd.read_csv(csv_path)
    embeddings = df['Intent'].apply(lambda x: model.encode(str(x))).tolist()
    metadata = df[['Function Name', 'Category', 'Syntax', 'Parameters', 'Return Value', 'Remarks', 'Example', 'Example Explanation', 'Related Functions']].to_dict(orient='records')
    
    # Generate unique ids (using the index of the DataFrame)
    ids = [str(i) for i in range(len(df))]
    
    # Add embeddings and metadata to Chroma
    for i, (embedding, metadata_item) in enumerate(zip(embeddings, metadata)):
        collection.add(
            ids=[ids[i]],  # Unique identifier for each document
            documents=[str(df['Intent'][i])],  # Intent as the document
            metadatas=[metadata_item],  # Metadata for each document
            embeddings=[embedding]  # Store embeddings
        )

    print("Embeddings stored in Chroma DB!")
    document_count = collection.count()
    print("Number of documents in Chroma:", document_count)
    # TODO: Check how the formulas retrievd from ChromaDB are structured

def query_knowledge_base(operation):
    operation_embedding = model.encode(operation)
    results = collection.query(query_embeddings=[operation_embedding], n_results=5)

    print("Query Results:", results)  # Debug output

    if 'metadatas' in results and 'documents' in results:
        # Extract relevant information from Chroma results
        documents = results['documents'][0]
        metadatas = results['metadatas'][0]

        
        df_results = pd.DataFrame(metadatas)
        df_results['Document'] = documents 

        return df_results
    else:
        print("No results found!")
        return pd.DataFrame()
    
def generate_prompt(operation, table_structure, shortlist):
      
    instructions = (
        "You are a DAX expert tasked with generating DAX formulas based on user requirements.\n"
        "1. Read and understand the **User Input Operation** carefully.\n"
        "2. Analyze the **Optional Input Table** to determine which columns are involved in the operation. If no table is provided, create a generic formula with placeholder columns.\n"
        "3. Use the **Relevant DAX Formulas** to help guide your formula creation. You can modify or combine them to generate the final DAX formula.\n"
        "4. Ensure the formula is syntactically correct and directly solves the operation described by the user.\n"
        "5. If the table structure is provided, reference the appropriate columns in your formula. If no table structure is provided, use general placeholders like `<table>[<column>]`.\n"
    )
   
    prompt = (
        instructions + 
        f"\n### Operation Description:\n{operation}\n" +
        f"\n### Optional Input Table:\n{table_structure}\n" +
        f"\n### Shortlist of Relevant DAX Formulas:\n{shortlist}\n"
    )

    return prompt


def call_llm(prompt):
    
    pipe = pipeline("text2text-generation", model="google/flan-t5-base")
    response = pipe(
        prompt, 
        max_length=700,  # Specify max length for the output
        truncation=True,  # Enable truncation for long inputs
        pad_token_id=50256,  # Set the pad_token_id to a specific value (adjust based on the model)
        num_return_sequences=1
    )
    return response[0]['generated_text']

def process_llm_response(operation, table_structure):
    operation, table_structure = preprocess_input(operation, table_structure)
    store_embeddings_in_chroma()
    shortlist = query_knowledge_base(operation)
    prompt = generate_prompt(operation, table_structure, shortlist)
    response = call_llm(prompt)
    return response


if __name__ == "__main__":
    store_embeddings_in_chroma()
    operation = "Sum of Sales"
    table_structure = {
        "columns": ["Date", " Category", "Sales Amount"], 
        "data": [["2024-01-01", "Electronics", 5000], ["2024-02-01", "Furniture", 3000]]
    }

    # Convert table_structure to a pandas DataFrame
    table_df = pd.DataFrame(table_structure["data"], columns=[col.strip() for col in table_structure["columns"]])

    print("Before processing:")
    print(f"Operation: '{operation}'")
    print(f"Table Structure:\n{table_df}")

    # Process inputs with the function
    cleaned_operation, cleaned_table_structure = preprocess_input(operation, table_df)

    print("\nAfter processing:")
    print(f"Cleaned Operation: '{cleaned_operation}'")
    print(f"Cleaned Table Structure:\n{cleaned_table_structure}")
    shortlist = query_knowledge_base(operation)
    prompt = generate_prompt(operation, table_structure, shortlist)
    response = call_llm(prompt)
    #result = process_llm_response(response)
    print(prompt)
    print(response)
