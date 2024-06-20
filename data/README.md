# About Dataset

This is my first dataset! The goal of this dataset is to run a classification model on the images to determine if an images is a **grid** or a **maze**.  
This grid generation will eventually be utilized as a baseline for image transformation detection but that will be another dataset! 

## About Data collection methodology

Essentially all images are generated with the target of a 16:9 aspect ratio however there is a tolerance that is given to enlarge the mazes to be greater then the target 1280x720 pixel size.  
There is an uneven distribution of data here, there are 10 mazes generated for each pixel and cell size while only one grid will be generated.  You can duplicate each grid 10 times to accommodate this or perform other techniques to utilize all the information when training a model! 

### Description of the data

Very simple file storage structure, images are sorted based on whether or not they are grids or mazes. Images are saved with the following file format "{X Width}_x_{Y Width}_{Wall Pixel Size}_{Cell Pixel Size}".  If the image is a maze, there will be a run counter.  This is a number to indicate the run count, we generate 10 mazes to every 1 grid.  There is then a "g" or "m" to indicate maze or grid. 

```
data/
  -grid/
    -16_x_9_1_79g.jpg
    -16_x_9_2_78g.jpg
    -...
  -maze/
    -16_x_9_1_79_0m.jpg
    -16_x_9_1_79_1m.jpg
    -...
  -README.md

```

### And file formats

```
-352 images, format jpg.
```

## Online Repository link

* [DataRepository](https://www.kaggle.com/datasets/nickleland/grids-and-mazes)

## Authors

* **Nick Leland** - *Initial work* - [nick-leland](https://github.com/nick-leland)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to Greg Cope for the great write up on DFS maze generation which initially sparked the project! [Link to article](https://www.algosome.com/articles/maze-generation-depth-first.html)
* Thanks to Shashvatshah9 for the dataset [README template](https://gist.github.com/shashvatshah9/5d587605cd087182ccffb46b6cf9e449) used!