t = 0:0.01:1;

nu = 10;

%compare against known result for alpha = 2
alpha2 = 2;
result2 = talbot_inversion(@(s) s*nu^alpha2/((s+nu)^alpha2 - nu^alpha2), t, 16);
figure(1)
plot(t, result2, 'kx',t, nu^2*exp(-2*nu*t) )

%compare against known result for alpha = 3
alpha3 = 3;
result3 = talbot_inversion(@(s) s*nu^alpha3/((s+nu)^alpha3 - nu^alpha3), t, 16);
figure(2)
plot(t, result3,'kx', t, 2*sqrt(3)/3 *nu^2.*exp(-3*nu.*t/2).*sin(sqrt(3)*nu.*t/2))