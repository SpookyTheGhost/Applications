/*
 * The purpose of this project is to determine increased chances of "vehicle shaking" may occur soon. The concept utilizes Fourier Transform on a continuous time sample of clutch signal frequencies. If the chances of "vehicle shaking" may occur in the near future, then a flag is thrown that activates a light beacon in the vehicle.
*/

#include <stdio.h>
#include <fourierTransform.h>
#include <math.h>


VeTCCC_f_LoopFreq = 1/CeTCCC_t_LoopTime;
VeTCCC_f_LoopFreqBase = VeTCCC_f_LoopFreq/CeTCCC_Cnt_FFT_NumOfPnts;


void PermTCCC_ShutterDetect(double *VeTCCC_Amplitude) {
	// get actual signal value at specified time sample
	for (int i = CeTCCC_Cnt_FFT_NumOfPnts-1; i >= 1; i--) {
		VeTCCC_n_InSpd[i] = VeTCCC_n_InSpd[i-1];
	}
	// call to get current vehicle speed
	VeTCCC_n_InSpd[0] = vehicleSpeed();

	// call fourierTransform on all input
	ExceTCCC_FFT(VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts], *LeTCCC_Amplitude);

	scanf("%d", KeTCCC_ShutterThresh);
	// turn on the indicator light
	if (LeTCCC_Amplitude[6] > KeTCCC_ShutterThresh || LeTCCC_Amplitude[7] > KeTCCC_ShutterThresh || LeTCCC_Amplitude[8] > KeTCCC_ShutterThresh || LeTCCC_Amplitude[9] > KeTCCC_ShutterThresh) {
		VeTCCC_b_ShutterDetect = true;
	}	
}

// fast Fourier transform
double * ExceTCCC_FFT(double VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts], double *LeTCCC_Amplitude) {
	double LeTCCC_Real[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	double LeTCCC_Imag[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	double LeTCCC_Freq[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	static double LeTCCC_Amplitude[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	double LeTCCC_Angle[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	double LeTCCC_deg_Rad[CeTCCC_Cnt_FFT_NumOfPnts] = {0};
	
	// k is current sample
	for (int k = 0; k < CeTCCC_Cnt_FFT_NumOfPnts; k++) {
		// only need to calculate first half range
		for (int CeTCCC_Cnt_FFT_NumOfPnts = 0; CeTCCC_Cnt_FFT_NumOfPnts < CeTCCC_Cnt_FFT_NumOfPnts; CeTCCC_Cnt_FFT_NumOfPnts++) {
			//double f = k * VeTCCC_f_LoopFreqBase; // useless calculation?
			LeTCCC_Freq[k] = k * (CeTCCC_Cnt_FFT_NumOfPnts/CeTCCC_Cnt_FFT_NumOfPnts);
			LeTCCC_deg_Rad[k] = -2 * CeTCCC_Pi * LeTCCC_Freq[k];
			LeTCCC_Real[k] += VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts] * cos(LeTCCC_deg_Rad[k])
			LeTCCC_Imag[k] += VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts] * sin(LeTCCC_deg_Rad[k])
			&LeTCCC_Amplitude[k] = sqrt(pow(LeTCCC_Real[CeTCCC_Cnt_FFT_NumOfPnts], 2) + pow(LeTCCC_Imag[CeTCCC_Cnt_FFT_NumOfPnts], 2));
			LeTCCC_Angle[k] = atan2(sin(LeTCCC_deg_Rad)/cos(LeTCCC_deg_Rad));
		}	
	}
	return LeTCCC_Amplitude;
}
