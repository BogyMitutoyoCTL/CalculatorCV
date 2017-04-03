import cv2

class Window:

    def create_window(self, fenster_name):
        cv2.namedWindow(fenster_name)

    def wait_key(self):
        cv2.waitKey(0) & 0xFF

    def create_Trackbar(self, fenster_name):
        cv2.createTrackbar("lower_h", fenster_name, 0, 180, self.lower_h_changed)
        cv2.createTrackbar("upper_h", fenster_name, 0, 180, self.upper_h_changed)
        cv2.createTrackbar("lower_s", fenster_name, 0, 255, self.lower_s_changed)
        cv2.createTrackbar("upper_s", fenster_name, 0, 255, self.upper_s_changed)
        cv2.createTrackbar("lower_v", fenster_name, 0, 255, self.lower_v_changed)
        cv2.createTrackbar("upper_v", fenster_name, 0, 255, self.upper_v_changed)
        cv2.createTrackbar("minimalgröße", fenster_name, 0, 1080, self.size_changed)

    def lower_h_changed(self, wert):
        """Funktion die geändert werden soll"""

    def upper_h_changed(self,wert):
        """Funktion die geändert werden soll"""

    def lower_s_changed(self,wert):
        """Funktion die geändert werden soll"""

    def upper_s_changed(self,wert):
        """Funktion die geändert werden soll"""

    def lower_v_changed(self,wert):
        """Funktion die geändert werden soll"""

    def upper_v_changed(self,wert):
        """Funktion die geändert werden soll"""

    def size_changed(self,wert):
        """Funktion die geändert werden soll"""


Fenster = Window()
Fenster.create_window("Taschenrechner")
Fenster.create_window("Präsentation")
Fenster.wait_key()
Fenster.create_Trackbar("Taschenrechner")
Fenster.wait_key()