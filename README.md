# TriumvirLabs

Small Streamlit demo app using **Python 3.12** and **Poetry**.

## Setup

```bash
git clone https://github.com/leventeharsanyi/TriumvirLabs
cd triumvirlabs
poetry env use python3.12
poetry shell
poetry install
```

If `poetry shell` is not working, try `eval $(poetry env activate)`

## Secret Keys
The .env should be at the level of pyproject.toml. Add the `ELEVENLABS_API_KEY` and the `ANTHROPIC_API_KEY`.

```bash
ELEVENLABS_API_KEY=<YOUR_API_KEY>
ANTHROPIC_API_KEY=<YOUR_API_KEY>
```

## Running the app

```bash
poetry run streamlit run app/main.py
```


## Data
The sythetic EHR data used for this project comes from Synthea, you can find out more details about there open-source patient population simulation data [here](https://synthea.mitre.org/downloads).

## Used APIs
- [ElevenLabs](https://elevenlabs.io/)
- [Anthropic](https://anthropic.com/)