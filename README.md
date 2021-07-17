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

It aims to create a brand to establish an image in the public eye for the shop, to show it's quality and professionalism. It aims to allow the owner full control over their content and promote their items in the best way. It's elegant bright sophisticate but simple design aims to encourage users to explore it. It's clear navigation and shopping experience encourage retuning customer and it's features, gift presentation, free delivery, recipes and chat encourage user to create an account an become a loyal customer

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
<img src="documentation/readme-images/x.png" width="90%">
</h2>

### Skeleton Plane

The interface is aesthetically functionally all the time creating a positive reaction in the user with every click, 
making the user feel both at home here and part of an interesting journey. Details of this are found in the Design section.

[Back to Table of Content](#table-of-content)

### User stories

 - #### First Time User Goals

1. As a First Time User, I want to learn what the site has to offer and how to use the site quickly.
2. As a First Time User, I want to view specific categories and specific products.
2. As a First Time User, I want to search for specific products, know if it's available or not and see how many results there are for the search.
2. As a First Time User, I want to sort products by price, rating and category.
3. As a First Time User, I want to find the best prices for different sizes or quantities of each product.
4. As a First Time User, I want to know what I have added to my shopping bag, make updates or remove items and see the total.
5. As a First Time User, I want to purchase specific products.
6. As a First Time User, I want to purchase products quickly without having to sign up.
7. As a First Time User, I want to register easily.

 - #### Returning User Goals

8. As a Returning User, I want to easily login and logout.
9. As a Returning User, I want to view or update my profile.
8. As a Returning User, I want to see products ratings and reviews.

  - #### Frequent User Goals

6. As a Frequent User, I want to view or update my profile.
7. As a Frequent User, I want to view my order history and payment details.
8. As a Frequent User, I want to easily recover my password if I forget it.
6. As a Frequent User, I want to view the latest recipe and all recipes.
6. As a Frequent User, I want to view and add comments and questions.

  - #### Owner User Goals

1. As the owner/admin user I want to upload new products.
2. As the owner/admin user I want to edit product details.
3. As the owner/admin user I want to edit product prices.
4. As the owner/admin user I want to edit images.
5. As the owner/admin user I want to delete images and products.
1. As the owner/admin user I want to upload new products.
1. As the owner/admin user I want to upload new recipes.
6. As the owner/admin user I want to post or respong on chat to users questions.
7. As the owner/admin user I want control over material posted on the site for legal and other purposes.

[Back to Table of Content](#table-of-content)


## Design

<h2 align="center">
<img src="documentation/readme-images/x.png" width="90%">
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

<p align="center"> <strong>Small Screen 320px</strong></p>
<h2 align="center">
<img src="documentation/readme-images/x.png" width="25%">
</h2>

[Back to Table of Content](#table-of-content)

### Allauth Login/Register/Logout Pages and Security

  The user can browse and purchase items on the sit but they are encouraged to create an account. On one of the many links to register the user is brought to the Allauth Register page. Like all other pages I customed it to give to a personal easy to use friendly feel. Allauth is used throughout the site to look after all security issues concerning users and deals with all other issues like forgetting passwords and email confirmations.

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

### Admin's Base Page

  As discussed above in "Security Measures" defensive programming will only allow access to the admin features if user is the a superuser user and this is implemented both in the front-end and back-end. The superuser/owner can upload products and recipes and edit and delete them as well. These will be given the option to delete a user. When they go to the chat page a check box displays for them only and on checking it add is_shop to the chat object saved which is interpretted in the template to render a certain style to let the users know that message is from the shop.

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
