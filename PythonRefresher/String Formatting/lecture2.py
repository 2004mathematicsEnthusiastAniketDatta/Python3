def emoji_generator(text):
    """Convert text expressions to emojis"""
    emoji_map = {
        # Happy emotions
        ':)': '😊',
        ':-)': '😊',
        ':D': '😃',
        ':-D': '😃',
        'XD': '😆',
        ':P': '😛',
        ':-P': '😛',
        
        # Sad emotions
        ':(': '😢',
        ':-(': '😢',
        ":'(": '😭',
        
        # Other emotions
        ';)': '😉',
        ';-)': '😉',
        ':|': '😐',
        ':-|': '😐',
        ':o': '😮',
        ':-o': '😮',
        '<3': '❤️',
        '</3': '💔',
        
        # Words to emojis
        'happy': '😊',
        'sad': '😢',
        'love': '❤️',
        'fire': '🔥',
        'star': '⭐',
        'heart': '❤️',
        'thumbsup': '👍',
        'thumbsdown': '👎',
        'clap': '👏',
        'party': '🎉'
    }
    
    result = text
    for expression, emoji in emoji_map.items():
        result = result.replace(expression, emoji)
    
    return result

# Example usage
if __name__ == "__main__":
    # Test the emoji generator
    test_texts = [
        "I'm so happy :D",
        "That's fire! thumbsup",
        "Feeling sad :( today",
        "I love this <3",
        "Great job! clap party"
    ]
    
    print("Emoji Generator Demo:")
    print("-" * 30)
    
    for text in test_texts:
        converted = emoji_generator(text)
        print(f"Input:  {text}")
        print(f"Output: {converted}")
        print()