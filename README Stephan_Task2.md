# OIBSIP
                                                                        BMI CALCULATOR
                                                                        
Project Overview
This BMI Calculator is a Python-based desktop application developed as part of the Oasis Infobyte Python Programming Internship. The project helps users calculate their Body Mass Index (BMI), classify health status, store records in a PostgreSQL database, and analyze BMI trends through graphical visualization.
This project demonstrates the practical application of Python programming, database management, graphical user interface development, data visualization, and problem-solving techniques.
Objectives
1.	Calculate BMI using standard BMI formula.
2.	Categorize BMI according to health standards.
3.	Store user records securely in PostgreSQL.
4.	Display historical BMI records.
5.	Visualize BMI trends using graphs.
6.	Provide a user-friendly graphical interface.
Features:-
BMI Calculation-Users can enter their weight and height to calculate their BMI instantly.’
Health Classification- The application automatically categorizes BMI values into:
1.	Underweight
2.	Normal Weight
3.	Overweight
4.	Obese
PostgreSQL Database Integration-All user records are stored in a PostgreSQL database for future reference and analysis.
Historical Record Viewing-Users can view previously saved BMI records through an integrated history table.
BMI Trend Analysis-The application generates graphical BMI trend reports using Matplotlib.
User-Friendly Interface-The GUI is designed using Tkinter to provide an intuitive and responsive user experience.
Input Validation-The application validates user inputs and prevents invalid values from being processed.
Error Handling-Proper exception handling is implemented to improve reliability and prevent application crashes.
Database Structure:-Table name is (bmi_records)
Column      Data Type
Id	        SERIAL PRIMARY KEY
Name	      VARCHAR(100)
Weight	    REAL
Height	    REAL
Bmi	        REAL
Category	  VARCHAR(50)
record_date	TIMESTAMP
BMI Formula:-
BMI is calculated using:
BMI = Weight (kg) / Height² (m²)
BMI Categories:-BMI Range	Category are as given below
Less than 18.5:-	Underweight
18.5 - 24.9:	-   Normal Weight
25.0 - 29.9:   -	Overweight
30 and above: - 	Obese
Creative Elements:-
  1.	Developed an interactive GUI using Tkinter.
  2.	Implemented PostgreSQL database storage for persistent record management.
  3.	Added historical record tracking.
  4.	Created BMI trend visualization using graphs.
  5.	Improved usability through organized layout and user-friendly controls.
Problem-Solving:-
  1.	Implemented input validation to prevent incorrect data entry.
  2.	Used exception handling to manage runtime and database errors.
  3.	Solved long-term data storage requirements using PostgreSQL.
  4.	Enabled users to monitor health progress over time through trend analysis.
  5.	Automated BMI categorization based on international standards.
Project Workflow:-
  1.	User enters name, weight, and height.
  2.	Application validates the input.
  3.	BMI is calculated.
  4.	BMI category is determined.
  5.	Data is stored in PostgreSQL.
  6.	Historical records are displayed.
  7.	BMI trends can be visualized through graphs.
  8.	Conclusion:-
  9. In conclusion this Project First takes the data from user Name, weight and Height, then it calculates the it using the formula given of BMI after that the result is compared to differnt identify if the peron is obese, normal, underweight and Overweight after it is done we could genarte a graph by the help of python library matplotlib and the result is displayed and saved in the database table bmi_records and displayed in the screen.

