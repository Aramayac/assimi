#!/bin/sh

echo "⏳ Attente de MySQL..."
until python -c "import pymysql; 
pymysql.connect(host='db', user='root', password='root', database='flaskdb')" 2>/dev/null; do
  sleep 2
done

echo "✅ MySQL est prêt, application des migrations..."
flask db upgrade

echo "🚀 Lancement de Flask..."
exec python run.py
