

x = xlsread('Seizure data\P1.xlsx'); % example raw signal

figure(1);
subplot(121);
plot(x);
title('Raw signal');

a= smoothdata(x, 'movmean', 4);
subplot(122);
plot([x' a']);
title('Smoothed signal');
legend('Orginal SIgnal', 'Smoothed signal');

% Band pass filter
fs=256;
ts=1/fs;
t=(0:length(a)-1)*ts;
z=bandpass(a,[1,40],fs) ;
figure(2);
plot(t,z);
title('Bandpass');

[thr,sorh,keepapp]= ddencmp('den','wv',z); 

% 6 levels of wavelet decomposition 
% Wavelet type is Daubechies wavelet
% wavelet denoising and compression

xd=wdencmp('gbl',z,'db6',6,thr,sorh,keepapp); 

figure(4);
plot(x);
hold on;
plot(xd);

legend('Orginal signal', 'Denoised signal');


p=bandpower(xd);
disp('power');
disp(p);
