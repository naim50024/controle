# Utiliser l'image officielle Nginx
FROM nginx:alpine

# Copier le fichier de configuration Nginx dans le conteneur
COPY nginx.conf /etc/nginx/nginx.conf
