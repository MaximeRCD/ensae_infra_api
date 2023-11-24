# Use the official MongoDB image with the specified tag
FROM mongodb/mongodb-community-server:7.0-ubuntu2204

# Expose the default MongoDB port
EXPOSE 27017

# Copy the MongoDB configuration file to the container
COPY mongod.conf /etc/mongod.conf

# Start MongoDB with the custom configuration file
CMD ["mongod", "--config", "/etc/mongod.conf"]