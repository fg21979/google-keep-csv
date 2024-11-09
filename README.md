# Google Keep Scraper
The script has been updated to handle JSON files directly from the Google Keep export. There are now two script versions:
	•	keep.py for basic exports
	•	keep-url.py for exporting notes with URL extraction from textContent

Credit to Joe Contini jcontini/google-keep-csv for the original code inspiration.

## Install
1. Clone or download this repository
1. Open a terminal to the repository folder (`google-keep-scraper`)
1. Run `pipenv install` to install dependencies

## Import Keep Archive
First we need to download all the Keep files through Google Takeout.
1. Go to [Google Takeout](https://takeout.google.com/settings/takeout)
1. Make sure the 'Keep' checkbox is selected (you can deselect all others)
1. When archive is ready, download and unzip it.
1. Open the Takeout folder, and move the Keep folder into this repo folder so it’s alongside keep.py and keep-url.py

## Run
Run pipenv shell to ensure dependencies are loaded.
1. Run python keep-url.py.
1. This will create a CSV with an additional column url, which contains the first URL found in the textContent if any.

All of your Keep notes will be exported to CSV files in the same folder as the script.

## Troubleshooting
If you get an error about a missing dependency, be sure to run `pipenv install` prior to running the script so that it can download the dependencies needed.
