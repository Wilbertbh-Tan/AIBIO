from fastai.vision import *
import numpy as np

def promoterClass(imagepath):
    path =  'model'
    model = load_learner(path, 'promModel.pkl')
    img1 = open_image(imagepath)
    pred_class,pred_idx,outputs = model.predict(img1)
    display(pred_class)
promoterClass('pBAD_inducer_response.png')
