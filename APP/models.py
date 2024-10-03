from django.db import models
from django.contrib.auth.models import User
import numpy as np
import pickle
import pandas as pd 


from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
#from keras.models import load_model
#import cv2
import numpy as np
import pickle

import json
from PIL import Image
















class UserPredictModel(models.Model):
    image = models.ImageField(upload_to = 'images/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
    