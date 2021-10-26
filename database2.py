class Patient:

    def __init__(self, input_name, id_no, age):
        self.name = input_name
        self.id_no = id_no
        self.age = age
        self.tests = []

    def __repr__(self):  # representation
        return"{}: {}".format(self.id_no, self.name)

    def is_adult(self):
        if self.age >= 21:
            return True
        else:
            return False


def class_work():
    new_patient = Patient("Ann Ables", 120, 36)
    # run the class to create a new instance of this class
    print(new_patient.id_no)
    print(new_patient.name)
    x = Patient("Bob Boyles", 24, 33)
    # x.name = "Bob Boyles"  # can assign value to properties of instances
    print(x.name)
    print(x)


# if use dictionary as database
def create_database_entry(patient_name, id_no, age):
    # new_patient = [patient_name, id_no, age, []]
    # if use dictionary as database:
    # new_patient = {"name": patient_name, "id_no": id_no,
    #                "age": age, "tests": []}
    # if use Patient class
    new_patient = Patient(patient_name, id_no, age)
    return new_patient


def print_database(db):
    # for patient in db: #patient is automatically an object in list
    #     print(patient) #printing each patient in one line
    #     print(patient[0]) #printing only patient names

    # A better way is:
    # for i in range(len(db)): # i iterates from 0 to len-1, 0123 in this case
    #     print("{} - {}".format(i, db[i]))

    # Or, use enumerate:
    locations = ["Room 1", "Room4", "ER", "Post-Op"]
    # for i, patient in enumerate(db):
    #     print("{} - {} - {}".format(i, patient, locations[i]))

    # Or, zip the two lists:
    for patient, location in zip(db, locations):  # can zip two lists
        print("{} - {}".format(patient, location))

    # Or, can enumerate the zip as well:
    # for i, (patient, location) in enumerate(zip(db, locations)):
    # # can enumerate a zip
        # print("{} - {}".format(i, (patient, location)))


def print_patients_over_age(age, db):  # don't forget to take db as input!!!
    for patient in db:
        # if patient[2] > age:
        if patient["age"] > age:
            print(patient[0])  # prints patient's name, who is older than age


def get_patient(db, id_no):
    patient = db[id_no]
    return patient
    # for patient in db:   #command+1 to comment code block
    #     # if patient[1] == id_no:
    #     if patient["id_no"] == id_no: #after changing list to a dictionary
    #         return patient


def main():
    # db = []
    db = {}  # can create db as a dictionary too!
    x = create_database_entry("Ann Ables", 120, 30)
    # db.append(x)
    db[x["id_no"]] = x  # pull out the id_no as the key of dictionary
    # this step stores the newly created instance to the key of id_no.
    x = create_database_entry("Bob Boyles", 24, 31)
    # db.append(x)
    db[x["id_no"]] = x
    x = create_database_entry("Chris Chou", 33, 33)
    # db.append(x)
    db[x["id_no"]] = x
    x = create_database_entry("David Dinkins", 14, 34)
    # db.append(x)
    db[x["id_no"]] = x
    print(db)

    # y = db[-1] # [-1] takes you the last entry, review video b/f this
    # print(y)
    # print(db[1:3]) #index 1 and 2, separated by comma
    # print(db[1][0]) #print Bob's name

    # print_database(db) #prints all patients, each in one line

    # print_patients_over_age(32, db)

    # found_patient = get_patient(db, 3)
    # print(found_patient)

    patient_id_tested = 24
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    # patient[3].append(test_done)
    # patient["tests"].append(test_done)  # if changed from list to dictionary
    patient.test.append(test_done)
    print(patient.is_adult())
    print(db[24].tests)

    print_database(db)


if __name__ == "__main__":
    main()


# can treat string like a list, Slicing
str = "abcdef"
str[-1]  # 'f'
str[1:3]  # 'bc'
str[-3:-1]  # 'de', include first not include second index
str[-3:]  # 'def', all the way to the end
