# How to run

## Using docker

If you are using proxy, you need to set the proxy in the Dockerfile.

### Build the image

```bash
docker build -t ts-walk .
```

### Run the container

```bash
docker run ts-walk
```

## Without docker

### Install dependencies

```bash
npm install
```

### Run the script

```bash
tsc main.ts
```

```bash
node main.js
```
