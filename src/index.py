import pandas as pd
import numpy as np

#  Read the data from the CSV file
def read_data(file_path):
    data = pd.read_csv(file_path, index_col=0)
    return data

#  Preprocess the sequences
def preprocess_sequences(data):
    """
    Preprocesses a given DataFrame of sequences by padding all sequences to the maximum length.
    
    Args:
        data (pandas.DataFrame): A DataFrame containing sequences as values.
        
    Returns:
        list: A list of padded sequences, where each sequence is padded with 'X' to make them the same length.
    """
    max_length = max(len(seq) for seq in data.values.flatten())
    padded_sequences = []
    for seq in data.values.flatten():
        padded_seq = seq.ljust(max_length, 'X')  # Pad with 'X' to make all sequences the same length
        padded_sequences.append(padded_seq)
    return padded_sequences

#  Extract features
def extract_features(sequences):
    """
    Extracts features from a list of sequences.

    Parameters:
        sequences (List[str]): A list of sequences.

    Returns:
        Tuple[List[np.ndarray], List[List[float]]]: A tuple containing two lists. 
        The first list contains one-hot encoded vectors for each sequence, and the second list 
        contains letter compositions for each sequence.

    Raises:
        None
    """
    one_hot_encoded_vectors = []
    letter_compositions = []
    
    # One Hot Encoded Letter Vector
    letter_to_index = {letter: i for i, letter in enumerate('ACDEFGHIKLMNPQRSTVWYX')}
    for seq in sequences:
        one_hot_encoded_seq = np.zeros((len(seq), 21))
        for i, letter in enumerate(seq):
            if letter in letter_to_index:
                one_hot_encoded_seq[i][letter_to_index[letter]] = 1
            else:
                one_hot_encoded_seq[i][-1] = 1  # Encoding 'X'
        one_hot_encoded_vectors.append(one_hot_encoded_seq.flatten())
    
    # Letter Composition
    for seq in sequences:
        letter_count = {letter: seq.count(letter) for letter in 'ACDEFGHIKLMNPQRSTVWYX'}
        total_letters = sum(letter_count.values())
        composition_vector = [letter_count[letter] / total_letters for letter in 'ACDEFGHIKLMNPQRSTVWYX']
        letter_compositions.append(composition_vector)
    
    return one_hot_encoded_vectors, letter_compositions

#  Organize features into a data structure
def create_data_structure(identifiers, one_hot_encoded_vectors, letter_compositions):
    """
    Creates a data structure with the given identifiers, one-hot encoded vectors, and letter compositions.

    Parameters:
        identifiers (List[str]): A list of identifiers.
        one_hot_encoded_vectors (List[np.ndarray]): A list of one-hot encoded vectors.
        letter_compositions (List[List[float]]): A list of letter compositions.

    Returns:
        dict: A dictionary representing the data structure. The keys are 'Identifier', 'One Hot Encoded Letter Vector', and 'Letter Composition'. The values are the corresponding input arguments.
    """
    data_structure = {
        'Identifier': identifiers,
        'One Hot Encoded Letter Vector': one_hot_encoded_vectors,
        'Letter Composition': letter_compositions
    }
    return data_structure

#  Return the data structure
def process_data(file_path):
    """
    Processes data from a file and returns a data structure containing preprocessed sequences with extracted features.

    Args:
        file_path (str): The path to the file containing the data.

    Returns:
        dict: A dictionary representing the data structure. The keys are 'Identifier', 'One Hot Encoded Letter Vector', and 'Letter Composition'. The values are the corresponding input arguments.
    """
    #  Read the data
    data = read_data(file_path)
    
    #  Preprocess the sequences
    sequences = preprocess_sequences(data)
    
    #  Extract features
    one_hot_encoded_vectors, letter_compositions = extract_features(sequences)
    
    #  Organize features into a data structure
    identifiers = data.index.tolist()
    data_structure = create_data_structure(identifiers, one_hot_encoded_vectors, letter_compositions)
    
    return data_structure


# Test the implementation
file_path = "data/uniprot_sequences.csv"
processed_data = process_data(file_path)
print(processed_data)

# Convert processed_data to a DataFrame
df_processed_data = pd.DataFrame(processed_data)

# Define the output file path
output_file_path = "processed_data.csv"

# Save the processed data to a CSV file
df_processed_data.to_csv(output_file_path, index=False)

print("Processed data saved to:", output_file_path)