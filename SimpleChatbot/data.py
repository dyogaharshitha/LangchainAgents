
import pandas as pd
from transformers import pipeline

# Initialize TaPaS model
tapas = pipeline("table-question-answering", model="google/tapas-small-finetuned-sqa") #google/tapas-large-finetuned-wtq

def tapas_search_question( question: str ) -> str :
    """Search movie database given query."""
    
    csv_path = "movies.csv"
    intermediate_results = pd.DataFrame()
    chunk_size=200 
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
        chunk = chunk.reset_index(drop=True)
        chunk = chunk.fillna("").astype(str)

        # Drop unnamed or badly-formatted columns (optional)
        chunk = chunk.loc[:, ~chunk.columns.str.contains('^Unnamed')]
        chunk.drop(['crew', 'production_companies', 'homepage'], inplace=True, axis=1)

        try:
            # Ask the question on the chunk
            result = tapas(table=chunk, query=question) ;

            if isinstance(result, dict):
                answer = result["answer"] 
                row_indices = {coord[0] for coord in result["coordinates"]}
                matched_rows = chunk.iloc[list(row_indices)] ; print(matched_rows)

                # Find rows where ANY cell matches the answer
                matching_rows = chunk.apply(
                    lambda row: row.astype(str).str.contains(str(answer), case=False, na=False).any(),
                    axis=1
                )
                matched_rows = chunk[matching_rows]
                intermediate_results = pd.concat([intermediate_results, matched_rows], ignore_index=True)  
        except Exception as e:
            print(f"Error on chunk: {e}")
            continue

    # Re-run the question on the intermediate results
    if not intermediate_results.empty:
        intermediate_results = intermediate_results.reset_index(drop=True)
        try:
            final_result = tapas(table=intermediate_results, query=question)
            row_indices = {coord[0] for coord in final_result["coordinates"]}
            matched_rows = chunk.iloc[list(row_indices)]
            return final_result #, intermediate_results
        except Exception as e:
            print(f"Error during second pass: {e}")
            return  intermediate_results
    else:
        print("No matching rows found.")
        return None

