# Crawler directory

LaunchForth crawler based on `Scrapy` framework. Store the crawled json data in `MongeDB`.

# Prerequests

`MongoDB` `PyMongo` `Scrapy`

# Run crawler

firstly run MongoDB on server. 

```
mongod --dbpath ~/data/db
```

(Modify `MONGODB_SERVER` and `MONGODB_PORT` to change DB server address and port.)

Then run the `run` bash file in another process to start crawling.

```
./run
```

# Data storage

The data are stored in mongoDB in directory `~/data/db`. 

Database name is `launchforth`. Collection names are api suffixes of the API.

To see the structure of Database in console:

```
$ mongo
> show dbs
> use launchforth
> show collections
```