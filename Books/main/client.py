import requests

def create_book(title, author):
    headers={
        'title':title,
        'author':author
    }
    response = requests.post('http://127.0.0.1:8000/books/', headers)
    print(f"New book {title} by {author} has been created,\n\n")

def get_all_books():
    response = requests.get('http://127.0.0.1:8000/books/')
    return response.json()


create_book('Parallel worlds', 'Michio Kaku')

books = get_all_books()
for book in books:
    print(f"Book {book['id']}:")
    print(f"  Title: {book['title']}")
    print(f"  By: {book['author']}")