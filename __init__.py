import data_loaders
import transformers
import pdb
from sqlalchemy import create_engine

# Database definition
engine = create_engine(
    'postgresql://postgres:postgres123@localhost:5434/postgres')

# Data Loading
initial_data = {
    'offerings': data_loaders.load_offerings(),
    'reviews': data_loaders.load_reviews()
}

# Data Transorming

df = transformers.transform_data(**initial_data)
# Data exporting
