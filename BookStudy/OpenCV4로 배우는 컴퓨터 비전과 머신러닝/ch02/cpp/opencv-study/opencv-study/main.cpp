#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>

using namespace std;
using namespace cv;

int main(int argc, const char * argv[]) {
    cout << "Hello OpenCV " << CV_VERSION << endl;
    Mat img;
    img = imread("lenna.bmp");

    if (img.empty()) {
        cerr << "Image load failed!" << endl;
        return -1;
    }

    namedWindow("image");
    imshow("image", img);

    waitKey();
    
    return 0;
}
