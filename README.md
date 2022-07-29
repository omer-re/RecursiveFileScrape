# Recursive File Scraper

A Python script that recursively downloads files from a webpage and links within that page.
Single page downloading and page component filter and other configurations are available.

## Setup

**Source:**

Python 3 is required to run the script.

Clone the repository, enter the directory and run the following line to install the script's dependencies:
```bash
pip install -r requirements.txt
```

**Binary:**

If a binary has been precompiled for your platform, it will be available in the releases section and no further steps are required.

Binaries are generated using Nuitka.

## Usage
Run the relevant file with any additional flags:
```bash
recursivescrape[.py/.exe/Linux64/arm] [flags]
```

The available flags are:

|Flag|Description|Default|
|---|---|---|
|-h --help||
|-c --cookies|Add any cookies that are required to access the webpages in a json format. Example: '{"session":"12kmjyu72yberuykd57"}'|'{}'|
|-u --url|URL to start the scraping from. **REQUIRED**||
|-o --overwrite|Download and overwrite existing files. If not added, files that already exist will be skipped.||
|-v --verbose|Increase output detail. use -vv for even more detail.||
|-r --resume|Resume previous progress from file PROGRESS_FILE, will ignore URL and no-recursion arguments if file is found.||
|--id|Component id that contains the files and following paths, on empty searches the whole page, unrecommended to leave empty.|""|
|-bi --backup-interval|Saves the current progress every BACKUP_INTERVAL pages, 0 will disable automatic backup.|500|
|-f --progress-file|The file to save and load progress with.|"progress.dat"|
|-l --dont-prevent-loops|Save memory by not remembering past pages but increase the chance of checking pages multiple times, do not add if there are any loops in the directory. Changing this flag between resumed runs results in undefined behaviour.||
|-nr --no-recursion|Only download files from the given pages and do not follow links recursively||

|-h, --help|Show the help page of the program and all available flags||
|-u, --url||URL to start from. **REQUIRED**||
|-p, --download-path|Directory to download files to. Will use the current directory by default.||
|-c, --cookies| Cookie values as needed in the json format. Example: '{"session":"12kmjyu72yberuykd57"}'|"{}"|
|--id|Component id that contains the files and following paths. by default will check the whole page.||
|-o, --overwrite|Download and overwrite existing files. If not added, files that already exist will be skipped.|False|
|-r, --resume|Resume previous progress from file PROGRESS_FILE, will ignore url and no-recursion arguments if file is found.|False|
|-bi, --backup-interval|Saves the current progress every BACKUP_INTERVAL pages, 0 will disable automatic backup.|0|
|-f, --progress-file|The file to save and load progress with, relative to the download path.|progress.dat|
|-l, --dont-prevent-loops|Save memory by not remembering past pages but increase the chance of checking pages multiple times, do not add if there are any loops in the directory. Changing this flag between resumed runs results in undefined behaviour.|False|
|-nr, --no-recursion|Only download files from the given url and do not follow links recursively|False|
|-v, --verbose|Increase output detail. use -vv for even more detail.||

## To Do
- Allow method calling to download instead of standalone only. 
- Utilize async to parallel requests and speed up the process.  

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test changes before sending a request.

## License
[MIT](https://choosealicense.com/licenses/mit/)
