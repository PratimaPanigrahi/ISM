from fastapi import FastAPI,UploadFile, File
import pandas as pd 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.services.rm_service import calculate_rm_from_ssim
from app.services.frm_service import calculate_frm
from app.services.level_partition_service import calculate_level_partition
from app.services.conical_service import generate_conical_and_reduced

app = FastAPI(title="ISMIC Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SSIMInput(BaseModel):
    grid: list[list[str]]

@app.get("/")
def home():
    return {"message": "ISMIC backend running"}

@app.post("/calculate-rm")
def calculate_rm(data: SSIMInput):
    rm, driving_power, dependence_power = calculate_rm_from_ssim(data.grid)

    return {
        "reachability_matrix": rm,
        "driving_power": driving_power,
        "dependence_power": dependence_power
    }

@app.post("/calculate-frm")
def calculate_frm_endpoint(data: dict):
    frm, driving_power, dependence_power = calculate_frm(data["rm"])

    return {
        "frm": frm,
        "driving_power": driving_power,
        "dependence_power": dependence_power
    }

@app.post("/calculate-levels")
def calculate_levels_endpoint(data: dict):
    frm = data["frm"]
    variables = data["variables"]

    elements = calculate_level_partition(frm, variables)

    return {"elements": elements}

@app.post("/calculate-conical")
def calculate_conical(data: dict):
    frm = data["frm"]
    elements = data["elements"]

    conical, reduced, ordered_variables = generate_conical_and_reduced(frm, elements)

    return {
        "conical_matrix": conical,
        "reduced_conical_matrix": reduced,
        "ordered_variables": ordered_variables
    }

@app.post("/upload-ssim")
async def upload_ssim(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    # Extract variable names from header
    variables = list(df.columns)[1:]

    n = len(variables)

    # Create grid
    grid = [["" for _ in range(n+1)] for _ in range(n+1)]

    # Fill column headers
    for j in range(n):
        grid[0][j+1] = variables[j]

    # Fill row headers
    for i in range(n):
        grid[i+1][0] = variables[i]

    # Fill SSIM values
    for i in range(n):
        for j in range(n):
            grid[i+1][j+1] = df.iloc[i][variables[j]]

    return {"grid": grid}