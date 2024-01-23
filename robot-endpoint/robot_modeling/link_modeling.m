clear all
close all

%syms theta1 theta2 theta3 a1 a2 a3 d1 d2 d3 alpha1 alpha2 alpha3

theta = [90 0 -90 0]*pi/180; %angle of each axis in degrees
alpha = [0 0 0 0]; %zero for a planar manipulator
a = [1 1 1 1]; % link length
d = [0 0 0 0 ]; % translation

% define the transformation matrices
i = 1; %end of link 1 to the base of link 1
%T1 is 1 to 0
T1 = [cos(theta(i)) -sin(theta(i))*cos(alpha(i)) sin(theta(i))*sin(alpha(i)) a(i)*cos(theta(i));
sin(theta(i)) cos(theta(i))*cos(alpha(i)) -cos(theta(i))*sin(alpha(i)) a(i)*sin(theta(i));
0 sin(alpha(i)) cos(alpha(i)) d(i);
0 0 0 1;];

i = 2; %end of link 2 to the base of link 2
T2 = [cos(theta(i)) -sin(theta(i))*cos(alpha(i)) sin(theta(i))*sin(alpha(i)) a(i)*cos(theta(i));
sin(theta(i)) cos(theta(i))*cos(alpha(i)) -cos(theta(i))*sin(alpha(i)) a(i)*sin(theta(i));
0 sin(alpha(i)) cos(alpha(i)) d(i);
0 0 0 1;];

i = 3; %end of link 3 to the base of link 3s
T3 = [cos(theta(i)) -sin(theta(i))*cos(alpha(i)) sin(theta(i))*sin(alpha(i)) a(i)*cos(theta(i));
sin(theta(i)) cos(theta(i))*cos(alpha(i)) -cos(theta(i))*sin(alpha(i)) a(i)*sin(theta(i));
0 sin(alpha(i)) cos(alpha(i)) d(i);
0 0 0 1;];

i = 4; %end of link 3 to the base of link 3s
T4 = [cos(theta(i)) -sin(theta(i))*cos(alpha(i)) sin(theta(i))*sin(alpha(i)) a(i)*cos(theta(i));
sin(theta(i)) cos(theta(i))*cos(alpha(i)) -cos(theta(i))*sin(alpha(i)) a(i)*sin(theta(i));
0 sin(alpha(i)) cos(alpha(i)) d(i);
0 0 0 1;];

%from frame 1 to base (0)
T10 = T1;
%from frame 2 to base (0)
T20 = T1 * T2;
%from frame 3 to base (0)
T30 = T1 * T2 * T3;
%from frame 4 to base (0)
T40 = T1 * T2 * T3 * T4;

%there is no rotation from the tip fream from the base frame but is shifted
%3 units along x
% T30 =
% 
%      1     0     0     3
%      0     1     0     0
%      0     0     1     0
%      0     0     0     1


%%PLOT LINKS

% plot link 1
P1s = [0,0]; %link 1 start at 0
P1e = [T10(1,4), T10(2,4)]; %link 1 end
% got from the transformation matrix P1x and P1y
plot([P1s(1) P1e(1)], [P1s(2) P1e(2)], 'k', 'LineWidth', 4);
hold on %to stop last graph overwriting old one; until hold off, then it's applied

% plot link 2
P2s = P1e; %link 2 start at 1 end
P2e = [T20(1,4), T20(2,4)];  %link 2 end
% got from the transformation matrix P2x and P2y
plot([P2s(1) P2e(1)], [P2s(2) P2e(2)], 'k', 'LineWidth', 4);

% plot link 3
P3s = P2e; %link 3 start at 2 end
P3e = [T30(1,4), T30(2,4)];  %link 3 end
% got from the transformation matrix P3x and P3y
plot([P3s(1) P3e(1)], [P3s(2) P3e(2)], 'k', 'LineWidth', 4);

