import json
import os

class JSONConverter:
    @staticmethod
    def to_json(data, indent=2):
        """Convert Python object to JSON string"""
        try:
            return json.dumps(data, indent=indent, ensure_ascii=False)
        except TypeError as e:
            return f"Error: {e}"
    
    @staticmethod
    def from_json(json_string):
        """Convert JSON string to Python object"""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            return f"Error: {e}"
    
    @staticmethod
    def save_to_file(data, filename):
        """Save Python object as JSON file"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(script_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return f"Data saved to {filepath}"
        except Exception as e:
            return f"Error: {e}"
    
    @staticmethod
    def load_from_file(filename):
        """Load JSON data from file"""
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(script_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"]
    }
    
    converter = JSONConverter()
    
    # Convert to JSON string
    json_string = converter.to_json(data)
    print("JSON String:")
    print(json_string)
    
    # Convert back to Python object
    python_obj = converter.from_json(json_string)
    print("\nPython Object:")
    print(python_obj)
    
    # Save to file
    result = converter.save_to_file(data, "example.json")
    print(f"\n{result}")
    
    # Load from file
    loaded_data = converter.load_from_file("example.json")
    print("\nLoaded Data:")
    print(loaded_data)