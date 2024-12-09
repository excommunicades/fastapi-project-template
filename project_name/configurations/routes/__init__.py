from project_name.configurations.routes.routes import Routes
from project_name.internal.routes import health

__routes__ = Routes(routers=(health.router, ))