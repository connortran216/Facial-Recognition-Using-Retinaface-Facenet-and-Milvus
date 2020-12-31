import uvicorn
from fastapi import FastAPI, File
import requests


app = FastAPI()


@app.post("/add_index/image")
async def add_api(file: bytes = File(...)):

	url = "http://core:8000/add_api_add_index_image_post"
	payload = {}
	files = [
		('file', file)
	]
	headers = {}

	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	res = {
		"text": response.content.decode("utf-8"),
		"status": 200
	}
	return res


@app.post("/predict/image")
async def predict_api(file: bytes = File(...)):
	url = "http://core:8000/predict_api_predict_image_post"

	payload = {}
	files = [
		('file', file)
	]
	headers = {}

	response = requests.request("POST", url, headers=headers, data=payload, files=files)

	res = {
		"text": response.content.decode("utf-8"),
		"status": 200
	}
	return res


if __name__ == "__main__":
	# host = 'localhost' if run local else '0.0.0.0'
	uvicorn.run(app, port=8888, host='api_gateway', debug=True)