# Importing the dependencies
from mangum import Mangum
from api.resource import app

# Running the App with Uvicorn
if __name__ == "__main__":
    handler = Mangum(app)