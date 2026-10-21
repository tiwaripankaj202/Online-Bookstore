# Test Cases for Online Bookstore Management System

| Test Case ID | Test Description | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-01 | Customer registration | Valid name, email, password, phone, address | Account is created successfully |  |  |
| TC-02 | Customer login | Valid email and password | User is logged in and redirected |  |  |
| TC-03 | Invalid login | Wrong email or wrong password | Login fails with error message |  |  |
| TC-04 | Book search | Search term: "Python" | Matching books are shown |  |  |
| TC-05 | Add to cart | Select a valid book and quantity | Item is added to cart |  |  |
| TC-06 | Update cart | Change quantity value | Cart quantity updates |  |  |
| TC-07 | Remove from cart | Remove one book | Item is removed from cart |  |  |
| TC-08 | Checkout | Valid cart with items | Order confirmation page is shown |  |  |
| TC-09 | Insufficient stock | Quantity exceeds stock | Error message shown |  |  |
| TC-10 | Order creation | Place order successfully | New order appears in order history |  |  |
| TC-11 | Order history | View customer orders | Orders are displayed |  |  |
| TC-12 | Admin login | Valid admin username and password | Admin dashboard opens |  |  |
| TC-13 | Add book | New valid book details | Book appears in admin list |  |  |
| TC-14 | Update book | Existing book modified | Book details update |  |  |
| TC-15 | Delete book | Delete a valid book | Book removed from list |  |  |
| TC-16 | Update order status | Change status to Shipped | Status updates successfully |  |  |
| TC-17 | Sales report | Open admin reports page | Summary metrics are displayed |  |  |