% plot link 4
P4s = P3e; %link 3 start at 2 end
P4e = [T40(1,4), T40(2,4)];  %link 3 end
% got from the transformation matrix P3x and P3y
plot([P4s(1) P4e(1)], [P4s(2) P4e(2)], 'k', 'LineWidth', 4);

%big dot to indicate joints
plot(0, -0.1, 'sr', 'MarkerSize', 30); %base
plot(0, 0, '.r', 'MarkerSize', 50); %joint 1
plot(T10(1,4), T10(2,4), '.r', 'MarkerSize', 50); %joint 2
plot(T20(1,4), T20(2,4), '.r', 'MarkerSize', 50); %joint 3
plot(T30(1,4), T30(2,4), '.r', 'MarkerSize', 50); %joint 3

%plot the frames
%Frame 0
s = 0.2; %len of each axis (frame)
plot([0 s],[0 0], 'b', 'LineWidth', 2) % x axis frame 0 (x of starting x of ending) (y of starting y of ending
plot([0 0],[0 s], 'g', 'LineWidth', 2) % y axis frame 0 (x of starting x of ending) (y of starting y of ending

%Frame 1 at end of link one
F1s = [T10(1,4), T10(2,4)]; % start of from 1
F1x = F1s + [T10(1,1)*s T10(2,1)*s];%projection of x1 onto y0 -- end of x1 mutlitplied by s to scale down
F1y = F1s + [T10(1,2)*s T10(2,2)*s];%end of x1
plot([F1s(1) F1x(1)],[F1s(2) F1x(2)], 'b', 'LineWidth', 2) % x1 axis
plot([F1s(1) F1y(1)],[F1s(2) F1y(2)], 'g', 'LineWidth', 2) % x1

%Frame 2 at end of link two
F2s = [T20(1,4), T20(2,4)]; % start of from 2
F2x = F2s + [T20(1,1)*s T20(2,1)*s];%projection of x1 onto y0 -- end of x1 mutlitplied by s to scale down
F2y = F2s + [T20(1,2)*s T20(2,2)*s];%end of x1
plot([F2s(1) F2x(1)],[F2s(2) F2x(2)], 'b', 'LineWidth', 2) % x2 axis
plot([F2s(1) F2y(1)],[F2s(2) F2y(2)], 'g', 'LineWidth', 2) % x2

%Frame 3 at end of link three
F3s = [T30(1,4), T30(2,4)]; % start of from 2
F3x = F3s + [T30(1,1)*s T30(2,1)*s];%projection of x1 onto y0 -- end of x1 mutlitplied by s to scale down
F3y = F3s + [T30(1,2)*s T30(2,2)*s];%end of x1
plot([F3s(1) F3x(1)],[F3s(2) F3x(2)], 'b', 'LineWidth', 2) % x3 axis
plot([F3s(1) F3y(1)],[F3s(2) F3y(2)], 'g', 'LineWidth', 2) % x3

%Frame 3 at end of link three
F4s = [T40(1,4), T40(2,4)]; % start of from 2
F4x = F4s + [T40(1,1)*s T40(2,1)*s];%projection of x1 onto y0 -- end of x1 mutlitplied by s to scale down
F4y = F4s + [T40(1,2)*s T40(2,2)*s];%end of x1
plot([F4s(1) F4x(1)],[F4s(2) F4x(2)], 'b', 'LineWidth', 2) % x4 axis
plot([F4s(1) F4y(1)],[F4s(2) F4y(2)], 'g', 'LineWidth', 2) % x4

%EXTRACT EULER ANGLES, XYZ, FIXED
beta = atan2(-T30(3,1), (T30(1,1)^2+T30(2,1)^2)^0.5);%
%beta is always 0 since this is a planar manipulator
alpha = atan2(T30(2,1)/cos(beta), T30(1,1)/cos(beta))*180/pi;

xlim([0.25 3]);
ylim([-0.35 3]);
axis equal