'''
Module with all APIs and to run the app
'''


# Import all the necessary modules and packages
import jwt
import uuid
from flask import current_app, json, request, jsonify, make_response, abort
from app import create_app, db
from models import Login, UserProject
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import sqlalchemy

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
def hello():
# @token_required
# def hello(current_user):
    return "Hello"


#### PROJECT PAGE ####

# API to view all projects with student information
@app.route("/projects", methods=["GET"])
def projects():
# @token_required
# def projects(current_user):
    """
    Get all projects
    :param current_user: The user who is making the get request
    :return: Details of all projects
    """
    if request.method == 'GET':
        try:
            data = []
            all_projects = UserProject.query.all()
            for project in all_projects:
                data.append(
                    {
                        "id": project.id,
                        "name": project.name,
                        "class_year": project.class_year,
                        "primary_major": project.primary_major,
                        "secondary_major": project.secondary_major,
                        "minor": project.minor,
                        "primary_concentration": project.primary_concentration,
                        "secondary_concentration": project.secondary_concentration,
                        "special_concentration": project.special_concentration,
                        "minor_concentration": project.minor_concentration,
                        "title": project.title,
                        "abstract": project.abstract,
                        "keywords": project.keywords,
                        "feature": project.feature,
                        "hsr_review": project.hsr_review,
                        "skills": project.skills,
                        "los": project.los,
                        "custom_los": project.custom_los,
                        "advisor": project.advisor,
                        "skills_offering": project.skills_offering,
                        "skills_requesting": project.skills_requesting,
                        "location": project.location,
                        "last_updated": project.last_updated,
                    }
                )
            response = make_response(jsonify(data=data, status=200))

            return response

        except Exception as e:
            return(str(e))


# API to view project by id
@app.route("/projects/<int:project_id>", methods=["GET"])
def get_project_by_id(project_id):
# @token_required
# def get_project_by_id(current_user, project_id):
    """
    Get project by id
    :param current_user: The user who is making the get request
    :param project_id: Id of the project
    :return: Project details
    """

    if request.method == 'GET':
        try:
            project_info = UserProject.query\
                .filter(UserProject.id==project_id)\
                .first()
            data = {
                    "id": project_info.id,
                    "user_id": project_info.user_id,
                    "name": project_info.name,
                    "class_year": project_info.class_year,
                    "primary_major": project_info.primary_major,
                    "secondary_major": project_info.secondary_major,
                    "minor": project_info.minor,
                    "primary_concentration": project_info.primary_concentration,
                    "secondary_concentration": project_info.secondary_concentration,
                    "special_concentration": project_info.special_concentration,
                    "minor_concentration": project_info.minor_concentration,


                    "title": project_info.title,
                    "abstract": project_info.abstract,
                    "keywords": project_info.keywords,
                    "feature": project_info.feature,
                    "hsr_review": project_info.hsr_review,
                    "skills": project_info.skills,
                    "los": project_info.los,
                    "custom_los": project_info.custom_los,
                    "advisor": project_info.advisor,
                    "skills_offering": project_info.skills_offering,
                    "skills_requesting": project_info.skills_requesting,
                    "location": project_info.location,
                    "last_updated": project_info.last_updated,
            }
            response = make_response(jsonify(data=data, status=200))

            return response

        except Exception as e:
            return(str(e))


# API to edit project by id
@app.route("/projects/<int:project_id>", methods=["PUT"])
def update_project_by_id(project_id):
# @token_required
# def update_project_by_id(current_user, project_id):
    if request.method == 'PUT':
        """
        Update project by id
        :param current_user: The user who is making the update request
        :param project_id: Id of the project
        :return: Success message if current_user.id == project.user_id
        """

        try:
            project_info = UserProject.query\
                .filter(UserProject.id==project_id)\
                .first()
            
            # if project_info.user_id == current_user.id:

            request_data = request.get_json()

            if request_data:
                if 'name' in request_data:
                    project_info.name = request_data['name']

                if 'class_year' in request_data:
                    project_info.class_year = request_data['class_year']

                if 'primary_major' in request_data:
                    project_info.primary_major = request_data['primary_major']                

                if 'secondary_major' in request_data:
                    project_info.secondary_major = request_data['secondary_major']

                if 'primary_concentration' in request_data:
                    project_info.primary_concentration = request_data['primary_concentration']

                if 'secondary_concentration' in request_data:
                    project_info.secondary_concentration = request_data['secondary_concentration']                

                if 'special_concentration' in request_data:
                    project_info.special_concentration = request_data['special_concentration']

                if 'minor' in request_data:
                    project_info.minor = request_data['minor']

                if 'minor_concentration' in request_data:
                    project_info.minor_concentration = request_data['minor_concentration']                


                if 'title' in request_data:
                    project_info.title = request_data['title']

                if 'abstract' in request_data:
                    project_info.abstract = request_data['abstract']

                if 'keywords' in request_data:
                    project_info.keywords = request_data['keywords']             

                if 'feature' in request_data:
                    project_info.feature = request_data['feature']

                if 'hsr_review' in request_data:
                    project_info.hsr_review = request_data['hsr_review']

                if 'skills' in request_data:
                    project_info.skills = request_data['skills']

                if 'los' in request_data:
                    project_info.los = request_data['los']

                if 'custom_los' in request_data:
                    project_info.custom_los = request_data['custom_los']    

                if 'advisor' in request_data:
                    project_info.advisor = request_data['advisor']

                if 'skills_offering' in request_data:
                    project_info.skills_offering = request_data['skills_offering']

                if 'skills_requesting' in request_data:
                    project_info.skills_requesting = request_data['skills_requesting'] 

                if 'location' in request_data:
                    project_info.location = request_data['location'] 

                project_info.last_updated = datetime.utcnow()
                db.session.commit()

            response = make_response(jsonify(data="Success", status=200))
            return response

            # else:
            #     abort(403, description="Doesn't have the privilege to update the project")

        except Exception as e:
            return(str(e))


