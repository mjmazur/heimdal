import cv2


class Writer:
    def __init__(self,
                 filename,
                 width,
                 height,
                 fourcc='THEO',
                 framerate=20):
        self.filename = filename
        self.writer = cv2.VideoWriter(
            filename,
            cv2.cv.CV_FOURCC(*fourcc),
            framerate,
            (width, height))

    def close(self):
        self.writer.release()

    def __call__(self, frame):
        self.writer.write(frame)