%%time-stepping for the memory kernel
t = 0:0.001:1;
dt = t(2)-t(1);
Nhist = length(t);

%%%parameters for the alpha distribution
nu = 9;
alpha = 3;
result2 = talbot_inversion(@(s) s*nu^alpha/((s+nu)^alpha - nu^alpha), t, 16);

result2 = result2(2:end); %%the first element of the inversion is a NaN, remove it

result2 = result2/sum(result2); %%normalize

figure(1)
plot(t(1:end-1), result2)


%%%binning the queue
Qmax = 2;
Nbins = 100;
Nstates = Nbins*Qmax + 1;

%%%initialize probability distribution
P = zeros(Nstates, Nhist);
P(1,:) = 1;

%%%generate transition matrix for the renewal process

Tmatrix = zeros(Nstates);
for ii = 1:Nstates-Nbins
    Tmatrix(ii+Nbins,ii)=1;
    Tmatrix(ii,ii) = -1;
end


Nsteps = 5000; %number of Euler steps to run 
%%%results arrays
realP = zeros(Qmax+1,1);
avtraffic = zeros(1,Nsteps);

for j = 1:Nsteps
     %%%deterministic service is represented by a shift in the probability
     %%%array
     if mod(j,10)==0
        Q = zeros(size(P));
        Q(1,:) = P(1,:) + P(2,:);
        Q(2:end-1,:) = P(3:end,:);
        P = Q;
     end
    
    %%%convolution with memory kernel 
    Phist = P(:,end-Nhist+2:end);
%    Pnew = P(:,end); %poisson
    Pnew = zeros(Nstates,1);
    for i = 1:Nstates
        Pnew(i) = sum(result2'.*fliplr(Phist(i,:)))*dt;
    end
    Pnew = Pnew/sum(Pnew); %normalize to eliminate numerical error in the convolution
    
    Pnew = P(:,end) + dt*nu/alpha*Tmatrix*Pnew; %euler step
       
    P(:,end+1) = Pnew; %add the new step to the end of the array
    
    
    %%%collect probability for each occupancy value
    realP(1,j) = P(1,end);
    for jj = 2:Qmax+1
        realP(jj,j) = sum(P(Nbins*(jj-2)+2:Nbins*(jj-1)+1,end));
        avtraffic(j) = avtraffic(j) + (jj-1)*realP(jj,j);
    end
end
figure(2)
plot(realP(:,1:10:end)')

figure(3)
%plot(realP(:,end))
plot(avtraffic)