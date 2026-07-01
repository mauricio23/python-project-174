import pytest
import os
from gendiff.scripts.gendiff import generate_diff

def get_fixture_path(filename):
    return os.path.join('tests', 'archivos', filename)

def read_file(filename):
    with open(get_fixture_path(filename), 'r', encoding='utf-8') as f:
        return f.read()

def test_generate_diff_json_stylish():
    file1 = get_fixture_path('filepath1.json')
    file2 = get_fixture_path('filepath2.json')
    expected = read_file('result_stylish.txt')
    
    assert generate_diff(file1, file2) == expected

def test_generate_diff_yaml_stylish():
    file1 = get_fixture_path('filepath1.yaml')
    file2 = get_fixture_path('filepath2.yaml')
    expected = read_file('result_stylish.txt')
    
    assert generate_diff(file1, file2) == expected

def test_generate_diff_json_plain():
    file1 = get_fixture_path('filepath1.json')
    file2 = get_fixture_path('filepath2.json')
    expected = read_file('result_plain.txt')
    
   
    assert generate_diff(file1, file2, 'plain') == expected

def test_generate_diff_yaml_plain():
    file1 = get_fixture_path('filepath1.yaml')
    file2 = get_fixture_path('filepath2.yaml')
    expected = read_file('result_plain.txt')
    
    assert generate_diff(file1, file2, 'plain') == expected