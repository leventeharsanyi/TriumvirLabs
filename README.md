# TriumvirLabs

Small Streamlit demo app using **Python 3.13** and **Poetry**.

## Setup

```bash
git clone https://github.com/leventeharsanyi/TriumvirLabs
cd triumvirlabs
poetry env use python3.13
poetry shell
poetry install
```

If `poetry shell` is not working, try `eval $(poetry env activate)`

## Adding an env file and put a secret key there
The .env should be at the level of pyproject.toml. For testing purposes add a secret like this to the env. Also add the ELEVENSLAB api key.

```bash
MY_SECRET_MESSAGE=You_did_it!
ELEVENLABS_API_KEY=<YOUR_API_KEY>
```

## Running the app

```bash
poetry run streamlit run app/main.py
```


## Data
The sythetic EHR data used for this project comes from Synthea, you can find out more details about there open-source patient population simulation data [here](https://synthea.mitre.org/downloads).