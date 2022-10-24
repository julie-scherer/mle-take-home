# Running the app

## In a Docker container

1. Clone/fork the git repo

```
git clone https://github.com/schererjulie/mle-take-home.git
```


2. Build the Docker image
```
// check docker is installed
docker -v

// build a docker image
docker build --tag mle-take-home .

// list all docker images available in the environment
docker images
```

3. Run the Docker image
```
// run a docker container in daemon mode with ports exposed
docker run -it -d -p 5000:5000 mle-take-home

// list all running containers
docker ps

// list all containers
docker ps -a
```

4. Send a POST request to the Flask server using the 'api' endpoint: ```localhost:5000/api```

    * The request body must be a valid JSON object with two fields: `img_dims` and `corner_points`. See the expected format of the request body in the examples below.

5. Stop the running container
```
// stop running container
docker stop <container-id>

// (optional) free up space by removing any unused resources
docker container prune
```

## On your local computer
1. Clone/fork the git repo

```
git clone https://github.com/schererjulie/mle-take-home.git
```

2. Create and active a virtual environment inside the app directory

macOS
```
cd mle-take-home
python3 -m venv venv
. venv/bin/activate
```

Windows
```
cd mle-take-home
py -3 -m venv venv
venv\Scripts\activate
```

3. Install the requirements

```
pip install -r requirements.txt
```

4. Run the application

```
python3 run.py
```



**_Helpful documentation_**
- [Flask Application Factories](https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/)
- [The Flask Mega-Tutorial Part XXIII: Application Programming Interfaces (APIs)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis)
- [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/)
- [How to Dockerize a Flask Application](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)



# Examples

### Run 1

Request
```
{
    "img_dims": "(3, 3)",
    "corner_points": "[(1, 1), (3, 1), (1, 3), (3, 3)]"
}
```

Response
```
{
    "solution": "[
        [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]], 
        [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]], 
        [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]]"
}
```

### Run 2

Request
```
{
    "img_dims": "(5, 3)",
    "corner_points": "[(-1, -1), (3, -1), (-1, 3), (3, 3)]"
}
```

Response
```
{
    "solution": "[
        [[-1.0, 3.0], [1.0, 3.0], [3.0, 3.0]], 
        [[-1.0, 2.0], [1.0, 2.0], [3.0, 2.0]], 
        [[-1.0, 1.0], [1.0, 1.0], [3.0, 1.0]], 
        [[-1.0, 0.0], [1.0, 0.0], [3.0, 0.0]], 
        [[-1.0, -1.0], [1.0, -1.0], [3.0, -1.0]]]"
}
```

### Run 3

Request
```
{
    "img_dims": "(10, 12)",
    "corner_points": "[(1.5, 1.5),  (4.0, 1.5),  (1.5, 8.0),  (4.0, 8.0)]"
}
```

Response
```
{
    "solution": "[
        [[1.5, 8.0], [1.73, 8.0], [1.95, 8.0], [2.18, 8.0], [2.41, 8.0], [2.64, 8.0], [2.86, 8.0], [3.09, 8.0], [3.32, 8.0], [3.55, 8.0], [3.77, 8.0], [4.0, 8.0]], 
        [[1.5, 7.28], [1.73, 7.28], [1.95, 7.28], [2.18, 7.28], [2.41, 7.28], [2.64, 7.28], [2.86, 7.28], [3.09, 7.28], [3.32, 7.28], [3.55, 7.28], [3.77, 7.28], [4.0, 7.28]], 
        [[1.5, 6.56], [1.73, 6.56], [1.95, 6.56], [2.18, 6.56], [2.41, 6.56], [2.64, 6.56], [2.86, 6.56], [3.09, 6.56], [3.32, 6.56], [3.55, 6.56], [3.77, 6.56], [4.0, 6.56]], 
        [[1.5, 5.83], [1.73, 5.83], [1.95, 5.83], [2.18, 5.83], [2.41, 5.83], [2.64, 5.83], [2.86, 5.83], [3.09, 5.83], [3.32, 5.83], [3.55, 5.83], [3.77, 5.83], [4.0, 5.83]], 
        [[1.5, 5.11], [1.73, 5.11], [1.95, 5.11], [2.18, 5.11], [2.41, 5.11], [2.64, 5.11], [2.86, 5.11], [3.09, 5.11], [3.32, 5.11], [3.55, 5.11], [3.77, 5.11], [4.0, 5.11]], 
        [[1.5, 4.39], [1.73, 4.39], [1.95, 4.39], [2.18, 4.39], [2.41, 4.39], [2.64, 4.39], [2.86, 4.39], [3.09, 4.39], [3.32, 4.39], [3.55, 4.39], [3.77, 4.39], [4.0, 4.39]], 
        [[1.5, 3.67], [1.73, 3.67], [1.95, 3.67], [2.18, 3.67], [2.41, 3.67], [2.64, 3.67], [2.86, 3.67], [3.09, 3.67], [3.32, 3.67], [3.55, 3.67], [3.77, 3.67], [4.0, 3.67]], 
        [[1.5, 2.94], [1.73, 2.94], [1.95, 2.94], [2.18, 2.94], [2.41, 2.94], [2.64, 2.94], [2.86, 2.94], [3.09, 2.94], [3.32, 2.94], [3.55, 2.94], [3.77, 2.94], [4.0, 2.94]], 
        [[1.5, 2.22], [1.73, 2.22], [1.95, 2.22], [2.18, 2.22], [2.41, 2.22], [2.64, 2.22], [2.86, 2.22], [3.09, 2.22], [3.32, 2.22], [3.55, 2.22], [3.77, 2.22], [4.0, 2.22]], 
        [[1.5, 1.5], [1.73, 1.5], [1.95, 1.5], [2.18, 1.5], [2.41, 1.5], [2.64, 1.5], [2.86, 1.5], [3.09, 1.5], [3.32, 1.5], [3.55, 1.5], [3.77, 1.5], [4.0, 1.5]]]"
}
```

