# Utiliser une image officielle de Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt en premier pour optimiser le cache Docker
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste du projet
COPY . .

# Exposer le port 5000 pour accéder à l'application Flask
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "app.py", "--host=0.0.0.0"]
