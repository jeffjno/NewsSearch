import json
import os

class JsonMerger:
    def __init__(self, input_directory):
        self.input_directory = input_directory

    def merge_json_files(self, output_file):
        merged_data = {}

        for filename in os.listdir(self.input_directory):
            if filename.endswith('.json'):
                filepath = os.path.join(self.input_directory, filename)
                
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                if isinstance(data, list):
                    if not isinstance(merged_data, list):
                        merged_data = []
                    merged_data.extend(data)
                elif isinstance(data, dict):
                    merged_data.update(data)
                else:
                    raise ValueError(f"Arquivo JSON não contém lista ou dicionário: {filename}")

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f)