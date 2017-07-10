import io
from google.cloud import vision
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()

vision_client = vision.Client(project='reading books')

with io.open('page.jpg', 'rb') as image_file:
    content = image_file.read()

image = vision_client.image(content=content)

texts = image.detect_text()
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                    for bound in text.bounds.vertices])

    print('bounds: {}'.format(','.join(vertices)))