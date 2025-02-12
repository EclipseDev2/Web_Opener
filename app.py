from flask import Flask, render_template, request
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import threading

app = Flask(__name__)

# Map input to website URLs
def get_website_url(choice):
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'wikipedia': 'https://www.wikipedia.org',
        'gmail': 'https://mail.google.com',
        'facebook': 'https://www.facebook.com',
        'instagram': 'https://www.instagram.com',
    }
    return websites.get(choice.lower(), None)

# Route to show the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and open the website
@app.route('/open_site', methods=['POST'])
def open_site():
    site_choice = request.form['site']
    url = get_website_url(site_choice)

    if url:
        # Set up Chrome options
        options = Options()
        options.headless = False  # Set to True if you want the browser to run in the background

        # Use WebDriver Manager to get the correct chromedriver
        service = Service(ChromeDriverManager().install())

        # Function to open the browser in a separate thread to prevent blocking the Flask app
        def open_browser():
            browser = webdriver.Chrome(service=service, options=options)
            browser.get(url)

        # Start the browser opening in a separate thread
        threading.Thread(target=open_browser).start()

        return render_template('index.html', message=f"Opening {url} in the browser...")

    else:
        return render_template('index.html', message="Invalid choice. Please select a valid site.")

if __name__ == '__main__':
    app.run(debug=True)
