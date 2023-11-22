import data_loaders
import transformers
import data_exporters
# Data Loading
initial_data = {
    'offerings': data_loaders.load_offerings(),
    'reviews': data_loaders.load_reviews()
}
# Data Transorming
data_transformed = transformers.transform_data(**initial_data)
# Data Exporting
data_exporters.export_to_sql(data_transformed)
print("Done!")
