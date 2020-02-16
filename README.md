# raid-finder-bot

## Installation

### Pre-requisites

Before installing this bot you will need the following installed:
- **Git** - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- **Python 3** - https://realpython.com/installing-python/

### Clone The Bot

To check out this bot to your local machine, do the following in your terminal / PowerShell:

```bash
git clone https://github.com/cottonmalone/raid-finder-bot <path to install dir>
```

### Install Dependencies

First `cd` into the project folder, create a virtual environment for this
project:
   
```bash
python3 -m venv .venv/raid-finder
```

The virtual environment will create a local python environment that we will
use to run the both with all the libraries required installed.

To activate the current environment on **Linux / Mac** type:
```bash
source .venv/raid-finder/bin/activate
```
or if you are on **Windows**:
```batch
.venv\raid-finder\Scripts\activate.bat
```

Now we can install the project dependencies:
   
```bash
pip install -r requirements.txt
```

### Running The Bot

Make sure that the python environment that we created above is currently
active, and if not activate it.

To run the bot, type:

```bash
python -m raid-finder
```

