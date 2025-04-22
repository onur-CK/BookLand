# Template Path Resolution Bug

## Bug Description
During the development of BookLand's user profile functionality, we encountered a "TemplateDoesNotExist" error when attempting to access the profile page. The error indicated that Django was unable to locate the `profiles/profile.html` template, despite the template file existing in what appeared to be the correct location.

## Error Message
```
TemplateDoesNotExist at /profile/
profiles/profile.html
C:\Users\cpkon\Documents\GitHub\BookLand\profiles\views.py, line 28, in profile
    return render(request, template, context)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

[TemplateDoesNotExist](media/bugs_and_fixes/profile%20page%20can%20not%20be%20displayed.png)

## Root Cause
The root cause of this issue was a context variable mismatch between the view function and the template. While the template directory structure was correct (`profiles/templates/profiles/profile.html`), the template was expecting a `year_range` variable in the context dictionary to populate the date of birth dropdown selector. Since this variable wasn't being passed from the view function, Django failed to render the template and raised the "TemplateDoesNotExist" error.

This type of error can be particularly confusing because the error message suggests a file path issue rather than a context variable problem.

## Solution Implemented
We resolved the issue by updating the profile view function to:

1. Pass all required context variables, including `year_range` for the date of birth dropdown
2. Use direct template path specification in the render function instead of storing it in a variable
3. Simplify the context dictionary structure for improved readability

### First Version of the View Function
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

### Updated View Function:
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

## Lessons Learned
This bug highlights several important considerations for Django development:

1. **Template Error Messages**: Django's "TemplateDoesNotExist" errors can sometimes be misleading. The issue might not always be a missing template file, but rather problems with the context data needed to render the template.

2. **Context Consistency**: Ensure that all template context variables expected by a template are properly passed from the view function.

3. **Template Debugging**: When encountering template rendering issues, it's helpful to start with a minimal template and gradually add complexity to isolate the problem.

4. **Form and Model Integration**: When working with forms tied to models (like in our UserProfile case), we made sure to include all the necessary context data required for the form to render properly.


## Impact on BookLand
Resolving this bug ensured that users can successfully access and manage their profile information, which is a critical component of our e-commerce platform. The profile management functionality allows users to:

- Update personal information
- Manage default shipping addresses
- View order history


# Template Literal Display Bug in Wishlist Counter

## Bug Description
During development of BookLand's navigation bar, we encountered a visual bug where the raw Django template code `{{ wishlist_count|default:"0" }}` was being displayed as literal text next to the wishlist icon instead of being properly evaluated to show the numerical count. Additionally, at screen sizes below 991px (mobile view), there were two wishlist icons appearing side by side.

## Error Manifestation
The navigation bar displayed the raw template code `{{ wishlist_count|default:"0" }}` instead of the actual count value from the context processor. This occurred in the wishlist badge element in the main navigation. On mobile devices, there was a duplication of the wishlist icon due to improper display class configuration.

![Wishlist Template Bug](media/bugs_and_fixes/wishlist%20counter%20bug.png)

![Duplicating Wishlist Icon](media/bugs_and_fixes/double%20wishlist%20icon.png)

## Root Cause
The root cause was twofold:

1. **Template Formatting Issue**: The Django template tags in the nav bar were improperly formatted, causing Django's template engine to incorrectly parse the template literals. Specifically, the spacing and newlines within the conditional statements affected template rendering.

2. **Duplicate Mobile Elements**: There were two wishlist icon container divs both marked with the `d-lg-none` class, causing them to both appear on mobile screen sizes, resulting in duplicated elements.

3. **Associated View Function Issue**: There was also a method name typo in the `add_to_wishlist` view function (`get_object_or_create` instead of `get_or_create`), which would have prevented the counter from properly incrementing even if the display was fixed.

## Solution Implemented
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

### Original Navigation Code:
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

### Updated Navigation Code:
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

## Lessons Learned
This bug highlights several important considerations for Django template development:

1. **Template Tag Formatting**: Django template tags can be sensitive to formatting. When using conditionals and variables, proper spacing and line breaks can help ensure correct rendering. It's important to structure complex template tags with clear indentation and line breaks for readability and proper parsing.

2. **Mobile Responsiveness Testing**: Always test the site at various breakpoints to ensure responsive elements appear correctly. It's easy to create duplicate elements when implementing responsive designs without careful testing.

3. **Consistent Class Naming**: Using consistent class names for similar elements (like `d-lg-none` and `d-none d-lg-block`) helps maintain clarity in responsive layouts.

4. **Code Review for Template Logic**: Regular code reviews for template files are just as important as for Python code, as template errors can lead to confusing user experiences even when the underlying functionality works correctly.

## Impact on BookLand
Resolving this bug ensured that users can now see the correct numerical count of items in their wishlist, and the navigation bar displays correctly across all device sizes. This supports our goal of providing a consistent and user-friendly experience regardless of the device being used to access BookLand.


# Category Duplication in Navigation and Product Page

## Bug Description
During the development of BookLand's product browsing functionality, we encountered a visual bug where category names were being displayed multiple times in both the navigation dropdown menu and in the category badges section below the "All Books" header. Specifically, the Philosophy category appeared 2 times, Psychology 2 times, and Self Development 3 times across the interface.

## Error Manifestation
The navigation dropdown and category badges sections displayed duplicate entries for each category despite having a single definition in our database schema. This created a cluttered and unprofessional appearance in the user interface and could potentially confuse users browsing our product categories.

![Category Dropdown Duplication Bug Screenshot](media/bugs_and_fixes/duplicating%20category.png)

![Category Buttons Duplication Bug Screenshot](media/bugs_and_fixes/duplicating%20category%20buttons.png)

## Root Cause
The root cause was related to how category data was being queried and displayed in the templates:

1. **Database Query Issue**: The context processor in `products/contexts.py` was retrieving all categories from the database without filtering for uniqueness, potentially including duplicate entries that had been created during development.

2. **Template Processing**: The template logic in both `main_nav.html` and `products.html` was iterating through the entire `all_categories` context variable, displaying each entry regardless of duplication.

3. **Development Data**: During development and testing, categories may have been inadvertently created multiple times with slightly different attributes but the same name.

## Solution Implemented
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

## Lessons Learned
This bug highlights several important considerations for e-commerce development:

1. **Data Integrity**: Even in development environments, maintaining data integrity is crucial. Implementing unique constraints on category names from the beginning would have prevented duplicate entries.

2. **Static vs. Dynamic Content**: For relatively stable content like product categories, a static implementation in templates can sometimes be more predictable and maintainable than dynamic database queries.

3. **UI Consistency**: Regular visual testing across the application is essential to catch display anomalies that might not trigger functional errors but can significantly impact user experience.

4. **Solution Trade-offs**: When addressing bugs, consider both database-level solutions (cleaning duplicates, adding constraints) and presentation-level solutions (fixed template elements). Choose the approach that balances immediate fix needs with long-term maintenance.

## Impact on BookLand
Resolving this bug improved the user experience by presenting a clean, professional category navigation system. The fixed category implementation also provides greater control over the presentation and ordering of our book categories, which are fundamental to helping customers browse our inventory effectively. This aligns with our goal of creating an intuitive and frustration-free shopping experience.


# Cart Removal Button Not Working (X icon replaced with trash icon)

## Bug Description
During the development of BookLand's shopping cart functionality, we encountered an issue where the trash button for removing items from the cart did not trigger any action when clicked. This prevented users from being able to remove items directly from the cart view without adjusting the quantity to zero, resulting in a suboptimal user experience.

## Error Manifestation
The cart page correctly displayed the removal button with the trash icon, but clicking on the icon produced no response - the item remained in the cart and no JavaScript errors were visible in the browser console. This was inconsistent with the expected behavior where clicking the button should trigger a request to the `remove_from_cart` view and then reload the page to reflect the changes.

![Cart Removal Button Not Working](media/bugs_and_fixes/x%20to%20delete%20products.png)

## Root Cause
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

## Solution Implemented
We resolved the issue by taking a more straightforward approach, replacing the JavaScript-based solution with a direct form submission approach:

1. **Added proper `extra_js` block to base.html**: 
```html
<!-- Extra JavaScript -->
{% block extra_js %}
{% endblock %}
```

2. **Replaced the JavaScript-dependent remove button with a simple form**:

### Original Implementation:
```html
<td class="py-3">
    <a class="remove-item text-danger" id="remove_{{ item.item_id }}">
        <i class="bi bi-trash"></i>
    </a>
</td>
```

### Updated Implementation:
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

## Lessons Learned
This bug highlights several important considerations for frontend development in Django:

1. **Simplicity Over Complexity**: Where possible, use native HTML features (like forms) rather than custom JavaScript solutions for basic interactions.

2. **Template Structure**: Ensure that your base template clearly defines all necessary blocks and their proper locations in the DOM hierarchy.

3. **Progressive Enhancement**: Design features to work without JavaScript first, then enhance with JavaScript if needed.

4. **Direct DOM Interaction**: For critical user actions like removing items from a cart, direct form submissions provide more reliable behavior than JavaScript-based interactions.

5. **Template Blocks Positioning**: The position of JavaScript blocks in relation to the DOM content is crucial for proper execution - they should be placed after the content they interact with.

## Impact on BookLand
Resolving this bug ensures that users can easily remove items from their cart with a single click, providing a smoother and more intuitive shopping experience. This functionality is crucial for the cart management workflow and directly impacts the user's ability to customize their order before proceeding to checkout.

This improvement aligns with our goal of creating a frustration-free shopping experience by ensuring that all interactive elements behave as expected, reducing friction in the purchase process.