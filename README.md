# mandelbrot

![Mandelbrot](docs/pics/mandelbrot_wallpaper.png)

Collection of Mandelbrot things

## Walpaper generator

```bash
./mandelbrot.py --help
Usage: mandelbrot.py [OPTIONS] [FILENAME]

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

Playing with parameters

``` bash
./mandelbrot.py --width 400 --height 300 --radius 2

```


![](docs/pics/radius2.png)
