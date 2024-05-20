# Gesture Control

This project enables gesture-based control of volume and brightness using hand gestures captured from a webcam.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/IsfarMohi/Gesture-Control.git
    cd Gesture-Control
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` file includes:
    ```plaintext
    opencv-python
    numpy
    pycaw
    screen_brightness_control
    mediapipe
    ```

3. **Run the main script:**
    ```sh
    python main.py
    ```

## Usage

1. **Use hand gestures to control volume and brightness:**
    - Hold your left hand palm facing the camera to control brightness.
    - Hold your right hand palm facing the camera to control volume.
    - Move your hands closer or further to adjust the volume or brightness accordingly.

2. **Quit the application:**
    Press `q` to exit the application.

## Technologies Used

- **OpenCV:** For video processing and hand gesture detection.
- **NumPy:** For numerical operations.
- **pycaw:** For controlling system audio volume.
- **screen_brightness_control:** For adjusting screen brightness.
- **MediaPipe:** For hand landmark detection.

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository.**
2. **Create your feature branch:**
    ```sh
    git checkout -b feature/YourFeature
    ```
3. **Commit your changes:**
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch:**
    ```sh
    git push origin feature/YourFeature
    ```
5. **Open a pull request.**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please open an issue on [GitHub](https://github.com/IsfarMohi/Gesture-Control/issues) or contact the project owner at [IsfarMohi](https://github.com/IsfarMohi).
