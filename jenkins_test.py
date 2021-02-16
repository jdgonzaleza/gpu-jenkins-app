import cv2


def test_is_working():
    count = cv2.cuda.getCudaEnabledDeviceCount()
    assert count == 1
