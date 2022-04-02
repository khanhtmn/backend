"""
Module with all APIs and to run the app
(DEPRECATED - LEGACY)
"""


# Import all the necessary modules and packages
import jwt
import uuid
from flask import current_app, json, request, jsonify, make_response, abort
from app import create_app, db
from models import Login, User, Project
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Create an application instance
app = create_app()


#### AUTHENTICATION ####

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            data = {'message': 'Valid token is missing'}
            response = make_response(jsonify(data=data, status=400))
            return response

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            # return jsonify({'token': jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])})
            current_user = Login.query.filter_by(public_id=data['public_id']).first()
            return f(current_user, *args, **kwargs)
        except:
            data = {'message': 'Invalid token'}
            response = make_response(jsonify(data=data, status=400))
            return response
    return decorator


# API to register new user
@app.route("/register", methods=["POST"])
def register_user():
    email = request.json.get("email") # Test if this is the right way to get info
    password = request.json.get("password")
    
    if not email or not password:
        abort(400, description="Empty email or password")
    
    if Login.query.filter_by(email = email).first() != None:
        abort(400, description="Existing user")
    
    if not '@minerva.kgi.edu' in email and not 'minerva.edu' in email:
        data = {'message': 'Need to register with Minerva email address'}
        response = make_response(jsonify(data=data, status=400))
        return response

    hashed_password = generate_password_hash(password, method='sha256')

    new_user = Login(public_id=str(uuid.uuid4()), email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    data = {'message': 'Registered successfully'}
    response = make_response(jsonify(data=data, status=201))
    return response

# API to authenticate
@app.route("/login", methods=["GET", "POST"])
def login_user():

    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        data = {'message': 'Could not verify yes', 'WWW.Authentication': 'Basic realm: "login required"'}
        response = make_response(jsonify(data=data, status=401))
        return response

    try:
        user = Login.query.filter_by(email=auth.username).first()
        
        if check_password_hash(user.password, auth.password):
            token = jwt.encode({'public_id': user.public_id}, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})
            # https://stackoverflow.com/questions/48570320/how-to-send-and-receive-jwt-token
            # return jsonify({'token': jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])})
        else:
            data = {'message': 'Could not verify 2', 'WWW.Authentication': 'Basic realm: "login required"'}
            response = make_response(jsonify(data=data, status=401))
            return response
    except:    
        data = {'message': 'Could not verify 3', 'WWW.Authentication': 'Basic realm: "login required"'}
        response = make_response(jsonify(data=data, status=401))
        return response


# Define a route to fetch data

# Placeholder route for main page
@app.route("/", methods=["GET"])
@token_required
def hello(current_user):
    return "Hello"


#### PROJECT PAGE ####

# API to view all projects with student information
@app.route("/projects", methods=["GET"])
@token_required
def projects(current_user):
    """
    Get all projects
    :param current_user: The user who is making the get request
    :return: Details of all projects
    """
    if request.method == 'GET':
        try:
            data = []
            all_projects = Project.query\
                .join(User, Project.user_id==User.id)\
                .add_columns(User.id, User.firstname, User.lastname,User.primary_major,\
                    User.secondary_major, User.minor, User.primary_concentration,\
                        Project.title, Project.abstract, Project.feature)\
                .filter(Project.user_id==User.id)\
                .all()
            for project in all_projects:
                data.append(
                    {
                        "id": project.id,
                        "firstname": project.firstname,
                        "lastname": project.lastname,
                        "primary_major": project.primary_major,
                        "secondary_major": project.secondary_major,
                        "minor": project.minor,
                        "title": project.title,
                        "abstract": project.abstract,
                        "feature": project.feature,
                    }
                )
            response = make_response(jsonify(data=data, status=200))

            return response

        except Exception as e:
            return(str(e))


