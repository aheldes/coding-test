# How to run

## Using docker

If you are using proxy, you need to set the proxy in the Dockerfile. If not, you can remove the `ENV` line in the
Dockerfile.

### Build the image

```bash
docker build -t ts-paths .
```

### Run the container

```bash
docker run ts-paths
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
