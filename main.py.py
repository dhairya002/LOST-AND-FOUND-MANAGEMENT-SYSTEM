import mysql.connector as k
from datetime import date


# ---------------- DATABASE CONNECTION ----------------

try:
    mycon = k.connect(
        host="localhost",
        user="root",
        passwd="YOUR_PASSWORD",
        database="amber"
    )

    cur = mycon.cursor()
    print("Successfully connected to database.")

except k.Error as e:
    print("Database connection failed:", e)
    exit()


# ---------------- ADD RECORD ----------------

def insert_record():
    print("\n--- Add Lost / Found Item ---")
    print("1. Report a Lost Item")
    print("2. Report a Found Item")

    choice = input("Enter choice: ")

    if choice not in ("1", "2"):
        print("Invalid choice.")
        return

    status = "lost" if choice == "1" else "found"

    item_name = input("Enter item name: ")
    description = input("Enter description: ")
    location = input("Enter location: ")
    reporter_name = input("Enter reporter name: ")
    contact = input("Enter contact number: ")

    query = """
        INSERT INTO found
        (item_name, description, location, date_reporting,
         status, reporter_name, contact)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        item_name,
        description,
        location,
        date.today(),
        status,
        reporter_name,
        contact
    )

    try:
        cur.execute(query, values)
        mycon.commit()
        print("\nRecord added successfully!")

    except k.Error as e:
        print("Error while adding record:", e)


# ---------------- SEARCH RECORDS ----------------

def conditional_search():
    print("\n--- Search Records ---")
    print("1. Search by Date")
    print("2. Search by Item Name")
    print("3. Search by Location")

    choice = input("Enter choice: ")

    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return

    if choice == "1":

        search_date = input("Enter date (YYYY-MM-DD): ")

        query = """
            SELECT * FROM found
            WHERE date_reporting = %s
        """

        values = (search_date,)

    elif choice == "2":

        item_name = input("Enter item name: ")

        query = """
            SELECT * FROM found
            WHERE item_name LIKE %s
        """

        values = ("%" + item_name + "%",)

    else:

        location = input("Enter location: ")

        query = """
            SELECT * FROM found
            WHERE location LIKE %s
        """

        values = ("%" + location + "%",)

    try:
        cur.execute(query, values)
        data = cur.fetchall()

        if not data:
            print("\nNo records found.")
            return

        print("\n--- Search Results ---")

        for record in data:
            print(record)

    except k.Error as e:
        print("Error while searching:", e)


# ---------------- DISPLAY RECORDS ----------------

def display_all():
    print("\n--- Display Records ---")
    print("1. Display Lost Items")
    print("2. Display Found Items")
    print("3. Display All Items")

    choice = input("Enter choice: ")

    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return

    if choice == "1":

        query = """
            SELECT * FROM found
            WHERE status = 'lost'
        """

    elif choice == "2":

        query = """
            SELECT * FROM found
            WHERE status = 'found'
        """

    else:

        query = """
            SELECT * FROM found
        """

    try:
        cur.execute(query)
        data = cur.fetchall()

        if not data:
            print("\nNo records found.")
            return

        print("\n--- Records ---")

        for record in data:
            print(record)

    except k.Error as e:
        print("Error while displaying records:", e)


# ---------------- UPDATE STATUS ----------------

def admin_login():

    print("\n--- Admin Login ---")

    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    # Simple login for project demonstration
    if username != "admin" or password != "admin123":
        print("Invalid username or password.")
        return

    print("\nLogin successful!")

    update_status()


def update_status():

    print("\n--- Update Item Status ---")

    item_id = input("Enter Item ID: ")

    print("\n1. Lost")
    print("2. Found")
    print("3. Returned")

    choice = input("Enter new status: ")

    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        return

    if choice == "1":
        status = "lost"

    elif choice == "2":
        status = "found"

    else:
        status = "returned"

    query = """
        UPDATE found
        SET status = %s
        WHERE id = %s
    """

    values = (status, item_id)

    try:
        cur.execute(query, values)

        if cur.rowcount == 0:
            print("\nNo item found with that ID.")
        else:
            mycon.commit()
            print("\nItem status updated successfully!")

    except k.Error as e:
        print("Error while updating status:", e)


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n================================")
        print(" LOST AND FOUND MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Lost / Found Item")
        print("2. Search Records")
        print("3. Display Records")
        print("4. Admin Login")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            insert_record()

        elif choice == "2":
            conditional_search()

        elif choice == "3":
            display_all()

        elif choice == "4":
            admin_login()

        elif choice == "5":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")




main()

mycon.close()
