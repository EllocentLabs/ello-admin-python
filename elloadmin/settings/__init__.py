from .base import *

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)

PROJECT_MODE = 'dev'

if PROJECT_MODE == 'prod':
    from .prod import *
elif PROJECT_MODE == 'dev':
    from .dev import *
