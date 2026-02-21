Basics of HTTP/HTTPS
1️⃣ Differences Between HTTP and HTTPS
What is HTTP?

HTTP (Hypertext Transfer Protocol) is the foundation of communication on the web. It allows clients (such as web browsers) to send requests to servers and receive responses. However, HTTP does not encrypt the transmitted data.

What is HTTPS?

HTTPS (Hypertext Transfer Protocol Secure) is the secure version of HTTP. It uses SSL/TLS encryption to protect the communication between client and server. The "S" stands for "Secure".

Main Differences
Feature	HTTP	HTTPS
Security	Not encrypted	Encrypted (SSL/TLS)
Data Protection	Vulnerable to interception	Protected from eavesdropping
Port	80	443
Use Case	Informational websites	Login, banking, email, payments
Security Aspect

HTTP sends data in plain text, meaning attackers can intercept and read it. HTTPS encrypts the data, making it unreadable to unauthorized parties. Therefore, HTTPS ensures:

Data confidentiality

Data integrity

Authentication of the website

2️⃣ Structure of an HTTP Request and Response

When a client communicates with a server, the process consists of two parts: Request and Response.

HTTP Request Structure

An HTTP request typically contains:

Request Line

Method (GET, POST, etc.)

URL (path)

HTTP version

Example:

GET /index.html HTTP/1.1


Headers

Provide additional information (Host, User-Agent, Content-Type, etc.)

Body (Optional)

Contains data (used mainly in POST, PUT requests)

HTTP Response Structure

An HTTP response typically contains:

Status Line

HTTP version

Status code

Status message

Example:

HTTP/1.1 200 OK


Headers

Metadata about the response (Content-Type, Content-Length, etc.)

Body

The actual content returned (HTML page, JSON data, image, etc.)

3️⃣ Common HTTP Methods
1. GET

Description: Retrieves data from the server.
Use Case: Fetching a web page or retrieving data from an API.

2. POST

Description: Sends data to the server to create a new resource.
Use Case: Submitting a registration form.

3. PUT

Description: Updates an existing resource on the server.
Use Case: Updating user profile information.

4. DELETE

Description: Removes a resource from the server.
Use Case: Deleting a user account or removing an item from a database.

4️⃣ Common HTTP Status Codes

HTTP status codes are grouped by their first digit:

1xx → Informational

2xx → Success

3xx → Redirection

4xx → Client Errors

5xx → Server Errors

1. 200 – OK

Description: Request was successful.
Scenario: A webpage loads correctly.

2. 201 – Created

Description: A new resource was successfully created.
Scenario: A new user account is registered.

3. 301 – Moved Permanently

Description: Resource has been permanently redirected.
Scenario: Website redirects from HTTP to HTTPS.

4. 404 – Not Found

Description: Requested resource does not exist.
Scenario: User enters an incorrect URL.

5. 500 – Internal Server Error

Description: Server encountered an unexpected condition.
Scenario: Backend application crashes or has a bug.

Conclusion

HTTP is the fundamental protocol for web communication but lacks security. HTTPS enhances HTTP by adding SSL/TLS encryption, ensuring secure and reliable data transfer. Understanding HTTP methods, status codes, and request/response structure is essential for working with web applications and RESTful APIs.