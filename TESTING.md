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


