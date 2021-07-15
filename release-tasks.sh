rm -rf app/library/migrations
python manage.py makemigrations library
python manage.py migrate
python manage.py runscript create_books
