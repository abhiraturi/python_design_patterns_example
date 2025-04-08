# python_design_patterns_example

design patterns used:
1. Singleton


Directory Structure:

python_design_patterns_example/
├── Process_Data/
│   └── process.py                  # Builder and Filter patterns
│
├── clients/
│   └── clients.py                 # Factory methods for API interaction
│
├── lib/
│   └── logger.py                  # Singleton logger with env-based formatting
│
├── user_and_product_info.py       # Orchestrates Factory client calls
├── main.py                        # Entry point: uses all modules



✅ Design Patterns Used
1. 🔁 Singleton Pattern
File: lib/logger.py
Class: Logger
Purpose: Ensures only one instance of the logger is created, regardless of how many times you try to instantiate it.

Why it's Singleton:

It uses a class-level _instances dictionary.

Uses __new__ to control instantiation.

Shared logger across the app.

python
Copy
Edit
if logger_name not in cls._instances:
    instance = super(Logger, cls).__new__(cls)
    ...
✅ Use Case: Keeps logger configuration consistent throughout the app.

2. 🏭 Factory Pattern
File: user_and_product_info.py (indirect usage), clients/clients.py
How:

Client.user() and Client.products() are factory methods.

They abstract the API call logic for different types of clients.

Why it's Factory:

Instead of instantiating a class per client type, static methods return data from different endpoints (users, products).

Allows centralized control over how clients are used or replaced.

✅ Use Case: Simplifies how different client endpoints are consumed.

3. 🏗️ Builder Pattern
File: Process_Data/process.py
Class: DataExtraction

Why it's Builder:

Constructs a complex dictionary (user_dic) through chained methods (extract_email, extract_username, etc.).

Final build() returns the constructed object.

python
Copy
Edit
data = DataExtraction(item).extract_email().extract_username().build()
✅ Use Case: Cleanly extracts specific fields from large data objects in a customizable manner.

4. 🧹 Filter Pattern (Behavioral Pattern, often implemented ad-hoc)
File: Process_Data/process.py
Class: Filter

Why it's Filter:

A static method that iterates through data and applies filtering logic.

Decouples filtering from extraction or data retrieval.

✅ Use Case: Applies filtering logic without cluttering data handling classes.



python_design_patterns_example/
├── Process_Data/
│   └── process.py                  # Builder and Filter patterns
│
├── clients/
│   └── clients.py                 # Factory methods for API interaction
│
├── lib/
│   └── logger.py                  # Singleton logger with env-based formatting
│
├── user_and_product_info.py       # Orchestrates Factory client calls
├── main.py                        # Entry point: uses all modules
