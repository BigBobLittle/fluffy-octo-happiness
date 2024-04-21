import os
import pytest
import pandas as pd
from ..src.index import read_data, preprocess_sequences, extract_features, create_data_structure, process_data

current_dir = os.path.dirname(__file__)
test_data_path = os.path.join(current_dir, '..', 'data', 'test_data.csv')
@pytest.fixture
def test_data():
    return pd.DataFrame({'Sequence': ['MER', 'AAAAA', 'GGG']})

def test_read_data():
    file_path = test_data_path
    data = read_data(file_path)
    assert isinstance(data, pd.DataFrame)
    assert len(data) > 0

def test_preprocess_sequences(test_data):
    sequences = preprocess_sequences(test_data)
    assert sequences == ['MERXX', 'AAAAA', 'GGGXX']

def test_extract_features():
    sequences = ['MER', 'AAAAA', 'GGG']
    one_hot_encoded_vectors, letter_compositions = extract_features(sequences)
    assert len(one_hot_encoded_vectors) == len(sequences)
    assert len(letter_compositions) == len(sequences)

def test_create_data_structure():
    identifiers = ['ID1', 'ID2']
    one_hot_encoded_vectors = [[0, 1, 0], [1, 0, 0]]
    letter_compositions = [[0.2, 0.5, 0.3], [0.4, 0.3, 0.3]]
    data_structure = create_data_structure(identifiers, one_hot_encoded_vectors, letter_compositions)
    assert isinstance(data_structure, dict)
    assert 'Identifier' in data_structure
    assert 'One Hot Encoded Letter Vector' in data_structure
    assert 'Letter Composition' in data_structure

def test_process_data():
    file_path = test_data_path
    processed_data = process_data(file_path)
    assert isinstance(processed_data, dict)
    assert 'Identifier' in processed_data
    assert 'One Hot Encoded Letter Vector' in processed_data
    assert 'Letter Composition' in processed_data
