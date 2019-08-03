# cv-function
cv方面会用到的各种功能性函数整理。

#### lmdb2img.py : 将lmdb格式的图片，还原回jpg格式或者其他图片格式。

#### merge_lmdbdata.py : 对多个lmdb数据进行合并，生成一个lmdb数据。

#### resize1.py : 对图片进行固定尺寸的resize，背景用纯色补全。

#### sample.py : 抽样函数，从文件夹中随机抽取一定数量的数据。

#### sort.py : 将字符集重新排序sort一下。

#### re_correct.py : 识别出来的结果做后处理，替换相关字符。

#### crop_savelabel.py : 将整图中所有titles截取出来，并以titles图片名保存label文件。

#### print_bbox.py : 根据检测框信息，将bbox在整图中标出，方便查看。使用时注意bbox的格式。

#### fen.py : 根据bbox_label.txt按照一定比例划分训练集和测试集。
