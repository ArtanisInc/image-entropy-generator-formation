# 📸 Image Entropy Generator

## Overview
The **Image Entropy Generator** is a Python-based tool that generates a unique entropy value derived from an image. It leverages OpenCV for face detection, NumPy for statistical calculations, and hashlib for cryptographic hashing. The generated entropy value incorporates:

- The number of detected faces.
- The image file's creation timestamp.
- A SHA-256 checksum of the image file.
- Statistical entropy derived from pixel values.


## ✨ Features

- **Face Detection**: Uses a pre-trained Haar Cascade classifier to detect faces in an image.
- **Image Entropy Calculation**: Computes entropy using pixel distribution and statistical variance.
- **Timestamp Integration**: Incorporates precise file creation time for uniqueness.
- **Cryptographic Hashing**: Uses SHA-256 to enhance randomness and uniqueness.
- **Configurable Length**: Allows users to specify the length of the final entropy value (up to 100 characters).


## 📦 Requirements

Ensure you have Python 3 installed, along with the necessary dependencies.

### Install Dependencies

```bash
pip install -r requirements.txt
```


## 📂 Project Files

| File | Description |
|------|-------------|
| `main.py` | Main script for generating the entropy value. |
| `cascade.xml` | Haar Cascade XML file used for face detection. |
| `requirements.txt` | List of required Python dependencies. |
| `sample1.jpg` | Sample image for testing the script. |


## 🚀 Usage

### Running the Script

1. Ensure your image is in the same directory as the script.
2. Run the script from the command line with a specified length for the entropy value:

```bash
python main.py --length <desired_length>
```

📌 Replace `<desired_length>` with the number of characters you want (max: 100).

### Example:

```bash
python main.py --length 50
```


## 🖥️ Expected Output

When executed, the script will display:

- Number of faces detected in the image.
- Creation timestamp of the image file.
- SHA-256 checksum of the image.
- Final entropy value of the specified length.

### Sample Output:

```
Number of faces detected: 2
Creation date and time: 01/03/2025 15:45:32.789
SHA256 Checksum: 3a7d3e8b9f6c...
Final product (length 50): 239817462392847612039472...
```


## ⚙️ Customization

- **Modify `MAX_LENGTH`** in `main.py` to change the maximum allowable length.
- **Use a different image** by replacing `sample1.jpg` with your own.
- **Update the cascade classifier** by using a different `cascade.xml` file if needed.


## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or bug fixes.


## 📧 Contact

For any questions or suggestions, feel free to open an issue or reach out via GitHub.


## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
