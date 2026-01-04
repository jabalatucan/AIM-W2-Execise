import numpy as np
import pandas as pd
import os

# Function to collect user data
def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    birthday = input("Enter your birthday (YYYY-MM-DD): ")
    height = input("Enter your height (in cm): ")
    weight = input("Enter your weight (in kg): ")

    # Store data in a NumPy array
    user_data = np.array([[name, age, birthday, height, weight]])
    return user_data

# Function to save data to CSV
def save_to_csv(data, filename='user_data.csv'):
    df = pd.DataFrame(data, columns=['Name', 'Age', 'Birthday', 'Height (cm)', 'Weight (kg)'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Function to read existing CSV file
def read_csv(filename='user_data.csv'):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print("\nExisting Data:")
        print(df)
    else:
        print("No existing CSV file found.")

# Function to edit existing CSV file: add, edit, or delete rows
def edit_csv(filename='user_data.csv'):
    if os.path.exists(filename):
        df = pd.read_csv(filename)
        print("Current Data:")
        print(df)

        while True:
            print("\nEdit Options:")
            print("1. Add Row")
            print("2. Edit Row")
            print("3. Delete Row")
            print("4. Go Back")

            edit_choice = input("Select an option (1-4): ")

            if edit_choice == '1':
                new_data = collect_user_data()
                new_df = pd.DataFrame(new_data, columns=df.columns)
                df = pd.concat([df, new_df], ignore_index=True)  # Append new data
                save_to_csv(df, filename)
            elif edit_choice == '2':
                index_to_edit = int(input("Enter the index of the entry you want to edit (0 for the first entry): "))
                if 0 <= index_to_edit < len(df):
                    df.at[index_to_edit, 'Name'] = input("Edit Name: ")
                    df.at[index_to_edit, 'Age'] = input("Edit Age: ")
                    df.at[index_to_edit, 'Birthday'] = input("Edit Birthday (YYYY-MM-DD): ")
                    df.at[index_to_edit, 'Height (cm)'] = input("Edit Height (in cm): ")
                    df.at[index_to_edit, 'Weight (kg)'] = input("Edit Weight (in kg): ")

                    # Save changes back to the CSV file
                    save_to_csv(df, filename)
                else:
                    print("Invalid index.")
            elif edit_choice == '3':
                index_to_delete = int(input("Enter the index of the entry you want to delete: "))
                if 0 <= index_to_delete < len(df):
                    df = df.drop(index_to_delete).reset_index(drop=True)
                    save_to_csv(df, filename)
                else:
                    print("Invalid index.")
            elif edit_choice == '4':
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("No existing CSV file found.")

# Function to delete a CSV file
def delete_csv(filename='user_data.csv'):
    if os.path.exists(filename):
        os.remove(filename)
        print("CSV file deleted successfully.")
    else:
        print("No existing CSV file found.")

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Read existing .csv file")
        print("2. Create a new file")
        print("3. Edit existing .csv file")
        print("4. Delete .csv file")
        print("5. Exit")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            read_csv('user_data.csv')
        elif choice == '2':
            all_user_data = np.empty((0, 5), dtype=object)  # Initialize an empty numpy array
            while True:
                user_data = collect_user_data()
                all_user_data = np.vstack([all_user_data, user_data])  # Append new data

                # Ask user if they want to add more data
                continue_input = input("Do you want to add another entry? (yes/no): ").strip().lower()
                if continue_input != 'yes':
                    break

            # Save all collected data to CSV
            save_to_csv(all_user_data, filename='user_data.csv')
        elif choice == '3':
            edit_csv('user_data.csv')
        elif choice == '4':
            delete_csv('user_data.csv')
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()