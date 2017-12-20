# project-shotgun

This is a technical challenge for Synthesis.

## Setup

1. Install python dependencies: `$ pip install --user --upgrade requests beautifulsoup4 pandas`
2. Create a file `config.json` with a Facebook Graph API token
```json
{
    "access_token": "your_access_token"
}
```
3. Run the code: `$ python synthesis_technical_challenge.py`. The csv output would be in `output.csv`.

## Insights

14 fields are extracted from the data. We are interested in the relation between posts characteristics and their performance; the following table summarises possible attributes/ information that could be extracted from the data.

| Field | Type | Possible processing steps
| --- | --- | ---
| `reactions_*` (6 fields) | `int` | <ul><li>Get the posts' interaction counts</li><li>Get the posts' sentiment value (assign each reaction a score e.g. `like=1`, `sad=-1` then calculate the weighted average for each post)</li></ul>
| `comments`, `shares` | `int` | Get the posts' interaction counts
| `created_time` | `datetime` | <ul><li>Analyse the posts' date (posts on a certain day of the week might have higher interactions</li><li>Analyse the posts' timing (posts at a certain time of the day might have higher interactions)</li></ul>
| `type` | `enum{link, status, photo, video, offer}` | Analyse the posts based on post types (different post types might have different interactions)
| `message` | `string` | <ul><li>Analyse the products mentioned in posts (posts about a certain product might attract more interactions. Products could be extracted using either Named Entity Recognition or posts' image recognition)</li></ul>
| `story` | `string` | Indicate special post types (cover photo, profile photo updates, live videos, etc.) that needs different processing