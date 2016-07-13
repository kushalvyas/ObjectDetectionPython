#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/opencv.hpp"
#include "iostream"
#include "cmath"

using namespace std;
using namespace cv;

int main(){
	cout<<"Template matching \n";
	Mat tImage, aImage, aCopy;
	tImage = imread("tempCrop.jpg",0);
	aImage = imread("temA1.jpg",0);
	aCopy = imread("temA1.jpg");


	// performing template matching using SAD method
	Size Tsize, Isize ;
	Tsize = tImage.size();
	Isize = aImage.size();

	
	long int minSAD = 999999999999, SAD=0;
	int xloc=0, yloc=0, sadloc=0;
	// loop through the actual image
	int a_i, a_j;
	for (a_i =0; a_i < Isize.height - Tsize.height; a_i++){
		for (a_j=0; a_j < Isize.width - Tsize.width; a_j++){
			SAD = 0;

			// check every pixel of actual image with the template image
			// loop through the template image
			for(int t_j=0; t_j < Tsize.width; t_j++){
				for(int t_i=0; t_i < Tsize.height; t_i++){
					uchar aT = aImage.at<uchar>( a_i+t_i, a_j+t_j );
					uchar tT = tImage.at<uchar>(t_i, t_j);
					SAD += pow(abs(int(aT) - int(tT)),2);
				}
			}
			// cout <<"SASD sis "<<SAD<<endl; 
			// save the best found position
			if(minSAD > SAD ){
				cout <<" SAD "<< SAD<<endl;
				minSAD = SAD;
				yloc = a_i;
				xloc = a_j;
				sadloc = SAD;
			}
		}
	}

	cout<<"Template size"<<Tsize<<endl;
	cout<<"Image size"<<Isize<<endl;

	cout<<a_i<<" "<<a_j<<endl;

	cout<<xloc<<","<<yloc<<" SAD is "<<sadloc<<endl;

	// create a rectangle to demarkate the region
	rectangle(aCopy, Point(xloc, yloc), Point(xloc+Tsize.width, yloc+Tsize.height), Scalar(0,0,255), 2);

	// imshow("Template image", tImage);
	imshow("Actual image", aImage);
	imshow("Matched Image", aCopy);
	waitKey();
	destroyAllWindows();

	return 0;
}