Little Lemon 🍋




Little Lemon is a charming neighborhood bistro that serves simple food and classic cocktails in a lively but casual environment. The restaurant features a locally sourced menu with daily specials.

The restaurant is in the process of transition from a one-page website to a database driven web application using the Django framework. Currently, the pages for Home, About and Book are completed.

For the menu page, the owners would like to store the menu information in a database that can be updated as the menu changes seasonally.

Table of Contents
Installation
Commands
Contributing
License
Contact
Installation
To download and set up the project, use the following commands:

# Clone the repository
git clone https://github.com/lkhandelwal559/Little-Lemon.git

# Navigate to the project directory
cd Little-Lemon

# Install dependencies
pip install -r requirements.txt
Running the Project
After cloning the project, open it in your IDE and run the following commands:

# Perform migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Run the server
python3 manage.py runserver

# Create a super user
python3 manage.py createsuperuser

Contact
For any inquiries, please contact Love Khandelwal.
