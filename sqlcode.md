-- Create the USER table
CREATE TABLE "USER" (
    user_ID SERIAL PRIMARY KEY,
    last_name VARCHAR(24) NOT NULL,
    first_name VARCHAR(24) NOT NULL,
    middle_name VARCHAR(24) NOT NULL,
    suffix VARCHAR(10) NOT NULL,
    street VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    province VARCHAR(50) NOT NULL,
    contact_number VARCHAR(15),
    email_address VARCHAR(50),
    facebook_link VARCHAR(50),
    instagram_link VARCHAR(50)
);

-- Create the RESCUES table
CREATE TABLE RESCUES (
    rescue_ID SERIAL PRIMARY KEY,
    rescue_name VARCHAR(144) NOT NULL,
    gender CHAR(1) CHECK (Gender IN ('M', 'F')),
    age INTEGER,
    category VARCHAR(20)
    breed VARCHAR(144),
    Background VARCHAR(1080),
    med_condition VARCHAR(2160)
);

-- Create the STAFF table
CREATE TABLE STAFF (
    staff_ID SERIAL PRIMARY KEY,
    staff_name VARCHAR(240) NOT NULL
);

-- Create the INTERVIEW table
CREATE TABLE INTERVIEW (
    interview_ID SERIAL PRIMARY KEY,
    interview_date DATE,
    staff_ID INTEGER REFERENCES STAFF (staff_ID),
    interview_Score INTEGER
);

-- Create the APPLICATION table
CREATE TABLE APPLICATION (
    application_ID SERIAL PRIMARY KEY,
    user_ID INTEGER REFERENCES "USER" (user_ID),
    rescue_ID INTEGER REFERENCES RESCUES (rescue_ID),
    interview_ID INTEGER REFERENCES INTERVIEW (interview_ID),
    application_details TEXT
);

-- Create the ADOPTION table
CREATE TABLE ADOPTION (
    adoption_ID SERIAL PRIMARY KEY,
    application_ID INTEGER REFERENCES APPLICATION (application_ID)
);
