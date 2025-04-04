<h1 align='center'><b> Game Ratings </b></h1>

## Overview
This project looks at game data from the IGDB API, with the goal of determining what genres, themes, and keywords are most common in released games, as well as determining which genres, themes, and keywords appear in highly rated games. This will give insight into what trends in video games occur as far as type of gameplay and focus material, as well as providing a look into what types of games players enjoy playing.
## Data
The data in this project comes from the [Internet Game Database]() using API calls to retrieve data regarding video games, their initial release dates and year released, the genres, themes, and keywords the games are tagged with, as well as the total rating and number of ratings the game received. 
## Project Structure

## Features

## Getting Started
To run this project, first you'll need to clone the repository to your local machine.
```bash
git clone https://github.com/jubilbee/Game_Ratings_EDA.git
```
Navigate into the project repository:
```bash
cd Game_Ratings_EDA
```
Set up the virtual environment using the instructions below, ensuring the environment is being made inside the Game_Ratings_EDA folder. 
## Dependencies
To properly run this project, the user will need to have the following: 
* An integrated development environment such as __VS Code__ (Recommended for this project)
* __Python 3.13.1 or higher__ installed on the user's system. 
    * Ensure that Python is located on the system's PATH, allowing Python commands to be executed from the terminal or command prompt. Refer to the official [Python](https://docs.python.org/3/using/windows.html#the-full-installer) documentation for more info.
    * ___For VS Code Users___: Ensure that the Python Extension is installed on VS Code.
* Jupyter Notebook is required for running __Game_Ratings_EDA.ipynb__.
    * ___For VS Code Users___: Install the Jupyter Extension on VS Code.
* __Git Bash__ (Recommended for Windows Users) 
* The API calls in this project requires the user to have a Client ID, Access Token, and token type to make the request to pull the data. More info on how to get these credentials []().

### Modules:
The following modules are used in this project and are included in __requirements.txt:__
* requests 
* time
* dotenv
* pandas
* matplotlib
* seaborn 

Refer to requirements.txt for full list of version-specific dependencies and requirements.
### Virtual Environment Instructions
1. After you have cloned the repo to your machine, navigate to the project folder in GitBash/Terminal.
2. Create a virtual environment in the project folder.
3. Activate the virtual environment.
4. Install the required packages.
5. When you are done working on your repo, deactivate the virtual environment.

__Virtual environment commands__
| Command | Linux/Mac | Git Bash |
| ------- | --------- | ------- |
| Create | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `source venv/Scripts/activate` |
| Install | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Deactivate | `deactivate` | `deactivate` |

__Note for VS Code Users__:

If you're using VS Code to run the Jupyter Notebook or Python script, ensure that the virtual environment(```venv```) is selected as the kernel. This is necessary for the modules installed from __requirements.txt__ to be active when running the project.
* To select the kernel, open the __Command Palette__ (``Ctrl+Shift+P`` or ``Cmd+Shift+P`` on Mac) and search for __"Python: Select Interpreter"__. Choose the one for the virtual environment (``venv``).


### Running the Project
This repository makes API calls to the [IGDB API](). For security, the user will have to set up a .env file with the necessary credentials to run this project.



## Credits
__IGDB API Data__

This project integrates with the IGDB API to fetch game-related data. Any data derived from the IGDB API is governed by the [Twitch Developer Services Agreement](https://www.twitch.tv/p/legal/developer-agreement/). Users of this project must adhere to the terms outlined in Twitch’s Agreement, which restricts redistribution and usage of Linked User Data and Aggregate Data.

By using this project, you acknowledge and agree to comply with the Twitch Developer Services Agreement when interacting with IGDB data.
## Licenses 
Project Code
This project is licensed under the MIT License, which allows anyone to freely use, modify, and distribute the code. You can find the full text of the license in the ```License``` file included with this repository.
