# Recipe Finder

[![made-with-python](https://img.shields.io/badge/Coded%20with-Python-21496b.svg?style=for-the-badge&logo=Python)](https://www.python.org/)
![Github code size](https://img.shields.io/github/languages/code-size/agustinroviraquezada/recipefinder?style=for-the-badge&logo=Github)
![GitHub license](https://img.shields.io/github/license/agustinroviraquezada/recipefinder?style=for-the-badge&logo=Github)
[![Github Follow](https://img.shields.io/github/followers/agustinroviraquezada?style=social&label=Follow)](https://github.com/agustinroviraquezada)

## Overview

**Recipe Finder** is a web application built using Flask, designed to fetch and display ingredients for various dishes. This project is one of my initial explorations into Flask, focusing on learning how to build web applications with this framework.

## Features

- **Search for Dishes**: Enter a dish name in the search bar to find its ingredients.
- **Dynamic Content**: Fetches data from TheMealDB and Edamam APIs to provide ingredient information.

## Folder Structure

Here is the structure of the project:

recipe_finder/
│
├── app/
│   ├── __init__.py         # Initialize the Flask application
│   ├── main.py             # Contains routes and view functions
│   ├── recipe_service.py   # Logic for interacting with APIs
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css # Styles for the application
│   ├── templates/
│           └──index.html      # Static HTML file
│   
├── run.py                  # Entry point to run the Flask application
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation


## Installation
1. Clone the Repository:
```
git clone https://github.com/YOUR_GITHUB_USERNAME/recipe_finder.git
cd recipe_finder
```
2.Create a Virtual Environment:
```
python -m venv venv
```
3. Activate the Virtual Environment:
```
venv\Scripts\activate
```

4. Install Dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Run the Flask Application:
```
python run.py
```
2. Access the Application: Open your web browser and go to http://127.0.0.1:9000/. You should see a search bar where you can enter the name of a dish.
3. Search for Ingredients: Enter a dish name and click "Search" to find the ingredients.


## Development
For development and contributions, you can make changes to the app/ directory. The static files (CSS, JavaScript, HTML) are served from the static/ directory, while the dynamic logic is handled in main.py and recipe_service.py.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
Your Name - agustinroviraquezada@gmail.com
