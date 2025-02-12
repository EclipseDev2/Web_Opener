# Web Opener

Web Opener is a simple Flask-based web application that allows users to select a website (Google, YouTube, Wikipedia, Gmail, Facebook, Instagram) from a dropdown menu and open the selected website in a browser using Selenium WebDriver.

## Features

- Allows the user to choose from a list of predefined websites.
- Opens the selected website in the browser using Selenium WebDriver.
- Built with Flask for the backend and basic HTML, CSS, and JavaScript for the frontend.
- Styled with a responsive, clean layout.

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.x
- Flask
- Selenium
- WebDriver Manager (for managing the correct WebDriver for the browser)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/EclipseDev2/web-opener.git
cd web-opener
```

### 2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

Create a `requirements.txt` file with the following contents:

```
Flask==2.2.2
selenium==4.1.0
webdriver-manager==3.8.0
```

### 4. Run the Flask app:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/` in your browser.

## Usage

1. Open the web application in your browser at `http://127.0.0.1:5000/`.
2. Select a website from the dropdown menu (Google, YouTube, Wikipedia, Gmail, Facebook, Instagram).
3. Click on the "Open Site" button.
4. The selected website will open in your browser.

## Project Structure

```
/your_project_directory
    /app.py           # The main Flask app
    /templates
        /index.html   # HTML form to select the website
    /static
        /style.css    # Custom styles for the app
        /script.js    # Optional JavaScript for interactivity
    /requirements.txt # List of dependencies
    /README.md        # This file
