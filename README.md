# Onion Searcher
```
     ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █      ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ ▓█████  ██▀███  
    ▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
    ▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒
    ▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
    ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██░   ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
    ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
      ░ ▒ ▒░ ░ ░░   ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
    ░ ░ ░ ▒     ░   ░ ░  ▒ ░░ ░ ░ ▒     ░   ░ ░    ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░   ░     ░░   ░ 
        ░ ░           ░  ░      ░ ░           ░          ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░   ░  ░   ░     
```

Onion Searcher is a search engine scraper designed to extract `.onion` links from various search engines on the dark web. It checks for Tor connectivity, rotates IPs, applies custom user agents for better anonymity, and categorizes links using keywords.

## Features
- Checks if Tor is connected.
- Performs IP rotation for anonymity.
- Uses custom User-Agent for each request.
- Categorizes extracted links using keyword matching.
- Outputs results in a CSV file, sorted in ascending order of `.onion` links.

## Search Engines added
  ```python
  urls = {
    "Ahmia" : "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion",
    "Torch" : "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion",
    "Notevil" : "http://notevilcdlnwra7bbxio2rnrrpxyecw6dvodqeelvujf66ja3ssbdcid.onion"
}
  ```
## Future Work
- Implement Natural Language Processing (NLP) for better categorization.
- Integrate additional search engines.
- Improve performance and filtering logic.

## Setup Guide
Follow these steps to install and run the scraper:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lakshaytyagi111/onionSearcher.git
    cd onionSearcher
    ```

2. **Install Requirements**:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Start Tor Service**:
    ```bash
    sudo systemctl start tor
    sudo systemctl status tor
    ```
Ensure that tor is installed on your system and its status is active.

4. **Run the Scraper**:
    ```bash
    sudo python3 scrapper.py <search_query>
    ```

5. **View Results**:
    The output will be stored in a CSV file, with onion links sorted in ascending order.

## Notes
- Torch has limited utility as it often provides repeated links, resulting in less effective output.
- Ensure that Tor is running before executing the script.

## Usage Disclaimer

This project, **Onion Searcher**, is intended for **educational and research purposes only**. It is designed to demonstrate how search engines can be used to extract and analyze .onion links for legal investigations, cybersecurity research, and network analysis.

The author does **not condone** or support any illegal activities. Any misuse of this software for unauthorized access, monitoring, or malicious activities is strictly prohibited. The author assumes **no responsibility** for any consequences resulting from the use of this tool.

Please ensure compliance with all **local, state, and international laws** before using this software. Users are responsible for their own actions.

By using this project, you agree to these terms.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
