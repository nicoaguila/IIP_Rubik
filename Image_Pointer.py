import threading
import cv2


class Image_Pointer(threading.Thread):
    """Image Pointer class representation pointing capabilities."""

    def __init__(self, img_path, thread_id, thread_name, thread_lock=None):
        """Initialize Image_Pointer instance."""
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.img_path = img_path
        self.thread_name = thread_name
        self.__thread_lock = thread_lock
        self.xy = []

    def run(self):
        """Start image pointer."""
        print('Starting', self.thread_name)
        self.__show_image()
        print('Exiting', self.thread_name)
        return self.xy

    def __show_image(self):
        """Show image."""
        self.img = cv2.imread(self.img_path, 1)
        # Diplay the image
        cv2.imshow(self.thread_name, self.img)
        # Set mouse callback
        cv2.setMouseCallback(self.thread_name, self.__click_event)
        # Wait for the window to close
        cv2.waitKey(0)
        # close the window
        cv2.destroyAllWindows()

    def __click_event(self, event, x, y, flags, params):
        """Display the coordinates of the points clicked on the image."""
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            # displaying the coordinates
            # on the Shell
            print(f'X:{x}, Y:{y}')
            self.xy.append((x, y))

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.img, str(x) + ',' +
                        str(y), (x, y), font,
                        1, (255, 0, 0), 2)
            cv2.imshow(self.thread_name, self.img)

        # checking for right mouse clicks
        if event == cv2.EVENT_RBUTTONDOWN:

            # displaying the coordinates
            # on the Shell
            print(f'X:{x}, Y:{y}')
            self.xy.append((x, y))
            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            b = self.img[y, x, 0]
            g = self.img[y, x, 1]
            r = self.img[y, x, 2]
            cv2.putText(self.img, str(b) + ',' +
                        str(g) + ',' + str(r),
                        (x, y), font, 1,
                        (255, 255, 0), 2)
            cv2.imshow(self.thread_name, self.img)
