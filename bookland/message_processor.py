from django.contrib import messages


def categorize_messages(request):
    """
    Context processor to categorize messages as shopping-related or not.
    Shopping-related messages will display with cart information.
    Other messages will display as standard toast notifications.
    """
    if not hasattr(request, 'session'):
        return {}

    # Get messages from session
    storage = messages.get_messages(request)
    shopping_messages = []
    other_messages = []

    # Comprehensive list of shopping-related phrases and keywords
    shopping_phrases = [
        # Cart actions
        'added to cart', 'added to your cart', 'updated cart', 'removed from cart', 
        'removed from your cart', 'updated quantity', 'in your cart', 'to cart',
        'cart updated', 'adjusted cart', 'cart quantity', 'item added',
        
        # Wishlist actions
        'wishlist', 'added to wishlist', 'removed from wishlist', 'saved for later',
        'moved to cart', 'added to your wishlist', 'added to your saved items',
        
        # Checkout and order actions
        'checkout complete', 'order confirmed', 'order placed', 'thank you for your order',
        'purchase complete', 'payment confirmed', 'shipping info', 'delivery',
        'successfully processed', 'order number', 'order summary', 'confirmation',
        
        # Product-specific mentions
        'book', 'title', 'author', 'quantity', 'products', 'items'
    ]

    # Process all messages
    for message in storage:
        # Convert message to string and check for shopping-related content
        message_text = str(message).lower()
        
        # Check if message contains any shopping-related phrases
        is_shopping_related = any(phrase in message_text for phrase in shopping_phrases)
        
        # Additional check for product-specific messages that might mention specific actions
        product_actions = ['added', 'removed', 'updated', 'purchased', 'ordered']
        has_product_action = any(action in message_text for action in product_actions)
        
        # Categorize the message
        if is_shopping_related or has_product_action:
            shopping_messages.append(message)
        else:
            other_messages.append(message)

    # Return both categories of messages
    return {
        'shopping_messages': shopping_messages,
        'other_messages': other_messages,
    }