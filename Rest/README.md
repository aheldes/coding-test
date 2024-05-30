# How to run

## Using docker

If you are using proxy, you need to set the proxy in the Dockerfile. If not, you can remove the `ENV` line in the
Dockerfile.

### Build the image

```bash
docker build -t rest .
```

### Run the container

```bash
docker run rest
```

## Without docker

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the script

```bash
uvicorn main:app --reload
```

App will be available at `http://localhost:8000/`

### Documentation

Feel free to use swagger at `/docs` to test the API or redoc at `/redoc` to see documentation.
