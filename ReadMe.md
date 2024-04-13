# FastAPI Examples

official link: [FastAPI](https://fastapi.tiangolo.com/)

## Setting up environment

Create a new environment using [conda](https://docs.anaconda.com/free/miniconda/index.html)

```sh
conda create --name apitest python=3.10 pip
```

Now activate and install requirments

```sh
conda activate apitest
pip install -r requirements.txt
```

## Running examples

Just provide folder with main and app. e.g.

```sh
uvicorn 01_basics.main:app
```
