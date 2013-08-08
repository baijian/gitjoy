# -*- coding: utf-8 -*-
from flask import current_app
from sqlalchemy import or_
from pygit2 import Repository, init_repository

from ..extensions import db
from .models import Repo

def create_repo(user_id, repo_name):
    repo = Repo(repo_name, user_id)
    db.session.add(repo)
    return repo

def rename_repo(repo_id, repo_name):
    raise NotImplementedError

def delete_repo(repo_id):
    raise NotImplementedError

def transfer_repo(repo_id, new_user_id, new_repo_name=None):
    raise NotImplementedError
    
def fork_repo(repo_id, new_user_id, new_repo_name=None):
    raise NotImplementedError
    
def get_repo(repo_id=None, **kwargs):
    """
    """

def create_repository(namespace, repo_name):
    repositories_root = current_app.config["REPOSITORIES_ROOT"]
    repo_path = "%s%s%s.git" % (repositories_root, namespace, repo_name)
    return init_repository(repo_path, True)

def get_repository(namespace, repo_name):
    """
    """
    repositories_root = current_app.config['REPOSITORIES_ROOT']
    repo_path = "%s%s%s.git" % (repositories_root, namespace, repo_name)
    try:
        return Repository(repo_path)
    except:
        return None

def get_repo_like(query):
    return Repo.query.filter(or_(Repo.name,like('%'+query+'%'))).limit(10).all()
