from flask import jsonify
from flask_restful import abort, Resource

from . import db_session
from .jobs import Jobs
from .reqparse_jobs import parser


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    jobs = session.query(Jobs).get(jobs_id)
    if not jobs:
        abort(404, message=f"Job {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        return jsonify({'news': jobs.to_dict(
            only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader'))})

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        session = db_session.create_session()
        jobs = session.query(Jobs).get(jobs_id)
        session.delete(jobs)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader')) for item in jobs]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        jobs = Jobs(
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=args['start_date'],
            ens_date=args['end_date'],
            is_finished=args['is_finished'],
            team_leader=args['team_leader']
        )
        session.add(jobs)
        session.commit()
        return jsonify({'success': 'OK'})