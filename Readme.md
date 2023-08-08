# Vanilla Forum Search Script

This repository contains a Python script to search discussions and comments in a Vanilla forum within the past two weeks for specific keywords. The script then returns the results as a pretty-printed JSON object.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/ohnotnow/vanilla-forum-search.git
cd vanilla-forum-search
```

2. Install the required dependencies:

```bash
pip3 install requests
```
(Depending on your install it might just be `pip` - and indeed just `python` below)
## Configuration

You need to set an environment variable with the base of your vanilla install.  Eg,
```bash
export VANILLA_URL="https://vf.example.com"
```

## Usage

Run the script with the keywords you want to search for:

```bash
python3 ./main.py word1 word2 word3
```

The script will search for discussions from the past two weeks and comments containing the specified keywords, and then output the results as a JSON object.  If you want a more 'plain text' result you can use [jq](https://jqlang.github.io/jq/download/) :
```bash
python3 main.py word1 word2 word3 | jq -r '.[] | .Thread, (.Matches[] | "Keywords: \(.keywords)", "Comment URL: \(.comment_url)", "Embedded URLs: \(.embedded_urls | join(", "))")'
```
## License

MIT.
