# BookLand Project - Agile Development Process

## **Table of Contents**

* [Agile Methodology](#agile-methodology)
  * [Overview](#overview)
  * [MoSCoW Prioritization](#moscow-prioritization)
  * [Epics](#epics)
  * [User Stories](#user-stories)
  * [Sprint Notes](#sprint-notes)
    * [Sprint 1: Planning & Setup](#sprint-1-planning--setup)
    * [Sprint 2: Core Features Development](#sprint-2-core-features-development)
    * [Sprint 3: Shopping & Checkout](#sprint-3-shopping--checkout)
    * [Sprint 4: Profile & Admin Features](#sprint-4-profile--admin-features) 
    * [Sprint 5: Refinement & Additional Features](#sprint-5-refinement--additional-features)
    * [Sprint 6: Testing & Deployment](#sprint-6-testing--deployment)

## Overview

For the BookLand project, we implemented Agile methodology to manage development efficiently and ensure the final product meets user needs. We followed Agile principles by breaking work into sprints, prioritizing tasks, and conducting regular reviews to adjust course as needed.

Instead of using external project management tools, we tracked progress using a combination of markdown documents and task lists. This lightweight approach allowed us to maintain Agile practices without the overhead of more complex tools that would be necessary for larg teams.

Each sprint was planned with a specific focus area and contained a mix of must-haves, should-haves, and could-haves to ensure steady progress toward a minimum viable product (MVP) while also addressing enhancements when possible.

## MoSCoW Prioritization

We used the MoSCoW method to prioritize features throughout the development process:

### Must Have
- User registration and authentication
- Book browsing and searching
- Shopping cart and checkout
- Payment processing
- Admin book management
- Responsive design

### Should Have
- User profiles with order history
- Wishlist functionality
- Email notifications
- Category filtering
- Sorting options

### Could Have
- Newsletter subscription
- Advanced search filters
- Related book recommendations 
- Social login integration

### Won't Have 
- E-book downloads
- Membership/subscription model
- Author profiles/pages
- Book preview feature
- Advanced analytics

## Epics

### Epic 1: User Management

**Description**: This epic covers all functionality related to user accounts, authentication, and profile management.

**Business Value**: Enables users to create accounts, access personalized features, and securely authenticate with the platform, which is foundational for building customer relationships and tracking user preferences.

**Acceptance Criteria**:
- Users can register, login, and manage their accounts
- User profiles store personal information and preferences
- Password reset functionality works as expected 
- Email notifications for account actions are sent appropriately

### Epic 2: Book Catalog

**Description**: This epic encompasses all functionality related to displaying, organizing, and managing the book inventory.

**Business Value**: Provides the core product browsing experience, allowing customers to discover and learn about books, which directly impacts sales and customer satisfaction.

**Acceptance Criteria**:
- Books are properly categorized and displayed
- Book details include all required information
- Search and filter functionality works efficiently
- Sorting options are available and functional
- Admin can manage the book catalog effectively

### Epic 3: Shopping Experience

**Description**: This epic covers the end-to-end shopping process, from adding items to cart through checkout and payment.

**Business Value**: Creates a seamless purchase flow that maximizes conversion rates and minimizes cart abandonment, directly affecting revenue generation.

**Acceptance Criteria**:
- Shopping cart functions correctly across sessions
- Checkout process is intuitive and efficient
- Payment processing is secure and reliable
- Order confirmation is provided
- Order history is accessible to users

### Epic 4: Admin Features

**Description**: This epic encompasses all administrative functionality needed to manage the BookLand platform.

**Business Value**: Provides the tools necessary for efficient platform operation, inventory management, and customer service, reducing operational costs and improving service quality.

**Acceptance Criteria**:
- Book inventory can be managed  effectivly
- Orders can be processed and tracked
- Customer information can be accessed and managed
- Categories can be created and modified

### Epic 5: Technical Infrastructure

**Description**: This epic covers the technical foundation of the platform, including deployment, performance, and security.

**Business Value**: Ensures the platform is reliable, secure, and performs well, which affects customer trust, satisfaction, and the overall viability of the business.

**Acceptance Criteria**:
- Platform is responsive across all device sizes
- Site performance meets industry standards
- Security measures protect user data
- Deployment pipeline is efficient
- Error handling provides good user experience

## User Stories

### User Management User Stories

#### User Story 1: User Registration

**Story**: As a new visitor, I want to create an account so that I can track my orders and save my preferences.

**Acceptance Criteria**:
- [x] Registration form includes fields for name, email, password
- [x] Email verification is required
- [x] Password strength requirements are enforced
- [x] User receives welcome email upon successful registration
- [x] Duplicate email addresses are not allowed

**Priority**: Must Have

#### User Story 2: User Login

**Story**: As a registered user, I want to securely log in to my account so that I can access my personal information and order history.

**Acceptance Criteria**:
- [x] Login form accepts email/username and password
- [x] "Remember me" functionality is available
- [x] Password reset option is accessible from login form
- [x] User session persists appropriately

**Priority**: Must Have

#### User Story 3: User Profile Management

**Story**: As a logged-in user, I want to view and edit my profile information so that my account reflects my current details.

**Acceptance Criteria**:
- [x] User can view all current profile information
- [x] User can edit name, email, password, and contact information
- [x] User can add/edit shipping addresses
- [x] Changes are saved immediately upon submission
- [x] User receives confirmation of significant changes

**Priority**: Should Have

### Book Catalog User Stories

#### User Story 5: Book Browsing by Category

**Story**: As a customer, I want to browse books by category so that I can easily find books in genres I'm interested in.

**Acceptance Criteria**:
- [x] Categories are clearly displayed on the main page
- [x] Clicking a category shows all books within that category
- [x] Books display cover image, title, author, and price
- [x] Category view is paginated appropriately

**Priority**: Must Have

#### User Story 6: Book Search and Filtering

**Story**: As a customer, I want to search for books and filter results so that I can quickly find specific titles or authors I'm looking for.

**Acceptance Criteria**:
- [x] Search bar is prominently displayed on products and main page
- [x] Search works by title, author, and description
- [x] Search results can be filtered by category
- [x] No results state provides helpful suggestions

**Priority**: Must Have

#### User Story 7: Book Detail View

**Story**: As a customer, I want to view detailed information about a book so that I can make an informed purchase decision.

**Acceptance Criteria**:
- [x] Detail page shows cover image, title, author, price, description, and rating
- [x] Inventory status is clearly displayed
- [x] "Add to cart" and "Add to wishlist" buttons are prominent
- [x] Related books in same category are suggested

**Priority**: Must Have

### Shopping Experience User Stories

#### User Story 8: Shopping Cart Management

**Story**: As a customer, I want to add books to my cart and manage cart contents so that I can prepare for checkout.

**Acceptance Criteria**:
- [x] Books can be added to cart from book detail pages and search results
- [x] Cart icon shows current number of items
- [x] Cart page displays all items with images, titles, and prices
- [x] Quantities can be adjusted on cart page
- [x] Items can be removed from cart
- [x] Cart contents persist between sessions

**Priority**: Must Have

#### User Story 9: Wishlist Functionality

**Story**: As a customer, I want to save books to my wishlist so that I can keep track of books I'm interested in but not ready to purchase.

**Acceptance Criteria**:
- [x] Books can be added to wishlist from book detail pages and search results
- [x] Wishlist is accessible from user profile
- [x] Items can be moved from wishlist to cart
- [x] Items can be removed from wishlist
- [x] Wishlist is saved to user account

**Priority**: Should Have

#### User Story 10: Checkout Process

**Story**: As a customer, I want a streamlined checkout process so that I can complete my purchase quickly and securely.

**Acceptance Criteria**:
- [x] Checkout page collects shipping address
- [x] Checkout page collects payment information
- [x] Order summary is displayed for review
- [x] Shipping options are presented
- [x] Confirmation is required before final submission
- [x] Order confirmation is displayed after successful checkout

**Priority**: Must Have

#### User Story 11: Payment Processing

**Story**: As a customer, I want secure payment processing so that I can confidently complete my purchase.

**Acceptance Criteria**:
- [x] Credit card processing via Stripe is implemented
- [x] Payment information is securely handled
- [x] Payment errors are clearly communicated
- [x] Successful payments trigger order processing
- [x] Checkout confirmation is emailed after successful payment

**Priority**: Must Have

#### User Story 12

# User Story: Order History and Tracking

## Story
As a customer, I want to view my order history and track current orders so that I can monitor my purchases.

## Acceptance Criteria
- [ ] Order history page shows all past orders
- [ ] Order detail view displays complete order information
- [ ] Current order status is clearly indicated
- [ ] Order history is sortable by date and status
- [ ] Order details can be printed or saved as PDF

## Tasks
- [ ] Design order history page
- [ ] Implement order detail view
- [ ] Create order status indicators
- [ ] Set up sorting functionality
- [ ] Implement print/save functionality

## Priority
Should Have

### Admin Features User Stories

#### User Story 13

# User Story: Admin Dashboard

## Story
As an admin, I want a comprehensive dashboard so that I can quickly access key metrics and platform management functions.

## Acceptance Criteria
- [ ] Dashboard displays sales summary
- [ ] Recent orders are listed with status
- [ ] Low inventory items are highlighted
- [ ] Quick access links to management functions are provided
- [ ] Key metrics are visualized with charts

## Tasks
- [ ] Design dashboard layout
- [ ] Implement sales summary component
- [ ] Create recent orders list
- [ ] Set up inventory alerts
- [ ] Implement data visualization components

## Priority
Should Have

#### User Story 14

# User Story: Admin Book Management

## Story
As an admin, I want to add, edit, and remove books from the catalog so that I can keep the inventory up to date.

## Acceptance Criteria
- [ ] Book creation form includes all necessary fields
- [ ] Existing books can be edited
- [ ] Books can be marked as out of stock
- [ ] Books can be permanently removed
- [ ] Bulk actions are available for efficiency

## Tasks
- [ ] Design book management interface
- [ ] Implement book CRUD operations
- [ ] Create image upload functionality
- [ ] Set up inventory status management
- [ ] Implement bulk action functionality

## Priority
Must Have

#### User Story 15

# User Story: Order Management

## Story
As an admin, I want to view and process orders so that I can fulfill customer purchases efficiently.

## Acceptance Criteria
- [ ] Orders list shows all orders with status and date
- [ ] Orders can be filtered by status, date, and customer
- [ ] Order details show complete purchase information
- [ ] Order status can be updated (processing, shipped, delivered)
- [ ] Order cancellation is supported with reason tracking

## Tasks
- [ ] Design order list and detail views
- [ ] Implement order filtering functionality
- [ ] Create order status management
- [ ] Set up order detail display
- [ ] Implement order cancellation process

## Priority
Must Have

#### User Story 16

# User Story: Category Management

## Story
As an admin, I want to create and manage book categories so that books are properly organized for customers.

## Acceptance Criteria
- [ ] Categories can be created with name and description
- [ ] Categories can be edited and deleted
- [ ] Categories can be arranged in hierarchical structure
- [ ] Books can be assigned to multiple categories
- [ ] Category visibility can be toggled

## Tasks
- [ ] Design category management interface
- [ ] Implement category CRUD operations
- [ ] Create hierarchical category structure
- [ ] Set up book-category relationship management
- [ ] Implement category visibility controls

## Priority
Must Have

### Technical Infrastructure User Stories

#### User Story 17

# User Story: Responsive Design Implementation

## Story
As a user, I want the website to work well on all my devices so that I can shop for books anywhere.

## Acceptance Criteria
- [ ] All pages function correctly on desktop, tablet, and mobile
- [ ] Navigation adapts to screen size
- [ ] Images and text are properly sized across devices
- [ ] Touch targets are appropriately sized on mobile
- [ ] Performance is consistent across device types

## Tasks
- [ ] Implement responsive grid system
- [ ] Create mobile navigation component
- [ ] Set up responsive image handling
- [ ] Test and optimize touch targets
- [ ] Perform cross-device testing

## Priority
Must Have

#### User Story 18

# User Story: Performance Optimization

## Story
As a user, I want the website to load quickly and respond promptly so that I can shop efficiently.

## Acceptance Criteria
- [ ] Pages load in under 3 seconds
- [ ] Images are optimized for quick loading
- [ ] Database queries are efficient
- [ ] Client-side rendering is optimized
- [ ] Core Web Vitals meet Google's requirements

## Tasks
- [ ] Implement image optimization
- [ ] Set up database query monitoring
- [ ] Optimize database indexes
- [ ] Implement lazy loading for images
- [ ] Set up performance monitoring

## Priority
Should Have

#### User Story 19

# User Story: Deployment Setup

## Story
As a developer, I want a streamlined deployment process so that I can efficiently update the live site.

## Acceptance Criteria
- [ ] Heroku deployment is configured
- [ ] PostgreSQL database is properly set up
- [ ] Static files are served via Whitenoise
- [ ] Environment variables are properly managed
- [ ] Deployment can be triggered from version control

## Tasks
- [ ] Set up Heroku application
- [ ] Configure PostgreSQL database connection
- [ ] Implement Whitenoise for static file serving
- [ ] Set up environment variable management
- [ ] Configure CI/CD pipeline

## Priority
Must Have

#### User Story 20

# User Story: Error Handling and Logging

## Story
As a developer, I want comprehensive error handling and logging so that I can identify and fix issues quickly.

## Acceptance Criteria
- [ ] User-friendly error pages are implemented
- [ ] Server errors are properly logged
- [ ] Client-side errors are tracked
- [ ] Critical errors trigger notifications
- [ ] Logs are easily accessible and searchable

## Tasks
- [ ] Design error pages
- [ ] Set up server-side logging
- [ ] Implement client-side error tracking
- [ ] Configure error notifications
- [ ] Set up log storage and search functionality

## Priority
Should Have






## Sprint Notes

Below is a summary of work accomplished and lessons learned from each sprint.

### Sprint 1: Planning & Setup

**Duration**: 1 week 

**Focus**: Project setup, initial structure, and environment configuration

**Tasks Completed**:
- Created project repository and Django project structure
- Set up database models for books and categories
- Implemented basic authentication using Django-allauth
- Configured project settings and URL routing
- Created initial templates for base layout

**Challenges & Learnings**:
- Initially struggled with setting up the Django-allauth configuration correctly but resolved by consulting documentation
- Had to refactor the models once after realizing the book model needed additional fields
- Learned to use Django's template inheritance more efficiently

**Bug Fixes**:
- Fixed an issue where static files weren't loading correctly

**Outcome**: 
Successfully completed initial setup ahead of schedule, allowing more time for feature development in the next sprint. The project structure now provides a solid foundation for implementing the core features.

### Sprint 2: Core Features Development

**Duration**: 1 week 

**Focus**: Implement book catalog, category filtering, and search functionality

**Tasks Completed**:
- Created book catalog views and templates
- Implemented category filtering functionality
- Added search functionality with results filtering
- Developed product detail page with all required information
- Created admin interface for book management

**Challenges & Learnings**:
- Fixed category duplication issue in navigation and product page
- Had to rework the search query logic to improve performance
- Spent additional time on responsive image handling for book covers

**Bug Fixes**:
- Fixed category duplication in navigation and product page
- Resolved an issue with search not handling empty search terms correctly

**Outcome**: 
Core browsing and search functionality is now working well. Users can browse by category, search for specific books, and view detailed information about each book. The product detail page also shows related books from the same category.

### Sprint 3: Shopping & Checkout

**Duration**: 1 week 

**Focus**: Shopping cart, wishlist, and checkout process

**Tasks Completed**:
- Implemented shopping cart functionality with session storage
- Created wishlist feature for logged-in users
- Developed checkout process with form validation
- Integrated Stripe for payment processing
- Added order confirmation and email notifications

**Challenges & Learnings**:
- Cart removal button (X icon) wasn't working - fixed by replacing with trash icon and form submission
- Stripe payment integration took longer than expected due to debugging webhook handlers(also too much bootstrap and css styling caused a bug)
- Had to revise the shopping cart context processor to improve performance

**Bug Fixes**:
- Fixed cart removal button not working by implementing a more direct form-based approach
- Resolved a "NoneType object has no attribute 'split'" error in Stripe payment processing

**Outcome**: 
Users can now add items to cart, move items between wishlist and cart, and complete purchases securely. The checkout process is streamlined and intuitive, with proper error handling and confirmation emails.

### Sprint 4: Profile & Admin Features

**Duration**: 1 week 

**Focus**: User profiles, order history, and admin features

**Tasks Completed**:
- Implemented user profile management
- Created order history and order details views
- Added default delivery information storage
- Enhanced admin interface for order management
- Implemented webhook handler to create orders from Stripe events

**Challenges & Learnings**:
- Template path resolution bug with profiles page required explicit path format
- Order history detail view showed incorrect success message
- Realized the importance of context flags to conditionally render templates based on access path

**Bug Fixes**:
- Fixed template path resolution bug in profile view
- Created dedicated order_detail view to separate from checkout_success flow
- Fixed wishlist counter template literals display bug

**Outcome**: 
Users can now manage their profiles, view order history, and save default delivery information. Admins have enhanced tools for managing orders and inventory.

### Sprint 5: Refinement & Additional Features

**Duration**: 1 week 

**Focus**: Extra pages, UI refinements, and additional features

**Tasks Completed**:
- Added about, contact, FAQ, and policy pages
- Implemented newsletter signup in footer
- Enhanced navigation and mobile responsiveness
- Added toast notifications for user feedback
- Created free shipping threshold indicator in cart

**Challenges & Learnings**:
- Missing `subtract` template filter for free shipping threshold calculation
- Mobile responsive menu required significant adjustments
- Toast notification positioning needed fine-tuning

**Bug Fixes**:
- Created custom `subtract` template filter for cart calculations
- Fixed responsive layout issues on mobile devices
- Resolved toast notification stacking problem

**Outcome**: 
The site now has a complete set of information pages and enhanced features that improve the user experience. The UI is polished and responsive across all device sizes.

### Sprint 6: Testing & Deployment

**Duration**: 1 week 

**Focus**: Testing, bug fixing, and deployment preparation

**Tasks Completed**:
- Conducted comprehensive testing across all features
- Fixed remaining bugs and inconsistencies
- Optimized database queries for performance
- Prepared deployment configuration
- Created documentation (README, TESTING, DEPLOYMENT)

**Challenges & Learnings**:
- Discovered and fixed several edge cases in shopping cart and checkout
- Stripe webhook testing revealed some error handling improvements needed
- Had to optimize several database queries to improve page load times

**Bug Fixes**:
- Fixed payment processing edge cases
- Optimized image loading and database queries
- Resolved inconsistencies in responsive layout

**Outcome**: 
The BookLand project is now thoroughly tested, optimized, and ready for deployment. All core features are working correctly, and the user experience is polished across device sizes.

## Conclusion

The Agile approach proved effective for managing the BookLand project development. By prioritizing features using MoSCoW and organizing work into focused sprints, we were able to deliver a fully functional e-commerce platform that meets user needs.

Key benefits of using Agile for this project:

1. **Iterative Development**: Building features incrementally allowed us to test and refine as we went rather than waiting until the end.

2. **Prioritization**: The MoSCoW method helped ensure that essential features were completed first, guaranteeing a functional MVP even with time constraints.

3. **Flexibility**: When bugs or issues arose, we could adjust sprint contents to address critical problems without derailing the overall project timeline.

4. **Focus**: Breaking work into sprints with specific goals helped maintain focus on completing cohesive feature sets rather than jumping between unrelated tasks.




