# Natrec 
 
Natrec is a web application that emulates AI tools including text generation, language translation, creative content writing, and accurate question answering. It is built using the Python Flask framework and provides a user-friendly interface for users to interact with. 
 
## Motivation 
 
The motivation behind Natrec was to create a web application that makes people's lives easier with AI. The AI part of the application was not implemented but instead, Natrec focuses on providing a Minimal Viable Product(MVP) that offers the basic functionality of an AI-powered web application. 

> It was just an idea that I had when I was learning about General Artificial Intelligence(AI) and thought it would be fun to build a AI powered web application.
 
## Features 
 
Natrec offers several pages including the home page, about page, contact page, and blog page, as well as pages for getting started, tutorials, login, signup, logout, and users management. Some of the key features of Natrec include: 
 
- **Text generation:** Natrec can generate text based on user input, making it useful for tasks such as summarizing long documents or generating content for social media. 
 
- **Language translation:** Natrec can translate text between different languages, making it useful for communicating with people who speak different languages. 
 
- **Creative content writing:** Natrec can generate creative content such as slogans or headlines, making it useful for marketing and advertising. 
 
- **Question answering:** Natrec can answer questions based on user input, making it useful for tasks such as customer support or research. 

> **Note:** Realise that none of them were implemented yet.
 
## Getting Started 
 
To get started with Natrec, follow these steps: 
 
1. Clone the repository to your local machine. 
2. Install Python if it is not already installed on your machine. 
3. Install Flask by running the command  pip install flask  in your terminal. 
4. Run the application by running the command  python app.py  in your terminal. 
5. Open your web browser and navigate to  http://localhost:5000 to access the Natrec application. 

There are default users one including username: `admin` and password: `password`. The admin can create new users, delete existing users, and update existing users.

Please note that there is no database which means users are stored in memory. This means that if you restart the application, all the users will be lost. Flask session is used to store the user's login details to allow them to login and logout.
 
## Technologies Used 
 
Natrec is built using the following technologies: 
 
- **Python Flask framework:** Flask is a lightweight web framework that provides tools and libraries for building web applications in Python. 
 
- **Jinja templating engine:** Jinja is a popular templating engine for Python that allows developers to create dynamic HTML pages. 
 
- **Bootstrap 5:** Bootstrap is a popular front-end framework that provides a set of tools and styles for building responsive and mobile-first web pages. 


## Showcase

Here are some images of Natrec's home page and user admin pages:

### Home Page

![Natrec Home Page](/path/to/home-page-image.png)

### User Admin Pages

![Natrec User Admin Pages](/path/to/user-admin-pages-image.png)

Feel free to replace the placeholder images with real images of your choice.
 
## Contributing 
 
If you would like to contribute to Natrec, please feel free to submit a pull request or open an issue on the GitHub repository. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements. 
 
## License 
 
Natrec is licensed under the MIT License. See the LICENSE file for more information.
