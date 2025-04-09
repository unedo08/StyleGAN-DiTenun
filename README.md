##Dataset 
G-Drive : https://drive.google.com/drive/folders/1fB-uTaNfcuXyi45-jUZEdVCW7mDjvKzG?usp=sharing

## Usage
```
├── dataset
   └── YOUR_DATASET_NAME
       ├── 000001.jpg 
       ├── 000002.png
       └── ...
```

### Train
```
> python main.py --dataset FFHQ --img_size 1024 --gpu_num 4 --progressive True --phase train
```

### Test
```
> python main.py --dataset FFHQ --img_size 1024 --progressive True --batch_size 16 --phase test
```

### Draw
#### Figure02 uncurated
```
python main.py --dataset FFHQ --img_size 1024 --progressive True --phase draw --draw uncurated
```

#### Figure03 style mixing
```
python main.py --dataset FFHQ --img_size 1024 --progressive True --phase draw --draw style_mix
```

#### Figure08 truncation trick
```
python main.py --dataset FFHQ --img_size 1024 --progressive True --phase draw --draw truncation_trick
```

## Our Results (1024x1024)
* Training time: **2 days 14 hours** with **V100 * 4**
* **`max_iteration`** = **900**
  * **`Official code`** = **2500**


##author : Unedo Ignasius Manalu, SandraUlina Siregar, Evelin Theresia Panjaitan

