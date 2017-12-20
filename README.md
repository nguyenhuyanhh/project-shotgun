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

Running of time of the script is 50 seconds for 100 posts.

## Insights

16 fields are extracted from the [Bobbi Brown Cosmetics page](https://www.facebook.com/bobbibrown.sg/), using [Facebook Graph API](https://developers.facebook.com/docs/graph-api/reference). We are interested in the relation between posts characteristics and their performance, with respect to specific characteristics of beauty products (which is what the page is about); the following table summarises possible attributes/ information that could be extracted from the data.

| Field | Type | Possible processing steps
| --- | --- | ---
| `reactions_*` (6 fields) | `int` | <ul><li>Get the posts' interaction counts</li><li>Get the posts' sentiment value (assign each reaction a score e.g. `like=1`, `sad=-1` then calculate the weighted average for each post)</li></ul>
| `comments`, `shares` | `int` | Get the posts' interaction counts
| `created_time` | `datetime` | <ul><li>Analyse the posts' date (posts on a certain day of the week might have higher interactions</li><li>Analyse the posts' timing (posts at a certain time of the day might have higher interactions)</li></ul>
| `type` | `enum{link,status,photo,video,offer}` | Analyse the posts based on post types (different post types might have different interactions)
| `data_photo` | `string` | Analyse the products mentioned in the photo (possibly using image recognition)
| `data_video` | `string` | Analyse the products mentioned in the video <ul><li>Using the keyframes of the video (image recognition)</li><li>Using the closed captions/ transcripts associated with the video</li></ul>
| `message` | `string` | <ul><li>Analyse the keywords/ hashtags in the message</li><li>Analyse the products mentioned in posts, which could be extracted using Named Entity Recognition (posts about a certain product might attract more interactions)</li></ul>
| `story` | `string` | Indicate special post types (cover photo, profile photo updates, live videos, etc.) that needs different processing

The post comment data could also be extracted using Graph API, but are excluded for the purpose of the challenge.