echo "Removing old migrations and database..."
rm -rf artisendapi/migrations/*
touch artisendapi/migrations/__init__.py
rm -f db.sqlite3

echo "Creating new migrations..."
python manage.py makemigrations artisendapi

echo "Applying migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser

echo "Loading fixture data..."
python manage.py loaddata mediums.json
python manage.py loaddata skills.json
python manage.py loaddata posts.json

echo "Database reset complete!"