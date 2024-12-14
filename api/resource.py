# Importing the dependencies
from .dependencies import *
from src.dependencies import *
from src.utils import *
from src.logger import *
from src.exception import *
from .data_models import *


# Initialising the API from FastAPI and APIRouter
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://dating-ai-agent-prototype-frontend-ffvcxdyvt.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello from AI Dating Agent!"

# VectorDB Record Creation Endpoint
@app.post("/aiAgent/getQuestion",response_model = Response)
async def getQuestion(query: ChatQuery = Body(...)):
    """AI endpoint to generate relevant question"""
    try:
            answer = generate_question(query.conversation)
            logging.info(answer.choices[0].message.content)
            return { "response" : answer.choices[0].message.content}
        
    except CustomException as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
