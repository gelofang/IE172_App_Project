-- Create the Users table
CREATE TABLE Users (
    userID SERIAL PRIMARY KEY,
    lastName VARCHAR(255),
    firstName VARCHAR(255),
    middleName VARCHAR(255),
    suffix VARCHAR(10),
    street VARCHAR(255),
    city VARCHAR(255),
    province VARCHAR(255),
    contactNo VARCHAR(15),
    emailAddress VARCHAR(255) UNIQUE,
    facebookLink VARCHAR(255),
    instagramLink VARCHAR(255),
    birthDate DATE,
    incomeSource VARCHAR(255),
    dwellingType VARCHAR(100),
    dwellingOwn BOOLEAN,
    petsAllowed BOOLEAN,
    password VARCHAR(255)
);

-- Create the Rescue table
CREATE TABLE Rescue (
    rescueID SERIAL PRIMARY KEY,
    rescueName VARCHAR(255),
    category VARCHAR(100),
    gender VARCHAR(10),
    age INTEGER,
    breed VARCHAR(100),
    medCondition TEXT,
    description TEXT,
    rescueStatus VARCHAR(100),
    adoptedTo INTEGER REFERENCES Users(userID)
);

-- Create the Application table
CREATE TABLE Application (
    applicationID SERIAL PRIMARY KEY,
    userID INTEGER REFERENCES Users(userID),
    householdNo INTEGER,
    householdSupport VARCHAR(255),
    rescueID INTEGER REFERENCES Rescue(rescueID),
    ownershipExperience TEXT,
    vetCheck BOOLEAN,
    petsCaredList TEXT,
    petsCaredStatus TEXT,
    foundPawssion VARCHAR(255),
    whyAdopt TEXT,
    idPic VARCHAR(255),
    interviewDate DATE,
    interviewTime TIME,
    approval BOOLEAN,
    adoptedTo INTEGER REFERENCES Rescue(rescueID)
);

-- Create the Adoption table
CREATE TABLE Adoption (
    adoptionID SERIAL PRIMARY KEY,
    userID INTEGER REFERENCES Users(userID),
    rescueID INTEGER REFERENCES Rescue(rescueID),
    applicationID INTEGER REFERENCES Application(applicationID)
);

-- Optional: Insert demo data here

