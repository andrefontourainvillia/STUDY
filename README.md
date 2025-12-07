# STUDY

## JW.org Content Fetcher

This repository contains a script to fetch content from JW.org webpages and format it as Markdown.

### Requirements

- Python 3.7 or higher
- Internet connection

### Installation

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

To fetch and format content from the specified JW.org page:

```bash
python fetch_jw_content.py
```

Or provide a custom URL:

```bash
python fetch_jw_content.py "https://www.jw.org/your-custom-url"
```

The script will:
1. Fetch the content from the webpage
2. Convert it to Markdown format
3. Save it to `jw_content.md`
4. Display the content in the console

### Default URL

The script is configured to fetch content from:
```
https://www.jw.org/finder?srcid=jwlshare&wtlocale=T&prefer=lang&docid=2025566
```

### Output

The formatted content will be saved in `jw_content.md` in the current directory.