import keras_ocr
import matplotlib.pyplot as plt

def ocr_model(images):

    pipeline = keras_ocr.pipeline.Pipeline()

    images = [
          keras_ocr.tools.read(img) for img in ["image-1.jpg", "image-2.jpg", "image-3.png", "image-4.jpg"]
            ]

    len(images)
    prediction_grps = pipeline.recognize(images)

    fig, axs = plt.subplots(nrows = len(images), figsize = (8,16))
    for ax, image, predictions in zip(axs, images, prediction_grps):
        keras_ocr.tools.drawAnnotations(image = image, predictions = predictions, ax = ax)




ocr_model("images")
