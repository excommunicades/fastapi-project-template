from project_name.configurations.routes.routes import Routes
from project_name.internal.routes import example

__routes__ = Routes(routers=(example.router, ))