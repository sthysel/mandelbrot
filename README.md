# Mandelbrot (Version 0.1.0)

![Mandelbrot](docs/pics/mandelbrot_wallpaper.png)

A fast Mandelbrot fractal wallpaper generator.

## Usage

```zsh

Usage: mandelbrot [OPTIONS] [FILENAME]

  Generate a Mandelbrot fractal image using the specified parameters.

Options:
  --xmin FLOAT              [default: -2.1]
  --xmax FLOAT              [default: 0.8]
  --ymin FLOAT              [default: -1.16]
  --ymax FLOAT              [default: 1.16]
  --width INTEGER           [default: 1200]
  --height INTEGER          [default: 960]
  --max-iterations INTEGER  [default: 200]
  --radius INTEGER          [default: 100]
  --help                    Show this message and exit.
```

![Radius](docs/pics/radius2.png)


## Install

```zsh
$ poetry install
```

## A fast Mandelbrot set wallpaper renderer

- https://www.reddit.com/r/math/comments/2abwyt/smooth_colour_mandelbrot
- https://github.com/neozhaoliang/pywonderland
