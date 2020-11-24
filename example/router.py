from framework.api.data import Request
from framework.api.router import Router
from framework.lang.module import load_module
from framework.task.runner import Runner


def resolve(request: Request) -> Runner:
    routes = {
        'GET /models': lambda: load_module('example.controllers.models', 'action'),
    }
    return Router(routes).resolve(request.method, request.path)
