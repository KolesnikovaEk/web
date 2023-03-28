from flask import Flask, make_response, jsonify
from flask_restful import Api

from data import db_session, news_resources, users_resource, jobs_resource
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app, catch_all_404s=True)


def main():
    db_session.global_init("db/blogs.db")
    # для списка объектов
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

    # для одного объекта
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')


    app.run(port=8030, host='127.0.0.1')


if __name__ == '__main__':
    main()
