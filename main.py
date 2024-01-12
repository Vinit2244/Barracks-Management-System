import os
import pymysql
from datetime import datetime

class TextColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ORANGE = '\033[38;5;208m'
    END = '\033[0m'

con = None
cur = None

# NOTES
# Do late fine updation dynamically

# Database credentials
host = "localhost"
user = "root"
password = "vinit123"
db = "Barracks_Brigade"
 
rank_list = ['Field Marshal', 'General', 'Lieutenant General', 'Major General', 'Brigadier', 'Colonel', 'Lieutenant Colonel', 'Major', 'Captain', 'Lieutenant']
month_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
equipment_type_list = ['weapon', 'gear', 'uniform']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Runs the query and returns the list of columns (in order) and the data in the table (in order of tuples), if an error occurs it just displays the error and re run the main funtion
def run_query(query):
    output = None
    column_names = None
    try:
        # Connect to the MySQL database
        conn = pymysql.connect(host=host, user=user, password=password, database=db)
        cursor = conn.cursor()

        # Execute your MySQL query
        cursor.execute(query)
        
        query_type = query.split()[0].lower()
        
        if (query_type == "select"):
            column_names = [col[0] for col in cursor.description]
            output = cursor.fetchall()

        # Commit the changes (if applicable)
        conn.commit()
        conn.close()

    except pymysql.Error as e:
        # Handle the error
        print(f"{TextColors.RED}MySQL error: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    return column_names, output

def clear_screen():
    # Check if the operating system is Windows or Unix-like (Linux, macOS)
    if os.name == 'nt':  # for Windows
        os.system('cls')
    else:  # for Unix-like systems
        os.system('clear')

def main():
    clear_screen()
    print(f'{TextColors.BLUE}Welcome to our Barracks Database!{TextColors.END}')
    print()
    print(TextColors.YELLOW)
    print('Menu')
    print('1. Insert')      # working completely
    print('2. Delete')      # working completely
    print('3. Update')
    print('4. Retrieval')   # working completely
    print('5. Analysis')    # working completely
    print('6. Execute')
    print()
    print('7. Exit')
    print(TextColors.END)
    print()
    choice = input('Enter your choice: ')
    if choice == '1':
        insert_data()
    elif choice == '2':
        delete_data()
    elif choice == '3':
        update_data()
    elif choice == '4':
        retrieve_data()
    elif choice == '5':
        analyse_data()
    elif choice == '6':
        execute_query()
    elif choice == '7':
        print(f"{TextColors.ORANGE}DNA over!{TextColors.END}")
        exit()
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
def retrieve_data():
    clear_screen()
    
    print(TextColors.YELLOW)
    print("Selection")
    print("1. Select all Soldiers working in a unit")
    print("2. Select all Soldiers registered in a mess")
    print("3. Select all Soldiers having a particular rank")
    print("4. Select all Soldiers above a particular age")
    print()
    
    print("Projection")
    print("5. List all equipments issued on a particular date")
    print("6. List the number of soldiers in each sector")
    print()
    
    print("Aggregate")
    print("7. Average salary of soldiers in a barrack")
    print("8. Total number of military equipments in all sectors")
    print()
    
    print("Search")
    print("9. Search for a soldier whose first name starts with certain initials")
    print("10. Search for the sector name starting with some initials")
    print("11. Search in messes for a particular item")
    print(TextColors.END)
    
    print()
    choice = input("Enter your choice: ")
    if choice == '1':
        select_soldiers_in_unit()
    elif choice == '2':
        select_soldiers_in_mess()
    elif choice == '3':
        select_soldiers_with_rank()
    elif choice == '4':
        select_soldiers_above_age()
    elif choice == '5':
        list_equipments_issued_on_date()
    elif choice == '6':
        list_num_of_soldiers_in_each_sector()
    elif choice == '7':
        avg_salary_of_soldiers_in_barrack()
    elif choice == '8':
        total_num_of_equipment_in_all_sectors()
    elif choice == '9':
        search_soldier_by_initials()
    elif choice == '10':
        search_sector_by_initials()
    elif choice == '11':
        search_mess_for_item()
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
def select_soldiers_in_unit():
    clear_screen()
    
    unit_name = input("Enter unit name: ")
    query = f"SELECT Soldier_id, Fname, Lname FROM Soldiers JOIN Units ON Soldiers.Unit_id = Units.Unit_id WHERE Units.Unit_name = '{unit_name}';"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def select_soldiers_in_mess():
    clear_screen()
    
    mess_id = input("Enter Mess ID: ")
    query = f"SELECT Soldier_id, Fname, Lname FROM Soldiers WHERE Mess_id = {mess_id};"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def select_soldiers_with_rank():
    clear_screen()
    
    rank = input("Enter Rank: ")
    if rank not in rank_list:
        print(f"{TextColors.RED}Invalid rank{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
        
    query = f"SELECT Soldier_id, Fname, Lname FROM Soldiers WHERE Soldier_rank = '{rank}';"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def select_soldiers_above_age():
    clear_screen()
    
    age = input("Enter Age: ")
    
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    y = formatted_date.split("-")[0]
    
    query = f"SELECT Soldier_id, Fname, Lname FROM Soldiers WHERE {y} - Birth_year >= {age};"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def list_equipments_issued_on_date():
    clear_screen()
    
    date = input("Enter Date(YYYY-MM-DD): ")
        
    query = f"SELECT M.Equipment_id, M.Type FROM Military_equipment AS M INNER JOIN Issue_log AS I ON M.Equipment_id = I.Equipment_id AND I.Issue_date = '{date}' GROUP BY M.Equipment_id"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def list_num_of_soldiers_in_each_sector():
    clear_screen()
    
    query = f"SELECT Barracks.Sector_id, COUNT(*) AS No_soldiers FROM Soldiers JOIN Barracks ON Soldiers.Barrack_id = Barracks.Barrack_id GROUP BY Barracks.Sector_id"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def avg_salary_of_soldiers_in_barrack():
    clear_screen()
    
    query = f"SELECT Barracks.Barrack_id, AVG(Salary) FROM Soldiers JOIN Barracks ON Soldiers.Barrack_id = Barracks.Barrack_id GROUP BY Barracks.Barrack_id"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def total_num_of_equipment_in_all_sectors():
    clear_screen()
    
    query = f"SELECT B.Sector_id, COUNT(*) AS No_equipments FROM Military_equipment AS M JOIN Soldiers AS S ON M.Soldier_id = S.Soldier_id INNER JOIN Barracks AS B ON S.Barrack_id = B.Barrack_id GROUP BY B.Sector_id"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def search_soldier_by_initials():
    clear_screen()
    
    initials = input("Enter initials: ")
    
    query = f"SELECT Soldiers.Soldier_id, Soldiers.Fname, Soldiers.Lname FROM Soldiers WHERE Fname LIKE '{initials}%'"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def search_sector_by_initials():
    clear_screen()
    
    initials = input("Enter initials: ")
    
    query = f"SELECT * FROM Sectors WHERE Sector_name LIKE '{initials}%'"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def search_mess_for_item():
    clear_screen()
    
    menu_item = input("Enter Menu Item: ")
    
    query = f"SELECT Mess.Mess_name FROM Mess JOIN Menu_items ON Mess.Mess_id = Menu_items.Mess_id WHERE Breakfast_item = '{menu_item}' OR Lunch_item = '{menu_item}' OR Dinner_item = '{menu_item}'"
    
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
def analyse_data():
    clear_screen()
    
    print(TextColors.YELLOW)
    print("1. Name of sectors in decreasing order of strength")
    print("2. Decreasing popularity of messes based on how many soldiers go to mess")
    print("3. Types of complaints and their frequency in decreasing order")
    print(TextColors.END)
    print()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        strength_of_unit()
    elif choice == '2':
        popularity_of_messes()
    elif choice == '3':
        complaints_frequency()
    else:
        print("Invalid choice")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
        
def complaints_frequency():
    clear_screen()
    
    # Executing query to get the data
    col_size = 15
    col_names, output = run_query("SELECT Complaints.Type, COUNT(*) AS No_of_complaints FROM Complaints GROUP BY Complaints.Type ORDER BY No_of_complaints DESC;")
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()

def delete_data():
    clear_screen()
    
    print(TextColors.YELLOW)
    print('Delete Data')
    print('1. Soldier')
    print('2. Equipment')
    print('3. Bunk_Bed')
    print('4. Mess')
    print('5. Training Ground')
    print('6. Barrack')
    print(TextColors.END)
    print()
    choice = input('Enter your choice: ')
    if choice == '1':
        delete_soldier()
    elif choice == '2':
        delete_equipment()
    elif choice == '3':
        delete_bunk_bed()
    elif choice == '4':
        delete_mess()
    elif choice == '5':
        delete_training_ground()
    elif choice == '6':
        delete_barrack()
    else:
        delete_mess()

def delete_barrack():
    barrack_id = input("Enter Barrack ID to delete: ")
    query = f"DELETE FROM Barracks WHERE Barrack_id = {barrack_id};"
    run_query(query)
    print(f"{TextColors.GREEN}Barrack with ID {barrack_id} deleted successfully.{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    input()
    main()
    
def delete_training_ground():
    clear_screen()
    try:
        training_ground_id = input("Enter Training Ground ID to delete: ")
        query = f"DELETE FROM Training_grounds WHERE Training_ground_id = {training_ground_id};"
        run_query(query)
        print(f"{TextColors.GREEN}Training Ground with ID {training_ground_id} deleted successfully.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    except Exception as e:
        print(f"{TextColors.RED}Error deleting training ground: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()

def delete_soldier():
    clear_screen()
    try:
        soldier_id = input("Enter Soldier ID to delete: ")
        query = f"DELETE FROM Soldiers WHERE Soldier_id = {soldier_id};"
        run_query(query)
        print(f"{TextColors.GREEN}Soldier with ID {soldier_id} deleted successfully.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    except Exception as e:
        print(f"{TextColors.RED}Error deleting soldier: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()

def delete_equipment():
    clear_screen()
    try:
        equipment_id = input("Enter Equipment ID to delete: ")
        run_query(f"DELETE FROM Military_equipment WHERE Equipment_id = {equipment_id};")
        print(f"{TextColors.GREEN}Equipment with ID {equipment_id} deleted successfully.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    except Exception as e:
        print(f"{TextColors.RED}Error deleting equipment: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
def delete_bunk_bed():
    clear_screen()
    try:
        Bb_s_no = input("Enter Bunk Bed Serial No. to delete: ")
        query = f"DELETE FROM Bunk_bed WHERE Bb_s_no = {Bb_s_no};"
        run_query(query)
        print(f"{TextColors.GREEN}Bunk Bed with serial no. {Bb_s_no} deleted successfully.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    except Exception as e:
        print(f"{TextColors.RED}Error deleting equipment: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()

def delete_mess():
    clear_screen()
    try:
        mess_id = input("Enter Mess ID to delete: ")
        query = f"DELETE FROM Mess WHERE Mess_id = {mess_id};"
        temp1, temp2 = run_query(query)
        print(f"{TextColors.GREEN}Mess with ID {mess_id} deleted successfully.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    except Exception as e:
        print(f"{TextColors.RED}Error deleting mess: {e}{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

def update_data():
    clear_screen()
    
    print(TextColors.YELLOW)
    print('Update data')
    print('1. Password') # Inside soldier: Credentials, soldier phone numbers
    print('2. Soldier Details')
    print('3. Barrack Details')
    print('4. Update complaints status')
    print('5. Update cleaning schedule')
    print('6. Update Dependent Information')
    print('7. Update Mess Menu')
    print(TextColors.END)
    print()
    choice = input('Enter your choice: ')
    if choice == '1':
        update_credentials()
    elif choice == '2':
        update_soldier_details()
    elif choice == '3':
        update_barrack_details()
    elif choice == '4':
        update_complaint_status()
    elif choice == '5':
        update_cleaning_schedule()
    elif choice == '6':
        update_dependent_info()
    elif choice == '7':
        update_mess_menu()
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
def update_mess_menu():
    clear_screen()
    
    print("What do you want to update?")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print()
    choice = input("Enter your choice: ")
    print()
    if choice == '1':
        mess_id = input("Mess ID: ").strip()
        day = input("Enter Day: ").strip()
        if day not in days_of_week:
            print(f"{TextColors.RED}Invalid day{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
        item = input("Enter new breakfast item: ").strip()
        
        run_query(f"UPDATE Menu_items SET Breakfast_item = '{item}' WHERE Mess_id = {mess_id} AND Week_day = {day};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    elif choice == '2':
        mess_id = input("Mess ID: ").strip()
        day = input("Enter Day: ").strip()
        if day not in days_of_week:
            print(f"{TextColors.RED}Invalid day{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
        item = input("Enter new lunch item: ").strip()
        
        run_query(f"UPDATE Menu_items SET Lunch_item = '{item}' WHERE Mess_id = {mess_id} AND Week_day = {day};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    elif choice == '3':
        mess_id = input("Mess ID: ").strip()
        day = input("Enter Day: ").strip()
        if day not in days_of_week:
            print(f"{TextColors.RED}Invalid day{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
        item = input("Enter new dinner item: ").strip()
        
        run_query(f"UPDATE Menu_items SET Dinner_item = '{item}' WHERE Mess_id = {mess_id} AND Week_day = {day};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

def update_dependent_info():
    clear_screen()
    
    print("What do you want to update?")
    print("1. Name")
    print("2. Relation")
    print("3. Gender")
    print("4. Address")
    print()
    choice = input("Enter your choice: ")
    print()
    if choice == '1':
        soldier_id = input("Soldier ID: ").strip()
        dependent_name = input("Enter new name: ").strip()
        
        run_query(f"UPDATE Dependents SET Dependent_name = '{dependent_name}' WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    elif choice == '2':
        soldier_id = input("Soldier ID: ").strip()
        relation = input("Enter new relation: ").strip()
        
        run_query(f"UPDATE Dependents SET Relation = '{relation}' WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    elif choice == '3':
        soldier_id = input("Soldier ID: ").strip()
        dependent_name = input("Enter dependent name: ").strip()
        gender = input("Enter new gender(M/F): ").strip()
        
        if gender.lower() not in ['m', 'f']:
            print(f"{TextColors.RED}Invalid gender{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
        
        run_query(f"UPDATE Dependents SET gender = '{gender.upper()}' WHERE Soldier_id = {soldier_id} AND Dependent_name = '{dependent_name}';")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    elif choice == '4':
        soldier_id = input("Soldier ID: ").strip()
        dependent_name = input("Enter dependent name: ").strip()
        address = input("Enter new address: ").strip()
        address_parts = address.strip().split(",")
        if (len(address_parts) < 6):
            print(f"{TextColors.RED}Invalid address!{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
            
        house_no, street_no, area, city, state, pin_code = address_parts[0].strip(), address_parts[1].strip(), address_parts[2].strip(), address_parts[3].strip(), address_parts[4].strip(), address_parts[5].strip()
        try:
            if len(pin_code) < 6:
                print(f"{TextColors.RED}Invalid pincode{TextColors.END}")
                print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
                input()
                main()
            pin_code = int(pin_code)
            house_no = int(house_no)
            street_no = int(street_no)
        except:
            print(f"{TextColors.RED}Invalid Address{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
            
        run_query(f"UPDATE Dependents SET House_no = {house_no}, Street_no = {street_no}, Area = '{area}', City = '{city}', State = '{state}', Pin_code = {pin_code} WHERE Soldier_id = {soldier_id} AND Dependent_name = '{dependent_name}';")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

def update_cleaning_schedule():
    clear_screen()
    
    barrack_id = input("Barrack ID: ")
    room_no = input("Room Number: ")
    floor_no = input("Floor Number: ")
    day = input("Day: ")
    if day not in days_of_week:
        print(f"{TextColors.RED}Invalid day{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    run_query(f"UPDATE Rooms SET Cleaning_schedule = '{day}' WHERE Barrack_id = {barrack_id} AND Room_no = {room_no} AND Floor_no = {floor_no};")
    print(f"{TextColors.GREEN}Cleaning schedule updated successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    input()
    main()
    
def update_complaint_status():
    clear_screen()
    
    complaint_no = input("Complaint Number: ")
    complaint_status = input("Complaint Status(pending/solved): ")
    if complaint_status not in ['pending', 'solved']:
        print(f"{TextColors.RED}Invalid complaint status{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    run_query(f"UPDATE Complaints SET Status = '{complaint_status}' WHERE Complaint_no = {complaint_no};")
    print(f"{TextColors.GREEN}Complaint status updated successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()

def update_credentials():
    clear_screen()
    
    # Name
    soldier_id = input("Soldier ID: ")
    soldier_password = input("Password: ")
    
    if len(password)>=8:
        # Password should contain both alphabets and digts and symbols
        if not(password.isalpha()):  # Password should not contain only alphabets
            if not(password.isdigit()):  # Password should not contain only digits
                pass
            else:
                print(f"{TextColors.RED}Password must contain alphabets, digits and special symbols{TextColors.END}")
        else:
            print(f"{TextColors.RED}Password must contain alphabets, digits and special symbols{TextColors.END}")
    else:  # Password length less the 8 characters
        print(f"{TextColors.RED}Password length should be greater than 8 characters{TextColors.END}")
        
    run_query(f"UPDATE Credentials SET Password = '{soldier_password}' WHERE Soldier_id = {soldier_id};")
    print(f"{TextColors.GREEN}Password updated successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()
    
def update_soldier_details():
    clear_screen()
    print('Update data')
    print('1. Contact') # Inside soldier: Credentials, soldier phone numbers
    print('2. Rank')
    print('3. Salary')
    print('4. Salary')

    print()
    choice=input('Enter Choice: ')
    soldier_id = input("Soldier ID: ")
    if choice =='1':
    # Contact
        soldier_contact = input("Phone Number: ")
        if len(soldier_contact) != 10:
            print(f"{TextColors.RED}Invalid phone number. Please enter a 10-digit number.{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
        
        run_query(f"UPDATE Soldier_ph_no SET Phone_no = '{soldier_contact}' WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

    elif choice=='2':
        # Rank
        rank = input("Enter rank of the soldier: ")                  # Rank will be enum (Field Marshal, General, Lieutenant General, Major General, Brigadier, Colonel, Lieutenant Colonel, Major, Captain, Lieutenant)
        if rank not in rank_list:
            print(f"{TextColors.RED}Invalid rank{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
            
        run_query(f"UPDATE Soldiers SET Soldier_rank = '{rank}' WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

    elif choice=='3':
        # Salary
        salary = int(input("Salary: "))

        run_query(f"UPDATE Soldiers SET Salary = '{salary}' WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    elif choice =='4':
        soldier_id = input("Soldier ID: ")
        address = input("Enter new address: ")
        address_parts = address.strip().split(",")
        if (len(address_parts) < 6):
            print(f"{TextColors.RED}Invalid address!{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
        
        house_no, street_no, area, city, state, pin_code = address_parts[0].strip(), address_parts[1].strip(), address_parts[2].strip(), address_parts[3].strip(), address_parts[4].strip(), address_parts[5].strip()
        try:
            if len(pin_code) < 6:
                print(f"{TextColors.RED}Invalid pincode{TextColors.END}")
                print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
                input()
                main()
            pin_code = int(pin_code)
            house_no = int(house_no)
            street_no = int(street_no)
        except:
            print(f"{TextColors.RED}Invalid Address{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
            
        run_query(f"UPDATE Soldiers SET House_no = {house_no}, Street_no = {street_no}, Area = '{area}', City = '{city}', State = '{state}', Pin_code = {pin_code} WHERE Soldier_id = {soldier_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
def update_barrack_details():
    clear_screen()
    
    print('Update data')
    print('1. Last Date Of Maintainance') # Inside soldier: Credentials, soldier phone numbers
    print('2. Landline')
    print()
    choice=input('Enter choice: ')

    barrack_id = input("Barrack ID: ")
    if choice=='1':
        # Last date of Maintainance
        dob = input("Last Date of Maintainance(YYYY-MM-DD): ")  # DOB day/month/year format (day should be int, month should be int, year should be int)
  
        run_query(f"UPDATE Barracks SET Last_maintainance_date= '{dob}' WHERE Barrack_id = {barrack_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

    elif choice=='2':     
        # Landline Number
        landline = input("Phone Number: ") 
        if len(landline) != 10:  
            print(f"{TextColors.RED}Invalid phone number. Please enter a 10-digit number.{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            input()
            main()
            
        run_query(f"UPDATE Barracks SET Landline_no = '{landline}' WHERE Barrack_id = {barrack_id};")
        print(f"{TextColors.GREEN}Updated successfully{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

def insert_data():
    clear_screen()
    
    print(TextColors.YELLOW)
    print('Insert data')
    print('1. Soldier') # Inside soldier: Credentials, soldier phone numbers
    print('2. Barracks')
    print('3. File a Complaint')
    print('4. Mess')
    print('5. Bunk Bed')
    print('6. Military Equipment')
    print('7. Mess Menu item')
    print('8. Training Ground')
    print('9. Security Personnel')
    print(TextColors.END)
    print()
    choice = input('Enter your choice: ')
    if choice == '1':
        insert_soldier_details()
    elif choice == '2':
        insert_barrack_details()
    elif choice == '3':
        file_complaint()
    elif choice == '4':
        insert_mess_details()
    elif choice == '5':
        insert_bunk_bed()
    elif choice == '6':
        insert_equipment()
    elif choice == '7':
        insert_menu_items()
    elif choice == '8':
        insert_training_ground()
    elif choice == '9':
        insert_security_personnel()
    else:
        print(f"{TextColors.RED}Please enter a valid choice{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()

def insert_security_personnel():
    security_prsnl_id = input("Security Personnel ID: ")
    name = input("Name: ")
    date_posted = input("Date Posted(YYYY-MM-DD): ")
    ph_no = input("Phone Number: ")
    if len(ph_no) != 10:
        print(f"{TextColors.RED}Invalid phone number. Please enter a 10-digit number.{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    
    run_query(f"INSERT INTO Security_personnel VALUES({security_prsnl_id}, '{name}', '{date_posted}', '{ph_no}');")
    print(f"{TextColors.GREEN}Security Personnel inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    input()
    main()

def insert_training_ground():
    clear_screen()
    
    ground_id = input("Ground ID: ").strip()
    ground_name = input("Ground Name: ").strip()
    start_time = input("Start Time(HH:MM:SS): ").strip()
    end_time = input("End Time(HH:MM:SS): ").strip()
    ground_type = input("Ground Type: ").strip().lower()
    if ground_type not in ['indoor', 'outdoor']:
        print(f"{TextColors.RED}Invalid ground type{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
    sector_id = input("Sector ID: ").strip()
    
    run_query(f"INSERT INTO Training_grounds VALUES({ground_id}, '{ground_name}', '{start_time}', '{end_time}', '{ground_type}', {sector_id});")
    print(f"{TextColors.GREEN}Training ground inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    input()
    main()
    
def insert_menu_items():
    mess_id = input("Mess ID: ")
    day = input("Day: ")
    if day not in days_of_week:
        print(f"{TextColors.RED}Invalid day{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    breakfast_item = input("Breakfast Item: ")
    lunch_item = input("Lunch Item: ")
    dinner_item = input("Dinner Item: ")
    
    run_query(f"INSERT INTO Menu_items VALUES({mess_id}, '{day}', '{breakfast_item}', '{lunch_item}', '{dinner_item}');")
    print(f"{TextColors.GREEN}Menu item inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    input()
    main()

def insert_soldier_details():
    clear_screen()
    # Soldier Id
    soldier_id = input("Soldier ID: ")
    try:
        soldier_id = int(soldier_id)
    except:
        print(f"{TextColors.RED}Invalid Soldier ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Name
    soldier_name = input("Name: ")  # Contains first name, middle name and last name separated by space
    name_parts = soldier_name.strip().split()
    try:
        first_name, middle_name, last_name = name_parts[0].strip(), name_parts[1].strip(), name_parts[2].strip()
    except:
        print(f"{TextColors.RED}Error occured{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # DOB
    dob = input("Date of Birth: ")  # DOB day/month/year format (day should be int, month should be int, year should be int)
    dob_parts = dob.strip().split("/")
    try:
        day = int(dob_parts[0].strip())
        month = int(dob_parts[1].strip())
        year = int(dob_parts[2].strip())
        if day not in range(1, 32) or month not in range(1, 13) or len(str(year)) != 4:
            print("HERE")
            print(f"{TextColors.RED}Invalid Date of Birth{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
            inp = input()
            main()
        month = month_list[month - 1]
    except:
        print(f"{TextColors.RED}Invalid Date of Birth{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    # Rank
    rank = input("Enter rank of the soldier: ")                  # Rank will be enum (Field Marshal, General, Lieutenant General, Major General, Brigadier, Colonel, Lieutenant Colonel, Major, Captain, Lieutenant)
    if rank not in ['Field Marshal', 'General', 'Lieutenant General', 'Major General', 'Brigadier', 'Colonel', 'Lieutenant Colonel', 'Major', 'Captain', 'Lieutenant']:
        print(f"{TextColors.RED}Invalid rank{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()

    # Address will contain House number, Street, Area, City, State, Pin Code in comma separated
    address = input("Address: ")
    address_parts = address.strip().split(",")
    if (len(address_parts) < 6):
        print(f"{TextColors.RED}Invalid address!{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
        
    house_no, street_no, area, city, state, pin_code = address_parts[0].strip(), address_parts[1].strip(), address_parts[2].strip(), address_parts[3].strip(), address_parts[4].strip(), address_parts[5].strip()
    try:
        if len(pin_code) < 6:
            print(f"{TextColors.RED}Invalid pincode{TextColors.END}")
            print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
            input()
            main()
        pin_code = int(pin_code)
        house_no = int(house_no)
        street_no = int(street_no)
    except:
        print(f"{TextColors.RED}Invalid Address{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()

    # Aadhar Details
    aadhar_no = input("Aadhar Number: ")
    if len(aadhar_no) < 12:
        print(f"{TextColors.RED}Invalid Aadhar Number{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
    try:
        aadhar_no = int(aadhar_no)
    except:
        print(f"{TextColors.RED}Invalid Aadhar Number{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
    
    # Gender
    gender = input("Gender(M/F): ").strip()
    if gender not in ['M', 'F', 'm', 'f']:
        print(f"{TextColors.RED}Invalid gender{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
        
    # Salary
    salary = input("Salary: ")
    try:
        salary = int(salary)
    except:
        print(f"{TextColors.RED}Invalid salary{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
    
    # Unit
    unit = input("Unit name: ").strip()
    # First extract unit id and then insert
    col_names, all_units = run_query("SELECT * FROM Units;")
    unit_id_idx = unit_name_idx = None
    for i in range(len(col_names)):
        if col_names[i] == "Unit_id":
            unit_id_idx = i
        if col_names[i] == "Unit_name":
            unit_name_idx = i
            
    unit_id = None
    for i in range(len(all_units)):
        if all_units[i][unit_name_idx] == unit:
            unit_id = all_units[i][unit_id_idx]
            break
        
    # Barrack id
    barrack_id = input("Barrack id: ")
    # First extract barrack id and check if it exists or not
    col_names, all_barracks = run_query("SELECT Barrack_id FROM Barracks;")
    try:
        if int(barrack_id) in all_barracks:
            pass
    except:
        print(f"{TextColors.RED}Invalid Barrack id - Barrack DNE{TextColors.END}")
        print(f"{TextColors.BLUE}Press Enter to continue.....{TextColors.END}")
        input()
        main()
    
    # Mess
    mess = input("Mess name: ")
    # Find out mess id and check if the mess belongs to the same sector or not (optional do at last) if not then show error
    col_names, all_mess = run_query("SELECT * FROM Mess;")
    mess_id_idx = mess_name_idx = None
    for i in range(len(col_names)):
        if col_names[i] == "Mess_id":
            mess_id_idx = i
        if col_names[i] == "Mess_name":
            mess_name_idx = i
            
    mess_id = None
    for i in range(len(all_mess)):
        if all_mess[i][mess_name_idx] == mess:
            mess_id = all_mess[i][mess_id_idx]
            break
    
    # Check if the mess belongs to the same sector as that of the soldier's barrack
    temp, barrack_sector_id = run_query("SELECT Sector_id FROM Barracks WHERE Barrack_id = " + str(barrack_id) + ";")
    temp, mess_sector_id = run_query("SELECT Sector_id FROM Mess WHERE Mess_id = " + str(mess_id) + ";")
    
    barrack_sector_id = barrack_sector_id[0][0]
    mess_sector_id = mess_sector_id[0][0]
    
    if barrack_sector_id != mess_sector_id:
        print(f"{TextColors.RED}Mess does not belong to the same sector as that of the soldier's barrack{TextColors.END}")
        print(f"{TextColors.BLUE}Press Enter to continue.....{TextColors.END}")
        input()
        main()
    
    # Head Officer id
    officer_id = input("Officer id: ")
    # First extract officer id and check if it exists or not
    col_names, all_soldiers_id = run_query("SELECT Soldier_id FROM Soldiers;")
    all_soldiers_id = [soldier[0] for soldier in all_soldiers_id]
    try:
        if int(officer_id) in all_soldiers_id:
            # Checking if rank is higher or not
            curr_rank = rank
            temp, ranks = run_query(f"SELECT Soldier_rank FROM Soldiers WHERE Soldier_id = {officer_id};")
            officer_rank = ranks[0][0]
            curr_rank_idx = None
            officer_rank_idx = None
            for i in range(len(rank_list)):
                if rank_list[i] == curr_rank:
                    curr_rank_idx = i
                if rank_list[i] == officer_rank:
                    officer_rank_idx = i
                    
            if curr_rank_idx < officer_rank_idx:
                print(f"{TextColors.RED}Rank of the officer should be higher than the soldier{TextColors.END}")
                print(f"{TextColors.BLUE}Press Enter to continue.....{TextColors.END}")
                input()
                main()
        else:
            print(f"{TextColors.RED}Invalid Officer id - Soldier DNE{TextColors.END}")
            print(f"{TextColors.BLUE}Press Enter to continue.....{TextColors.END}")
            input()
            main()
    except:
        print("here")
        print(f"{TextColors.RED}Invalid Officer id - Soldier DNE{TextColors.END}")
        print(f"{TextColors.BLUE}Press Enter to continue.....{TextColors.END}")
        input()
        main()
        
    # Finally insert the data
    run_query(f"INSERT INTO Soldiers VALUES({soldier_id}, '{middle_name}', '{first_name}', '{last_name}', {day}, '{month}', {year}, '{rank}', {house_no}, {street_no}, '{area}', '{city}', '{state}', {pin_code}, {aadhar_no}, '{gender}', {salary}, {unit_id}, {mess_id}, {barrack_id}, {officer_id});")
    print(f"{TextColors.GREEN}Data inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()

def insert_barrack_details():
    clear_screen()

    # Barrack Id
    b_id = input("BarackID: ")

    # Last date of Maintainance
    last_date_of_maintainance = input("Last Date of Maintainance: ")  # DOB day/month/year format (day should be int, month should be int, year should be int)

    # Landline Number
    landline = input("Phone Number: ") 
    if len(landline) != 10:  
        print(f"{TextColors.RED}Invalid phone number. Please enter a 10-digit number.{TextColors.END}")
        print(f"{TextColors.BLUE} Press Enter to continue.....{TextColors.END}")
        input()
        main()
    
    #Security_personal id
    sp_id = input("Security Personal id: ")
        
    # Sector id
    sector_id = input("Sector id: ")

    # Commander id
    commander_id = input("Commander id: ")
    
    # Finally insert the data
    run_query(f"INSERT INTO Barracks VALUES({b_id}, '{last_date_of_maintainance}', {landline}, {sp_id}, {sector_id}, {commander_id});")
    print(f"{TextColors.GREEN}Data inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()

def file_complaint():
    clear_screen()

    # complaint no
    c_no = int(input("Complaint No: "))

    #Complaint Type
    type = input("Enter complaint type: ").strip().lower().capitalize()
    if type not in ['Infrastucture', 'Mess','Officials']:
        print(f"{TextColors.RED}Invalid complaint type{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()

    # Filing Date 
    filing_date = input("Filing Date(YYYY-MM-DD): ")

    # Status
    status= input("Status(pending/solved): ").strip().lower()
    if status not in ['pending', 'solved']:
        print(f"{TextColors.RED}Invalid status{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
        input()
        main()
        
    # Soldier id
    s_id = input("Soldier id: ")

    # Finally insert the data
    run_query(f"INSERT INTO Complaints VALUES({c_no}, '{type}', '{filing_date}', '{status}', {s_id});")
    print(f"{TextColors.GREEN}Data inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()

def insert_mess_details():
    clear_screen()
    
    # Mess Id
    mess_id = input("Mess id: ")
    try:
        mess_id = int(mess_id)
    except:
        print(f"{TextColors.RED}Invalid Mess ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Mess Name
    mess_name = input("Mess name: ")
    
    # Chef Id
    chef_id = input("Chef id: ")
    try:
        chef_id = int(chef_id)
    except:
        print(f"{TextColors.RED}Invalid Chef ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Capacity
    capacity = input("Capacity: ")
    try:
        capacity = int(capacity)
    except:
        print(f"{TextColors.RED}Invalid Capacity{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Sector id
    sector_id = input("Sector id: ")
    try:
        sector_id = int(sector_id)
    except:
        print(f"{TextColors.RED}Invalid Sector ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()

    # Finally insert the data
    run_query(f"INSERT INTO Mess VALUES({mess_id}, '{mess_name}', {chef_id}, {capacity}, {sector_id});")
    print(f"{TextColors.GREEN}Data inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()  

def insert_bunk_bed():
    clear_screen()
    
    # Update both rooms and bunk bed table
    # Barrack Id
    barrack_id = input("Barrack id: ")
    try:
        barrack_id = int(barrack_id)
    except:
        print(f"{TextColors.RED}Invalid Barrack ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Bunk Bed Serial Number
    bb_s_no = input("Bunk Bed Serial Number: ")
    try:
        bb_s_no = int(bb_s_no)
    except:
        print(f"{TextColors.RED}Invalid Bunk Bed Serial Number{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Status
    status = input("Status: ")
    
    if status.lower() not in ['empty', 'occupied']:
        print(f"{TextColors.RED}Invalid status{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Room Number
    room_no = input("Room Number: ")
    try:
        room_no = int(room_no)
    except:
        print(f"{TextColors.RED}Invalid Room Number{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    # Floor Number
    floor_no = input("Floor Number: ")
    try:
        floor_no = int(floor_no)
    except:
        print(f"{TextColors.RED}Invalid Floor Number{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    # Soldier Id
    soldier_id = input("Soldier ID: ")
    try:
        soldier_id = int(soldier_id)
    except:
        print(f"{TextColors.RED}Invalid Soldier Id{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    # Cleaning Schedule
    cleaning_schedule = input("Cleaning Schedule: ").lower().capitalize()
    if cleaning_schedule not in days_of_week:
        print(f"{TextColors.RED}Invalid Cleaning Schedule{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        input()
        main()
        
    # Finally insert the data
    run_query(f"INSERT INTO Bunk_bed VALUES({barrack_id}, {bb_s_no}, '{status}', {room_no}, {floor_no}, {soldier_id});")
    run_query(f"INSERT INTO Rooms VALUES({barrack_id}, {room_no}, {floor_no}, '{cleaning_schedule}');")
    print(f"{TextColors.GREEN}Data inserted successfully{TextColors.END}")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()
    
def insert_equipment():
    clear_screen()
    
    # Equipment Id
    equipment_id = input("Equipment id: ").strip()
    try:
        equipment_id = int(equipment_id)
    except:
        print(f"{TextColors.RED}Invalid Equipment ID{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Equipment Type
    equipment_type = input("Equipment type: ").strip().lower()
    if equipment_type not in equipment_type_list:
        print(f"{TextColors.RED}Invalid Equipment Type{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    # Status
    equipment_status = input("Equipment status: ").strip().lower()
    if equipment_status not in ['issued', 'not issued']:
        print(f"{TextColors.RED}Invalid Equipment Status{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
    
    # Soldier Id
    soldier_id = input("Soldier ID: ")
    try:
        soldier_id = int(soldier_id)
    except:
        print(f"{TextColors.RED}Invalid Soldier Id{TextColors.END}")
        print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
        inp = input()
        main()
        
    late_fine = 200

    # Finally insert the data
    run_query(f"INSERT INTO Military_equipment VALUES({equipment_id}, '{equipment_type}', '{equipment_status}', {late_fine}, {soldier_id});")
    print("Data inserted successfully")
    print(f"{TextColors.BLUE}Press enter to continue......{TextColors.END}")
    inp = input()
    main()
    
def popularity_of_messes():
    clear_screen()
    
    # Executing query to get the data
    col_size = 15
    col_names, output = run_query("SELECT Mess.Mess_id AS Mess_id, Mess_name, COUNT(*) AS Num_of_Soldiers FROM Mess INNER JOIN Soldiers ON Mess.Mess_id = Soldiers.Mess_id GROUP BY Mess.Mess_id ORDER BY Num_of_Soldiers DESC;")
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()

def strength_of_unit():
    clear_screen()
    
    u_role=input('Enter Unit Role: ')
    
    # Executing query to get the data
    col_size = 15
    
    col_names, output = run_query(f"SELECT S.Sector_name, S.Sector_id, count(*) FROM ((Sectors AS S JOIN Barracks AS B ON S.Sector_id = B.Sector_id) JOIN Soldiers AS T on B.Barrack_id = T.Barrack_id JOIN Units as U ON T.Unit_id = U.Unit_id) WHERE U.Role = '{u_role}' GROUP BY S.Sector_id ORDER BY count(*) DESC;")
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()

def execute_query():
    clear_screen()
    
    query = input("Enter query: ")
    col_names, output = run_query(query)
    
    col_size = 15
    for headers in col_names:
        print(headers, end="")
        print(" " * (col_size - len(headers)), end = "")
    print()
    print()
    for row in output:
        for col in row:
            print(col, end="")
            print(" " * (col_size - len(str(col))), end = "")
        print()
    
    print(f"{TextColors.BLUE}Press enter to continue.....{TextColors.END}")
    input()
    main()
    
if __name__ == '__main__':
    main()
