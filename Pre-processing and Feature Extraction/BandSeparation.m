% Separating EEG into bands

% xd - denoised signal

%delta
w0=0.1/256;
w1=3.5/256;
wn=[w0,w1];
[b,c]=butter(4,wn);
delta=filter(b,c,xd);

%theta
w0=3.5/256;
w1=8/256;
wn=[w0,w1];
[b,c]=butter(4,wn);
theta=filter(b,c,xd);

%alpha
w1=13/256;
wn=[w0,w1];
[b,c]=butter(4,wn);
alpha=filter(b,c,xd);

%beta
w0=13/256;
w1=30/256;
wn=[w0,w1];
[b,c]=butter(4,wn);
beta=filter(b,c,xd);

%gamma
w0=30/256;
w1=40/256;
wn=[w0,w1];
[b,c]=butter(4,wn);
gamma=filter(b,c,xd);