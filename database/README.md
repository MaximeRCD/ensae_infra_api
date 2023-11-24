# About the database

The database is hosted by a docker and uses MongoDB Community server.

## How to launch it ?

Rebuild if needed:

```
docker build -t database-docker-image .
```

Run:

```
docker run -d -p 27017:27017 --name database-container database-docker-image
```

**The database is a self-running docker. Connect from another docker.**

You can then use `pymongo` to interact with the database.

If needed, debug with mongosh (from command line). Connect using:

```
mongosh --host localhost --port 27017
``` 