'''

import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from catalog.models import Author, Genre, Language, Book, BookInstance

class Command(BaseCommand):
    """
    Classe per il comando Django custom che popola il database con dati di esempio.
    """
    help = 'Populates the database with sample catalog data'

    def handle(self, *args, **options):
        # Pulizia dei dati esistenti nel database
        self.stdout.write('Clearing existing data...')
        BookInstance.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()
        Genre.objects.all().delete()
        Language.objects.all().delete()

        # Creazione di un superuser se non esiste già
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
            self.stdout.write(self.style.SUCCESS('Superuser created'))
'''
        # Creazione di generi letterari di esempio
        self.stdout.write('Creating genres...')
        genres_data = ['Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Thriller', 'Romance',
                       'Classics', 'Non-fiction', 'History', 'Biography', 'Science', 'Self-help']
        genres = []
        for genre_name in genres_data:
            genre = Genre.objects.create(name=genre_name)
            genres.append(genre)
            self.stdout.write(f'Created genre: {genre}')

        # Creazione delle lingue disponibili per i libri
        self.stdout.write('Creating languages...')
        languages_data = ['English', 'Spanish', 'French', 'German', 'Russian', 'Japanese', 'Chinese']
        languages = []
        for language_name in languages_data:
            language = Language.objects.create(name=language_name)
            languages.append(language)
            self.stdout.write(f'Created language: {language}')

        # Creazione di autori di esempio
        self.stdout.write('Creating authors...')
        authors_data = [
            {'first_name': 'Jane', 'last_name': 'Austen', 'date_of_birth': date(1775, 12, 16), 'date_of_death': date(1817, 7, 18)},
            {'first_name': 'F. Scott', 'last_name': 'Fitzgerald', 'date_of_birth': date(1896, 9, 24), 'date_of_death': date(1940, 12, 21)},
            {'first_name': 'George', 'last_name': 'Orwell', 'date_of_birth': date(1903, 6, 25), 'date_of_death': date(1950, 1, 21)},
            {'first_name': 'J.K.', 'last_name': 'Rowling', 'date_of_birth': date(1965, 7, 31), 'date_of_death': None},
            {'first_name': 'Harper', 'last_name': 'Lee', 'date_of_birth': date(1926, 4, 28), 'date_of_death': date(2016, 2, 19)},
        ]
        authors = []
        for author_data in authors_data:
            author = Author.objects.create(**author_data)
            authors.append(author)
            self.stdout.write(f'Created author: {author}')

        # Creazione di libri di esempio
        self.stdout.write('Creating books...')
        books_data = [
            {'title': 'Pride and Prejudice', 'summary': 'A classic novel.', 'isbn': '9780141439518', 'author': authors[0], 'language': languages[0], 'genre_names': ['Classics', 'Romance', 'Fiction']},
            {'title': '1984', 'summary': 'A dystopian novel.', 'isbn': '9780451524935', 'author': authors[2], 'language': languages[0], 'genre_names': ['Science Fiction', 'Classics', 'Fiction']},
        ]
        books = []
        for book_data in books_data:
            genre_names = book_data.pop('genre_names')  # Rimuove i generi dalla struttura
            book = Book.objects.create(**book_data)  # Crea il libro
            for genre_name in genre_names:
                genre = Genre.objects.get(name=genre_name)  # Recupera il genere
                book.genre.add(genre)  # Associa il genere al libro
            books.append(book)
            self.stdout.write(f'Created book: {book}')

            # Creazione di copie del libro con stato casuale
            for _ in range(random.randint(1, 5)):
                status_choices = ['m', 'o', 'a', 'r']  # Stati disponibili per i libri
                status = random.choice(status_choices)  # Seleziona uno stato casuale
                due_back = date.today() + timedelta(days=random.randint(1, 30)) if status == 'o' else None
                book_instance = BookInstance.objects.create(
                    book=book,
                    imprint=f'{book.title} {random.randint(1, 10)}th Edition',
                    status=status,
                    due_back=due_back,
                )
                self.stdout.write(f'  Created instance: {book_instance.id} ({book_instance.status})')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

  