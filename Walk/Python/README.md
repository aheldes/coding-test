# How to run

## Using docker

If you are using proxy, you need to set the proxy in the Dockerfile.

### Build the image

```bash
docker build -t python-walk .
```

### Run the container

```bash
docker run python-walk
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
