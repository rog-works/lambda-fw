def webapi_modules() -> dict:
    return {
        'lf2.api.error.ApiErrorHandler': 'lf2.api.error.ApiErrorHandler',
        'lf2.api.render.ApiRender': 'lf2.api.render.ApiRender',
        'lf2.api.request.Request': 'lf2.api.provider.request',
        'lf2.api.response.Response': 'lf2.api.response.Response',
        'lf2.api.route.Route': 'lf2.api.route.ApiRoute',
        'lf2.task.router.Router': 'lf2.api.provider.api_router',
        'lf2.task.runner.Runner': 'lf2.api.provider.runner',
    }
