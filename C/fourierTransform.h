#define CeTCCC_Pi M_PI;
#define CeTCCC_Cnt_FFT_NumOfPnts 128; // number of time samples
#define CeTCCC_t_LoopTime 0.00625; // time of sample
void ExceTCCC_FFT(double VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts]);

double VeTCCC_f_LoopFreq = 0;
double VeTCCC_f_LoopFreqBase = 0;
bool VeTCCC_b_ShutterDetect = false;
double KeTCCC_ShutterThresh = 0;
double VeTCCC_n_InSpd[CeTCCC_Cnt_FFT_NumOfPnts] = {0}; // value of time samples
