% Extracting Features Hjorth Parameters and Entropy

% Extracting Hjorth parameters

z = xd; %denoised signal

for i = 1:19 % for all 19 electrodes
    
        Hj_Parameters = Hjorth(z);
end

% Extracting Entropy

for i = 1:19
    x = xd(:,i);
    E = wentropy(x, 'shannon');
    
end  

M = [Hj_Parameters, E];

% Save features for each of the 19 electrodes
% Resultant is a 4x19 matrix
writematrix(M,'Features.xlsx')

%%
function [act,mob,comp] = Hjorth(z)

%Hjorth Parameters
% Activity
activity = var(z);
act = activity;
disp('activity');
disp(activity);
   
% Mobility
mobility = std(diff(z))./std(z);
mob = mobility;
disp('mobility');
disp(mobility);


% Complexity
complexity = std(diff(diff(z)))./std(diff(z))./mobility;
comp = complexity;
disp('complexity');
disp(complexity);

end