TALK SPACE
Visit Talk Space Website

Introduction to TalkSpace
TalkSpace is a social media application designed to provide users with a platform to share their thoughts, connect with others, and engage in meaningful discussions without the fear of judgment. Our app aims to foster a supportive and inclusive online community where users can express themselves freely and connect with like-minded individuals.

Key Features
User Registration and Authentication: Users can create an account securely and log in to access the platform's features.
Post Creation and Sharing: Users can create posts to share their thoughts, ideas, and experiences with the community.
Profile Management: Users have the ability to update their profile information, including their username and email.
Search Functionality: Users can search for other users by username and discover new connections.
User Interaction: Users can engage with posts by liking, commenting, and sharing them.
User Privacy: Our app prioritizes user privacy and provides tools for users to manage their account settings and privacy preferences.
Deployment
The TalkSpace application has been deployed to a live server, allowing users to access the platform from any device with an internet connection. Our deployment ensures a seamless user experience and ensures that users can enjoy the full range of features offered by the app.

Join TalkSpace today and be a part of our vibrant and supportive community!
Architecture
Frontend
HTML/CSS: The frontend of TalkSpace is built using HTML for structure and CSS for styling.
Template Engine: Flask's template engine is used to generate dynamic HTML content by embedding Python code within HTML templates.
Responsive Design: The frontend is designed to be responsive, ensuring a seamless user experience across various devices and screen sizes.
Backend
Flask Framework: TalkSpace is powered by the Flask web framework, which provides tools and libraries for building web applications in Python.
SQLAlchemy: SQLAlchemy is used as the ORM (Object-Relational Mapping) library to interact with the MySQL database. It allows seamless communication between the Python application and the database.
Flask-Bcrypt: Flask-Bcrypt is used for password hashing and verification to enhance security.
Session Management: Flask's session management is utilized to handle user authentication and maintain user sessions.
Routing: Flask's routing mechanism is employed to define endpoints for various functionalities such as user registration, login, profile management, post creation, etc.
Database
MySQL Database: TalkSpace uses a MySQL database to store user information, posts, and other application data.
Installation
To install and run the TalkSpace application, follow these steps:

Clone the Repository: Clone the TalkSpace repository from the source where it's hosted. You can use Git to clone the repository:

bash
Copy code
git clone https://github.com/avd1729/Talk-Space
Install Dependencies: Navigate into the cloned directory and install the required dependencies. You can install them using pip:

bash
Copy code
pip install -r requirements.txt
Set Up the Database: TalkSpace appears to use a MySQL database. Ensure you have MySQL installed and running locally. Create a new MySQL database for the application, and update the SQLALCHEMY_DATABASE_URI in the app.py file to point to your MySQL database.

Run the Application: Once the database is set up and the dependencies are installed, you can run the Flask application. Typically, you'd execute the app.py file:

bash
Copy code
python app.py
This command will start the Flask development server, and your TalkSpace application should be accessible locally.

Access the Application: Open a web browser and navigate to the address where the Flask server is running (usually http://localhost:5000 by default) to access the TalkSpace application.

That's it! You should now have the TalkSpace application up and running locally on your machine.

Usage
Register an Account: If you're a new user, click on the "Register" link on the homepage. Fill in the required information such as username, email, and password, then submit the registration form.
Login: After registering, or if you already have an account, click on the "Login" link and enter your username and password to log into your account.
Create New Post: Once logged in, you can create a new post by clicking on the "Create New Post" link. Enter a title and the content of your post, then submit the form.
Update Profile: You can update your profile information by clicking on the "Update Profile" link. Update your username, email, or any other details as needed, then submit the form to save the changes.
View Public Posts: On the homepage, you can view public posts from all users. These posts include the title, content, and the username of the author.
Search Users: Use the search functionality to find other users by their username. Enter the username you want to search for in the search bar and click "Search" to see the results.
View User Posts: You can view posts from a specific user by clicking on their username or navigating to /user/<username>.
Logout: To log out of your account, simply click on the "Logout" link.
API Documentation
Base URL: The base URL for the TalkSpace API is Home (talk-space-jd1v.onrender.com)

Authentication: The API does not require authentication for public endpoints. However, some endpoints may require user authentication using a JWT token.

Users Endpoints
List of all users
Endpoint: GET /users
Description: Retrieves a list of all users registered in the system.
Response: JSON array containing user objects.
Search by particular user name
Endpoint: GET /users/:name
Description: Searches for users by their username.
Parameters:
name (string): Username to search for.
Response: JSON object containing user information if found, or an empty object if not found.
Posts Endpoints
List of all posts
Endpoint: GET /posts
Description: Retrieves a list of all posts created by users.
Response: JSON array containing post objects.
List all posts by particular user name
Endpoint: GET /users/:name/posts
Description: Retrieves a list of posts created by a specific user.
Parameters:
name (string): Username of the user whose posts to retrieve.
Response: JSON array containing post objects created by the specified user.
