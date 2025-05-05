# Summarization Command-Line Tool

## Overview

The `summarization-command-tool` is a command-line utility for text summarization using the Hugging Face T5 model. This tool allows users to summarize text content either from a URL or a local file.

## Installation

To set up the tool, follow these steps:

1. Build the project:
    ```bash
    make all
    ```

2. Install the tool in development mode:
    ```bash
    make build
    ```
    or, alternatively, you can use the following command:
    ```bash
    python setup.py develop
    ```

## Usage

Once installed, you can access the summarization tool via the `summarize` command. To view the available options and usage instructions, run:
```bash
summarize --help
``` 
This will display the help message, including all available options and their descriptions.

## Example Usage
To summarize text from a URL, use the following command:
```bash
summarize --url <URL> 
```


To summarize text from a local file, use the following command:
```bash
summarize --file <FILE_PATH> 
```


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
