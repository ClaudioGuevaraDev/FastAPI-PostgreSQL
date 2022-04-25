FROM postgres

ENV POSTGRES_PASSWORD=contraseña

COPY db.sql /docker-entrypoint-initdb.d/db.sql

EXPOSE 5432