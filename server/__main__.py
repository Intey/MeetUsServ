import os
import sys
import logging
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

logging.basicConfig(level=logging.DEBUG)
from main import main

main()
