# Image Classification Project

This project is currently under development. It is a Flask-based web application for uploading and classifying images. Below is a brief overview of the project's setup and functionality.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Routes](#routes)
- [File Upload](#file-upload)
- [Image Classification](#image-classification)
- [Contributing](#contributing)
- [License](#license)

## Installation
To get started with the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/image-classification.git
    cd image-classification
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration
Set up the necessary configurations in the `main.py` file.

- `UPLOAD_FOLDER`: The folder where uploaded files will be stored.
- `ALLOWED_EXTENSIONS`: Allowed file extensions for uploads.
- `SECRET_KEY`: A secret key for session management.

## Usage
To run the application, use the following command:
```sh
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

## Routes
- `/`: Home page displaying a welcome message.
- `/upload_form`: Page to upload images for classification.
- `/upload`: Endpoint to handle file uploads and classification.

## File Upload
Files can be uploaded through the `/upload_form` route. The uploaded file must be of type `.jpg` or `.jpeg`.

### Example
```html
<form action="/upload" method="post" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
```

## Image Classification
The uploaded image is processed and classified using a predefined model. The results, including the label and confidence percentage, are displayed on the result page.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
