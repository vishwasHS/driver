{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "948679f2-3a1d-40eb-8d0a-7410a95eb196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (1.37.1)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (24.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (10.4.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (4.25.3)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (13.7.1)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (4.11.0)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: watchdog<5,>=2.1.5 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\vishwas\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c430d2f0-ba3f-4266-af63-07068d41cbc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pygame 2.6.1 (SDL 2.28.4, Python 3.12.7)\n",
      "Hello from the pygame community. https://www.pygame.org/contribute.html\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from scipy.spatial import distance\n",
    "from imutils import face_utils\n",
    "import imutils\n",
    "import dlib\n",
    "import cv2\n",
    "from pygame import mixer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "16c9bcda-e76e-40ad-bc20-5874c2e38ba7",
   "metadata": {},
   "outputs": [],
   "source": [
    "mixer.init()\n",
    "mixer.music.load(\"music.wav\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d818cb26-736c-43ce-97b2-c273fe7e33af",
   "metadata": {},
   "outputs": [],
   "source": [
    "def eye_aspect_ratio(eye):\n",
    "    A = distance.euclidean(eye[1], eye[5])\n",
    "    B = distance.euclidean(eye[2], eye[4])\n",
    "    C = distance.euclidean(eye[0], eye[3])\n",
    "    ear = (A + B) / (2.0 * C)\n",
    "    return ear"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "18568d0b-b92c-417e-9e25-4b67409efa1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "thresh = 0.25\n",
    "frame_check = 37\n",
    "detect = dlib.get_frontal_face_detector()\n",
    "predict = dlib.shape_predictor(\"shape_predictor_68_face_landmarks.dat\")\n",
    "(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS[\"left_eye\"]\n",
    "(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS[\"right_eye\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "92760e3c-bbed-4604-aa19-214a84bf81db",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-12-10 22:46:46.697 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\VISHWAS\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "st.title(\"Distracted Driver Detection\")\n",
    "run_app = st.checkbox(\"Run Detection\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "88090088-3385-4fbb-a6ce-35d928300914",
   "metadata": {},
   "outputs": [],
   "source": [
    "if run_app:\n",
    "    cap = cv2.VideoCapture(0)\n",
    "    flag = 0\n",
    "\n",
    "    stframe = st.empty()\n",
    "\n",
    "    while True:\n",
    "        ret, frame = cap.read()\n",
    "        if not ret:\n",
    "            st.error(\"Failed to access the camera!\")\n",
    "            break\n",
    "\n",
    "        frame = imutils.resize(frame, width=450)\n",
    "        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "        subjects = detect(gray, 0)\n",
    "\n",
    "        for subject in subjects:\n",
    "            shape = predict(gray, subject)\n",
    "            shape = face_utils.shape_to_np(shape)\n",
    "            leftEye = shape[lStart:lEnd]\n",
    "            rightEye = shape[rStart:rEnd]\n",
    "            leftEAR = eye_aspect_ratio(leftEye)\n",
    "            rightEAR = eye_aspect_ratio(rightEye)\n",
    "            ear = (leftEAR + rightEAR) / 2.0\n",
    "\n",
    "            leftEyeHull = cv2.convexHull(leftEye)\n",
    "            rightEyeHull = cv2.convexHull(rightEye)\n",
    "            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)\n",
    "            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)\n",
    "\n",
    "            # Alert check\n",
    "            if ear < thresh:\n",
    "                flag += 1\n",
    "                if flag >= frame_check:\n",
    "                    cv2.putText(frame, \"****************ALERT!****************\", (10, 30),\n",
    "                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)\n",
    "                    cv2.putText(frame, \"****************ALERT!****************\", (10, 325),\n",
    "                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)\n",
    "\n",
    "                    if not mixer.music.get_busy():\n",
    "                        mixer.music.play()\n",
    "            else:\n",
    "                flag = 0  # Reset the alert flag when eyes are open\n",
    "\n",
    "        # Display the frame in the Streamlit app\n",
    "        stframe.image(frame, channels=\"BGR\")\n",
    "\n",
    "        # Stop if the checkbox is unchecked\n",
    "        if not run_app:\n",
    "            break\n",
    "\n",
    "    cap.release()\n",
    "else:\n",
    "    st.write(\"Check the box above to start detection.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "7b68a8ab-da91-41d2-ba7f-0d7b42b32463",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (507122745.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[17], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run app.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run app.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37b47a4f-7459-4744-ae1d-78428ab31cf1",
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