# API to view project by id
@app.route("/projects/<int:project_id>", methods=["GET"])
@token_required
def get_project_by_id(current_user, project_id):
    """
    Get project by id
    :param current_user: The user who is making the get request
    :param project_id: Id of the project
    :return: Project details
    """

    if request.method == 'GET':
        try:
            project_info = Project.query\
                .filter(Project.id==project_id)\
                .join(User, Project.user_id==User.id)\
                .add_columns(Project.id, Project.user_id, User.firstname, User.lastname,\
                    User.primary_major,User.secondary_major, User.minor,\
                    User.primary_concentration,Project.title, Project.abstract,\
                    Project.keywords, Project.feature, Project.los,Project.custom_los,\
                    Project.hsr_review, Project.last_updated)\
                .first()
            data = {
                    "id": project_info.id,
                    "user_id": project_info.user_id,
                    "firstname": project_info.firstname,
                    "lastname": project_info.lastname,
                    "primary_major": project_info.primary_major,
                    "secondary_major": project_info.secondary_major,
                    "minor": project_info.minor,
                    "primary_concentration": project_info.primary_concentration,
                    "title": project_info.title,
                    "abstract": project_info.abstract,
                    "keywords": project_info.keywords,
                    "feature": project_info.feature,
                    "los": project_info.los,
                    "custom_los": project_info.custom_los,
                    "hsr_review": project_info.hsr_review,
                    "last_updated": project_info.last_updated,
            }
            response = make_response(jsonify(data=data, status=200))

            return response

        except Exception as e:
            return(str(e))


# API to edit project by id
@app.route("/projects/<int:project_id>", methods=["PUT"])
@token_required
def update_project_by_id(current_user, project_id):
    if request.method == 'PUT':
        """
        Update project by id
        :param current_user: The user who is making the update request
        :param project_id: Id of the project
        :return: Success message if current_user.id == project.user_id
        """

        try:
            project_info = Project.query\
                .filter(Project.id==project_id)\
                .first()
            
            if project_info.user_id == current_user.id:

                request_data = request.get_json()

                if request_data:
                    if 'title' in request_data:
                        project_info.title = request_data['title']

                    if 'abstract' in request_data:
                        project_info.abstract = request_data['abstract']

                    if 'keywords' in request_data:
                        project_info.keywords = request_data['keywords']             

                    if 'feature' in request_data:
                        project_info.feature = request_data['feature']

                    if 'los' in request_data:
                        project_info.los = request_data['los']

                    if 'custom_los' in request_data:
                        project_info.custom_los = request_data['custom_los']    

                    if 'hsr_review' in request_data:
                        project_info.hsr_review = request_data['hsr_review']

                    project_info.last_updated = datetime.utcnow()
                    db.session.commit()

                response = make_response(jsonify(data="Success", status=200))
                return response

            else:
                abort(403, description="Doesn't have the privilege to update the project")

        except Exception as e:
            return(str(e))


# API to create project info
@app.route("/projects", methods=["POST"])
@token_required
def create_new_project(current_user):
    if request.method == 'POST':
        """
        Create new project info
        :param current_user: The user who is making the post request
        :return: Success message for the creation of new project info
        """

        try:
            user = User.query\
                .filter(User.id==current_user.id)\
                .first()

            if user:

                request_data = request.get_json()

                title = None
                abstract = None
                keywords = None
                feature = None
                los = None
                custom_los = None
                hsr_review = None

                if request_data:
                    if 'title' in request_data:
                        title = request_data['title']

                    if 'abstract' in request_data:
                        abstract = request_data['abstract']

                    if 'keywords' in request_data:
                        keywords = request_data['keywords']

                    if 'feature' in request_data:
                        feature = request_data['feature']

                    if 'los' in request_data:
                        los = request_data['los']

                    if 'custom_los' in request_data:
                        custom_los = request_data['custom_los']

                    if 'hsr_review' in request_data:
                        hsr_review = request_data['hsr_review']

                    new_project = Project(user_id=current_user.id, title=title, abstract=abstract,\
                                keywords=keywords, feature=feature, los=los, custom_los=custom_los,\
                                hsr_review=hsr_review)
                    db.session.add(new_project)
                    db.session.commit()

                    data = {'message': 'Project information saved successfully'}
                    response = make_response(jsonify(data=data, status=201))
                    return response

            else:
                abort(404, description="Cannot find user profile. Please create your profile info and come back here")

        except Exception as e:
            return(str(e))


#### USER PAGE ####

# API to view user by id
@app.route("/users/<int:user_id>", methods=["GET"])
@token_required
def get_user_by_id(current_user, user_id):
    """
    Get user by id
    :param current_user: The user who is making the get request
    :param user_id: Id of the user to view
    :return: User details
    """

    if request.method == 'GET':
        try:
            user_info = User.query\
                .filter(User.id==user_id)\
                .join(Project, Project.user_id==User.id)\
                .add_columns(User.firstname, User.lastname,User.primary_major,\
                    User.secondary_major, User.minor,User.primary_concentration,\
                    Project.title, Project.abstract,Project.keywords, Project.feature,\
                    Project.los,Project.custom_los,Project.hsr_review, Project.last_updated)\
                .first()
            data = [{
                "firstname": user_info.firstname,
                "lastname": user_info.lastname,
                "primary_major": user_info.primary_major,
                "secondary_major": user_info.secondary_major,
                "minor": user_info.minor,
                "primary_concentration": user_info.primary_concentration,
                "title": user_info.title,
                "abstract": user_info.abstract,
                "keywords": user_info.keywords,
                "feature": user_info.feature,
                "los": user_info.los,
                "custom_los": user_info.custom_los,
                "hsr_review": user_info.hsr_review,
                "last_updated": user_info.last_updated,
            }]
            response = make_response(jsonify(data=data, status=200))

            return response

        except Exception as e:
            return(str(e))


