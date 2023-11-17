# Insurance Claim Processing

## Development

### Requirements

- Python 3.11
- Nodejs > 18
- An existing instance of Hugging Face TGI with a loaded model available at `INFERENCE_SERVER_URL`. This application is based on Mistral-TB Prompt format. You will need to modify this format if you are using a different model.

### Installation

Run `npm install` from the main folder.

If you want to install packages manually:

- In the `frontend` folder, install the node modules with `npm install`.
- In the `backend` folder, create a venv and install packages with the provided Pipfile/Pipfile.lock files.
- In the `backend` folder, create the file `.env` base on the example `.env.example` and enter the configuration for the Inference server.

### Develop

From the main folder, launch `npm run dev`. This will launch both backend and frontend.

- Frontend is accessible at `http://localhost:9000`
- Backend is accessible at `http://localhost:5000`, with Swagger API doc at `http://localhost:5000/docs`
