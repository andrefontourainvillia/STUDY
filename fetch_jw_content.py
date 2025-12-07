#!/usr/bin/env python3
"""
Script to fetch content from JW.org webpage and format it as Markdown.
"""

import requests
from bs4 import BeautifulSoup
import html2text
import sys


def fetch_and_format_content(url):
    """
    Fetch content from the given URL and format it as Markdown.
    
    Args:
        url (str): The URL to fetch content from
        
    Returns:
        str: Content formatted as Markdown
    """
    try:
        # Fetch the webpage with a user agent to simulate browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        print(f"Fetching content from: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer"]):
            script.decompose()
        
        # Get the main content area (adjust selector based on the site structure)
        # Try to find main content container
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content') or soup.body
        
        # Convert HTML to Markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap text
        
        # Get text content
        markdown_content = h.handle(str(main_content))
        
        return markdown_content
        
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"
    except Exception as e:
        return f"Error processing content: {e}"


def main():
    """Main function to execute the script."""
    # The specific URL from the problem statement
    url = "https://www.jw.org/finder?srcid=jwlshare&wtlocale=T&prefer=lang&docid=2025566"
    
    # Allow custom URL via command line argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    # Fetch and format content
    markdown_content = fetch_and_format_content(url)
    
    # Save to file
    output_file = "jw_content.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Content from JW.org\n\n")
        f.write(f"**Source URL:** {url}\n\n")
        f.write("---\n\n")
        f.write(markdown_content)
    
    print(f"\nContent saved to: {output_file}")
    
    # Also print to console
    print("\n" + "="*80)
    print("MARKDOWN CONTENT:")
    print("="*80 + "\n")
    print(markdown_content)


if __name__ == "__main__":
    main()
