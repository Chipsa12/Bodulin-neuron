from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
from application.modules.neuron.deformationImg import deformationImg

def main(filename):
    # draw each face separately
    def draw_faces(filename, result_list):
        # load the image
        data = pyplot.imread(filename)
        # plot each face as a subplot
        arr = []
        for i in range(len(result_list)):
            # get coordinates
            x1, y1, width, height = result_list[i]['box']
            x2, y2 = x1 + width, y1 + height
            # define subplot
            # pyplot.subplot(1, len(result_list), i + 1)
            pyplot.subplot(1, 1, 1)
            pyplot.axis('off')
            # plot face
            pyplot.imshow(data[y1:y2, x1:x2])
            arr.append(data[y1:y2, x1:x2])
            pyplot.savefig('face_found_people/img' + str(i) + '.jpg')
            deformationImg('face_found_people/', 'deformation_img/')
            # show the plot
            # pyplot.show()


    # load image from file
    pixels = pyplot.imread(filename)
    print(pixels)
    # create the detector, using default weights
    detector = MTCNN()
    # detect faces in the image
    faces = detector.detect_faces(pixels)
    # display faces on the original image
    draw_faces(filename, faces)
