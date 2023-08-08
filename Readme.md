# Vanilla Forum Search Script

This repository contains a Python script to search discussions and comments in a Vanilla forum within the past two weeks for specific keywords. The script then returns the results as a pretty-printed JSON object.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/vanilla-forum-search.git
cd vanilla-forum-search
```

2. Install the required dependencies:

```bash
pip install requests
```

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

The script will search for discussions from the past two weeks and comments containing the specified keywords, and then output the results as a JSON object.

## License

MIT.
