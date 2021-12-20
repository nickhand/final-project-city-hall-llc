import os

conda_prefix = os.environ['CONDA_PREFIX']
path = f"{conda_prefix}/lib/python3.8/site-packages/jupyter_server_proxy/handlers.py"
print(path)

with open(path, 'r') as f:
    contents = f.read()

for tag, value in zip(['connect', 'request'], ['250.0', '300.0']):
    contents = contents.replace(f"{tag}_timeout={value}", f"{tag}_timeout=1000.0")

with open(path, "w") as f:
    f.write(contents)
