from distutils.core import setup
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
)