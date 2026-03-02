# Smart Order Management System

## 1. Real-World Representation of Collections

Order data in this project is modeled as a list of dictionaries, similar to how JSON data is structured in real-world systems.

### List (`orders`)

Stores multiple orders within a single collection.  
In real-world systems, this can be compared to rows retrieved from an “orders” database table.

### Dictionary (`order`)

Represents a single order record using a key-value structure.  
Fields such as `customer`, `items`, `total`, and `is_paid` are accessed by name, which improves readability and structure.

### List (`items`)

Stores the products purchased within a single order in a sequential manner.  
Since the same product can be purchased multiple times, a list structure is appropriate.

---

## 2. Differences Between List, Set, and Tuple

| Feature | List | Tuple | Set |
|----------|------|--------|------|
| Ordered? | Yes | Yes | No |
| Mutable? | Yes | No | Yes |
| Allows duplicates? | Yes | Yes | No |
| Indexed access? | Yes | Yes | No |
| Typical usage | Dynamic data | Immutable data | Unique elements |

---

### Role of Boolean and Conditional Logic in System Design

One of the fundamental questions in an order system is:

> How many orders exist, and what is their payment status?

The payment status is modeled using a Boolean value:

- `True` → Payment completed  
- `False` → Payment pending  

Boolean values are widely used in system design for state management.  
Separating orders as paid or unpaid is critical for order processing and approval workflows.

---

## 3. Data Structures Used in the Project

### List

Orders are stored in a list because:

- Lists preserve order
- They allow dynamic insertion of new records
- They support duplicate entries

---

### Dictionary

Each order is modeled as a dictionary because:

- Fields can be accessed by name
- Data is organized in a meaningful and structured way
- It resembles real-world JSON and database records

---

### Set

Used for customer and product analysis to eliminate duplicate values.

- Automatically removes repeated elements
- Produces unique datasets
- Useful for analytics and aggregation logic

---

### Tuple

For each order, a summary in the format `(customer_name, total_amount)` is created using a tuple.

Tuples are chosen because:

- They are immutable
- They preserve data integrity
- They are ideal for fixed summary structures

---

### Boolean

The payment status of each order is modeled using `True` or `False`.

- Ideal for representing system states
- Drives decision-making logic (`if/else`)
- Controls the order approval process