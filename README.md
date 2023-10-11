# Gradio Chatbot with OpenAI API

This repository contains a Gradio chatbot application using the OpenAI API.

## Prerequisites

- Docker

## Building the Docker container

To build the Docker container, run the following command in the terminal:

```bash
docker build --build-arg OPENAI_API_URL=<your_openai_api_url> --build-arg OPENAI_API_KEY=<your_openai_api_key> --build-arg OPENAI_MODEL=<your_openai_model> -t gradio_chatbot .
```

Replace `<your_openai_api_url>`, `<your_openai_api_key>`, and `<your_openai_model>` with your OpenAI API URL, API key, and the model you want to use, respectively.

## Running the Docker container

To run the Docker container, use the following command:

```bash
docker run -p 7860:7860 gradio_chatbot
```

The Gradio chatbot interface will be accessible at http://localhost:7860.

## Running the application using Docker Compose

Before running the containers using Docker Compose, make sure you have set the environment variables OPENAI_API_KEY, OPENAI_MODEL, and HF_TOKEN. You can set them in a .env file or export them in your shell.

To build and run the containers using Docker Compose, execute the following command:

```bash
docker-compose up
```

The Gradio chatbot interface will be accessible at http://localhost:7860. The Mistral-7B model will be running in a separate container and will communicate with the Gradio chatbot interface internally.