### Run 4

Request
```
{
    "img_dims": "(10, 12)",
    "corner_points": "[(-12, -8), (-3, -8), (-12, -12),  (-3, -12)]"
}
```

Response
```
{
    "solution": "[
        [[-12.0, -8.0], [-11.18, -8.0], [-10.36, -8.0], [-9.55, -8.0], [-8.73, -8.0], [-7.91, -8.0], [-7.09, -8.0], [-6.27, -8.0], [-5.45, -8.0], [-4.64, -8.0], [-3.82, -8.0], [-3.0, -8.0]], 
        [[-12.0, -8.44], [-11.18, -8.44], [-10.36, -8.44], [-9.55, -8.44], [-8.73, -8.44], [-7.91, -8.44], [-7.09, -8.44], [-6.27, -8.44], [-5.45, -8.44], [-4.64, -8.44], [-3.82, -8.44], [-3.0, -8.44]], 
        [[-12.0, -8.89], [-11.18, -8.89], [-10.36, -8.89], [-9.55, -8.89], [-8.73, -8.89], [-7.91, -8.89], [-7.09, -8.89], [-6.27, -8.89], [-5.45, -8.89], [-4.64, -8.89], [-3.82, -8.89], [-3.0, -8.89]], 
        [[-12.0, -9.33], [-11.18, -9.33], [-10.36, -9.33], [-9.55, -9.33], [-8.73, -9.33], [-7.91, -9.33], [-7.09, -9.33], [-6.27, -9.33], [-5.45, -9.33], [-4.64, -9.33], [-3.82, -9.33], [-3.0, -9.33]], 
        [[-12.0, -9.78], [-11.18, -9.78], [-10.36, -9.78], [-9.55, -9.78], [-8.73, -9.78], [-7.91, -9.78], [-7.09, -9.78], [-6.27, -9.78], [-5.45, -9.78], [-4.64, -9.78], [-3.82, -9.78], [-3.0, -9.78]], 
        [[-12.0, -10.22], [-11.18, -10.22], [-10.36, -10.22], [-9.55, -10.22], [-8.73, -10.22], [-7.91, -10.22], [-7.09, -10.22], [-6.27, -10.22], [-5.45, -10.22], [-4.64, -10.22], [-3.82, -10.22], [-3.0, -10.22]], 
        [[-12.0, -10.67], [-11.18, -10.67], [-10.36, -10.67], [-9.55, -10.67], [-8.73, -10.67], [-7.91, -10.67], [-7.09, -10.67], [-6.27, -10.67], [-5.45, -10.67], [-4.64, -10.67], [-3.82, -10.67], [-3.0, -10.67]], 
        [[-12.0, -11.11], [-11.18, -11.11], [-10.36, -11.11], [-9.55, -11.11], [-8.73, -11.11], [-7.91, -11.11], [-7.09, -11.11], [-6.27, -11.11], [-5.45, -11.11], [-4.64, -11.11], [-3.82, -11.11], [-3.0, -11.11]], 
        [[-12.0, -11.56], [-11.18, -11.56], [-10.36, -11.56], [-9.55, -11.56], [-8.73, -11.56], [-7.91, -11.56], [-7.09, -11.56], [-6.27, -11.56], [-5.45, -11.56], [-4.64, -11.56], [-3.82, -11.56], [-3.0, -11.56]], 
        [[-12.0, -12.0], [-11.18, -12.0], [-10.36, -12.0], [-9.55, -12.0], [-8.73, -12.0], [-7.91, -12.0], [-7.09, -12.0], [-6.27, -12.0], [-5.45, -12.0], [-4.64, -12.0], [-3.82, -12.0], [-3.0, -12.0]]]"
}
```

