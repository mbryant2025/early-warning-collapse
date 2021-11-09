import json

with open('/Users/michaelbryant/Desktop/sampleData.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)

