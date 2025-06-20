# KS-Python
Team-A6 | Hotel Reservation System

## Author

Kendric ScolesFHNW - Bachelor in Business Artificial IntelligenceCourse: Anwendungsentwicklung mit Python



## Ressourcen

https://deepnote.com/workspace/Fachhochschule-Nordwestschweiz-Bachelor-Business-AI-8a7f9eed-981d-4902-9a28-e7a9a4e7820c/project/AnwendungsentwicklungmitPythonScolesLardinois-Duplicate-87d0d38b-da6f-4a15-8815-f6371a6d7983/notebook/Notebook-1-08f61a8664af47b4b24dfbb243c4cea2

📚 Project Overview

The goal of this project was to develop a fully functional hotel reservation system using Python and SQLite. The system is designed to meet the core functional needs of a hotel business: allowing guests to search for hotels and available rooms, create bookings, receive invoices, and cancel bookings. Furthermore, the system enables administrators to manage hotel data (add, update, delete hotels).

I adopted a clean 4-layer architecture to ensure modularity, maintainability, and testability, and followed a step-by-step user-story-driven development process.

🔹 Step-by-Step Development Process

1. Initial Planning

Defined the core functionalities needed by both guests and hotel admins

Designed a class diagram in Visual Paradigm with all required entities and relationships

2. Project Structure Setup

Created a GitHub repository (Scoles_Python)

Organized code into subfolders:

model/: Data models for Hotel, Room, Guest, etc.

data_access/: DAL files with SQL logic

business_logic/: Business functionality split by user story

database/: SQLite file used for data persistence

3. Database Design & Setup

The database schema was provided by the course instructors and served as the foundation for the project. With the exception of the room_facilities table—which was intentionally excluded due to its irrelevance to the defined user stories—no structural changes were made to the database. All development was carried out using the original schema.

4. Model Layer Development (model/)

Wrote one Python class per entity (e.g. Hotel, Room, Guest, Booking...)

Added full validation, type safety, private attributes, property decorators

Each class has from_row(), to_dict(), and __repr__() methods

Example:

class Room:
    def __init__(...):
        ...
    def to_dict(self): ...
    def from_row(cls, row): ...

5. Data Access Layer (data_access/)

Created a base class BaseDataAccess to handle DB connection, cursor management, error handling

For each entity, a matching DAL class was created (e.g. HotelDataAccess, BookingDataAccess, etc.)

Each DAL class supports:

read_by_id()

read_all()

create_*()

update_*()

delete_*()

Special care taken to avoid SQL injection (parameterized queries)

6. Business Logic Layer (business_logic/)

One logic file per user story

Examples:

hotel_search_logic.py: filtering by city, stars, availability

invoice_logic.py: creating and displaying invoices

booking_cancelation_logic.py: canceling a booking by setting is_cancelled = 1

7. User Story Implementation

Each story was implemented in the logic layer and tested through notebook interfaces. Detailed below:

User Stories Implementation

✅ User Story 1: Hotel Search

"As a guest, I want to search for hotels by city, stars, and availability."

Combined filters: city (case insensitive), star rating, guest capacity, and availability

Business logic: hotel_search_logic.py

DAL: HotelDataAccess, RoomDataAccess, RoomTypeDataAccess

Output: list of hotels with address and star rating

✅ User Story 2: Room Details

"As a guest, I want to view room types and pricing before booking."

Room type and max guest info is retrieved via RoomTypeDataAccess

Rooms filtered for selected date range

Prices per night included

Business logic: room_availability_logic.py

✅ User Story 3: Admin Hotel Management

"As an admin, I want to be able to add, edit, and delete hotels."

CRUD methods implemented in HotelDataAccess

Logic includes:

create_hotel() with address ID

update_hotel_name()

update_hotel_stars()

delete_hotel_by_id()

✅ User Story 4: Room Booking

"As a guest, I want to book a room for my stay."

Checks if the room is free between check_in and check_out

Adds new entry to Booking table

Total amount stored

Booking model tracks guest, room, dates, and price

✅ User Story 5: Invoice Generation

"As a guest, I want to receive an invoice after my stay."

Invoice created after booking with create_invoice()

Issue date retrieved from database (issue_date field)

Bug fixed: removed detect_types=sqlite3.PARSE_DECLTYPES to avoid ValueError

Output: printable invoice with booking info, guest, room, total, and date

✅ User Story 6: Cancel Booking

"As a guest, I want to cancel a booking if my plans change."

Cancel logic sets is_cancelled = 1

SQL logic handled in booking_DAL.py

Business logic in booking_cancelation_logic.py

Prevents cancelled bookings from blocking future availability

❌ Troubleshooting & Lessons Learned

Byte String Errors

Problem: b'2025-06-20 14:34:14' caused ValueError

Fix: .decode("utf-8") used in model classes to convert bytes to strings

SQLite Date Casting Errors

Problem: detect_types=sqlite3.PARSE_DECLTYPES forced SQLite to cast timestamps as date

Fix: Removed this option from _connect() in BaseDataAccess

Deepnote & Import Paths

Problem: ModuleNotFoundError in Deepnote due to relative imports

Fix: sys.path.append("/root/work/Scoles_Python") added in every test cell

Model-DAL Compatibility

Models used from_row() and to_dict() to cleanly map to SQL rows

Made logic layer much easier to test and reuse

🎯 Conclusion

This project was an in-depth introduction to real-world software architecture. The layered structure, combined with user-story-driven planning, ensured clarity and maintainability. Working through real bugs (like SQLite datetime parsing) also built deep debugging experience.

🌐 Future Improvements

Add user login and authentication

UI frontend with Flask, Django, or Streamlit

Export invoices as PDF

Track invoice payment status

Admin dashboard to show real-time room availability and revenue

