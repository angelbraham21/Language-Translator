def detect_labels(path):
    """Detects labels in the file."""
    from google.cloud import vision
    import io
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/ANGEL ABRAHAM/Downloads/qwiklabs-gcp-02-d6346f5fbcd0-f901dddf8e80.json"
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    l=[]
    for label in labels:
        l.append(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
                
    return l