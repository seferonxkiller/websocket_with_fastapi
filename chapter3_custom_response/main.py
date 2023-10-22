# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
#
# app = FastAPI(
#     title='custom_responce',
# )
#
#
# @app.get("/html", response_class=HTMLResponse)
# async def get_html():
#     return """
#         <html>
#             <head>
#                 <title>Hello world!</title>
#             </head>
#             <body>
#                 <h1>Hello world!</h1>
#             </body>
#         </html>
#     """
#
#
# @app.get("/text", response_class=PlainTextResponse)
# async def text():
#     return 'Hello world'

from enum import Enum
from typing import List

from fastapi import FastAPI, Path, Query, Body, Form, File, UploadFile, Header, Request, status, Response, HTTPException
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
from pydantic import BaseModel


class User(BaseModel):
    name: str = Body(..., min_length=2, max_length=200)
    age: int = Path(..., gt=1, lt=10)


class PublicPost(BaseModel):
    title: str = Form(..., min_length=2, max_length=10)


class Post(BaseModel):
    title: str = Form(..., min_length=2, max_length=10)


class UserType(str, Enum):
    teacher = "teacher"
    ADMIN = "admin"


class UserFormat(str, Enum):
    short = "short"
    full = "full"


app = FastAPI()

posts = {
    1: Post(title="Hello", nb_views=100)
}


@app.put("/posts/{id}")
async def update_or_create_post(id: int, post: Post, response: Response):
    if id not in posts:
        response.status_code = status.HTTP_201_CREATED
    posts[id] = post
    return posts[id]


@app.post("/password")
async def check_password(password: str = Body(...), check: str = Body(...)):
    if password != check:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "Password don't match",
                "hints": [
                    "Check the caps look on your keyboard",
                    "Try to make the password visible by clicking on the eye icon to check your typing",
                ],
            },
        )  # check password in fast api
    else:
        return HTTPException(status_code=status.HTTP_200_OK, detail="ok", headers={"password": password})


@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
    <html>
        <head>
            <title>Hello world!</title>
        </head>
        <body>
            <h1>Hello world!</h1>
        </body>
    </html>
    """


@app.get("/text", response_class=PlainTextResponse)
async def text():
    return "Hello world!"


@app.get("/redirect")
async def redirect():
    return RedirectResponse("/html")


# @app.get("/")
# async def custom_header(response: Response):
#     response.headers["Custom-Header"] = "Custom-Header-Value"
#     return {"hello": "world"}


#
# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# async def create_post(post: Post):
#     return post


# Dummy database
# posts = {
#     1: Post(title="Hello", nb_views=100),
# }
#
#
# @app.get("/posts/{id}", response_model=PublicPost)
# async def get_post(id: int):
#     return posts[id]

#
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_post(id: int):
#     posts.pop(id, None)
#     return None
# @app.post("/users")
# async def create_user(name: str = Form(..., min_length=2, max_length=10),
#                       age: int = Form(..., gt=2, lt=10)):  # form qlib jonatish
#     return {"name": name, "age": age}


# @app.post("/files")
# async def upload_file(file: bytes = File(...)):  # file upload qlish swaggerda
#     return {"file_size": len(file)}


# @app.post("/file")
# async def upload_file(file: UploadFile = File(...)):  # file ni upload qlish faqat koproq imkoniyatlari bor
#     return {"file_name": file.filename, "content_type": file.content_type}

#
@app.post("/files")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return [
        {"file_name": file.filename, "content_type": file.content_type}
        for file in files
    ]


# @app.get("/")
# async def get_header(hello: str = Header(...)): header qlish
#     return {"hello": hello}


# @app.get("/suer")
# async def get_request_object(request: Request):
#     return {"path": request.url.path}


# @app.get("/")
# async def hello_world():
#     return {"hello": "world"}


# @app.get("/users/{id}")
# async def get_user(id: int):
#     return {"id": id}

#
# @app.get("/users/{type}/{id}")
# async def get_user_type(type: UserType, id: int):
#     return {"type": type, "id": id}
#
#
# @app.get("/users/{id}")
# async def get_user_id(id: int = Path(...,
#                                      ge=1)):  # • ge: Greater than or equal to, • gt: Greater than,  • lt: Less than,  • le: Less than or equal to
#     return {"id": id}
#
#
# @app.get("/licence-plates/{license}")
# async def get_licence_plate(
#         license: str = Path(..., min_length=9, max_length=10)):  # min_length va lax_length bu chegara berish
#     return {"license": license}
#
#
# @app.get("/licence_plates/{license}")
# async def get_licence_plates(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
#     return {"license": license}


# @app.get("/users")
# async def get_user(page: int = 1, size: int = 10):
#     return {"page": page, "size": size}


# @app.get("/users")
# async def get_users(format: UserFormat):
#     return {"format": format}


# @app.post("/users")
# async def create_user(user: User, priority: int = Body(..., ge=1, le=3)):
#     return {"user": user, "priority": priority}


# @app.get("/users/")
# async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
#     return {"page": page, "size": size}
#
#
# @app.post("/users/")
# async def create_user_name(name: str = Body(...), age: int = Body(...)):
#     return {"name": name, "age": age}

#
@app.get("/")
async def custom_cookie(response: Response):
    response.set_cookie("cookie-name", "cookie-value", max_age=86400)
    return {"response": response}


@app.get("/hello")
async def het_hello():
    return {'hello': "Dilshod"}
