## Group 4

Mohammed Faiq Shaikh - 100905727, 

Favour Eseagwu - 100892897



Welcome to the Student Management System repository! This application allows you to manage student records using a RESTful API and a user-friendly web interface developed using the Flask framework.

## Features

- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on student records.
- **RESTful API:** Access the API endpoints programmatically for seamless integration with other systems.
- **User Interface:** Interact with the application through an intuitive web interface.
- **Database:** Store student information securely in an SQLite database.
- **Content Negotiation:** Handle JSON and HTML requests for flexible interaction.
- **Validation:** Ensure data integrity with robust validation mechanisms.

## Getting Started

1. **Installation:**

   Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/student-management-system.git
   ```

2. **Setup:**

   - Make sure you have Python and Flask installed.
   - Install dependencies using pip:

     ```
     pip install -r requirements.txt
     ```

   - Initialize the database:

     ```
     python create_db.py
     ```

3. **Running the Application:**

   Run the Flask application:

   ```
   python app.py
   ```

   The application will be accessible at `http://localhost:5000`.

## Usage

- Access the web interface by visiting `http://localhost:5000/ui` in your browser.
- Use the API endpoints for programmatic interaction. Example API requests can be found in the `examples` directory.

## Directory Structure

- `app.py`: The main Flask application.
- `templates/`: Contains HTML templates for the user interface.
- `README.md`: Documentation for the repository.

## Collaborators

This project was developed collaboratively by:
- [Mohammed Faiq Shaikh](https://github.com/mfaiq)
- [Eseagwu Favour](https://github.com/favourcodes)

## Future Improvements

- Implement user authentication for enhanced security.
- Incorporate front-end frameworks for a more interactive interface.
- Provide comprehensive API documentation.
- Dockerize the application for easy deployment.



