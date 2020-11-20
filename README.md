# **Product Market Analysis**

[![Code Grade](https://www.code-inspector.com/project/15860/score/svg)](https://frontend.code-inspector.com/project/15860/dashboard)
[![Code Grade](https://www.code-inspector.com/project/15860/status/svg)](https://frontend.code-inspector.com/project/15860/dashboard)
***

## **Description:**

Product Market Analysis (abbreviated as PMA) is a software, that makes market research for an upcoming product of a company, a much less strenuous task. Based on sentiment analysis, the software deduces the user&#39;s experience with a product based on their facial expressions.

The software has 2 types of users:

1. Admin:
      1. Can add/delete products
      2. Can view various reactions to the available products
2. Reviewers:
      1. Can view available products and review them

The software is completely dynamic and once a user has reviewed a particular product, they cannot re-review it hence keeping the experience of the product much more honest.

There can be an unlimited number of reviewer and admin accounts with each admin account having an unlimited number of products that they think should be reviewed. The user can see all available products and start reviewing them.

    To run the software, simply run the "driver.py".
   
****

## **Technical Details:**

_ **Model:** _

The Sentiment Analysis model is built on the fer2013 dataset giving an accuracy of _68.61% on train data_ and _65.92% on test data_.

This dataset has a benchmark accuracy of _71.6% on the Inception Model_, _72.4% on Res-Net,_ and _72.7% on VGG_

This dataset consists of 28709 train images and 7178 test images having faces showing 7 different kinds of emotions.

Model Structure:

        1. Model-> CNN\Model\Structure.png

        2. Model-> CNN\Model\Details.txt
        
<br>

_ **Graphical User Interface:** _

The GUI is completely created on Tkinter.

The logo used in the application was taken from the website (link is given below) and manually colored green

        
<br>

_ **Other Requirements:** _

    - numpy==1.16.4            → Array Handling
    - matplotlib==3.1.3        → Model Loss Graph Creation
    - pandas==1.0.1            → Reading Dataset
    - opencv\python==3.4.2.17  → Live Image Extraction
    - Keras==2.3.1             → ConvNet Model
    - Pillow==8.0.1            → Tkinter Image Display
    
****

## **Sources:**

Fer2013 dataset:

    https://www.kaggle.com/deadskull7/fer2013

Fer2013 benchmark details:

    https://paperswithcode.com/sota/facial-expression-recognition-on-fer2013

Tkinter Logo details:

    https://thenounproject.com/term/product-analysis/1542499/
