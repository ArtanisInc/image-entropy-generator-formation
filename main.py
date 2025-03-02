import cv2
import os
import datetime
import hashlib
import argparse
import time
import numpy as np

MAX_LENGTH = 100  # Maximum allowed length

def generate_entropy_value(img_path, cascade_path):
    # Face detection
    face_cascade = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.equalizeHist(img)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    face_count = max(1, len(faces))

    # File and time information
    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(img_path))
    nanosecond_time = time.time_ns()

    # Calculate hash and entropy of the image
    with open(img_path, "rb") as f:
        checksum = int(hashlib.sha256(f.read()).hexdigest(), 16)

    image_entropy = int(np.sum(img) * np.std(img) * 1e5)

    # Generate the final number
    entropy_value = int(f"{face_count * 137}{creation_time.year}{creation_time.month}{creation_time.day}"
                        f"{creation_time.hour}{creation_time.minute}{creation_time.second}{creation_time.microsecond}"
                        f"{nanosecond_time}{image_entropy}{str(checksum)[:20]}")

    return entropy_value, face_count, creation_time, checksum

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, required=True, help=f"Length of the generated number (max {MAX_LENGTH})")
    args = parser.parse_args()

    if args.length > MAX_LENGTH:
        print(f"⚠️ Length too large! Automatically reducing to {MAX_LENGTH}.")
        args.length = MAX_LENGTH

    entropy_value, face_count, creation_time, checksum = generate_entropy_value('sample1.jpg', 'cascade.xml')

    print(f"Number of faces detected: {face_count}")
    print(f"Creation date and time: {creation_time.strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]}")
    print(f"SHA256 Checksum: {checksum}")
    print(f"Final product (length {args.length}): {str(entropy_value)[:args.length]}")
