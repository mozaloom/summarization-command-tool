import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup


def extract_from_url(url):
    text = ''
    req = urllib.request.Request(
        url,
        data=None,
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 OPR/84.0.4316.31'}
    )
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, 'html.parser')
    for pharagraph in parser.find_all('p'):
        print(pharagraph.text)
        text += pharagraph.text
        
    return text

def process(text):
    summarizer = pipeline('summarization', model = "t5-small")
    result = summarizer(text, max_length=100)
    click.echo('summarization processed')
    click.echo("="*80)
    return result[0]['summary_text']

@click.command()
@click.option('--url')
@click.option('--file')
def main(url, file):
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r') as f:
            text = f.read()
    else:
        click.echo("Please provide either a URL or a file path.")
        return

    summary = process(text)
    click.echo(summary)