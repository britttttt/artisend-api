# artisend-api
<div style="display: flex; align-items: center;">
  <div>
  <img src="https://ik.imagekit.io/b0xq0alh4/Artisend/logo-light.png?updatedAt=1756248712592" alt="artisend logo" width="150" height="75" style="margin-right: 8px;">
  </div>
  <div>
  <span>Artisend is an application to connect local communities with artists and small businesses. Artists and businesses can share markets they’ll be selling at, as well as share their commission rates, and share photos of their craft. 
</span>
  </div>
</div>

<div style="display: flex; align-items: center;">
<img src="https://ik.imagekit.io/b0xq0alh4/Artisend/header-gif.gif?updatedAt=1756249224645" height="480" width="720
 ">
</div>

## Overview
 <div style="display: flex; align-items: center;">
  <span> Artisend is a CRUD application that connects local communities with artists and small businesses. Artists and businesses can share markets they’ll be selling at, as well as share their commission rates, and share photos of their craft. 
</span>
</div>


### Users can:
* Create a personal account or an account specifically for their art business
* Share their work through multiple jpeg, png, mp4, or mp3 files
* View posts created by users within a 25 mile radius of their account location
* Sort posts from chronological or reverse chronological order
* Edit any post they create
* Delete any post they create 


This is the Server-Side of the application. The Client-Side of the application can be found [here](https://github.com/britttttt/artisend)

## System Dependencies

1. Follow installation guide for installing [pipx](https://pipx.pypa.io/stable/installation/).
2. Run `pipx install poetry`.
3. Run the command below for your operating system.

### Mac OS

```sh
brew install libtiff libjpeg webp little-cms2
```

### Linux

```sh
sudo apt install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
```

## Setup

1. Clone this repository and change to the directory in the terminal.
2. Run `poetry env activate` and wait for the virtual environment to be created.
3. Run `poetry install` to install dependencies.
4. Run `pip install setuptools`
5. Run migrations and install starter data with the `./seed_data.sh` script.
6. Open the project in VS Code if you haven't yet.
7. Ensure that the correct Python Interpreter is chosen in VS Code.
8. Start your debugger.

## Postman Request Collection

1. Open the [Yaak](https://yaak.app/) API client
2. Click **Import**
3. Click **Select File**
4. Open the **`api-requests-collection.json`** file that is in this project.
5. Click **Import** to complete the process
6. You will see a confirmation that a new workspace has been created for you.

#### Test Login Request

1. Expand the **Profile** collection
2. Click on **Login** to open the request
3. Send the request.
4. You should get a response back that looks like this
   ```json
   {
       "valid": true,
       "token": "9ba45f09651c5b0c404f37a2d2572c026c146690",
       "id": 5
   }
   ```


## Contributors
<a href="https://github.com/britttttt">
  <img src="https://avatars.githubusercontent.com/u/51220225?v=4" height="50" width="50">
</a>

Made as my Server-Side Full Stack Capstone Project with JavaScript, NextJS, React, Python, and Django rest API's for [Nashville Software School's](https://nashvillesoftwareschool.com/) Full-Stack Software Developer Program (Cohort-76)



