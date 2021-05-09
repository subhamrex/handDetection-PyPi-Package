# Package Creation
#### 1. Create folder named handDetection and put our our hand_tracking_module.py file there.
#### 2. Create a __init__.py file in newly created handDetection folder and write `from handDetection import hand_tracking_module`.
#### 3. Create a LICENCE file.
#### 4. Create a setup.py file and write this code:
`from distutils.core import setup
setup(
  name = 'handDetection',         # How you named your package folder (MyLib)
  packages = ['handDetection'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Help to detect hand using OpenCV and mediapipe',   # Give a short description about your library
  author = 'Subham Kundu',                   # Type in your name
  author_email = 'subhamkundu486@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/subhamrex',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/subhamrex/handDetection-PyPi-Package',    # I explain this later on
  keywords = ['ComputerVision', 'HandDetection', 'handDetectionModule'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'opencv-python',
          'mediapipe',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)`
<br/>

#### 5. Create a README.md file

#### 6. Create a setup.cfg file and write: `[metadata]
description-file = README.md`

#### 7. Run `python setup.py sdist`

#### 8. Run `pip install twine`

#### 9. Run `twine upload dist/*` and Enter your username and password. After that It will be uploaded.


# handDetection Package `pip install handDetection==0.1`
### In our package we have handDetector class which has findHands,findPosition,fingersUp and findDistance functions.

#### 1. findHands function: It will take two parameters.But by default one parameter are given. You have pass at least one parameter.
`Parameters: img, draw=True` 
<br />
#### It will help you to detect your hand. 



#### 2. findPosition function:It will take three parameters.But by default two parameters are given. You have pass at least one parameter.
`Parameters: img, handNo=0, draw=True`
<br/>
#### It will help to find position of fingers in hand.


#### 3. fingersUp function:It will take no parameter.
<br/>

#### It will help you to detection your finger is u or not.

#### 4. findDistance function: It will take six parameters.But by default four parameters are given. You have pass at least two parameters.
`Parameters: point, point, image, draw= True, r =15 and t = 3`
<br/>

#### It will help to find the distance between fingers.

 
