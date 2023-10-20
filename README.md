# Fishing API

### This API tracks information about fish as well as what the latest fish caught is.

In order to access these routes, you need to use an api key. For all requests, you can use the api key as a query 
parameter with the key and value pair of: `api_key=4675636B20796F75`

### GET list of fish.

Example Path: `10.6.21.109:8000/fishes?api_key={API_KEY}`

Example Response:

````
[
    "swordfish",
    "salmon",
    "tilapia",
    "cod",
    "anchovies",
    "halibut",
    "catfish",
    "mahi-mahi",
    "betta",
    "flounder",
    "guppi",
    "bass",
    "goldfish",
    "tuna",
    "sardine",
    "trout",
    "pike",
    "carp",
    "perch",
    "barracuda"
]
````
### Get latest caught fish and their weight.

Example Path: `10.6.21.109:8000/catch?api_key={API_KEY}`

Example Response:

````
{
    "name": "flounder",
    "weight": 13.2
}
````
### Get information on specified fish.

Example Path: `10.6.21.109:8000/info/{type_of_fish}?api_key={API_KEY}`

Example Response:

````
{
    "population": 4892,
    "life_span": 6
}
````
