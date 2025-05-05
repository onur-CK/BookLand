# BookLand

BookLand is an online bookstore platform designed to provide book enthusiasts with a simple, modern, and responsive user experience across all device sizes. Our mission is to make discovering and purchasing books an enjoyable and seamless process.

As avid readers ourselves, we understand the joy of finding the perfect book. BookLand was born out of our passion for literature and our desire to create a digital space where readers can easily browse, purchase, and manage their book orders without the hassle often associated with online shopping.

![BookLand Logo/Hero Image](path-to-image)

[View live site here](link-to-deployed-site)

## 📚 Table of Contents

- [Overview](#overview)
- [Planning](#planning)
  - [Target Audience](#target-audience)
  - [Project Goals](#project-goals)
  - [Feature Planning](#feature-planning)
  - [Technology Stack](#technology-stack)
  - [UI/UX Considerations](#uiux-considerations)
    - [Design Principles](#design-principles)
    - [Accessibility](#accessibility)
    - [Responsive Design](#responsive-design)
  - [Data Management](#data-management)
    - [User Data](#user-data)
    - [Product Data](#product-data)
    - [Order History](#order-history)
  - [Future Enhancements](#future-enhancements)

- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Icons and UI Elements](#icons-and-ui-elements)
  - [Wireframes](#wireframes)

- [Database Schema](#database-schema)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Models](#database-models)
    - [User Profile Model](#user-model)
    - [Wishlist Item Model](#wishlist-item-model)
    - [Testimonial Model](#testimonial-model)
    - [Book Model](#book-model)
    - [Category Model](#category-model)
    - [Order Model](#order-model)
    - [Order Line Item Model](#order-line-item-model)
    - [Newsletter Subscriber Model](#newsletter-subscriber-model)
  
- [Features](#features)
  - [Navigation](#navigation)
    - [Main Menu](#main-menu)
    - [Homepage](#homepage)  
    - [Search Bar](#search-bar)
    - [Filters & Sorting](#filters--sorting)
  - [Product Details](#product-details)
    - [Add to Cart & Wishlist](#add-to-cart--wishlist)
  - [Shopping Cart](#shopping-cart)
  - [Checkout](#checkout))
    - [Order Confirmation](#order-confirmation)
  - [User Profile](#user-profile)
    - [Order History](#order-history-feature)
  - [Testimonials](#testimonials)
  - [Wishlist](#wishlist)
  - [Admin Features](#admin-features)
    - [Inventory Management](#inventory-management)
    - [User Management](#user-management)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks and Libraries](#frameworks-and-libraries)
  - [Tools and Platforms](#tools-and-platforms)
  - [Third-Party Services](#third-party-services)
- [Credits](#credits)
  - [Code](#code)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)
- [Agile Methodology](#agile-methodology)
- [Deployment](#deployment)
- [Testing](#testing)
- [SEO and Marketing](#seo-and-marketing)

## Overview

BookLand is a sophisticated e-commerce platform designed specifically for book enthusiasts who value a curated literary experience. Unlike mass-market retailers, our store focuses on quality over quantity, specializing in carefully selected titles across philosophy, psychology, literature, biographies, and self-development categories.

Our platform combines elegant simplicity with powerful functionality, creating an intuitive shopping experience that helps readers discover their next great book without overwhelm. The clean, responsive design ensures seamless browsing across all devices, while thoughtful features like wishlist management, detailed book information, and personalized recommendations enhance the discovery process.

BookLand stands apart through its commitment to community building among readers. Our testimonial system allows customers to share their experiences and recommendations, creating a sense of shared literary exploration. The platform's integration with Stripe ensures secure payment processing, while our robust order management system gives users complete visibility into their purchase history.

Developed using Django and Bootstrap, BookLand demonstrates modern web development principles with a focus on performance, security, and user experience. The application implements a comprehensive database schema that efficiently manages user profiles, product information, orders, and customer interactions.

Whether you're seeking philosophical classics, psychological insights, or personal growth literature, BookLand offers a refreshing alternative to algorithm-driven retail experiences—a digital bookstore where thoughtful curation meets seamless technology.




### Wireframes

[Home page medium+](media/wireframes/Home%20Page%20Medium%20Plus.png)

[Home page mobile](media/wireframes/Home%20Page%20Mobile.png)

[Checkout page shipping](media/wireframes/Checkout%20Page%20Shipping%20info%20and%20order%20summary.png)

[Order confirmation](media/wireframes/Order%20Confirmation%20Page.png)

[Product details medium+](media/wireframes/Product%20Details%20Medium%20Plus.png)

[Product details mobile](media/wireframes/Product%20details%20mobile.png)

[Profile management](media/wireframes/Profile%20Management.png)

[Shopping cart page](media/wireframes/Shopping%20Cart%20Page.png) ! Add explanation about the change of the cart summary position and talk through why without changing the ss !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

[Sign up](media/wireframes/Sign%20up.png)

[Login/Sign-In](media/wireframes/Login.png)

[Wishlist](media/wireframes/Wishlist.png)


