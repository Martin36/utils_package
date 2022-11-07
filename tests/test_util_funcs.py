import os
import unittest

from utils_package.util_funcs import (
  load_json, load_jsonl, load_txt, store_json, store_jsonl, 
  store_multiple_json, store_txt, unique
)

def remove_folder(folder: str):
  if os.path.exists(folder):
    for file in os.listdir(folder):
      os.remove(os.path.join(folder, file))
    os.rmdir(folder)

class TestUtilFuncs(unittest.TestCase):

  outputs_folder = "tests/outputs"
  
  def setUp(self):
    remove_folder(self.outputs_folder)    
      
  def test_load_json(self):
    input = "tests/data/data.json"
    output = load_json(input)
    self.assertIsNotNone(output, "The output should not be None")
  
  def test_load_jsonl(self):
    input = "tests/data/data.jsonl"
    output = load_jsonl(input)
    self.assertIsNotNone(output, "The output should not be None")

  def text_load_txt(self):
    input = "tests/data/data.txt"
    output = load_txt(input)
    self.assertIsNotNone(output, "The output should not be None")
    self.assertEqual(len(output), 3, "The output should contain same number of elements as the input file lines")
    
  def test_store_json(self):
    data = load_json("tests/data/data.json")
    file_name = "tests/outputs/data.json"
    store_json(data, file_name)
    self.assertTrue(os.path.exists(file_name), "The output file should exist")
  
  def test_store_jsonl(self):
    data = load_jsonl("tests/data/data.jsonl")
    file_name = "tests/outputs/data.jsonl"
    store_jsonl(data, file_name)
    self.assertTrue(os.path.exists(file_name), "The output file should exist")
    
  def test_store_multiple_json(self):    
    data_list = [
      load_json("tests/data/data.json"), 
      load_json("tests/data/data.json")
    ]
    file_names = ["tests/outputs/data1.json", "tests/outputs/data2.json"]
    store_multiple_json(data_list, file_names)
    for file in file_names:
      self.assertTrue(os.path.exists(file), "The output files should exist")
  
  def test_store_txt(self):
    data = ["a", "b", "c"]
    file_path = "tests/outputs/data.txt"
    store_txt(data, file_path)
    self.assertTrue(os.path.exists(file_path), "The output file should exist")  
  
  def test_unique(self):
    input = ["a", "b", "c", "a", "b", "c"]
    correct = ["a", "b", "c"]
    output = unique(input)
    self.assertEqual(output, correct, "The output for string list should NOT contain any duplicates")
    
    input = [{"a": 1}, {"b": 2}, {"c": 3}, {"a": 1}, {"b": 2}, {"c": 3}]
    correct = [{"a": 1}, {"b": 2}, {"c": 3}]
    output = unique(input)
    self.assertEqual(output, correct, "The output for dict list should NOT contain any duplicates")

    input = [["a", 1], ["b", 2], ["c", 3], ["a", 1], ["b", 2], ["c", 3]]
    correct = [["a", 1], ["b", 2], ["c", 3]]
    output = unique(input)
    self.assertEqual(output, correct, "The output for list of lists should NOT contain any duplicates")

    input = [{"a": {"b": 1}}, {"a": {"b": 2}}, {"a": {"b": 3}}, {"a": {"b": 1}}, {"a": {"b": 2}}, {"a": {"b": 3}}]
    correct = [{"a": {"b": 1}}, {"a": {"b": 2}}, {"a": {"b": 3}}]
    output = unique(input)
    self.assertEqual(output, correct, "The output for nested dicts should NOT contain any duplicates")


if __name__ == '__main__':
  unittest.main()