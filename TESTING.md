# BookLand - Testing Documentation

## Table of Contents
- [Introduction](#introduction)
  - [Testing Overview](#testing-overview)
  - [Testing Approach](#testing-approach)
  - [Testing Environment](#testing-environment)

- [Manual Testing](#manual-testing)
  - [User Stories Testing](#user-stories-testing)
    - [EPIC 1: User Management](#epic-1-user-management)
    - [EPIC 2: Book Catalog](#epic-2-book-catalog)
    - [EPIC 3: Shopping Experience](#epic-3-shopping-experience)
    - [EPIC 4: Admin Features](#epic-4-admin-features)
    - [EPIC 5: Technical Infrastructure](#epic-5-technical-infrastructure)

  - [Feature Testing](#feature-testing)
    - [Navigation & Core Functionality](#navigation--core-functionality)
    - [User Authentication](#user-authentication)
    - [Book Catalog Features](#book-catalog-features)
    - [Shopping Cart](#shopping-cart)
    - [Checkout Process](#checkout-process)
    - [User Profile](#user-profile)
    - [Wishlist Functionality](#wishlist-functionality)
    - [Order History](#order-history)
    - [Testimonials System](#testimonials-system)
    - [Admin Features](#admin-features)
    - [Newsletter Subscription](#newsletter-subscription)
    - [Toast Notifications](#toast-notifications)
    - [Error Pages](#error-pages)
    - [SEO and Marketing Features](#seo-and-marketing-features)
  - [Responsive Design Testing](#responsive-design-testing)
    - [Mobile Testing](#mobile-testing)
    - [Tablet Testing](#tablet-testing)
    - [Desktop Testing](#desktop-testing)
  - [Browser Compatibility Testing](#browser-compatibility-testing)
  - [Form Validation Testing](#form-validation-testing)
  - [Payment Processing Testing](#payment-processing-testing)
  - [CRUD Functionality Testing](#crud-functionality-testing)

- [Automated Testing](#automated-testing)
  - [Unit Tests](#unit-tests)
  - [Integration Tests](#integration-tests)
  - [System Tests](#system-tests)
  - [Coverage Report](#coverage-report)

- [Validation Testing](#validation-testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Python (PEP8) Validation](#python-pep8-validation)
  - [Accessibility Testing (WCAG)](#accessibility-testing-wcag)
  - [Performance Testing](#performance-testing)
    - [Lighthouse Results](#lighthouse-results)
    - [WebPageTest Results](#webpagetest-results)

- [Database Testing](#database-testing)
  - [Model Relationship Testing](#model-relationship-testing)
  - [Data Integrity Testing](#data-integrity-testing)
  - [Query Optimization Testing](#query-optimization-testing)

- [Security Testing](#security-testing)
  - [CSRF Protection](#csrf-protection)
  - [Form Validation Security](#form-validation-security)
  - [Authentication Testing](#authentication-testing)
  - [Authorization Testing](#authorization-testing)
  - [Data Protection](#data-protection)

- [User Experience Testing](#user-experience-testing)
  - [User Feedback Summary](#user-feedback-summary)
  - [Usability Testing Results](#usability-testing-results)
  - [User Journey Testing](#user-journey-testing)

- [Bugs and Issues](#bugs-and-issues)
  - [Fixed Bugs](#fixed-bugs)
    - [Template Path Resolution Bug](#template-path-resolution-bug)
    - [Template Literal Display Bug in Wishlist Counter](#template-literal-display-bug-in-wishlist-counter)
    - [Category Duplication in Navigation and Product Page](#category-duplication-in-navigation-and-product-page)
    - [Cart Removal Button Not Working (X icon replaced with trash icon)](#cart-removal-button-not-working-x-icon-replaced-with-trash-icon)
    - [Missing Subtract Filter Bug in Cart Template](#missing-subtract-filter-bug-in-cart-template)
    - [Stripe Payment Processing 'NoneType' Error](#stripe-payment-processing-nonetype-error)
    - [Order History Detail View Success Message Bug](#order-history-detail-view-success-message-bug)
    - [AWS S3 Integration Django Version Compatibility Bug](#aws-s3-integration-django-version-compatibility-bug)
  - [Known Issues](#known-issues)

- [Testing Procedures](#testing-procedures)
  - [Deployment Testing Process](#deployment-testing-process)
  - [Testing Schedule](#testing-schedule)
  - [Regression Testing](#regression-testing)

- [Conclusion](#conclusion)


## Introduction

### Testing Overview

The BookLand e-commerce project has undergone extensive testing to ensure functionality, usability, responsiveness, and security across all aspects of the application. This document provides a comprehensive overview of the testing methodologies employed, specific test cases performed, validation results, and bug fixes implemented throughout the development process.

### Testing Approach

Testing for BookLand followed a multi-layered strategy combining manual and automated approaches:

1.Manual Testing: Systematic verification of user stories, feature functionality, responsive design, browser compatibility, and user experience across various devices and screen sizes.
2. Validation Testing: Rigorous code validation using industry-standard tools to ensure HTML, CSS, JavaScript, and Python code meets best practices and standards.
3. Accessibility Testing: Evaluation of the application against WCAG guidelines to ensure inclusivity for all users, including those using assistive technologies.
4. Performance Testing: Analysis of application performance metrics including page load times, resource optimization, and overall responsiveness.
5. Security Testing: Verification of authentication flows, authorization controls, data protection, and form validation to protect user data and prevent security vulnerabilities.
6. User Experience Testing: Evaluation of the application from a user's perspective, including navigation flows, intuitive interaction, and consistent design patterns.

### Testing Environment

Testing was conducted across the following environments to ensure consistent behavior:

Devices: 
- Desktop computers (Windows, macOS)
- Laptops (13", 15", 17" screens)
- Tablets (iPad, Samsung Galaxy Tab)
- Mobile devices (iPhone 12/13/14, Samsung Galaxy S21/S22)

Browsers:

- Google Chrome (latest version)
- Mozilla Firefox (latest version)
- Safari (latest version)
- Microsoft Edge (latest version)

Screen Resolutions:

- Mobile: 320px - 480px
- Tablets: 768px - 1024px
- Laptops/Desktops: 1024px - 1920px+
- Ultrawide Monitors: 34 inch/3440 x 1440px(gigabyte M34WQ) / 38 inch/3840 x 1600px(LG 38GN950P-B)

Development and Production Environments

Local development environment with SQLite database
Production environment on Heroku with PostgreSQL database
AWS S3 for static and media file storage

This comprehensive testing approach has been essential in identifying and resolving issues throughout the development process, resulting in a robust, user-friendly, and reliable e-commerce platform. The following sections detail the specific tests performed, validation results, and bug fixes implemented to ensure BookLand meets high standards of quality and user experience.


## Manual Testing

### User Stories Testing

This section details the manual testing conducted for user stories defined in our Agile development process. Each user story has been thoroughly tested to ensure the implemented features meet the acceptance criteria.

#### **EPIC 1: User Management**

|Passed | **User Registration** - As a new visitor, I want to create an account so that I can track my orders and save my preferences.|
|:---:|:---|
|&check;| Registration form includes fields for name, email, and password.|
|&check;| Email verification process works correctly.|
|&check;| Password strength requirements are enforced.|
|&check;| Duplicate email addresses are not allowed.|
|&check;| Account creation success message displays after registration.|

|Passed | **User Login** - As a registered user, I want to securely log in to my account so that I can access my personal information and order history.|
|:---:|:---|
|&check;| Login form accepts email/username and password.|
|&check;| "Remember me" functionality keeps users logged in between sessions.|
|&check;| Appropriate error messages display for invalid credentials.|
|&check;| Redirect to intended page after successful login works correctly.|
|&check;| Success message confirms successful login.|

|Passed | **User Profile Management** - As a logged-in user, I want to view and edit my profile information so that my account reflects my current details.|
|:---:|:---|
|&check;| Profile page displays all current user information.|
|&check;| User can edit name, email, and contact information.|
|&check;| User can add/edit default shipping addresses.|
|&check;| Changes are saved immediately upon submission.|
|&check;| Validation prevents invalid data submission.|

|Not Implemented | **Social Login Integration** - As a new visitor, I want to register and login using my social media accounts.|
|:---:|:---|
|❌| This feature was designated as a "Should Have" in our MoSCoW prioritization but was not implemented in the current version. It will be considered for future releases.|

#### **EPIC 2: Book Catalog**

|Passed | **Book Browsing by Category** - As a customer, I want to browse books by category so that I can easily find books in genres I'm interested in.|
|:---:|:---|
|&check;| Categories are clearly displayed in navigation menu and on main product page.|
|&check;| Clicking a category shows all books within that category.|
|&check;| Books display cover image, title, author, and price.|
|&check;| Active category is highlighted to show current filter.|
|&check;| Category selection persists during sorting and pagination.|

|Passed | **Book Search and Filtering** - As a customer, I want to search for books and filter results so that I can quickly find specific titles or authors.|
|:---:|:---|
|&check;| Search bar is prominently displayed across the site.|
|&check;| Search works by title, author, and description.|
|&check;| Search results display with relevant information.|
|&check;| Empty search results provide helpful messaging.|
|&check;| Search term is retained and displayed with results.|

|Passed | **Book Detail View** - As a customer, I want to view detailed information about a book so that I can make an informed purchase decision.|
|:---:|:---|
|&check;| Detail page shows cover image, title, author, price, description, and rating.|
|&check;| Inventory status is clearly displayed.|
|&check;| "Add to cart" and "Add to wishlist" buttons are prominently displayed.|
|&check;| Related books in the same category are suggested.|
|&check;| Quantity selector functions correctly with validation.|

#### **EPIC 3: Shopping Experience**

|Passed | **Shopping Cart Management** - As a customer, I want to add books to my cart and manage cart contents so that I can prepare for checkout.|
|:---:|:---|
|&check;| Books can be added to cart from product details and listing pages.|
|&check;| Cart icon shows current number of items.|
|&check;| Cart page displays all items with images, titles, and prices.|
|&check;| Quantities can be adjusted with immediate total updates.|
|&check;| Items can be removed from cart with the trash icon.|
|&check;| Cart contents persist between sessions.|

|Passed | **Wishlist Functionality** - As a customer, I want to save books to my wishlist so that I can keep track of books I'm interested in but not ready to purchase.|
|:---:|:---|
|&check;| Books can be added to wishlist from product detail page.|
|&check;| Wishlist is accessible from user profile.|
|&check;| Items can be moved from wishlist to cart.|
|&check;| Items can be removed from wishlist.|
|&check;| Wishlist is saved to user account.|
|&check;| Wishlist count updates in real-time in the navigation bar.|

|Passed | **Checkout Process** - As a customer, I want a streamlined checkout process so that I can complete my purchase quickly and securely.|
|:---:|:---|
|&check;| Checkout page collects shipping address information.|
|&check;| Checkout page collects payment information securely.|
|&check;| Order summary is displayed for review before payment.|
|&check;| Form validation provides clear feedback for errors.|
|&check;| User can save delivery information for future orders.|
|&check;| Order confirmation is displayed after successful checkout.|

|Passed | **Payment Processing** - As a customer, I want secure payment processing so that I can confidently complete my purchase.|
|:---:|:---|
|&check;| Stripe integration for credit card processing works properly.|
|&check;| Payment information is securely handled.|
|&check;| Payment errors are clearly communicated.|
|&check;| Successful payments trigger order processing and confirmation.|
|&check;| Loading overlay displays during payment processing.|
|&check;| Checkout confirmation email is sent after successful payment.|

|Passed | **Order History and Tracking** - As a customer, I want to view my order history and track current orders so that I can monitor my purchases.|
|:---:|:---|
|&check;| Order history page displays all past orders with dates and totals.|
|&check;| Order detail view shows complete order information.|
|&check;| Order details can be accessed from profile.|
|&check;| Order confirmation is sent via email with relevant details.|
|&check;| Previous orders can be viewed without triggering new confirmation messages.|

#### **EPIC 4: Admin Features**

|Passed | **Admin Dashboard** - As an admin, I want a comprehensive dashboard so that I can quickly access key metrics and platform management functions.|
|:---:|:---|
|&check;| Django admin dashboard is accessible to administrators.|
|&check;| Dashboard displays key information in an organized manner.|
|&check;| Quick access to books, orders, users, and other management functions.|
|&check;| Admin can filter and search for specific information.|

|Passed | **Admin Book Management** - As an admin, I want to add, edit, and remove books from the catalog so that I can keep the inventory up to date.|
|:---:|:---|
|&check;| Book creation form includes all necessary fields.|
|&check;| Existing books can be edited with all fields updatable.|
|&check;| Books can be marked as out of stock or available.|
|&check;| Books can be permanently removed from the catalog.|
|&check;| Image upload functionality works correctly.|
|&check;| Book details are immediately reflected on the frontend after updates.|

|Passed | **Order Management** - As an admin, I want to view and process orders so that I can fulfill customer purchases efficiently.|
|:---:|:---|
|&check;| Orders list shows all orders with status and date.|
|&check;| Orders can be filtered by various criteria.|
|&check;| Order details show complete purchase information.|
|&check;| Customer contact information is accessible for fulfillment needs.|
|&check;| Order line items are clearly displayed with quantities and prices.|

|Passed | **Category Management** - As an admin, I want to create and manage book categories so that books are properly organized for customers.|
|:---:|:---|
|&check;| Categories can be created with name and description.|
|&check;| Categories can be edited and deleted.|
|&check;| Books can be assigned to categories.|
|&check;| Categories appear correctly in navigation.|
|&check;| Books can be filtered by category on the frontend.|

#### **EPIC 5: Technical Infrastructure**

|Passed | **Responsive Design Implementation** - As a user, I want the website to work well on all my devices so that I can shop for books anywhere.|
|:---:|:---|
|&check;| All pages function correctly on desktop, tablet, and mobile devices.|
|&check;| Navigation adapts to screen size with hamburger menu on mobile.|
|&check;| Images and text are properly sized across devices.|
|&check;| Touch targets are appropriately sized on mobile.|
|&check;| Forms and interactive elements work properly on all devices.|
|&check;| Layout adjusts appropriately at different breakpoints.|

|Passed | **Performance Optimization** - As a user, I want the website to load quickly and respond promptly so that I can shop efficiently.|
|:---:|:---|
|&check;| Pages load within acceptable timeframes.|
|&check;| Images are optimized for web display.|
|&check;| Database queries are efficient.|
|&check;| Cart operations perform without noticeable delay.|
|&check;| Search results appear promptly.|
|&check;| Lighthouse performance scores meet acceptable standards.|

|Passed | **Deployment Setup** - As a developer, I want a streamlined deployment process so that I can efficiently update the live site.|
|:---:|:---|
|&check;| Heroku deployment is configured correctly.|
|&check;| PostgreSQL database is properly set up.|
|&check;| Static files are managed effectively through AWS S3.|
|&check;| Environment variables are properly managed.|
|&check;| Deployment documentation is clear and comprehensive.|

|Passed | **Error Handling and Logging** - As a developer, I want comprehensive error handling and logging so that I can identify and fix issues quickly.|
|:---:|:---|
|&check;| User-friendly error pages are implemented (404, 500).|
|&check;| Form validation errors provide clear guidance to users.|
|&check;| Payment processing errors are handled gracefully.|
|&check;| Template errors are properly caught and managed.|
|&check;| Critical errors trigger appropriate messaging for users.|

#### **Additional Features**

|Passed | **Newsletter Signup** - As a user, I want to subscribe to a newsletter so that I can receive updates and offers.|
|:---:|:---|
|&check;| Newsletter signup form appears in the footer across all pages.|
|&check;| Form submits successfully to Gmail.
|&check;| Validation prevents invalid email submissions.|
|&check;| Success message confirms subscription.|
|&check;| Error handling for failed subscriptions works correctly.|

|Passed | **Contact and Information Pages** - As a user, I want to access information about the store policies and contact options.|
|:---:|:---|
|&check;| Contact form is accessible and functions correctly.|
|&check;| Privacy policy page contains comprehensive information.|
|&check;| Shipping policy information is clearly presented.|
|&check;| Returns policy information is detailed and accessible.|
|&check;| FAQ page addresses common customer questions.|
|&check;| All information pages are accessible from the footer.|

The testing shows that the vast majority of planned features have been successfully implemented and function as intended. The only exception is the Social Login Integration feature, which was designated as a "Should Have" in our MoSCoW prioritization but was not implemented in the current version due to time constraints. This feature will be considered for future development.


































## Bugs and Fixes During the Development Process

The bugs and fixes encountered during development are documented in detail in the TESTING.md file. Each bug includes a description of the issue, error manifestation, root cause, solution implemented, lessons learned, and the impact on the BookLand project. For detailed information about specific bugs, please refer to the individual bug documentation in that file.


### Template Path Resolution Bug

#### Bug Description
During the development of BookLand's user profile functionality, we encountered a "TemplateDoesNotExist" error when attempting to access the profile page. The error indicated that Django was unable to locate the `profiles/profile.html` template, despite the template file existing in what appeared to be the correct location.

#### Error Message
```
TemplateDoesNotExist at /profile/
profiles/profile.html
C:\Users\cpkon\Documents\GitHub\BookLand\profiles\views.py, line 28, in profile
    return render(request, template, context)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

[TemplateDoesNotExist](media/bugs_and_fixes/profile%20page%20can%20not%20be%20displayed.png)

#### Root Cause
The root cause of this issue was a context variable mismatch between the view function and the template. While the template directory structure was correct (`profiles/templates/profiles/profile.html`), the template was expecting a `year_range` variable in the context dictionary to populate the date of birth dropdown selector. Since this variable wasn't being passed from the view function, Django failed to render the template and raised the "TemplateDoesNotExist" error.

This type of error can be particularly confusing because the error message suggests a file path issue rather than a context variable problem.

#### Solution Implemented
We resolved the issue by updating the profile view function to:

1. Pass all required context variables, including `year_range` for the date of birth dropdown
2. Use direct template path specification in the render function instead of storing it in a variable
3. Simplify the context dictionary structure for improved readability

#### First Version of the View Function
```python
@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, template, context)
```

#### Updated View Function:
```python
@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(
        request,
        'profiles/profile.html', # -> Added this explicit path format 
        {
            'form': form,
            'profile': profile,
            'year_range': range(1940, 2006),  # -> Added this required context variable --- !!!!
        }
    )
```

#### Lessons Learned
This bug highlights several important considerations for Django development:

1. **Template Error Messages**: Django's "TemplateDoesNotExist" errors can sometimes be misleading. The issue might not always be a missing template file, but rather problems with the context data needed to render the template.

2. **Context Consistency**: Ensure that all template context variables expected by a template are properly passed from the view function.

3. **Template Debugging**: When encountering template rendering issues, it's helpful to start with a minimal template and gradually add complexity to isolate the problem.

4. **Form and Model Integration**: When working with forms tied to models (like in our UserProfile case), we made sure to include all the necessary context data required for the form to render properly.


#### Impact on BookLand
Resolving this bug ensured that users can successfully access and manage their profile information, which is a critical component of our e-commerce platform. The profile management functionality allows users to:

- Update personal information
- Manage default shipping addresses
- View order history


### Template Literal Display Bug in Wishlist Counter

#### Bug Description
During development of BookLand's navigation bar, we encountered a visual bug where the raw Django template code `{{ wishlist_count|default:"0" }}` was being displayed as literal text next to the wishlist icon instead of being properly evaluated to show the numerical count. Additionally, at screen sizes below 991px (mobile view), there were two wishlist icons appearing side by side.

#### Error Manifestation
The navigation bar displayed the raw template code `{{ wishlist_count|default:"0" }}` instead of the actual count value from the context processor. This occurred in the wishlist badge element in the main navigation. On mobile devices, there was a duplication of the wishlist icon due to improper display class configuration.

![Wishlist Template Bug](media/bugs_and_fixes/wishlist%20counter%20bug.png)

![Duplicating Wishlist Icon](media/bugs_and_fixes/double%20wishlist%20icon.png)

#### Root Cause
The root cause was twofold:

1. **Template Formatting Issue**: The Django template tags in the nav bar were improperly formatted, causing Django's template engine to incorrectly parse the template literals. Specifically, the spacing and newlines within the conditional statements affected template rendering.

2. **Duplicate Mobile Elements**: There were two wishlist icon container divs both marked with the `d-lg-none` class, causing them to both appear on mobile screen sizes, resulting in duplicated elements.

3. **Associated View Function Issue**: There was also a method name typo in the `add_to_wishlist` view function (`get_object_or_create` instead of `get_or_create`), which would have prevented the counter from properly incrementing even if the display was fixed.

#### Solution Implemented
We resolved the issue by:

1. **Proper Template Tag Formatting**: Restructuring the Django template tags with appropriate spacing and proper nesting to ensure correct evaluation:

```html
<span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
  {% if request.user.is_authenticated %}
    {{ wishlist_count|default:"0" }}
  {% else %}
    0
  {% endif %}
</span>
```

2. **Fixed Display Classes**: Removed the duplicate wishlist icon for mobile view and ensured proper display classes were applied to show only one wishlist icon at each screen size.

3. **Method Name Correction**: Fixed the typo in the view function by changing `WishlistItem.objects.get_object_or_create` to `WishlistItem.objects.get_or_create`.

#### Original Navigation Code:
```html
<!-- Wishlist for Mobile (visible on small screen only) -->
<div class="d-lg-none order-lg-3 mx-2">
  <a href="{% url 'wishlist' %}" class="text-danger position-relative">
    <i class="bi bi-heart fs-4"></i>
    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger wishlist-count">
      {% if request.user.is_authenticated %}{{ wishlist_count|default:"0" }}{% endif %}
    </span>
  </a>
</div>

<!-- Wishlist for Desktop (Not visible on small screen) -->
<div class="d-lg-none order-lg-3 mx-2">
  <a href="{% url 'wishlist' %}" class="text-danger position-relative">
    <i class="bi bi-heart fs-4"></i>
    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger wishlist-count">
      {% if request.user.is_authenticated %}{{ wishlist_count|default:"0" }}{% else %}0{% endif %}
    </span>
  </a>
</div>
```

#### Updated Navigation Code:
```html
<!-- Wishlist for Mobile (visible on small screen only) -->
<div class="d-lg-none order-lg-3 mx-2">
  <a href="{% url 'wishlist' %}" class="text-danger position-relative">
    <i class="bi bi-heart fs-4"></i>
    <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
      {% if request.user.is_authenticated %}
        {{ wishlist_count|default:"0" }}
      {% else %}
        0
      {% endif %}
    </span>
  </a>
</div>
```

#### Lessons Learned
This bug highlights several important considerations for Django template development:

1. **Template Tag Formatting**: Django template tags can be sensitive to formatting. When using conditionals and variables, proper spacing and line breaks can help ensure correct rendering. It's important to structure complex template tags with clear indentation and line breaks for readability and proper parsing.

2. **Mobile Responsiveness Testing**: Always test the site at various breakpoints to ensure responsive elements appear correctly. It's easy to create duplicate elements when implementing responsive designs without careful testing.

3. **Consistent Class Naming**: Using consistent class names for similar elements (like `d-lg-none` and `d-none d-lg-block`) helps maintain clarity in responsive layouts.

4. **Code Review for Template Logic**: Regular code reviews for template files are just as important as for Python code, as template errors can lead to confusing user experiences even when the underlying functionality works correctly.

#### Impact on BookLand
Resolving this bug ensured that users can now see the correct numerical count of items in their wishlist, and the navigation bar displays correctly across all device sizes. This supports our goal of providing a consistent and user-friendly experience regardless of the device being used to access BookLand.


### Category Duplication in Navigation and Product Page

#### Bug Description
During the development of BookLand's product browsing functionality, we encountered a visual bug where category names were being displayed multiple times in both the navigation dropdown menu and in the category badges section below the "All Books" header. Specifically, the Philosophy category appeared 2 times, Psychology 2 times, and Self Development 3 times across the interface.

#### Error Manifestation
The navigation dropdown and category badges sections displayed duplicate entries for each category despite having a single definition in our database schema. This created a cluttered and unprofessional appearance in the user interface and could potentially confuse users browsing our product categories.

![Category Dropdown Duplication Bug Screenshot](media/bugs_and_fixes/duplicating%20category.png)

![Category Buttons Duplication Bug Screenshot](media/bugs_and_fixes/duplicating%20category%20buttons.png)

#### Root Cause
The root cause was related to how category data was being queried and displayed in the templates:

1. **Database Query Issue**: The context processor in `products/contexts.py` was retrieving all categories from the database without filtering for uniqueness, potentially including duplicate entries that had been created during development.

2. **Template Processing**: The template logic in both `main_nav.html` and `products.html` was iterating through the entire `all_categories` context variable, displaying each entry regardless of duplication.

3. **Development Data**: During development and testing, categories may have been inadvertently created multiple times with slightly different attributes but the same name.

#### Solution Implemented
Instead of modifying the database or creating migrations to remove duplicates, we opted for a more straightforward approach by implementing fixed category listings in the templates:

1. **Fixed Navigation Dropdown**: We replaced the dynamic category loop in `main_nav.html` with manually defined category links:

```html
<li>
  <a class="dropdown-item" href="{% url 'products' %}?category=philosophy">
    Philosophy
  </a>
</li>
<li>
  <a class="dropdown-item" href="{% url 'products' %}?category=psychology">
    Psychology
  </a>
</li>
<!-- Additional fixed categories -->
```

2. **Fixed Category Badges**: Similarly, we replaced the dynamic category loop in `products.html` with manually defined category badges:

```html
<a href="{% url 'products' %}?category=philosophy" 
   class="category-badge {% if active_category and active_category.name == 'philosophy' %}active{% endif %}">
  Philosophy
</a>
<!-- Additional fixed category badges -->
```

This solution eliminated the duplicate display issues while maintaining all the original functionality.

#### Lessons Learned
This bug highlights several important considerations for e-commerce development:

1. **Data Integrity**: Even in development environments, maintaining data integrity is crucial. Implementing unique constraints on category names from the beginning would have prevented duplicate entries.

2. **Static vs. Dynamic Content**: For relatively stable content like product categories, a static implementation in templates can sometimes be more predictable and maintainable than dynamic database queries.

3. **UI Consistency**: Regular visual testing across the application is essential to catch display anomalies that might not trigger functional errors but can significantly impact user experience.

4. **Solution Trade-offs**: When addressing bugs, consider both database-level solutions (cleaning duplicates, adding constraints) and presentation-level solutions (fixed template elements). Choose the approach that balances immediate fix needs with long-term maintenance.

#### Impact on BookLand
Resolving this bug improved the user experience by presenting a clean, professional category navigation system. The fixed category implementation also provides greater control over the presentation and ordering of our book categories, which are fundamental to helping customers browse our inventory effectively. This aligns with our goal of creating an intuitive and frustration-free shopping experience.


### Cart Removal Button Not Working (X icon replaced with trash icon)

#### Bug Description
During the development of BookLand's shopping cart functionality, we encountered an issue where the trash button for removing items from the cart did not trigger any action when clicked. This prevented users from being able to remove items directly from the cart view without adjusting the quantity to zero, resulting in a suboptimal user experience.

#### Error Manifestation
The cart page correctly displayed the removal button with the trash icon, but clicking on the icon produced no response - the item remained in the cart and no JavaScript errors were visible in the browser console. This was inconsistent with the expected behavior where clicking the button should trigger a request to the `remove_from_cart` view and then reload the page to reflect the changes.

![Cart Removal Button Not Working](media/bugs_and_fixes/x%20to%20delete%20products.png)

#### Root Cause
After investigation, we identified multiple related issues contributing to the problem:

1. **JavaScript Loading Issue**: The JavaScript code responsible for handling the cart interactions was not being properly executed because the `extra_js` block was not properly defined in the base template structure.

2. **Event Binding Problems**: The click event handlers were not being correctly attached to the removal buttons due to DOM structure issues.

3. **DOM Ready Event Conflicts**: The approach of using JavaScript to dynamically create and submit a form had potential timing issues with when the DOM was fully ready.

4. **Template Block Structure**: The base template did not clearly define where custom JavaScript code should be placed in relation to the core scripts.

The primary JavaScript code intended to handle the removal looked like this:

```javascript
// Remove item and reload on click
const removeButtons = document.querySelectorAll('.remove-item');
removeButtons.forEach(button => {
    button.addEventListener('click', function() {
        const itemId = this.id.split('remove_')[1];
        const url = `/cart/remove/${itemId}/`;
        
        $.post(url)
         .done(function() {
             location.reload();
         });
    });
});
```

But this code was not properly executing due to the issues mentioned above.

#### Solution Implemented
We resolved the issue by taking a more straightforward approach, replacing the JavaScript-based solution with a direct form submission approach:

1. **Added proper `extra_js` block to base.html**: 
```html
<!-- Extra JavaScript -->
{% block extra_js %}
{% endblock %}
```

2. **Replaced the JavaScript-dependent remove button with a simple form**:

#### Original Implementation:
```html
<td class="py-3">
    <a class="remove-item text-danger" id="remove_{{ item.item_id }}">
        <i class="bi bi-trash"></i>
    </a>
</td>
```

#### Updated Implementation:
```html
<td class="py-3">
    <form method="POST" action="{% url 'remove_from_cart' item.item_id %}">
        {% csrf_token %}
        <button type="submit" class="btn btn-link text-danger p-0 mt-5">
            <i class="bi bi-trash"></i>
        </button>
    </form>
</td>
```

This solution:

1. Uses a native HTML form submission mechanism instead of relying on JavaScript
2. Properly handles CSRF token requirements for Django POST requests
3. Maintains the same visual appearance with the trash icon
4. Ensures reliable functionality across all browsers and devices

#### Lessons Learned
This bug highlights several important considerations for frontend development in Django:

1. **Simplicity Over Complexity**: Where possible, use native HTML features (like forms) rather than custom JavaScript solutions for basic interactions.

2. **Template Structure**: Ensure that your base template clearly defines all necessary blocks and their proper locations in the DOM hierarchy.

3. **Progressive Enhancement**: Design features to work without JavaScript first, then enhance with JavaScript if needed.

4. **Direct DOM Interaction**: For critical user actions like removing items from a cart, direct form submissions provide more reliable behavior than JavaScript-based interactions.

5. **Template Blocks Positioning**: The position of JavaScript blocks in relation to the DOM content is crucial for proper execution - they should be placed after the content they interact with.

#### Impact on BookLand
Resolving this bug ensures that users can easily remove items from their cart with a single click, providing a smoother and more intuitive shopping experience. This functionality is crucial for the cart management workflow and directly impacts the user's ability to customize their order before proceeding to checkout.

This improvement aligns with our goal of creating a frustration-free shopping experience by ensuring that all interactive elements behave as expected, reducing friction in the purchase process.


## Missing Subtract Filter Bug in Cart Template

#### Bug Description
During the development of BookLand's shopping cart functionality, we encountered a template syntax error when users viewed their shopping carts. The error prevented the cart page from displaying correctly, showing a server error instead. This occurred specifically when attempting to show users how much more they needed to spend to qualify for free shipping.

#### Error Message
```
TemplateSyntaxError at /cart/
Invalid filter: 'subtract'
113 Add ${{ 40|subtract:total|floatformat:2 }} more to get free shipping!
```

![Missing Subtract Filter Bug](media/bugs_and_fixes/tag%20library%20bug.png)

#### Root Cause
The root cause was the use of a `subtract` template filter in the cart.html template that doesn't exist in Django's default template filter library. Django provides many built-in template filters like `add`, `default`, and `floatformat`, but it doesn't include a `subtract` filter for performing subtraction operations in templates.

The problematic code was attempting to calculate how much more a customer needed to spend to reach the $40 free shipping threshold:

```html
{% if total < 40 %}
<div class="alert alert-info mt-2 text-center small">
    Add ${{ 40|subtract:total|floatformat:2 }} more to get free shipping!
</div>
{% endif %}
```

#### Solution Implemented
We resolved the issue by creating a custom template filter in the cart app. This approach followed Django's recommended method for extending template functionality.

#### Implementation Steps:

1. **Created a templatetags directory** in the cart app to hold custom template filters:
   ```
   cart/
     └── templatetags/
         ├── __init__.py
         └── cart_tags.py
   ```

2. **Implemented the subtract filter** in cart_tags.py:
   ```python
   from django import template

   register = template.Library()

   @register.filter
   def subtract(value, arg):
       return value - arg
   ```

3. **Added the template tag loading statement** at the top of cart.html:
   ```html
   {% extends "base.html" %}
   {% load static %}
   {% load cart_tags %}
   ```

4. **Kept the original template code** which could now successfully use the subtract filter:
   ```html
   {% if total < 40 %}
   <div class="alert alert-info mt-2 text-center small">
       Add ${{ 40|subtract:total|floatformat:2 }} more to get free shipping!
   </div>
   {% endif %}
   ```

#### Lessons Learned
This bug highlights several important considerations for Django template development:

1. **Know Your Template Filters**: Django's built-in template filters are powerful but limited. Familiarize yourself with the available options before assuming a particular operation is possible.

2. **Custom Template Filters**: Creating custom template filters is relatively straightforward and provides a clean way to extend Django's template language with application-specific functionality.

3. **Testing All Conditional Paths**: The bug only appeared when viewing a cart with a total less than $40. This emphasizes the importance of testing all conditional paths in templates, especially those involving calculations.

4. **Template Error Messages**: Django's template error messages provide specific line numbers and context, making it easier to locate and fix template-related issues.

#### Impact on BookLand
Resolving this bug ensured that users receive proper feedback about how much more they need to spend to qualify for free shipping, encouraging higher order values while providing a smooth user experience. This feature is aligned with our business goals of increasing average order value while maintaining transparency about shipping costs.

The implementation of the custom template filter also created a reusable component that can be leveraged for other subtraction operations throughout the template system, improving code maintainability and consistency.


### Stripe Payment Processing 'NoneType' Error

#### Bug Description
During the final stages of implementing the BookLand checkout process with Stripe integration, we encountered a critical error when users attempted to complete their orders. When clicking the "Complete Order" button on the checkout page, the application would throw an `AttributeError` stating that a `'NoneType' object has no attribute 'split'`.

#### Error Message
```
AttributeError at /checkout/

'NoneType' object has no attribute 'split'

C:\Users\cpkon\Documents\GitHub\BookLand\checkout\views.py, line 73, in checkout
pid = request.POST.get('client_secret').split('_secret')[0]
```

#### Root Cause
After investigation, we identified multiple issues contributing to the problem:

1. **Missing Error Handling**: The most critical issue was in the checkout view where we attempted to split the `client_secret` string without first checking if it was `None`. This occurred in `views.py`:
   ```python
   pid = request.POST.get('client_secret').split('_secret')[0]
   ```
   When the `client_secret` was not properly passed or was `None`, the code attempted to call the `split()` method on a `NoneType` object, causing the exception.

2. **Stripe Integration Issues**: The client secret value might not be properly passed due to:
   - Incorrect form submission handling
   - Issues with how Stripe was initialized
   - Problems with the hidden fields containing the Stripe parameters

#### Solution Implemented
We implemented a comprehensive solution that addressed both the error and the user interface concerns:

#### 1. Robust Error Handling in the Checkout View
We modified the checkout view to safely handle cases where `client_secret` might be `None` or not contain the expected format:

```python
# Get payment intent ID from client secret if it exists
client_secret = request.POST.get('client_secret')
if client_secret and '_secret' in client_secret:
    pid = client_secret.split('_secret')[0]
    order.stripe_pid = pid
else:
    # Handle missing or malformed client_secret
    # Still create the order but log the issue
    import logging
    logger = logging.getLogger(__name__)
    logger.warning(f"Order created without Stripe PID: client_secret was {client_secret}")
```

This change allows the checkout process to continue even if the Stripe payment intent ID cannot be extracted, while also logging the issue for debugging purposes.

#### 2. Enhanced Error Feedback
We improved the error handling in the JavaScript code to provide clearer feedback when payment processing fails:

```javascript
if (result.error) {
    // If payment processing failed, show the error
    const errorDiv = document.getElementById('card-errors');
    const html = `
        <span role="alert">
            <i class="bi bi-exclamation-circle"></i>
            ${result.error.message}
        </span>
    `;
    errorDiv.innerHTML = html;
    
    // Hide loading overlay and re-enable form
    document.getElementById('payment-processing-overlay').classList.add('d-none');
    card.update({ 'disabled': false });
    document.getElementById('submit-button').disabled = false;
}
```

#### 3. Cleaner Payment UI
We also updated the HTML and CSS for the payment form to provide a more streamlined and user-friendly experience:

```html
<div class="card-element-container border rounded p-3">
    <p class="text-muted mb-3">Enter your card details below:</p>
    <div id="card-element" class="mb-3"></div>
    <div id="card-errors" class="text-danger" role="alert"></div>
</div>
```

Along with CSS enhancements to provide visual feedback during the different states of payment entry (focus, invalid, complete).

#### Lessons Learned
This bug highlights several important considerations for e-commerce payment integrations:

1. **Defensive Programming**: Always check for `None` or empty values before performing operations like string splitting, especially when dealing with external APIs and payment providers.

2. **Graceful Degradation**: Design your payment flow to handle edge cases gracefully, including missing payment identifiers. While proper tracking is important, it shouldn't prevent order completion.

3. **Clear Error Messaging**: Provide meaningful error messages to users when payment processing fails, rather than exposing technical errors.

4. **Visual Feedback**: Use CSS transitions and state changes to give users clear feedback on the status of their payment information entry.

5. **Testing Edge Cases**: Thoroughly test payment processing with various edge cases, including what happens when certain fields are missing or invalid.

#### Impact on BookLand
Resolving this bug was critical for the core functionality of our e-commerce platform. The checkout process is the final and most important conversion point in the user journey. By fixing this issue:

1. Users can now successfully complete their orders without encountering technical errors
2. The checkout form is simpler and more user-friendly without the redundant postal code field
3. The system provides better feedback during the payment process
4. Order data is still properly recorded even in edge cases where Stripe integration has issues

These improvements directly support our business goals by reducing cart abandonment and creating a smoother purchasing experience, which is essential for customer satisfaction and retention.


### Order History Detail View Success Message Bug

#### Bug Description
When users viewed the details of a previous order from their order history page, they were incorrectly presented with a success message stating "Order successfully processed! Your order number is [order number]. A confirmation email will be sent to [email]." This message is appropriate for newly completed orders but confusing when viewing order history, as it gives the impression that a new order was just placed.

#### Error Manifestation
The bug manifested when a user clicked the "View Order Details" button on their order history page. Instead of simply displaying the order information, the system showed a success toast notification and included text suggesting the order was just completed and that a confirmation email would be sent.

![Order History Detail Message Bug](media/bugs_and_fixes/view%20orders%20message%20bug.png)

#### Root Cause
The root cause was that both the initial order confirmation (post-checkout) and the order history detail view were using the same view function and template:

1. **Shared View Function**: The `checkout_success` view function was being used both for redirecting users after a successful checkout and for displaying previous order details from the order history.

2. **Unconditional Success Messaging**: The view function always displayed success messages regardless of the context in which it was called.

3. **Navigation Context**: The template had no way to distinguish between a newly completed order and viewing a historical order.

This happened because when initially building the checkout flow, the `checkout_success` view was designed solely for the post-payment confirmation. Later, when the order history feature was implemented, the same view was reused without adapting it for the different context.

#### Solution Implemented
We resolved the issue by creating a dedicated view function for viewing order details from the order history:

1. **Created a New View Function**:
```python
def order_detail(request, order_number):
    """
    Display details of a specific order
    """
    # Get the order from the database
    order = get_object_or_404(Order, order_number=order_number)
    
    # Render checkout success template with order info, but without messages
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,  # Flag to indicate we're coming from profile page
    }
    
    return render(request, template, context)
```

2. **Added New URL Pattern**:
```python
path('order_detail/<order_number>', views.order_detail, name='order_detail'),
```

3. **Updated the Order History Template**:
```html
<a href="{% url 'order_detail' order.order_number %}" 
   class="btn btn-sm btn-outline-dark">
    View Details
</a>
```

4. **Modified the Order Detail Template** to conditionally display content based on context:
```html
{% if from_profile %}
    <h1>Order Details</h1>
{% else %}
    <h1>Thank You!</h1>
    <p class="lead">Your order has been successfully processed.</p>
{% endif %}

<!-- Bottom of the template -->
{% if from_profile %}
    <a href="{% url 'order_history' %}" class="btn btn-outline-dark">
        <i class="bi bi-arrow-left me-1"></i> Back to Order History
    </a>
{% else %}
    <p>
        A confirmation email has been sent to <strong>{{ order.email }}</strong>.
    </p>
    <a href="{% url 'products' %}" class="btn btn-dark">
        Continue Shopping
    </a>
{% endif %}
```

#### Lessons Learned
This bug highlights several important considerations for web application development:

1. **Context-Aware Views**: Views should be designed with awareness of the different contexts in which they might be used. In this case, viewing a past order is a different user journey than completing a new order.

2. **Context Flags**: Using flags in the context dictionary (such as `from_profile`) allows templates to render appropriately based on how they're being accessed.

3. **Message Appropriateness**: Success messages should only be displayed when an action has been successfully completed, not when simply viewing information.

4. **User Journey Consideration**: It's important to consider the full user journey when reusing components. What makes sense in one part of the journey may be confusing in another.

#### Impact on BookLand
Resolving this bug improved the user experience by providing clear context-appropriate messaging when viewing order details. Users now receive confirmation messages only when actually placing orders, eliminating confusion about whether viewing past orders might have triggered new purchases. This change contributes to our goal of providing a transparent and trustworthy shopping experience.


### AWS S3 Integration Django Version Compatibility Bug

#### Bug Description
During deployment of BookLand to Heroku with AWS S3 for static and media file hosting, we encountered persistent issues where static files were not being properly served despite successful collection. The integration was based on a tutorial from 2020 using an older Django==3.2.25, while our project used Django 5. Despite following the tutorial steps and confirming that static files were being collected, AWS S3 was not correctly serving these files to our application.

#### Error Manifestation
The main symptoms of this issue included:
- CSS and JavaScript not loading on the deployed site
- Missing images and styling throughout the application
- Developer console showing 404 errors for static resources
- Static files were successfully collected using `python manage.py collectstatic` 
- Files appeared to be uploaded to the S3 bucket but were not accessible
- No clear error messages in the application logs indicating the source of the problem

![No static folder on aws](media/bugs_and_fixes/aws.png)

#### Root Cause
After extensive investigation and consultation with tutor support, we identified several root causes:

1. **Django Version Compatibility**: The walkthrough tutorial used Django 3.2, which had different storage handling mechanics compared to Django 5. Most critically, the `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE` settings format had changed between versions.

2. **AWS S3 Configuration**: Despite trying multiple permission configurations (bucket policies, user permissions, ACL settings, and CORS configurations), the files were not being properly served due to mismatched configuration expectations between Django versions.

3. **Storage Backend Implementation**: The custom storage classes from the tutorial were not fully compatible with Django 5.3's storage handling expectations.

4. **Deployment Environment Variables**: Some environment variables were not being recognized correctly in the newer Django context.

The critical difference was in how Django 5.3 handles storage backends. In Django 5.3, the `STORAGES` dictionary setting is used instead of the previous `STATICFILES_STORAGE` and `DEFAULT_FILE_STORAGE` settings.

#### Solution Implemented
After consulting with tutor support, we completely reworked the AWS S3 integration code block, aligning it with Django 5.3's expected configuration format:

#### Original Configuration (Django 3.2 - Not Working):
```python
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'bookland-e-commerce'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

#### Updated Configuration (Django 5. - Working):
```python
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'bookland-e-commerce'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # This part is shared by tutor support for Django 5+
    STORAGES = {
        "default": {
            "BACKEND": "custom_storages.MediaStorage",
        },
        "staticfiles": {"BACKEND": "custom_storages.StaticStorage"},
    }
    STATICFILES_LOCATION = 'static'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

Additionally, we:

1- Updated our custom storage classes to ensure they were compatible with Django 5.3
2- Verified all environment variables were properly set in Heroku
3- Confirmed appropriate bucket permissions and policies
4- Cleared browser caches and tested across multiple browsers to ensure consistent functionality

Lessons Learned:
This bug highlights several important considerations for deployment with Django and AWS:

1- Django Version Awareness: Always check the Django version referenced in tutorials against your project's version, and consult the migration/upgrade guides for changes in configuration patterns.
2- Documentation First: When encountering deployment issues, prioritize official documentation over tutorials, especially for critical infrastructure components.
3- Environment Testing: Test deployment configurations in a staging environment before attempting production deployment.
4- Configuration Verification: Use Django's management commands (python manage.py check --deploy) to verify configurations before deployment.
5- Storage Backend Understanding: Develop a deeper understanding of how Django's storage backends work to better troubleshoot issues related to static and media files.
6- Version Migration Strategy: When upgrading Django versions, create a comprehensive checklist of configuration changes needed between versions.

Impact on BookLand
Resolving this issue was critical for the proper functioning of our site. Without correctly serving static files, the application had no styling, JavaScript functionality, or images - rendering it effectively unusable. With the configuration properly updated for Django 5.3, all static assets are now correctly served from AWS S3, providing:

1- Proper styling and layout throughout the site
2- Functional JavaScript components (cart management, search, etc.)
3- Responsive image loading and improved performance
4- More reliable operation in production
5- Proper separation of concerns between the application server and static content delivery

This fix ensures that users experience BookLand as intended, with full styling, interactivity, and visual assets, rather than as a broken, unstyled application.




