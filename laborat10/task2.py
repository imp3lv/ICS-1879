import os
import shutil

files = os.listdir('Python_docs')
print(files)

os.makedirs('RESULTS', exist_ok=True)

shutil.copy('Python_docs/' + files[0], 'RESULTS')
shutil.copy('Python_docs/' + files[1], 'RESULTS')
