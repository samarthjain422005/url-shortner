# URL Shortener

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Searching Shortened URLs](#searching-shortened-urls)
- [Deployment](#deployment)
- [Learning Takeaways](#learning-takeaways)
- [Resources](#resources)
- [License](#license)

## Introduction

The URL Shortener is a web application that allows users to shorten long URLs into shorter, more manageable links. It provides a convenient way to share long URLs in a concise format.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/samarthjain422005/url-shortener.git
   ```

2. Navigate to the project directory:

   ```
   cd url-shortener
   ```

3. Install the dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask development server:

   ```
   python main.py
   ```

5. Access the URL Shortener in your web browser at `http://localhost:5000`.

## Usage

1. Enter a long URL in the input field on the homepage.
2. Click the "Shorten" button.
3. The shortened URL will be displayed, which you can copy and share.

## Project Details

The URL Shortener is built using the Flask web framework in Python. It utilizes a SQLite database to store the original URLs and their corresponding shortened versions. When a user enters a long URL, the application generates a unique short code and saves the mapping in the database. The short code is then used to redirect users to the original URL when they access the shortened link.

## Searching Shortened URLs

This URL Shortener also provides the ability to search for previously shortened URLs using their aliases. Simply enter the alias in the search bar on the homepage, and if the alias exists, the original URL will be displayed.

## Deployment

The project has been deployed and can be accessed at [https://sammyboy-url-shortner.vercel.app/](https://sammyboy-url-shortner.vercel.app/). Feel free to try it out!

## Learning Takeaways

Throughout the development of this project, I gained the following learning takeaways:

- Understanding the basics of web development using Flask.
- Working with HTML templates to create dynamic web pages.
- Handling form submissions and user input validation.
- Utilizing databases for data storage and retrieval.
- Implementing URL routing and redirection.

## Resources

During the development of this project, I found the following resources helpful:

- [Flask documentation](https://flask.palletsprojects.com/)
- [W3Schools HTML tutorial](https://www.w3schools.com/html/)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.
