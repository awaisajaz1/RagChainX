import json

nb_path = 'rager_the_smasher.ipynb'

with open(nb_path, 'r') as f:
    nb = json.load(f)

new_code = [
    "from langchain_text_splitters import RecursiveCharacterTextSplitter\n",
    "\n",
    "splitter = RecursiveCharacterTextSplitter(\n",
    "    chunk_size=500,\n",
    "    chunk_overlap=50,\n",
    "    length_function=len,\n",
    "    is_separator_regex=False,\n",
    ")\n",
    "\n",
    "chunks = splitter.split_documents([doc])\n",
    "chunks"
]

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        # Check if this is the target cell
        if any('RecursiveCharacterTextSplitter' in line for line in source):
            cell['source'] = new_code
            break

with open(nb_path, 'w') as f:
    json.dump(nb, f, indent=1)
