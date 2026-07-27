from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model_dt = joblib.load("/model/iowa_model_dt.pkl")
features = joblib.load("model/iowa_features.pkl")

class HouseFeatures(BaseModel):
    lot_area: float
    year_built: int
    first_floor_sf: float
    second_floor_sf: float
    full_bath: int
    bedroom_above_gr: int
    total_rooms_above_grd: int

@app.get("/predict")
def predict_query(
    lot_area: float,
    year_built: int,
    first_floor_sf: float,
    second_floor_sf: float,
    full_bath: int,
    bedroom_above_gr: int,
    total_rooms_above_grd: int,):

    input_df = pd.DataFrame(
        [[
            lot_area,
            year_built,
            first_floor_sf,
            second_floor_sf,
            full_bath,
            bedroom_above_gr,
            total_rooms_above_grd

        ]],
        columns= features
    )
    prediction = model_dt.predict(input_df)[0]
    return = {"predict_price is": float (prediction)}
