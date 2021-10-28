import click
import numpy as np
from PIL import Image
from numba import jit


@jit
def color(z, i):
    v = np.log2(i + 1 - np.log2(np.log2(abs(z)))) / 5
    if v < 1.0:
        return v ** 4, v ** 2.5, v
    else:
        v = max(0, 2 - v)
        return v, v ** 1.5, v ** 3


@jit
def iterate(c, max_iters, radius):
    z = 0j
    for i in range(max_iters):
        if z.real * z.real + z.imag * z.imag > radius:
            return color(z, i)
        z = z * z + c
    return 0, 0, 0


@click.command()
@click.option(
    "--xmin",
    default=-2.1,
    show_default=True,
)
@click.option(
    "--xmax",
    default=0.8,
    show_default=True,
)
@click.option(
    "--ymin",
    default=-1.16,
    show_default=True,
)
@click.option("--ymax", default=1.16, show_default=True)
@click.option("--width", default=1200, show_default=True)
@click.option("--height", default=960, show_default=True)
@click.option("--max-iterations", default=200, show_default=True)
@click.option("--radius", default=100, show_default=True)
@click.argument("filename", default="wallpaper.png")
def cli(xmin, xmax, ymin, ymax, width, height, max_iterations, radius, filename):
    """
    Generate a Mandelbrot fractal image using the specified parameters.
    """
    y, x = np.ogrid[ymax : ymin : height * 1j, xmin : xmax : width * 1j]
    z = x + y * 1j
    red, green, blue = np.asarray(
        np.frompyfunc(iterate, 3, 3)(z, max_iterations, radius)
    ).astype(np.float)
    img = np.dstack((red, green, blue))

    click.echo("Writing to " + filename)
    Image.fromarray(np.uint8(img * 255)).save(filename)
