{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3e30abe-9ae8-4e08-a76e-6b25e9eac943",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.spatial import distance\n",
    "from imutils import face_utils\n",
    "from pygame import mixer\n",
    "import imutils\n",
    "import dlib\n",
    "import cv2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dc389d9e-c6eb-442d-8241-e8fe084919bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install cmake\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e33c1025-6774-4236-8fba-47f6d3082213",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install dlib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37c29b81-64f7-47b3-ace0-076594c3eaad",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.spatial import distance\n",
    "from imutils import face_utils\n",
    "from pygame import mixer\n",
    "import imutils\n",
    "import dlib\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a42d3041-447b-42ad-8d28-919bb0a2c06e",
   "metadata": {},
   "outputs": [],
   "source": [
    "mixer.init()\n",
    "mixer.music.load(\"music.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df1f6661-741b-465d-a8f2-6e1c9ab2b84b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def eye_aspect_ratio(eye):\n",
    "\tA = distance.euclidean(eye[1], eye[5])\n",
    "\tB = distance.euclidean(eye[2], eye[4])\n",
    "\tC = distance.euclidean(eye[0], eye[3])\n",
    "\tear = (A + B) / (2.0 * C)\n",
    "\treturn ear"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f3a76fd-4ac0-40cf-9f4e-fcadd34e5e32",
   "metadata": {},
   "outputs": [],
   "source": [
    "thresh = 0.25\n",
    "frame_check = 37\n",
    "detect = dlib.get_frontal_face_detector()\n",
    "predict = dlib.shape_predictor(\"shape_predictor_68_face_landmarks.dat\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "956f806d-e3d1-4101-bff6-f4d003dad145",
   "metadata": {},
   "outputs": [],
   "source": [
    "(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS[\"left_eye\"]\n",
    "(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS[\"right_eye\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "589a26e3-2468-44bc-bf51-4b39a3408dd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "cap = cv2.VideoCapture(0)\n",
    "flag = 0\n",
    "while True:\n",
    "    ret, frame = cap.read()\n",
    "    frame = imutils.resize(frame, width=450)\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    subjects = detect(gray, 0)\n",
    "\n",
    "    for subject in subjects:\n",
    "        shape = predict(gray, subject)\n",
    "        shape = face_utils.shape_to_np(shape)\n",
    "        leftEye = shape[lStart:lEnd]\n",
    "        rightEye = shape[rStart:rEnd]\n",
    "        leftEAR = eye_aspect_ratio(leftEye)\n",
    "        rightEAR = eye_aspect_ratio(rightEye)\n",
    "        ear = (leftEAR + rightEAR) / 2.0\n",
    "\n",
    "        leftEyeHull = cv2.convexHull(leftEye)\n",
    "        rightEyeHull = cv2.convexHull(rightEye)\n",
    "        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)\n",
    "        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)\n",
    "\n",
    "        # Alert check\n",
    "        if ear < thresh:\n",
    "            flag += 1\n",
    "            print(flag)\n",
    "            if flag >= frame_check:\n",
    "                # Display the alert message on the frame\n",
    "                cv2.putText(frame, \"****************ALERT!****************\", (10, 30),\n",
    "                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)\n",
    "                cv2.putText(frame, \"****************ALERT!****************\", (10, 325),\n",
    "                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)\n",
    "\n",
    "                # Play the alert sound\n",
    "                if not mixer.music.get_busy():  # Play sound only if not already playing\n",
    "                    mixer.music.play()\n",
    "        else:\n",
    "            flag = 0  # Reset the alert flag when eyes are open\n",
    "\n",
    "    # Show the frame with any text overlay\n",
    "    cv2.imshow(\"Frame\", frame)\n",
    "\n",
    "    # Break the loop if 'q' is pressed\n",
    "    key = cv2.waitKey(1) & 0xFF\n",
    "    if key == ord(\"q\"):\n",
    "        break\n",
    "\n",
    "# Release resources\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e99580a2-5373-417a-95a9-fe9314677f8c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
