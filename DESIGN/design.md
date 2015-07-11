# Design Documentation

Chia-Hung (Kevin) Hsiao : c3hsiaod


Stanley Yee: g3yeesta


Sri Wardhana Halim: g3halims


Trina Yeap: g3trinay

###Software architecture

Our project will be using with Python and Django framework with PostgreSQL as the database. It will use Django's modified MVC design pattern; Model-Template-View. 

The following is a high level view of our projects architecture.

![Architecture Diagram](https://raw.githubusercontent.com/FlyinKat/CSC309_A3/master/DESIGN/part_a.png)

The url module will interpret a URL that is requested by the browser and map it to the the appropriate view which may retrieve and/or modify data within the model and then return the appropriate HTML template to the browser. We will be using Django's built in admin site for our administrative view.

### Database Schema

Our project will use a PostgreSQL to store data about user and listings and ratings for users. The following will be our schema:

* **User** : {INTEGER userid, CHAR username, CHAR password, CHAR email, CHAR location, BOOLEAN courier }
* **Listing** {CHAR userid, CHAR itemInfo, CHAR logisticInfo, CHAR location, CHAR arrivalTime}
* **Rating** {CHAR userid, CHAR rater, CHAR comment, INTEGER rating}

### Pages

#### Main Page
Displays two sections, one for the customer & the other for the courier
There will be a register and a login button on the top right corner of the page for 
new customers to sign up or existing customers to sign in.

Once login is successful, the user ID will be shown and a log out button will be shown on the page,replacing the register/login buttons
    
The 2 sections represent:
* Customer column    Displays a search tab where a list containing 3 elements, where each element has a textbox next to it 
    to insert the places/time:
    *  Start destination
    *  End destination
    *  Pickup time
* Search button :
      This allows customers to search whether there are any courier services available according to its request, links to  search result page.
* Post button :
      If there are no available courier services, then the customer is able to post a job , links to search result page.
* Courier column :
    Displays a search tab where a list containing 3 elements, where each element has a textbox next to it 
    to insert the places/time:
    * Start destination
    *  End destination
    *  Pickup time
* Search button :
      This allows couriers to search whether there are any jobs services available according to its request, links to search result page.
* Post button :
      If there are no available services to be picked up by the courier, then the courier is able to post a job, links to  search result page.

#### Login Page
Redirects to this page if user tries to post listing or contact any user while not logged in.
  * Username text input box
  * Password text input box
  * Register button (for new users)
  * Login button (for existing users)
  * Forget username/password link: 
    If users forget their passwords, this link will redirect them to a new page, Forget Username/Password page.
  * Facebook login button
    If users do not want to create a new account, they can link their Facebook account instead.

#### Forget Username/Password page
  Users are redirected to this page if they forget their username/password.
  They are adviced to fill in the username textbox if they do not remember their password.
  If they can't recall both username and password, they should fill up the email textbox.
    Username text input box
    Email text input box
    Reset password button
      This will generate an email containing their username and a new password that sends to the 
      user's email linked with their username (if they provide a username), otherwise to the email 
      provided in the input box above.

#### Account page
  Lists all the information about the user (which are created in the Customer Registration Page)

#### Customer Registration Page
  Customers need to fill up the user details in the text input boxes with their descriptions provided below:  
 *   First name
 *   Last name
 *   Address
 *   City
 *   State
 *   Postal code
 *   Email
 *   Phone number
 *   Register button
 *  Cancel button :
    This takes users back to the main page

#### Courier Registration Page
  Couriers need to fill up the user details in the text input boxes with their descriptions provided below: 
*   First name
*   Last name
*   Address
*   City
*   State
*   Postal code
*   Email
*   Phone number
*   Register button
*   Cancel button :
    This takes users back to the main page

#### Courier Job Posting Page
* Text input boxes:
    * Item
    * Weight limit
    * Location
    * Time slot
*  Submit button

#### Customer Job Posting Page
*   Text input boxes:
    * Item to be delivered
    * Weight
    * Location
    * Time
*   Submit button

#### Customer Listings Page
  Lists all the information about the job that the courier posted
*   Contact info
*   Name
*   Email
*   Message
*   Submit button
*   Recommendation list for the customer by other couriers

#### Courier Listings Page
  Lists all the information about the job that the customer posted
*     Name
*     Email
*     Message
*   Submit button
*   Recommendation list for the courier by other customers

#### Search Results Page
  Lists all the jobs either from the courier or customer based on the search results provided in the main page and provide link to them.
