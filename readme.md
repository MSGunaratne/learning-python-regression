
- `app.py`: The main Flask application file, handling routing, data processing, and model prediction.
- `house_price_prediction.pkl`: The pre-trained machine learning model used for predictions.
- `templates/index.html`: The HTML template for the web interface, including the input form and prediction display.
- `requirements.txt`: Lists all the Python dependencies required for the project.

## Installation and Local Setup

Follow these steps to set up and run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MSGunaratne/learning-python-regression.git
    cd https://github.com/MSGunaratne/learning-python-regression.git
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`.

## Usage

Once the application is running:

1.  Open your web browser and go to `http://127.0.0.1:5000/`.
2.  Enter the values for the various housing features in the form.
3.  Click the "Predict Housing Price" button to see the predicted price.



```python
import os
# ... other imports

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000)) # Use environment variable PORT or default to 10000
    app.run(host="0.0.0.0", port=port, debug=True)
```

**Live Demo:**
https://learning-python-regression.onrender.com/

## Screenshot



## License

This project is licensed under the MIT License - see the LICENSE.md file for details. (Note: You might want to create a `LICENSE.md` file if you plan to openly license your project.)