# API to edit user by id
@app.route("/users/<int:user_id>", methods=["PUT"])
@token_required
def update_user_by_id(current_user, user_id):
    if request.method == 'PUT':
        """
        Get user by id
        :param current_user: The user who is making the update request
        :param user_id: Id of the user to update
        :return: Success message if current_user.id == user_id
        """

        try:
            user_info = User.query\
                .filter(User.id==user_id)\
                .first()

            if user_info.id == current_user.id:

                request_data = request.get_json()

                if request_data:
                    if 'firstname' in request_data:
                        user_info.firstname = request_data['firstname']

                    if 'lastname' in request_data:
                        user_info.lastname = request_data['lastname']

                    if 'role' in request_data:
                        user_info.role = request_data['role']

                    if 'primary_major' in request_data:
                        user_info.primary_major = request_data['primary_major']

                    if 'secondary_major' in request_data:
                        user_info.secondary_major = request_data['secondary_major']

                    if 'primary_concentration' in request_data:
                        user_info.primary_concentration = request_data['primary_concentration']

                    if 'secondary_concentration' in request_data:
                        user_info.secondary_concentration = request_data['secondary_concentration']

                    if 'special_concentration' in request_data:
                        user_info.special_concentration = request_data['special_concentration']

                    if 'minor' in request_data:
                        user_info.minor = request_data['minor']

                    if 'minor_concentration' in request_data:
                        user_info.minor_concentration = request_data['minor_concentration']

                    user_info.last_updated = datetime.utcnow()
                    db.session.commit()

                response = make_response(jsonify(data="Success", status=200))
                return response

            else:
                abort(403, description="Doesn't have the privilege to update user info")

        except Exception as e:
            return(str(e))


# API to create user info
@app.route("/users", methods=["POST"])
@token_required
def create_new_user(current_user):
    if request.method == 'POST':
        """
        Create new user profile
        :param current_user: The user who is making the post request
        :return: Success message for the creation of new user profile
        """

        try:
            login_id = Login.query\
                .filter(Login.id==current_user.id)\
                .first()

            if login_id:

                request_data = request.get_json()

                firstname = None
                lastname = None
                role = None
                primary_major = None
                secondary_major = None
                primary_concentration = None
                secondary_concentration = None
                special_concentration = None
                minor = None
                minor_concentration = None

                if request_data:
                    if 'firstname' in request_data:
                        firstname = request_data['firstname']

                    if 'lastname' in request_data:
                        lastname = request_data['lastname']

                    if 'role' in request_data:
                        role = request_data['role']

                    if 'primary_major' in request_data:
                        primary_major = request_data['primary_major']

                    if 'secondary_major' in request_data:
                        secondary_major = request_data['secondary_major']

                    if 'primary_concentration' in request_data:
                        primary_concentration = request_data['primary_concentration']

                    if 'secondary_concentration' in request_data:
                        secondary_concentration = request_data['secondary_concentration']

                    if 'special_concentration' in request_data:
                        special_concentration = request_data['special_concentration']

                    if 'minor' in request_data:
                        minor = request_data['minor']

                    if 'minor_concentration' in request_data:
                        minor_concentration = request_data['minor_concentration']

                    new_user = User(login_id=current_user.id, firstname=firstname, lastname=lastname,\
                                role=role, primary_major=primary_major, secondary_major=secondary_major,\
                                primary_concentration=primary_concentration,\
                                secondary_concentration=secondary_concentration,\
                                special_concentration=special_concentration,\
                                minor=minor, minor_concentration=minor_concentration)
                    db.session.add(new_user)
                    db.session.commit()

                    data = {'message': 'User profile created successfully'}
                    response = make_response(jsonify(data=data, status=201))
                    return response

            else:
                abort(404, description="Cannot find login info. Please register an account and sign in first")

        except Exception as e:
            return(str(e))


if __name__ == "__main__":
    app.run(debug=True)
