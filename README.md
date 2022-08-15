# REST API AND WEB SCRAPPING FOR INAPP

Follow the Below Instructions to deploy the project in Local Host

### Install Virtualenv Lbrary
`pip install virtualenv`

    follow the above command to install vitrualenv to activate environment for the project

### Creat Virtual Environement 
`python -m venv env`

    follow the above command to create env folder for environemnt

### Activate Vitual Environment
`source env/bin/activate`  for linux

`env\scripts\activate`     for windows 

    follow the above command to activate virtual environment

### Install Required Packages
`pip install -r requirements.txt`

    follow the above command to install all the required packages for the project

### Migrate Model into db
`python manage.py migrate`

    If you want Fresh database follow the above command  after deleteing db.sqlite3 file

### Run the Project in LocalHost
`python manage.py runserver`

    follow the above command to run the project in localhost

# REST API's 

## Create Blog post

### request

`POST /api/v1/blog/`

    Accept: application/json
    API:http://127.0.0.1:8000/api/v1/blog/


### Input 

    {
        "title":"blog ",
        "username":"tester",
        "description":"create blogs test"

    }

### Response 

    HTTP/1.1 200 OK
    Status: 200 OK
    Connection: close
    Content-Type: application/json

    {
        "id": 1,
        "username": "tester",
        "title": "blog",
        "description": "create blogs test",
        "image": null,
        "created_at": "2022-08-15T07:25:50.707294Z",
        "updated_at": "2022-08-15T07:25:50.707346Z"
    }


## List Blog Post

`GET /api/v1/blog/?limit=5&search=admin`

    Accept: application/json
    Method:GET
    API:http://127.0.0.1:8000/api/v1/blog/

    search and pagination:
    API :http://127.0.0.1:8000/api/v1/blog/?limit=5&search=admin

### Input 

    In parameters 
    limit:
    offset:
    search:

### Response 

    {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "tester",
            "title": "blog",
            "description": "create blogs test",
            "image": null,
            "created_at": "2022-08-15T07:25:50.707294Z",
            "updated_at": "2022-08-15T07:25:50.707346Z"
        }
    ]
    }

## UPDATE BLOG 

`PATCH api/v1/blog/１/`

    API : http://127.0.0.1:8000/api/v1/blog/1/
    Method : PATCH

### INPUT 

    {
        "title" : "value"
    }
    Parameter : 
            Id of the blog post

    update input field can to single or multiple


### Response 


    {
        
        "id": 1,
        "comments": [],
        "username": "tester",
        "title": "value",
        "description": "create blogs test",
        "image": null,
        "created_at": "2022-08-15T07:33:43.189864Z",
        "updated_at": "2022-08-15T07:33:43.189919Z"
    }
    
    
## DELETE BLOG POST

`DELETE api/v1/blog/１/`

    API : http://127.0.0.1:8000/api/v1/blog/1/
    Method : DELETE

### Input 

    Parameter : 
            Id of the blog post



### Response 

    {
        "detail": "deleted successfully"
    }

# Comment API's

## CREATE COMMENT 

`POST api/v1/comment/`

    API : http://127.0.0.1:8000/api/v1/comment/
    Method :POST

### Input 

    {
    "blog":1, #forgien key of blog 
    "username":"tester3",
    "comment":"testing3"
    }

### Response 

    {
    "id": 4,
    "username": "tester3",
    "comment": "testing3",
    "created_at": "2022-08-13T20:53:14.734587Z",
    "updated_at": "2022-08-13T20:53:14.734632Z",
    "blog": 1
    }



## List  Comments

`GET api/v1/comment/`

    API : http://127.0.0.1:8000/api/v1/comment/
    Method :GET

### Input 
    API : http://127.0.0.1:8000/api/v1/comment/?search=testing3&limit=1
    parameters : 
            limit 
            offset 
            search 

### Response 

    {
    "count": 3,
    "next": "http://127.0.0.1:8000/api/v1/comment/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "username": "tester3",
            "comment": "testing3",
            "created_at": "2022-08-15T10:18:14.760352Z",
            "updated_at": "2022-08-15T10:18:14.760411Z",
            "blog": 3
            }
        ]
        }

## Update Comment 

` PATCH api/v1/comment/2/`

    APi : http://127.0.0.1:8000/api/v1/comment/2/
    Method : PATCH

### Input 

    {
        "comment" : "updatetester3"
    }
    parameter :
            ID of the comment

    input field can be multiple or single


### Response 

    {
    "id": 2,
    "username": "updatetester3",
    "comment": "testing3",
    "created_at": "2022-08-15T10:18:47.594679Z",
    "updated_at": "2022-08-15T10:18:47.594738Z",
    "blog": 3
    }

## DELETE COMMENT 
` DELETE api/v1/comment/2/`

    APi : http://127.0.0.1:8000/api/v1/comment/2/
    Method : DELETE


### Input 

    parameter :
        ID of the comment 


### Response 


    {
        "detail": "deleted successfully"
    }



# WEB SCRAPPING 

### WEBSITE URLS FOR SCRAPPING 

 1: `https://elementor.com/blog/famous-wordpress-websites/`

 2: `https://www.wpbeginner.com/showcase/excellent-wordpress-website-examples/`

 3: `https://www.makeuseof.com/tag/most-popular-android-apps/`

    Only the above 3 url's work on the project 


## API ENDPOINT
`POST api/v1/blog-post-save/`

    API : http://127.0.0.1:8000/api/v1/blog-post-save/
    Method : POST 


### Input 

    {
        "url":"https://www.makeuseof.com/tag/most-popular-android-apps/"
    }

    url can be any one of the above url's


### Response

    [
    {
        "id": 1,
        "username": "Admin",
        "title": " Etsy Journal",
        "description": "If you don’t already know, the",
        "image": "",
        "created_at": "2022-08-15T06:44:35.029346Z",
        "updated_at": "2022-08-15T06:44:35.029398Z"
    },
    ]

`List of blogs will be the Response`