### Run 5

Request
```
{
    "img_dims": "(101, 201)",
    "corner_points": "[(-500.5, -1.345678), (-3, -1.345678), (-500.5, -500.5),  (-3, -500.5)]"
}
```

Response... ???

#### **Try it out with [Postman](https://www.postman.com/)!**


###
------------------------------------------------------------------------


# Fetch Rewards Coding Assessment - Machine Learning Engineer

https://fetch-hiring.s3.amazonaws.com/machine-learning-engineer/image-coordinates.html

Your objective in this challenge is to write a program that calculates pixel coordinate values for an image that is to be displayed on a two dimensional surface given the dimensions of the image and the corner points of the image as it is to be displayed.

For example, if an image is defined by a 3x3 grid of pixel values, and the (x, y) coordinates of the four corner points to display the image at are: (1, 1), (3, 1), (1, 3), and (3, 3) then the program should calculate and return the coordinates: (1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (3, 1), (3, 2), (3, 3) which are the coordinates at which to place the 9 pixels in the image such that they’re evenly spaced within the corner points. The solution can be seen visually in the image below.

![https://fetch-hiring.s3.amazonaws.com/assets/machine-learning-engineer/img_1.png](https://fetch-hiring.s3.amazonaws.com/assets/machine-learning-engineer/img_1.png)

## Input Specifications

The program will take two inputs:

### 1. Image dimensions

This will be a tuple defining the height and width of the image in terms of pixel counts.

For example, an input for this parameter of (10, 12) means that the image has 10 rows and 12 columns.

### 2. Corner Points

This will be a list of two-element tuples defining the x and y coordinates of the image corner points of the displayed image. It consists of four (x, y) pairs.

The specification will follow the following example format:

```python
corner_points = [
(1.5, 1.5),  # (x, y)  (4.0, 1.5),  # (x, y)  (1.5, 8.0),  # (x, y)  (4.0, 8.0)]  # (x, y)
```

These corner points are represented visually in the plot below.

![https://fetch-hiring.s3.amazonaws.com/assets/machine-learning-engineer/img.png](https://fetch-hiring.s3.amazonaws.com/assets/machine-learning-engineer/img.png)

## Output Specifications

Your program should calculate and return the x and y coordinates at which to plot each pixel in the input image such that the pixels are evenly spaced within the rectangle defined by the corner points.

The output should be of shape mxnx2 where m is the number of rows in the input image and n is the number of columns in the input image. The solution in the example at the beginning of this page would be:

```python
solution = [

[[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],

[[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],

[[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
]
```

For example, the x coordinate of the pixel at the top left corner of the image would be accessed with `solution[0, 0, 0]` and the y coordinate of the pixel at the bottom right of the image would be accessed with `solution[3, 3, 1]`.

## Assumptions & Requirements

- Your program can assume that the corner points will define a rectangle with sides that are parallel to the x and y axes (the rectangle will not be rotated)
- The corner points can be provided in any order, your program should determine which is the bottom left, top right etc.
- You aren’t allowed to develop your solution using any image processing libraries, however please feel free to use array manipulation libraries such as NumPy
- To enable us to run your program please package the application as a web service that performs that calculations in response to a POST request containing the inputs in the body of the payload. You may use external libraries (i.e, Flask).
- Additionally, please package the web service in a Docker container that can either be built locally or pulled down and run via Docker hub.
- Please submit your exercise by providing a link to a public repository (i.e., GitHub, Bitbucket) to your recruiter. The repository should include instructions for running your code

### FAQs

**How will this exercise be evaluated?**

An engineer will review the code you submit. At a minimum they must be able to run the program, and the program must produce the expected results. You should provide any necessary documentation within the repository. While your solution does not need to be fully production ready, you are being evaluated so put your best foot forward!

**I have questions about the problem statement.**

For any requirements not specified above, use your best judgement to determine expected result. You can elaborate on your decisions via the documentation you provide in your repo.

**Can I provide a private repository?**

If at all possible, we prefer a public repository because we do not know which engineer will be evaluating your submission. Providing a public repository ensures a speedy review of your submission. If you are still uncomfortable providing a public repository, you can work with your recruiter to provide access to the reviewing engineer.

**How long do I have to complete the exercise?**

There is no time limit for the exercise. Out of respect for your time, we designed this exercise with the intent that it should take you a few hours. But, please take as much time as you need to complete the work.