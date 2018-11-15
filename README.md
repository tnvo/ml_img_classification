# ml_img_classification

### Set up training folder
```
- created a data/ folder
- created train/ and validation/ subfolders inside data/
- created type1/ and type2/ subfolders inside each train/ and validation/

-Split 80/20 between train/validation(test) 


```

### Setting up
* Set up virtualenv 
* Install PIL, keras, numpy, argparse (if you plan on using CLI to pass in img)
 * Have yet to set up argparse in this one

### Training
* Run `python classifier.py`
  * This will output a `final.h5` file which will be used as the model

### Classification
* Run `python img_classification.py` with the correct path to img
  * This will predict if it's type 1 or 2
  
  
