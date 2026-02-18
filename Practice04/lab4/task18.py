x0, y0 = map(float, input().split())
x1, y1 = map(float, input().split())

# Reflect across x-axis
y0_reflect = -y0
xr = (x0 + x1) / 2
yr = 0.0

# More accurate formula for general case:
# Reflection point (xr, 0) satisfies slope equality:
# (y0 - 0)/(x0 - xr) = (0 - y1)/(xr - x1) -> solve for xr
xr = (x1*y0 + x0*y1) / (y0 + y1)
yr = 0.0

print(f"{xr:.10f} {yr:.10f}")
