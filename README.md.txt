# Lost and Found Management System 🔎

A simple **Lost and Found Management System** built using **Python and MySQL** to keep track of items that have been lost or found.

I created this project to practice working with databases in Python and to understand how a real-world problem can be converted into a small, functional software system.

## 📌 Problem

In schools and other organizations, lost items are often reported informally, which can make it difficult to keep track of them or find the owner.

This project provides a simple way to record lost and found items in a MySQL database and search through the records when needed.

## 💡 Solution

The system stores information such as:

* Item name
* Description
* Location
* Date of reporting
* Lost/Found status
* Reporter's name
* Contact information

The stored records can then be searched and displayed using different criteria.

## ✨ Features

* 📝 Add lost item records
* 🔎 Add found item records
* 📅 Search records by date
* 📦 Search records by item name
* 📍 Search records by location
* 📋 Display stored records
* 🔄 Update the status of an item
* 🗄️ Store data using MySQL
* 🐍 Python-based database interaction

## 🛠️ Technologies Used

* **Python**
* **MySQL**
* **mysql-connector-python**

## 🧠 What I Learned

While building this project, I got practical experience with:

* Connecting Python applications with MySQL
* Creating and executing SQL queries from Python
* Inserting and retrieving database records
* Using functions to organize a Python program
* Searching records using different conditions
* Updating database records
* Working with dates in Python
* Designing a basic database-driven application

## ⚙️ How It Works

The basic workflow is:

```text
User
  ↓
Python Program
  ↓
User enters item details
  ↓
Python processes the information
  ↓
MySQL Database
  ↓
Records can be searched / displayed / updated
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Lost-and-Found-Management-System.git
```

### 2. Install the required package

```bash
pip install mysql-connector-python
```

### 3. Create the MySQL database

Create a database and the required table in MySQL.

Example:

```sql
CREATE DATABASE lost_and_found;
USE lost_and_found;

CREATE TABLE found (
    item_name VARCHAR(100),
    Description VARCHAR(255),
    Location VARCHAR(100),
    Date_reporting DATE,
    status VARCHAR(20),
    Reporter_name VARCHAR(100),
    Contact VARCHAR(20)
);
```

### 4. Configure the database connection

Update the database connection in the Python file with your own MySQL username, password and database name.

**Do not upload your actual database password to GitHub.**

### 5. Run the program

```bash
python main.py
```

## 📷 Screenshots

Screenshots of the program and database output can be added here.

## 🔮 Future Improvements

Some improvements I would like to make in the future:

* Add a proper menu-driven interface
* Improve input validation
* Use parameterized SQL queries
* Add unique IDs for every item
* Add separate admin authentication
* Add an option to mark an item as returned
* Build a GUI version
* Add better error handling
* Improve the database structure
* Add automatic matching between lost and found items

## 👨‍💻 About the Project

This project was developed as a learning project to explore **Python, SQL and database management** through a practical real-world use case.

It is a work in progress, and there are several areas where the system can be improved as I continue learning.

---

⭐ If you find this project useful, feel free to explore the code and suggest improvements.
