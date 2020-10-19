clc;
clear all;
A= [4 1 0; 1 20 1; 0 1 4]
x=[1;1;1]
e=0.001
k_i=1
while 1
    y=A*x;
    k_f= norm(y,inf);
    x=(1/k_f)*y
    if abs(k_f-k_i)<e
        break;
    end
    k_i=k_f
end
disp("Eigen vector is")
disp(x)
disp("Largest Eigen value is")
disp(k_f)


