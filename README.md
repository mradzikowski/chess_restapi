# chess_restapi

### Purpose of the app
The rest api that helps with playing chess. It retrieves the available moves for the current position for chess figures
and also checks if the move for specific figure is valid. We assume that the board is empty and the single figure is on
the board, and also that we play white figures.

Assumption: if we put the pawn on the first row from the bottom, there are no moves for the pawn.
We do not consider the attacking moves as well.

The application might be extended, so it has both black and white figures and can imitate the actual game of chess.

### How to set up the application

#### Setting up the virtual environment

Make sure that you have virtual environment enabled
You can create one using Pycharm by going into `File -> Settings -> Project: chess_restapi -> Python Interpreter -> Add (settings icon)`

#### Creating python environment from terminal

```shell
python3 -m venv venv
source venv/bin/activate
```

If you had any problems creating the virtual environment refer to this link ->
[Virtual Environments Python](https://docs.python.org/3/tutorial/venv.html)

Then you can install the project dependencies

```shell
pip install -r requirements.txt
```

#### Run Project with docker-compose
Build the docker image and spin it in the detached mode:

```shell
docker-compose up -d --build
```

This will build the api_chess service

You can access the api documentation using SWAGGER UI here [API DOCUMENTATION SWAGGER](http://localhost:5004/doc).
You will be able to test there endpoints, see the schemas for the responses.

#### Linting using flake8 and docker image
```shell
docker-compose exec api_chess flake8 --max-line-length=88
```

#### Refactoring using black
```shell
docker-compose exec api_chess black .
```

#### To check with type checker mypy
Run
```shell
mypy .
```

#### To test using pytest run
All tests are in the backend/src/tests folder

```shell
docker-compose exec api_chess python -m pytest "src/tests" -p no:warnings
```

Alternatively you can see the html coverage report of the pytest running
```shell
docker-compose exec api_chess python -m pytest "src/tests" -p "no:warnings" --cov="src" --cov-report html
google-chrome backend/htmlcov/index.html
```

#### Alternative option to run the project without Docker
Install the dependencies in the python virtual environment and activate it, follow the steps from above.
```shell
python backend/manage.py
```

Then access the doc route for api documentation

### To install `pre-commit`

By installing the requirements for the project pre-commit will also be installed.
You can double-check if it is installed by `pre-commit --version`

You can always refer to [Pre-commit documentation](https://pre-commit.com/) for any help.
The config file for pre-commit is in root folder **pre-commit-config.yaml** file.

It will run on your commits, but you can also use `pre-commit run --all-files`
It consists of some checks and reformatting tools. It might change the code that you have added,
so you can apply changes and commit them to the codebase.
