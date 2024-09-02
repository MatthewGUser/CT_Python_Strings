# [ Task 1 ]

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    # Replace each keyword in the review with its uppercase version
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    
    # Print the modified review
    print(review)


# [ Task 2 ]

# Calculate amount sentiment for each review
def sentiment_tally(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    
    total_positive = 0
    total_negative = 0
    
    # Itterate through each review
    for review in reviews:
        review_lower = review.lower()
        
        # Count positive words
        for word in positive_words:
            total_positive += review_lower.count(word)
        
        # Count negative words
        for word in negative_words:
            total_negative += review_lower.count(word)
    
    return total_positive, total_negative

# Get the sentiment tally
positive_count, negative_count = sentiment_tally(reviews)
print(f"Total positive words: {positive_count}")
print(f"Total negative words: {negative_count}")

# [ Task 3 ]

# Summarize given review
def create_summary(review, max_length=30):
    # Review less than 30 characters so no need
    if len(review) <= max_length:
        return review  # Return the review as is if it's already within the limit

    # Split the review into words
    words = review.split()
    summary = ""
    total_length = 0

    # Itterate through each word
    for word in words:
        # Stop adding since it would exceed:
        if total_length + len(word) + 1 > max_length:
            break

        summary += (word + " ")
        total_length += len(word)

    summary = summary.strip() + "..."
    return summary

# Generate and print summaries for each review
for review in reviews:
    summary = create_summary(review)
    print(summary)