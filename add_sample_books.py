import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from books.models import Book

# Clear existing books (optional)
Book.objects.all().delete()

# Sample books data
books_data = [
    {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'description': 'A classic American novel set in the Jazz Age, exploring themes of wealth, love, and the American Dream.',
        'price': 299.00,
        'isbn': '9780743273565',
        'stock': 15,
        'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=400&h=500&fit=crop'
    },
    {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'description': 'A gripping tale of racial injustice and childhood innocence in the American South.',
        'price': 349.00,
        'isbn': '9780061120084',
        'stock': 20,
        'image_url': 'https://images.unsplash.com/photo-1512820790803-83ca734da794?w=400&h=500&fit=crop'
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'description': 'A dystopian masterpiece about totalitarianism, surveillance, and the power of language.',
        'price': 399.00,
        'isbn': '9780451524935',
        'stock': 25,
        'image_url': 'https://images.unsplash.com/photo-1495446815901-a7297e633e8d?w=400&h=500&fit=crop'
    },
    {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'description': 'A timeless romance exploring manners, morality, and marriage in Georgian England.',
        'price': 279.00,
        'isbn': '9780141439518',
        'stock': 18,
        'image_url': 'https://images.unsplash.com/photo-1543002588-bfa74002ed7e?w=400&h=500&fit=crop'
    },
    {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'description': 'An epic fantasy adventure of Bilbo Baggins and his quest to reclaim treasure from a dragon.',
        'price': 449.00,
        'isbn': '9780547928227',
        'stock': 12,
        'image_url': 'https://images.unsplash.com/photo-1621351183012-e2f9972dd9bf?w=400&h=500&fit=crop'
    },
    {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'description': 'A controversial classic about teenage rebellion and alienation in 1950s America.',
        'price': 329.00,
        'isbn': '9780316769174',
        'stock': 22,
        'image_url': 'https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=400&h=500&fit=crop'
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'description': 'The magical beginning of Harry Potter\'s journey at Hogwarts School of Witchcraft and Wizardry.',
        'price': 499.00,
        'isbn': '9780439708180',
        'stock': 30,
        'image_url': 'https://images.unsplash.com/photo-1551029506-0807df4e2031?w=400&h=500&fit=crop'
    },
    {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'description': 'An epic high-fantasy trilogy following the quest to destroy the One Ring.',
        'price': 899.00,
        'isbn': '9780544003415',
        'stock': 10,
        'image_url': 'https://images.unsplash.com/photo-1612932808116-4b5a5e65a82b?w=400&h=500&fit=crop'
    },
    {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'description': 'A philosophical novel about following your dreams and finding your personal legend.',
        'price': 250.00,
        'isbn': '9780062315007',
        'stock': 28,
        'image_url': 'https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?w=400&h=500&fit=crop'
    },
    {
        'title': 'Think Like a Monk',
        'author': 'Jay Shetty',
        'description': 'Transform your life with ancient wisdom for modern living and mindfulness.',
        'price': 399.00,
        'isbn': '9781982134488',
        'stock': 35,
        'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=500&fit=crop'
    }
]

# Create books
for book_data in books_data:
    book = Book.objects.create(**book_data)
    print(f"✅ Created: {book.title}")

print(f"\n🎉 Successfully added {len(books_data)} books!")