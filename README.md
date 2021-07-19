<h1 align="center"><strong>La Donut - Online Cake Shop/Patisserie Website</strong></h1>

[View the project live here.](https://la-donut.herokuapp.com/)

A web application for an online cake shop and patisserie. Primarily, the site allows the shop to display their goods and allows users to browse the goods and purchase them. Users are initally taken to a products page with a side menu from which they can select categories. They are given the option to close this and browse from the navbar where they will find a search option and another product menu.<br>
The user can select an item directly from the page or on viewing the item on it's own page. On doing so it is added to their bag which they can view at any time giving them the option to update or remove products. From the bag they can simply click to be taken to the checkout page where through Stripe they can complete their transaction.<br>
The user is offered the option to open an account throughout the site and on completion of they purchase order with the incentive of free delivery, free gift presentation and the opportunity to participate in the online chat feature. There is also a recipes page with a latest recipe feature which is displayed apon completing an order and this in turn encourages user to go to the chat page.<br>
The shop owner can easily manage the site through the admin and manage site pages where they can upload, edit and remove goods. They are given instructions as to how to make the most of the visual promoting of goods in terms of image display.<br>
Allauth is used for site security and user authentication. Future developments may include...

<h2 align="center"><img src="documentation/readme-images/x.png"></h2>

# Table of Content

- [User Experience (UX)](#user-experience--ux-)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [User stories](#user-stories)

- [Design](#design)

- [Existing Features](#existing-features)
  * [Responsive Design](#responsive-design)
  * [Login/Register Pages and Security Measures](#login-register-pages-and-security-measures)
  * [User Base Page](#user-base-page)
  * [Departments Page](#departments-page)
  * [Images Page](#images-page)
  * [Admin Page](#admin-page)

- [Database structure](#database-structure)

- [Languages Used](#languages-used)

- [Frameworks, Databases, Libraries & Programs Used](#frameworks--databases--libraries---programs-used)

- [Testing](#testing)

- [Lighthouse](#lighthouse)
  * [Summary of Issues](#summary-of-issues)
  * [Login page](#login-page)
  * [Register page](#register-page)
  * [User Base page](#user-base-page)
  * [Image page](#image-page)
  * [Departments page](#departments-page)

- [Testing User Stories from User Experience (UX)](#testing-user-stories-from-user-experience--ux-)
  * [First Time User Goals](#first-time-user-goals-1)
  * [Returning User Goals](#returning-user-goals-1)
  * [Frequent User Goals](#frequent-user-goals-1)
  * [Admin User Goals](#admin-user-goals-1)

- [Further Testing](#further-testing)
  * [Brute-Forcing Attacks](#brute-forcing-attacks)
  * [404 Error Handling](#404-error-handling)
  * [Login Page](#login-page)
  * [Register Page](#register-page)
  * [Logout](#logout)

- [Deployment](#deployment)
  * [Repository](#repository)
    + [Forking the GitHub Repository](#forking-the-github-repository)
    + [Making a Local Clone](#making-a-local-clone)
    + [Terminal](#terminal)
    + [Further steps required](#further-steps-required)

  * [Deploy to Heroku](#deploy-to-heroku)

- [Credits](#credits)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## User Experience (UX)

The business goals are to establish the online shop as a reputable purveyor of cakes and pastries of a top of the range quality, to create an online presence and establish it as a brand. It's primary purpose is to entice new customer to purchase goods and secure regular returning customers. It aims to inspire trust, familiarity and build a loyal cumstomer base.

For the user, the goal of the site is to easily browse goods or find particular items or categories and purchase them in an simple enjoyable manner. It is to find new and interesting items to try or specific item for a specific occasion. For businesses it is to have a high quality reliable supplier of pastries.

### Strategy Plane

The aim of the site is to create an app that establishes the online shop as a reputable purveyor of cakes and pastries of a top of the range quality, to create an online presence and establish it as a brand. It aims to be an enjoyable and simple shopping experience enticing new customers and building a regular, especially business client base.

It aims to create a brand to establish an image in the public eye for the shop, to show it's quality and professionalism. It aims to allow the owner full control over their content and promote their items in the best way. It's elegant bright sophisticate but simple design aims to encourage users to explore it. It's clear navigation and shopping experience encourage retuning customer and it's features, gift presentation and chat encourage user to create an account an become a loyal customer.

#### Brand Identity
- Brand promise: Highest quality and most luxurious pastries and desserts available.
- Vision: Classy romantic.
- Mission: To cater to your most luxurious culinary desires
- Values: Class and quality

### Scope Plane

The features included in the app at present reflect choices made around the following reflections.<br>
What is absolutely necessary for the app to deliver it’s basic marketed functionality?<br>  
What is the most enticing user frendly way of doing building these? <br>
What types of design would further these and become great user experience in themselves?<br>
Which proposed features are buildable?
What features are necessary to make the goods sellable, the shop sellable and in return the actual app sellable to other businesses?
The buildable and time frame aspect was vital for the scope of the app and several more advance features, like Allauth Social were repositioned as future features.

[Back to Table of Content](#table-of-content)

### Structure Plane

The site is structured so the user can navigate in an intuitive way through the different features and categories of products, all pages keeping a uniformed consistency. 
The user is taken on a journey into the site, all elements being discoverable as they proceed along. From finding the different categories of cakes and pastries available to adding them to the shopping bag to checking out. To discovering the advantage of ceating an account and the chat other extras availabe on doing so. The site aims to, through it's freindly structure, build a relationship with the user.<br>
The Menu is a key element to the structure. Here the user can feel like they are in a real shop and have a more personal user experience and ease and control over their shopping experience.<br>
The user will see clear states of change when they interact with the features and selection and choice buttons and be given clear feedback to assure them of their interactive success.
A message, success, info, warning and error will display after every important interaction.<br>
The information architecture is a tree structure allowing users to move through content quickly and simply becoming aware of the site’s inherent structure as they go. 

<h2 align="center">
<img src="documentation/readme-images/structure.png" width="90%">
</h2>

### Skeleton Plane

The interface is aesthetically functionally all the time creating a positive reaction in the user with every click, 
making the user feel both at home here and part of an interesting journey. Details of this are found in the Design section.

[Back to Table of Content](#table-of-content)

### User stories

 - #### First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.
2. As a First Time User, I want to view specific categories and specific products.
3. As a First Time User, I want to search for specific products, know if it's available or not and see how many results there are for the search.
4. As a First Time User, I want to sort products by price, rating and category.
5. As a First Time User, I want to find the best prices for different sizes or quantities of each product.
6. As a First Time User, I want to know what I have added to my shopping bag, make updates or remove items and see the total.
7. As a First Time User, I want to purchase specific products quickly without having to sign up.
8. As a First Time User, I want to register easily.

 - #### Returning User Goals

1. As a Returning User, I want to easily login and logout.
2. As a Returning User, I want to view or update my profile.
3. As a Returning User, I want to see products ratings and reviews.

  - #### Frequent User Goals

1. As a Frequent User, I want to view my order history and payment details.
2. As a Frequent User, I want to easily recover my password if I forget it.
3. As a Frequent User, I want to view the latest recipe and all recipes.
4. As a Frequent User, I want to view and add comments and questions.

  - #### Owner/Admin User Goals

1. As the Owner/Admin User I want to upload new products.
2. As the Owner/Admin User I want to edit product details.
3. As the Owner/Admin User I want to edit product prices.
4. As the Owner/Admin User I want to edit images.
5. As the Owner/Admin User I want to delete images and products.
6. As the Owner/Admin User I want to upload new products.
7. As the Owner/Admin User I want to upload new recipes.
8. As the Owner/Admin User I want to post or respong on chat to users questions.
9. As the Owner/Admin User I want control over material posted on the site for legal and other purposes.

[Back to Table of Content](#table-of-content)


## Design

<h2 align="center">
<img src="documentation/readme-images/shop-page.png" width="90%">
</h2>

### Colour Scheme
 - The site aims to be elegant, upmarket, clean, sharp, bright and sophisticated using a white background with gold lines and some gold text/icons along with the odd blue buttons and links for some more perfunctory actions. The actual images themselves supply the main bulk of the content and in doing so will greatly influence the overall colour scheme so I wanted a sophisticated sharp white and gold containment background. I gave the login and other Allauth pages a warm friendly look with a background image of a pink whipped cream.

  
### Typography
 - Playfair Display, a serif non-formal friendly font was used as the main font for the site. It has a sophisticated slightly old fashioned classy feel. Lato was used along side it for more matter of fact details. And Playball, a very stylish, flamboyent romantic feeling font was used for the main titles and in some other places to give the shop a classy romantic feel.


### Imagery
 - Set against the sophisticated white and gold background the cake and pastry images speak for themselves to entice the customers with mouth watering delights.

### Wireframes

 - PDF – Balsamic was used to design the layout for all pages.

   [View on Github](https://github.com/johnston9/la-donut)

[Back to Table of Content](#table-of-content)

## Existing Features

### Responsive Design

  The site is responsive to all sizes and the images remain whole and in proportion at all sizes. One of the major decisions I had to make was regarding the images which would be actually uploader by the owner. The modern repsonsive capabilities are something I really want to take advantage of resizing all images and content at all sizes. BUT...this would only work if all image are the same aspect ratio or it would throw the row symmetry off.
  I combated this by putting in specific image heights, something obviously recommended by Lighthouse but something that also hampers the full responsive capabilities. I greatly researched this and it is something that many in UX field are trying to find a solution to. I also instructed the owner/user that 3:2 aspect ratio was the optimum way to go and gave them a link to img-resize where they could resize their images if necessary. I also put in a link, this all being on the add product page in an instructions hide/show box, to a how to resize on img-resize page. An awful lot of detail and instruction but I believe very necessary as ultimately these images were the whole point of the site and I thought it relevant to advise owners about them. These instruction are intended as an aid to intuitive learning for the owner and lead to them being satisfied with the control and artistic input they had over their site and in turn being happy with the site.

<p align="center"> <strong>Large Screen</strong></p>
<h2 align="center">
<img src="documentation/readme-images/shop-page2.png" width="90%">
</h2>

<p align="center"> <strong>Small Screen 320px</strong></p>
<h2 align="center">
<img src="documentation/readme-images/shop-sm.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)


### Allauth Login/Register/Logout Pages and Security

  The user can browse and purchase items on the sit but they are encouraged to create an account. On one of the many links to register the user is brought to the Allauth Register page. Like all other Allauth pages I customised it to give to a personal easy to use friendly feel. Allauth is used throughout the site to look after all security issues concerning users and deals with all other issues like forgetting passwords and email confirmations.<br>
  See [Allauth](documentation/allauth) for all Allauth images.

  The site has a number of other security measures firstly the use of front end measures to allow admin access only to admin. Then in the backend the use of @login_required for pages only for authenticated users and a redirect if the user is not a superuser for admin only functions.

<p align="center"><strong>Register Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/x.png" width="90%">
</h2>

 See Further Testing login and register pages.

 - [Back to Table of Content](#table-of-content)

### Recipes Page

  This page shows images of different recipes the user can click on and go to each one. There is a Latest Recipe link on the Checkout Complete page to take the user to the Latest Recipe. This is a feature designed to take the user further into the site and create an account. Under each recipe there is a link to view or add comments on the Chat Page for which the user need to create an account.

<p align="center"><strong>Recipes Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/x.png" width="90%">
</h2>

<p align="center"><strong></strong></p>
<h2 align="center">
<img src="documentation/readme-images/x.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### ChatPage

  Once the user registers they can avail of the chat feature which allows they to chat to the Master Pastry chef and view other user's chats

<p align="center"><strong>Chat</strong></p>
<h2 align="center">
<img src="documentation/readme-images/.png" width="90%">
</h2>

[Back to Table of Content](#table-of-content)

### Superuser Features

  As discussed above in "Security Measures" defensive programming will only allow access to the admin features if user is a superuser user and this is implemented both in the front-end and back-end. The superuser/owner can upload products and recipes and edit and delete them as well. They can delete a user from admin also. When they go to the chat page a check box displays for them only and on checking it will add is_shop to the chat object which is interpretted in the template to render a certain style to let the users know that message is from the shop.

<p align="center"><strong></strong></p>
<h2 align="center">
<img src="documentation/readme-images/x.png" width="90%">
</h2>

<p align="center"><strong>Admin Page 320px</strong></p>

<h2 align="center">
<img src="documentation/readme-images/x.png" width="25%">
</h2>

Please see admin testing for further details.

[Back to Table of Content](#table-of-content)

## Future Features

### Social Account Login
This Allauth function allows users to sign up and log in using an existing third party account such as Google and Facebook. This would make encouraging users to sign up easier as they are just a click away and don't have to do any more. For the site owners apart from having more user sign ups this opens up hugh areas in terms of information and marketing.

### Social Media Share Icons
In terms of brand awareness through social media social media share icons would be most advantagous.


## Information Architecture

- Development 
**SQLight** was used during development and comes with Django. 

- Deployment 
**PostgreSQL** is used for deployment, and was added as an add-on with Heroku.

### Database structure - Model Tables by App

#### Django contrib auth
1 - <strong>User</strong> - to hold the authenticated users.<br>
  - Foreign Key to UserProfile

#### Product App
1 - <strong>Category</strong> - to hold the product categories.<br>

2 - <strong>Product</strong> - to hold the products.
  - Foreign Key to Category 

3 - <strong>Size</strong> - to hold the product's size prices.<br>
  - Foreign Key to Product

4 - <strong>Forsix</strong> - to hold the product's box quantity prices.<br>
  - Foreign Key to Product

5 - <strong>Review</strong> - to hold the product's reviews.<br>
  - Foreign Key to Product
  - Foreign Key to UserProfile


#### Checkout App
1 - <strong>Order</strong> - to hold the orders for all completed orders.<br>
  - Foreign Key to UserProfile

2 - <strong>OrderLineItem</strong> - to hold the order's items.
  - Foreign Key to Order
  - Foreign Key to Product

#### Profiles App
1 - <strong>UserProfile</strong> - to hold the registered users details.<br>
  - OneToOne Key to User

#### Recipe App
1 - <strong>Recipe</strong> - to hold the recipes.<br>
  - Foreign Key to User

2 - <strong>Comment</strong> - to hold the chat.<br>
  - Foreign Key to UserProfile

<p align="center"><strong>Entity Relationship Diagram</strong></p>

<h2 align="center">
<img src="documentation/readme-images/er_diagram.png" width="100%">
</h2>

[Back to Table of Content](#table-of-content)

## Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JAVASCRIPT](https://en.wikipedia.org/wiki/JavaScript)
- [PYTHON](https://en.wikipedia.org/wiki/Python_(programming_language))
- [djangotemplatelanguage](
  https://docs.djangoproject.com/en/3.2reftemplateslanguage/)

## Frameworks, Databases, Libraries & Programs Used

1. [Bootstrap:](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
   - Bootstrap with it's grid-based format was used to create the overall framework for the site This included the primary responsiveness
     and overall styling of the website. Also specific 
     Bootstrap features, which include the "Select", 
     the "Navbar" and "Sidenav", "Modals", "Tooltipped" and "Datepickers", were used in the site.
1. [Django:](https://www.djangoproject.com/)
   - Django the high-level Python Web framework was used to build the app.
1. [SQLight:](https://www.sqlite.org/index.html)
   - SQLight came with Django and was used as the database for development.
1. [PostgreSQL:](https://www.postgresql.org/)
   - PostgreSQL was added with Heroku and was used as the database for production.
1. [Pymongo:](https://pypi.org/project/pymongo/)
   - Pymongo was used for interacting with MongoDB database from the app.
1. [Font Awesome:](https://fontawesome.com/)
   - Font Awesome was used throughout the website for the icons.
1. [jQuery:](https://jquery.com/)
   - jQuery was used along with Javascript through-out the site for front-end functionality and to initialize some Bootstrap features.
1. [Git](https://git-scm.com/)
   - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
   - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
   - Balsamiq was used to create the [wireframes](https://github.com/johnston9/MS3-Shot-Caller) during the design process.
1. [Freeformatter](https://www.freeformatter.com/html-formatter.html)
   - Freeformatter was used to tidy up the final code.
1. [Gauger](https://gauger.io/fonticon/)
   - Gauger was used to create the favicon icon.
1. [Am-I-Responsive](http://ami.responsivedesign.is/):
   - Am I Responsive was used to test the site's responsive sizings and to generate responsive sizing images.
1. [GitHub Wiki TOC generator:](http://ecotrust-canada.github.io/markdown-toc/)
   - GitHub Wiki TOC generator was used to create the Table of Contents.
1. [dbdiagram.io](https://dbdiagram.io/home)
   - dbdiagram.io was used to create the Entity-Relationship Diagram.

A number of imports were used in Django for various functions and an inventory of these can be found in the Deployment section.

[Back to Table of Content](#table-of-content)

## Testing

W3C Markup Validator, W3C CSS Validator. PEP8 and JSHint were used to validate every page of the project.

- [W3C Markup Validator](https://validator.w3.org/) - [Results](https://github.com/johnston9/la-donut)
  - W3C "Direct Input" option was used on each html page where errors displayed due to template ...but on validated by URL no errors were shown - documentation/w3c-by-url.

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/johnston9/la-donut)
  - W3C showed no errors and only one warning for the hr rule's background color
    being the same as it's color, but this was intentional.
  
- [JSHint](https://jshint.com/) - [Results](https://github.com/johnston9/la-donut)
  - JSHint was used with "New JavaScript features (ES6)" and "jQuery" checked in the configuration menu.
    
- [PEP8 online check](http://pep8online.com/) - [Results](https://github.com/johnston9/la-donut)
  - PEP8 approved all pyhton pages. It gave a "no newline at end of file"
    but I researched this and found it was a common result and could be ignored. I explored the matter more and found that if
    the curser was at the start of the new line, I got an "All Right" result.

- [PythonChecker](https://www.pythonchecker.com/) - [Results](https://github.com/johnston9/la-donut)
  - PythonChecker gave 100% result.

[Back to Table of Content](#table-of-content)

## Testing User Stories from User Experience (UX) 

### First Time User Goals

1. #### As a First Time User, I want to learn what the site has to offer and how to use the site quickly.

    - The site is designed for first time learning. It is streamlined for specific user goals that upon first use the user with a few clicks will be able to find any item, feature or page. At the top of every page the navbar displays all options for the user so they can select their desired destination quickly and a menu is available on landing on the shop page.

<p align="center"><strong>Navbar and on Entry Shop Page</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/shop-page.png" width="90%">
</h2>

2. #### As a First Time User, I want to view specific categories and specific products.

    - Upon entering the user is take to the shop page where they can use the menu to find specific categories. They have the option to close the menu to shop from a larger items page and browse directly from the navbar. 

<p align="center"><strong>Menu Input</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/menu1.png" width="90%">
</h2>

<p align="center"><strong>Menu Result</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/menu2.png" width="90%">
</h2>

3. #### As a First Time User, I want to search for a specific product, know if it's available or not and see how many results there are for the search.

    - At the top of all pages is a search bar where the user can search for specific items. The number of results is displayed above the results or a message sating there were no results if that is the case.

<p align="center"><strong>Search Input</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/search1.png" width="90%">
</h2>

<p align="center"><strong>Search Result</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/search2.png" width="90%">
</h2>

4. #### As a First Time User, I want to sort products by price, rating and category.

    - The user can sort products by price - high to low or low to high, rating -high to low and category from the navbar and have the amount of products found display on top as well as the current sorting value the have chosen.

<p align="center"><strong>Sorting Selection</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/nav1a.png" width="90%">
</h2>

<p align="center"><strong>Sorting Result</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/sort2.png" width="90%">
</h2>

5. #### As a First Time User, I want to find the best prices for different sizes or quantities of each product.

    - All products have their prices showing for their sizes, if they have them or box quantity if they have them, both at first glance on the shop page or on closer inspection on the view item page. 

<p align="center"><strong>Prices</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/price.png" width="90%">
</h2>

6. #### As a First Time User, I want to know what I have added to my shopping bag, make updates or remove items and see the total.

    - Upon the adding of an item to the shopping bad a success message shows with a preview of all bag items and total and a link to the actual bag. The users total, updated on every transaction is displayed at the top of every page with a link to the bag. on going to the bag the user can see all their items and total and update select item quantities or remove the item entirely. A confirm alert displays if a user clicks Remove.

<p align="center"><strong>Add item Success Message</p>   
<h2 align="center">
<img src="documentation/readme-images/message1.png" width="90%">
</h2>

<p align="center"><strong>Shopping Bag</p>   
<h2 align="center">
<img src="documentation/readme-images/bag.png" width="90%">
</h2>

7. #### As a First Time User, I want to purchase specific products quickly without having to sign up.

    - All users can purchase items without having to sign up. The user can make a quick selection of any item and the size or box quantity they want right from the shop page without having to go to the view item page. This is also intended for regular users who know what the want and want to select items quickly. See prices image above.

8. #### As a First Time User, I want to register easily.

    - The user will be given the option to sign up from the landing page, when they go to checkout and anytime in the My Account nav link. On clicking they will be take to the Register Page and only have to enter a username, email and password to sign up. The Registration page as with all Allauth page has been customised for greater user experience.<br>
    See [Allauth](documentation/allauth) for all Allauth images.

<p align="center"><strong>My Account Nav Link</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/reg1.png" width="90%">
</h2>

<p align="center"><strong>Register page - Mobile view</strong></p>   
<h2 align="center">
<img src="documentation/readme-images/reg-mo.png" width="25%">
</h2>


[Back to Table of Content](#table-of-content)

### Returning User Goals

1. #### As a Returning User, I want to easily login and logout.

    - The user can login and logout easily from the My Account nav link which takes them to customed Allauth pages. <br>
    See [Allauth](documentation/allauth) for all Allauth images.

<p align="center"><strong>Login</strong></p>
<h2 align="center">
<img src="documentation/readme-images/login.png" width="90%">
</h2>


<p align="center"><strong>Logout - Mobile View</strong></p>
<h2 align="center">
<img src="documentation/readme-images/logout.png" width="25%">
</h2>

2. #### As a Returning User, I want to view or update my profile.

    - On clicking on the profile nav link in My Account the user is taken to their Profile Page where they can update their Primary Delivery Address and recieve a success message on doing so. This info is preset as the Delivery address when they checkout.

<p align="center"><strong>Profile Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/pro1.png" width="90%">
</h2>

<p align="center"><strong>Profile Page Update Success Message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/pro2.png" width="90%">
</h2>

3. #### As a Returning User, I want to see products ratings and reviews.

    - The product average customer rating is displayed for each item on the shop and view item pages. On the view item page the user will see a link to the item's reviews and another link to add a review if the user is authenticated or sign up to add a review if not. On the add review page the user can rate the product and this is displayed in stars on their review and also used to calculate the average rating. A customised Bootstrap paginated table is used to hold the reviews which includes a search function which I figured out from the Bootstrap4 docs.<br>
    [DataTables](https://datatables.net/examples/styling/bootstrap4)

<p align="center"><strong>Review Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/rev3.png" width="90%">
</h2>

<p align="center"><strong>Add Review Success message</strong></p>
<h2 align="center">
<img src="documentation/readme-images/rev4.png" width="90%">
</h2>

<p align="center"><strong>Result</strong></p>
<h2 align="center">
<img src="documentation/readme-images/rev5.png" width="90%">
</h2>


### Frequent User Goals

1. #### As a Frequent User, I want to view my order history and payment details.

   - When the user goes to their Profile they will find their order history there. On clicking on an order they will be taken to the checkout complete message recieved for that order.
  
<p align="center"><strong>Order History</strong></p>
<h2 align="center">
<img src="documentation/readme-images/.png" width="90%">
</h2>

2. #### As a Frequent User, I want to easily recover my password if I forget it.

   - When the user clicks forgot password on their login they will be taken to a customizes series of Allauth pages to get a new password.<br>
   See [Allauth](documentation/allauth) for all Allauth images.
  
<p align="center"><strong>Reset Password</strong></p>
<h2 align="center">
<img src="documentation/readme-images/password_reset.png" width="90%">
</h2>

6. #### As a Frequent User, I want to view the latest recipe and all recipes.

   1. When the user clicks Recipes in the nav they will be taken to the Recipe Page where they can select a Recipe and be taken to a page for it. After completing an order a large button displays on the checkout complete page to take them to the Latest Recipe.
  
<p align="center"><strong></strong></p>
<h2 align="center">
<img src="documentation/readme-images/.png" width="90%">
</h2>

6. #### As a Frequent User, I want to view and add comments and questions.

   1. When the user clicks on the Latest Updates button on their home base page
  
<p align="center"><strong>Latest Updates Page</strong></p>
<h2 align="center">
<img src="documentation/readme-images/la2.png" width="90%">
</h2>


### Owner/Admin User Goals


1. #### As the Owner/Admin User I want to upload new products.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to edit product details.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to upload new products.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to edit product prices.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to edit images.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to delete images and products.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to upload new products.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to upload new recipes.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want to post or respond on chat to users questions.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>

1. #### As the Owner/Admin User I want control over material posted on the site for legal and other purposes.

   - If the admin user clicks the upload script button available only to them
     
<h2 align="center">
<img src="documentation/readme-images/sc-1.png" width="90%">
</h2>
 