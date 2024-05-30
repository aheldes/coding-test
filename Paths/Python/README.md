# How to run

## Using docker

If you are using proxy, you need to set the proxy in the Dockerfile. If not, you can remove the `ENV` line in the
Dockerfile.

### Build the image

```bash
docker build -t python-paths .
```

### Run the container

```bash
docker run python-paths
```

## Without docker

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the script

```bash
python main.py
```
