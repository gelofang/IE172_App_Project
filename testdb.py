import dbconnect as db

# Function to add rescues to the table
def addRescue(rescue_name, gender, age, breed, background, med_condition, category):
    sqlcode = """
        INSERT INTO rescues (
            rescue_name, gender, age, breed, background, med_condition, category
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = [rescue_name, gender, age, breed, background, med_condition, category]
    db.modifyDB(sqlcode, values)


# Function to retrieve rescues table as a dataframe
def getRescuesTable():
    sqlcode = """
        SELECT rescue_id, rescue_name, gender, age, breed, background, med_condition, category
        FROM rescues
        ORDER BY rescue_name
    """
    values = []
    cols = ['ID', 'Name', 'Gender', 'Age', 'Breed', 'Background', 'Medical Condition', 'Category']
    
    rescues_db = db.getDataFromDB(sqlcode, values, cols)
    return rescues_db


# Function to clear all rescues and reset the table
def clearRescues():
    sqlcode = "TRUNCATE TABLE rescues RESTART IDENTITY CASCADE"
    db.modifyDB(sqlcode)


# Example usage
if __name__ == '__main__':
    # Add sample rescues to the database
    new_rescues = [
        ("Buddy", "M", 5, "Golden Retriever", "Rescued from a shelter", "Healthy", "Dog"),
        ("Mittens", "F", 3, "Domestic Shorthair", "Abandoned by previous owner", "Allergic to certain foods", "Cat"),
        ("Rex", "M", 7, "German Shepherd", "Retired police dog", "Arthritis", "Dog")
    ]

    for rescue in new_rescues:
        addRescue(*rescue)

    # Retrieve and display the rescues table
    print(getRescuesTable())

    # Optionally clear the table
    # clearRescues()