# API to create project info
@app.route("/projects", methods=["POST"])
def create_new_project():
# @token_required
# def create_new_project(current_user):
    if request.method == 'POST':
        """
        Create new project info
        :param current_user: The user who is making the post request
        :return: Success message for the creation of new project info
        """

        try:
            # user = User.query\
            #     .filter(User.id==current_user.id)\
            #     .first()

            # if user:

            request_data = request.get_json()

            name = None
            class_year = None
            primary_major = None
            secondary_major = None
            primary_concentration = None
            secondary_concentration = None
            special_concentration = None
            minor = None
            minor_concentration = None

            title = None
            abstract = None
            keywords = None
            feature = None
            hsr_review = None
            skills = None
            los = None
            custom_los = None
            advisor = None
            skills_offering = None
            skills_requesting = None
            location = None

            if request_data:
                if 'name' in request_data:
                    name = request_data['name']

                if 'class_year' in request_data:
                    class_year = request_data['class_year']

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


                if 'title' in request_data:
                    title = request_data['title']

                if 'abstract' in request_data:
                    abstract = request_data['abstract']

                if 'keywords' in request_data:
                    keywords = request_data['keywords']

                if 'feature' in request_data:
                    feature = request_data['feature']

                if 'hsr_review' in request_data:
                    hsr_review = request_data['hsr_review']

                if 'skills' in request_data:
                    skills = request_data['skills']

                if 'los' in request_data:
                    los = request_data['los']

                if 'custom_los' in request_data:
                    custom_los = request_data['custom_los']

                if 'advisor' in request_data:
                    advisor = request_data['advisor']

                if 'skills_offering' in request_data:
                    skills_offering = request_data['skills_offering']

                if 'skills_requesting' in request_data:
                    skills_requesting = request_data['skills_requesting'] 

                if 'location' in request_data:
                    location = request_data['location'] 


                # new_project = Project(user_id=current_user.id, title=title, abstract=abstract,\
                #             keywords=keywords, feature=feature, los=los, custom_los=custom_los,\
                #             hsr_review=hsr_review)


                new_project = UserProject(
                    name=name, class_year=class_year, primary_major=primary_major, secondary_major=secondary_major, primary_concentration=primary_concentration, secondary_concentration=secondary_concentration, special_concentration=special_concentration, minor=minor, minor_concentration=minor_concentration,title=title, abstract=abstract,keywords=keywords, feature=feature, hsr_review=hsr_review, skills=skills, los=los, custom_los=custom_los, advisor=advisor, skills_offering=skills_offering, skills_requesting=skills_requesting, location=location
                    )

                db.session.add(new_project)
                db.session.commit()

                data = {'message': 'Project information saved successfully'}
                response = make_response(jsonify(data=data, status=201))
                return response

            # else:
            #     abort(404, description="Cannot find user profile. Please create your profile info and come back here")

        except Exception as e:
            return(str(e))


def serialize_item(item):

    """Helper function to convert item to dictionary (JSON-compatible)"""

    return {
        'id': item.id,
        'name': item.name,
        'class_year': item.class_year,
        'primary_major': item.primary_major,
        'secondary_major': item.secondary_major,
        'primary_concentration': item.primary_concentration,
        'secondary_concentration': item.secondary_concentration,
        'special_concentration': item.special_concentration,
        'minor': item.minor,
        'minor_concentration': item.minor_concentration,
        'title': item.title,
        'abstract': item.abstract,
    }

def serialize_many(items):

    """Helper function to convert item to a list of dictionaries (JSON-compatible)"""

    list_json_of_items = [serialize_item(item) for item in items]
    return list_json_of_items

@app.route("/search", methods=["GET"])
def search_projects():

    """Full-text search function by Postgres"""

    search_string = request.args.get('q')

    if search_string:
        tq = sqlalchemy.func.plainto_tsquery('english', search_string)
        q = UserProject.query.filter(UserProject.__ts_vector__.op('@@')(tq))

    return jsonify(serialize_many(
        q.all()
    ))


if __name__ == "__main__":
    app.run(debug=True)
