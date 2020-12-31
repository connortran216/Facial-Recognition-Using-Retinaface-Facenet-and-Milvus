import uvicorn
from fastapi import FastAPI, File

from retina_model import predict, read_imagefile
from retina_milvus_search import add

api_receive = FastAPI(title='Test Deep Learning')


@api_receive.post("/add_api_add_index_image_post")
async def index_api(file: bytes = File(...)):
	image = read_imagefile(file)
	addition = add(image)

	return addition

@api_receive.post("/predict_api_predict_image_post")
async def index_api(file: bytes = File(...)):
	image = read_imagefile(file)
	prediction = predict(image)

	return prediction

if __name__ == "__main__":
	# host = 'localhost' if run local else '0.0.0.0'
	uvicorn.run(api_receive, port=8000, host='core', debug=True)