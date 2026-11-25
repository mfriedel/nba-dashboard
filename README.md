# NBA Dashboard

A Streamlit dashboard exploring NBA team-game data, deployed to Streamlit Community Cloud.

## Data

`data/nba.csv` has **one row per team per completed game** (2,460 rows). Each game
appears as exactly **two rows**, one for each team.

Notes on the data:

- There is no game ID column. A game is identified by `DATE` plus the two teams
  named in `MATCHUP`.
- `DATE` is text in `M/D/YYYY` format and is parsed on load.
- `W.L` and `PD` (point differential) reveal the game result, so they are **never**
  used as predictors in any model.

## Tabs

1. **Explore Data** — descriptive views of the data.
2. **Logistic Regression** — modeling win/loss from pre-outcome features.
3. **Clustering** — unsupervised grouping of teams/games.

## Running locally

```bash
uv run --project ~/code/DS6021_F26 streamlit run app.py
```

Or with a plain virtual environment:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment

Pushed to GitHub and deployed on Streamlit Community Cloud with `app.py` as the
entry point. `requirements.txt` pins the versions used locally (Python 3.12).
