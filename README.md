# Alfaz Book Store - Product Management System

A simple web application built with Flask for managing and displaying a catalog of book products. It features a public-facing product page and an admin dashboard for CRUD (Create, Read, Update, Delete) operations on products.

This project was created by:

  - Muhammad Ferdiansyah
  - Faiz Rayhan Ramadhan
  - Wahyu Dwi Saputra

## ✨ Features

  - **Public View**: A main page that displays all available products to users.
  - **Product Detail Page**: Users can click on a product to see a more detailed view.
  - **Admin Dashboard**: A central place for administrators to view, edit, and delete all products.
  - **Add Product**: A form to add new products with details like name, description, price, stock, and an image.
  - **Edit Product**: Update the information of existing products.
  - **Delete Product**: Remove products from the catalog.
  - **Image Uploads**: Supports uploading product images.

## 🛠️ Technologies Used

  - **Backend**: Python, Flask
  - **Database**: Flask-SQLAlchemy, MySQL (with PyMySQL)
  - **Frontend**: HTML, Bootstrap 5
  - **Server**: Werkzeug (Flask's development server)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have the following installed:

  - Python 3.x
  - pip (Python package installer)
  - A running MySQL server

### Installation & Setup

1.  **Clone the Repository**

    ```bash
    git clone https://your-repository-url.git
    cd your-project-directory
    ```

2.  **Create and Activate a Virtual Environment**

      - **Windows**:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
      - **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Dependencies**
    Install all the required Python packages:

    ```bash
    pip install Flask Flask-SQLAlchemy PyMySQL
    ```

4.  **Database Configuration**

      - Make sure your MySQL server is running.
      - Create a new database named `flask_auth`.
        ```sql
        CREATE DATABASE flask_auth;
        ```
      - The application is configured to connect to a MySQL database at `mysql+pymysql://root:@localhost:3306/flask_auth`. If your database credentials (username, password, host) are different, update the `SQLALCHEMY_DATABASE_URI` in `main.py`:
        ```python
        # in main.py
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://YOUR_USER:YOUR_PASSWORD@YOUR_HOST/flask_auth'
        ```

5.  **Run the Application**
    Execute the `main.py` file to start the Flask development server.

    ```bash
    python main.py
    ```

    The application will be running at `http://127.0.0.1:5000`.

## Usage

  - **Public Product Page**: Navigate to [http://127.0.0.1:5000/](https://www.google.com/search?q=http://127.0.0.1:5000/) to see the list of all products.
  - **Admin Dashboard**: To manage products (add, edit, delete), go to the admin dashboard:
    [http://127.0.0.1:5000/dashboard](http://127.0.0.1:5000/dashboard)
