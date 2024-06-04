# Final Semester Project: Generative AI themed Chatbot

**Author:** Deva Manikanta (BCA Program)

This project showcases a generative AI themed chatbot application built using Chatterbot, Flask, and a dynamic HTML/CSS interface. It leverages the Gemini API to enhance the chatbot's responsiveness and interactivity.

## Project Overview

* **Chatbot Engine:** I have used Chatterbot framework, where it provides the core functionalities for building the conversational AI.
* **Web Framework:** For the design of web interfaces I have used Flask framework which facilitates the creation of a web-based interfaces with user interaction and the chatbot.
* **API Integration:** To add more spice to the my Vortex, I also added the Gemini API, where this integration empowered the chatbot to access and process external information, enriching its responses.
* **User Interface:** I have created an interactive HTML and CSS interface that provides a user-friendly platform for engaging with the chatbot.

## Key Features

* **Conversational AI:** The chatbot interacts with users in a natural, text-based manner.
* **API Integration:** Access to external information expands the chatbot's knowledge base (limited to SEP-2021) and potential responses.
* **Interactive Interface:** The HTML/CSS interface enables users to conveniently interact with the chatbot.


**Documentations That I have reffered:**

* Chatterbot library (https://pypi.org/project/ChatterBot/)
* Flask library (https://pypi.org/project/Flask/)
* Additional libraries as needed (e.g., Gemini API client library)

**Installation:**

1. Clone or download the project repository.
2. Install required Python libraries using `pip install -r requirements.txt` (if a requirements.txt file exists).

**Run the Application:**

1. Navigate to the project directory in your terminal.
2. Start the Flask development server: `flask run`
3. Access the application in your web browser by visiting `http://127.0.0.1:5000/` (or the specified port)

## How It Works

* The Chatterbot framework handles the core conversation logic, including pattern matching and response generation.
* Flask powers the web server, enabling users to interact with the chatbot through the interface.
* The Gemini API integration (if applicable) allows the chatbot to retrieve information from external sources and incorporate it into its responses.
* The HTML and CSS interface presents a user-friendly platform for interacting with the chatbot via text input and output.

## Further Development

* Train the chatbot on more extensive datasets to enhance its conversational abilities.
* Integrate additional APIs for a wider range of information access.
* Implement natural language processing (NLP) techniques for more sophisticated language understanding.
* Improve the user interface's design and functionality.
