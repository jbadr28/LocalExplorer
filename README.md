#Local Explorer App

## Overview

Weather Explorer is a user-friendly application developed using OpenAPI, Streamlit, OpenWeather API, and Google Maps API. This application allows users to explore weather conditions for a given location and provides personalized activity or place suggestions based on the weather and location data. Additionally, it utilizes the Google Maps API to display the best route to the recommended destination.
[Link](https://jbe-local-explorer-gpt.streamlit.app/)
## Features

- **Location-based Weather Information:** Retrieve real-time weather data for any location.
- **Activity Recommendations:** Receive personalized activity suggestions based on the current weather conditions.
- **Route Planning:** Utilize Google Maps API to find the best route to the recommended destination.

## Technologies Used

- **Streamlit:** A Python library for creating web applications with minimal code.
- **OpenAPI:** An open standard for building APIs, used for seamless communication with OpenWeather API.
- **OpenWeather API:** Provides weather data for any location in the world.
- **Google Maps API:** Allows integration with Google Maps functionality, including route planning.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jbadr28/LocalExplorer.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up API keys:**
   - Get an API key from [OpenWeather](https://openweathermap.org/api) and replace `'YOUR_OPENWEATHER_API_KEY'` in the code with your key.
   - Get an API key from [Google Cloud Platform](https://cloud.google.com/maps-platform/) and replace `'YOUR_GOOGLE_MAPS_API_KEY'` in the code with your key.

## Usage

1. **Run the application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your browser and navigate to the provided local address (usually `http://localhost:8501`).**

3. **Enter the desired location and explore the weather, activity suggestions, and the best route on the interactive map.**

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file to provide more specific details about your application or include additional sections as needed.
