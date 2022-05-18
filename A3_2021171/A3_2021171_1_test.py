from A3_2021171_1 import matmul, scale, rotate, translate


def test_matmul(A, B, true_C):
    a = matmul(A, B)
    try:
        assert a == true_C
        return True
    except AssertionError:
        return False


def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    a, b, c = scale(x, y, z, sx, sy, sz)
    try:
        assert [a, b, c] == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    a, b, c = translate(x, y, z, tx, ty, tz)
    try:
        assert [a, b, c] == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    a, b, c = rotate(x, y, z, axis, phi)
    try:
        assert [a, b, c] == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

x = [5, 8, 1, 2]
y = [6, 7, 3, 0]
z = [4, 5, 9, 1]

true_C = [[114, 16, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]]

sx, sy, sz = 2, 3, 4
tx, ty, tz = 2, 3, 4
axis, phi = "x", 65

true_xs, true_ys, true_zs = [10, 16, 2, 4], [18, 21, 9, 0], [16, 20, 36, 4]

true_xt, true_yt, true_zt = [7, 10, 3, 4], [9, 10, 6, 3], [8, 9, 13, 5]
true_xr, true_yr, true_zr = [5, 8, 1, 2], [-3.3747231074290323, -3.9371769586672043, -1.6873615537145161, -0.0, 3.3073147179604137, 4.134143397450517, 7.4414581154109305,
                                           0.8268286794901034], [4.960972076940621, 5.787800756430724, 2.4804860384703105, 0.0, -2.249815404952688, -2.81226925619086, -5.062084661143548, -0.562453851238172]


print(test_matmul(A, B, true_C))
print(test_scale(x, y, z, sx, sy, sz, true_xs, true_ys, true_zs))
print(test_translate(x, y, z, tx, ty, tz, true_xt, true_yt, true_zt))
print(test_rotate(x, y, z, axis, phi, true_xr, true_yr, true_zr))
