# Receipt_Tracker
Purpose of Application: Vendors across Canada have different date formats on their receipts (i.e., MM/DD/YY , DD/MM/YY, or YY/MM/DD). This is confusing when completing tax documents, especially for accounting firms, and can often result in guess-work. This application is tied to a database that stores receipt/invoice date formats so that individuals/businesses can look up vendor names and make more educated guesses when completing tax documents.


Warnings / Dependencies:  
dependencies: sqlalchemy, pillow (PIL) 

run : 
-m pip install --upgrade Pillow  
pip SQLAlchemy

Warnings:
- Before running the program, download DB Browser for SQLite and open vendors.sqlite with it.
- vendors.sqlite must be in the same directory as main.py - main.py does not initialize a new database, only uses an existing database with a specific format.
- Currently the database only has one entry, but can be populated through application.
- Make sure sqlite database is closed before using the program. The program cannot use the database if someone is looking/editing it.
- Always ensure there is at least one entry in the database. When you are deleting an entry, make sure the database is populated with at least another entry.
- Do not enter data directly into the database (use program). Wrongly formatted data could cause the receipt program to crash, or could cause the program to not display data properly. 

How to Use: Information in "guide for receipt program.pdf" stored in repository.
