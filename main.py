# Importing the dependencies
from mangum import Mangum
from api.resource import app

handler = Mangum(app)