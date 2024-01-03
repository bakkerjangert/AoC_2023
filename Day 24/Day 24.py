import matplotlib.pyplot as plt
import numpy as np

file = 'input.txt'
# file = 'test.txt'
with open(file, 'r') as f:
    data = f.read().splitlines()


class Line:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x0, self.y0, self.z0 = x, y, z
        self.vx, self.vy, self.vz = vx, vy, vz
        self.a, self.b = self.vy / self.vx, self.y0 - self.x0 * self.vy / self.vx

# Formulas --> evaluate to y = ax + b
# x = x0 + vx * t  -->  t = (x - x0) / vx
# y = y0 + vy * t  -->  t = (y - y0) / vy
# (x - x0) / vx = (y - y0) / vy  --> x / vx - x0 / vx = y / vy - y0 /vy
# y / vy = x / vx - x0 / vx + y0 / vy
# y = x * vy / vx - x0 * vy / vx + y0
# a = vy /vx and b = y0 - x0 * vy / vx

    def intersect(self, other):
        if self.a == other.a and self.b != other.b:
            return None, None  # lines parallel
        elif self.a == other.a and self.b == other.b:
            return float('inf'), float('inf')
        # Solve a1x + b1 = a2x + b2
        # a1x - a2x = b2 - b1
        # x(a1 - a2) = b2 - b1
        # x = (b2 - b1) / (a1 - a2)
        x = (other.b - self.b) / (self.a - other.a)
        y1, y2 = self.a * x + self.b, other.a * x + other.b
        return x, y1

    def get_t(self, x, y):
        # Solve x = x0 + vx * t
        # t = (x - x0) / vx
        t1, t2 = (x - self.x0) / self.vx, (y - self.y0) / self.vy
        return (x - self.x0) / self.vx

    def __repr__(self):
        return f'Hailstone {self.x0, self.y0, self.z0} with vel {self.vx, self.vy, self.vz}'


test_low, test_high = 200_000_000_000_000, 400_000_000_000_000
# test_low, test_high = 7, 27
lines = []
x_min, y_min, z_min, x_max, y_max, z_max = float('inf'), float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
for row in data:
    data = list(map(int, row.replace('@', ',').split(', ')))
    lines.append(Line(*map(int, data)))
    x_min, y_min, z_min = min(x_min, lines[-1].x0), min(y_min, lines[-1].y0), min(z_min, lines[-1].z0)
    x_max, y_max, z_max = max(x_max, lines[-1].x0), max(y_max, lines[-1].y0), max(z_max, lines[-1].z0)

pt1 = 0
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        l1, l2 = lines[i], lines[j]
        x, y = l1.intersect(l2)
        if x is None:
            continue
        t1, t2 = lines[i].get_t(x, y), lines[j].get_t(x, y)
        if t1 < 0 or t2 < 0:
            pass
        elif test_low <= x <= test_high and test_low <= y <= test_high:
            pt1 += 1

print(f'Part 1: {pt1}')

# Stone  	X, Y, Z, VX, VY, VZ  	    UPPER = unknowns
# Hail  	x, y, z, vx, vy, vz 		lower = knowns
#
# Step 1: Collision of 1 hail with Stone
# X + VX.t1 = x + vx.t1
# t1.VX – t1.vx = x – X
# t1(VX – vx) = (x – X)
# t1 = (x – X)/(VX – vx)                Same equations for y and z
# t1 = (y – Y)/(VY – vy)
# t1 = (z – Z)/(VZ – vz)
#
# Step 2: equation in x and y
# (x – X)/(VX – vx) = (y – Y)/(VY – vy)
# (x – X).(VY – vy) = (y – Y).(VX – vx)
# x.VY – x.vy – X.VY + X.vy = y.VX – y.vx – Y.VX + Y.vx
# Y.VX - X.VY = y.VX – y.vx + Y.vx – x.VY + x.vy – X.vy
#
# Note how left-hand side is independent of hail
#
# Step 3: add in another hail, lets say hail[i] and hail[j]
# yi.VX – yi.vxi + Y.vxi – xi.VY + xi.vyi – X.vyi = yj.VX – yj.vxj + Y.vxj – xj.VY + xj.vyj – X.vyj
# X(vyj – vyi) + Y(vxi – vxj) + VX(yi – yj) + VY(xj – xi) = yi.vxi - xi.vyi – yj.vxj + xj.vyj
#
# Note how this is just a linear equation with 4 unknowns
#
# Step 4: Solve Linear equation with 4 unknowns
# Solve with Linear Algebra (Numpy in this case) using multiple lines
#
# Step 5: replace y for z and redo calculation

# Shift base-point to prevent numerical errors
for line in lines:
    line.x0, line.y0, line.z0 = line.x0 - (x_min + x_max) // 2, line.y0 - (y_min + y_max) // 2, line.z0 - (z_min + z_max) // 2
    # print(line)

eq_xy, eq_xz = np.array([[0] * 4] * 4, dtype=np.float64), np.array([[0] * 4] * 4, dtype=np.float64)
sol_xy, sol_xz = np.array([0] * 4, dtype=np.float64), np.array([0] * 4, dtype=np.float64)

for i in range(4):
    j = i + 1
    eq_xy[i, 0] = lines[j].vy - lines[i].vy
    eq_xz[i, 0] = lines[j].vz - lines[i].vz
    eq_xy[i, 1] = lines[i].vx - lines[j].vx
    eq_xz[i, 1] = lines[i].vx - lines[j].vx
    eq_xy[i, 2] = lines[i].y0 - lines[j].y0
    eq_xz[i, 2] = lines[i].z0 - lines[j].z0
    eq_xy[i, 3] = lines[j].x0 - lines[i].x0
    eq_xz[i, 3] = lines[j].x0 - lines[i].x0
    sol_xy[i] = lines[i].y0 * lines[i].vx - lines[i].x0 * lines[i].vy - lines[j].y0 * lines[j].vx + lines[j].x0 * lines[j].vy
    sol_xz[i] = lines[i].z0 * lines[i].vx - lines[i].x0 * lines[i].vz - lines[j].z0 * lines[j].vx + lines[j].x0 * lines[j].vz

X, Y, VX, VY = np.linalg.solve(eq_xy, sol_xy)
_, Z, _, VZ = np.linalg.solve(eq_xz, sol_xz)
X, Y, Z = round(X + (x_min + x_max) // 2, 0), round(Y + (y_min + y_max) // 2, 0), round(Z + (z_min + z_max) // 2, 0)
print(f'Part 2: {int(X + Y + Z)}')
