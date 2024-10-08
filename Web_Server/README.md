
### README for Web_Server

**File: `Web_Server/README.md`**

```markdown
# Web Server

## Description
This section contains the files related to the web server that interfaces with both the Arduino and the gesture recognition system. It includes PHP scripts to manage database connections and fetch bulb status data.

## Setup Instructions
1. **Dependencies**: Ensure you have a web server (e.g., Apache2) and MySQL installed.
2. **Database Setup**:
   - Create a MySQL database named `bulb_project`.
   - Create necessary table (`bulb_data`) and data (refer to the SQL scripts if available).

3. **Installation**:
   - Place the `bulb_project` folder in your web server’s root directory (e.g., `/var/www/html/` for Apache).
   - Update the database connection parameters in `db_connect.php` as needed.

## Database Configuration

Before running the **Web Server** component of the project, you need to set up the database connection parameters in the `db_connect.php` file. Follow these instructions:

1. Open the `db_connect.php` file located in the **Web_Server/bulb_project/** directory.
   
2. Locate the following lines in the code:

   ```php
   $servername = "servername";
   $username = "username";
   $password = "password";
   $dbname = "database_name";
   $port = 1111; // Your mysql port number 

## Usage
- Open `index.html` in a web browser to view the interface.
- The interface will automatically fetch and display the current status of the bulbs from the database.

## Example
- Use the web interface to turn on/off the bulbs and view their statuses in real-time.
