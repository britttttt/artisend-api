echo "Removing old migrations and database..."
rm -rf artisendapi/migrations
rm -f db.sqlite3

echo "Creating new migrations..."
python manage.py makemigrations artisendapi

echo "Applying migrations..."
python manage.py migrate

echo "Creating superuser..."
python manage.py createsuperuser

echo "Creating mediums"
python manage.py loaddata mediums.json
python manage.py loaddata skills.json

echo "Database reset complete!"